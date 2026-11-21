#!/usr/bin/env python3
"""make.fun entry: the-passport-page-of-a-countr-2-20261121-0318.

The picture ships next to this file as ``image.jpg``: an open
passport spread from the Republic of Vessalia, a small tidal
island republic that does not exist.  Aurelia Voss's data page
faces a visas page stamped through Kharatia and Ondria, with
the harbour ministry's tide-tax stamp paid at Port Sennic.

This program is the delivery mechanism.  It reads the picture,
makes sure it still satisfies the contest's mechanical rules
(a whole PNG or JPEG, no more than 1 MiB, no more than
1024 pixels on a side), then writes it to ``/output/entry.png``
without changing a byte, and proves the copy by hashing both
sides of the write.

Standard library only; no network.
"""

import hashlib
import os
import struct
import sys

FOLDER = os.path.dirname(os.path.abspath(__file__))
PICTURE = "image.jpg"
OUT_FOLDER = "/output"
OUT_FILE = "entry.png"

BYTE_LIMIT = 1024 * 1024
SIDE_LIMIT = 1024

PNG_HEAD = b"\x89PNG\r\n\x1a\n"
JPEG_HEAD = b"\xff\xd8\xff"

# Markers with no length field: TEM, SOI, EOI and the restarts.
NO_LENGTH = {0x01, 0xD8, 0xD9} | set(range(0xD0, 0xD8))
# Start-of-frame markers: the segment after them holds the size.
FRAME_MARKERS = {0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7,
                 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF}


class BadPicture(Exception):
    """Raised when the picture breaks one of the contest rules."""


def png_size(data):
    """(width, height) out of the IHDR chunk of a PNG."""
    if len(data) < 24 or data[12:16] != b"IHDR":
        raise BadPicture("PNG opening chunk is not IHDR")
    return struct.unpack(">II", data[16:24])


def jpeg_size(data):
    """(width, height) out of the first frame segment of a JPEG."""
    i = 2
    end = len(data)
    while i + 1 < end:
        if data[i] != 0xFF:
            raise BadPicture("JPEG marker prefix missing at %d" % i)
        marker = data[i + 1]
        if marker in NO_LENGTH:
            i += 2
            continue
        if i + 4 > end:
            raise BadPicture("JPEG segment header runs off the end")
        seg = struct.unpack(">H", data[i + 2:i + 4])[0]
        if seg < 2:
            raise BadPicture("JPEG segment length makes no sense")
        if marker in FRAME_MARKERS:
            if i + 9 > end:
                raise BadPicture("JPEG frame segment runs off the end")
            height, width = struct.unpack(">HH", data[i + 5:i + 9])
            return width, height
        i += 2 + seg
    raise BadPicture("no frame segment anywhere in the JPEG")


def probe(data):
    """Check every mechanical rule; describe the picture briefly."""
    if not data:
        raise BadPicture("the picture file is empty")
    if len(data) > BYTE_LIMIT:
        raise BadPicture(
            "%d bytes is over the %d-byte limit" % (len(data), BYTE_LIMIT))
    if data.startswith(PNG_HEAD):
        kind, (width, height) = "PNG", png_size(data)
    elif data.startswith(JPEG_HEAD):
        kind, (width, height) = "JPEG", jpeg_size(data)
    else:
        raise BadPicture("the opening bytes are neither PNG nor JPEG")
    if width == 0 or height == 0:
        raise BadPicture("a side of the picture is zero pixels")
    if width > SIDE_LIMIT or height > SIDE_LIMIT:
        raise BadPicture(
            "%dx%d is over the %dx%d limit"
            % (width, height, SIDE_LIMIT, SIDE_LIMIT))
    return "%s, %d x %d px, %d bytes" % (kind, width, height, len(data))


def run():
    path = os.path.join(FOLDER, PICTURE)
    if not os.path.isfile(path):
        print("missing picture: %s" % path, file=sys.stderr)
        return 1
    with open(path, "rb") as fh:
        data = fh.read()
    try:
        summary = probe(data)
    except BadPicture as exc:
        print("picture refused: %s" % exc, file=sys.stderr)
        return 1

    try:
        os.makedirs(OUT_FOLDER, exist_ok=True)
        target = os.path.join(OUT_FOLDER, OUT_FILE)
        with open(target, "wb") as fh:
            fh.write(data)
    except OSError as exc:
        print("cannot write the entry: %s" % exc, file=sys.stderr)
        return 1

    want = hashlib.sha256(data).hexdigest()
    with open(target, "rb") as fh:
        got = hashlib.sha256(fh.read()).hexdigest()
    if got != want:
        print("copy does not match: %s != %s" % (got, want),
              file=sys.stderr)
        return 1

    print("%s -> %s (sha256 %s)" % (summary, target, want))
    return 0


if __name__ == "__main__":
    sys.exit(run())
