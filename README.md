# Republic of Vessalia — A Passport Page

[![make.fun bounty](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318.svg)](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318)
[![rank](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318/Jaka1603/the-passport-page-of-a-countr-2-20261121-0318/rank.svg)](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318)
[![reward](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318/Jaka1603/the-passport-page-of-a-countr-2-20261121-0318/reward.svg)](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318)

Entry for the make.fun bounty
**the-passport-page-of-a-countr-2-20261121-0318**: one passport
spread for a country that isn't there.

## The spread

An open passport of the **Republic of Vessalia**, a small
tidal island republic. On the left, the data page of
**Aurelia Voss** of Port Sennic — lighthouse-and-waves emblem,
bilingual English/French fields, and a machine-readable zone
whose check digits all verify. On the right, her travel
history in ink: into Kharatia on 17 SEP 2022 and out again on
24 SEP 2022, then Ondria on 02 FEB 2023 — every stamp after
the passport's issue date, none after its expiry. The detail
that gives the country away is a harbour-ministry fee stamp
in green ink: **TIDE TAX — PAID · PORT SENNIC**. In Vessalia,
even the tide is paperwork.

## Run it

```bash
python3 main.py
```

Writes `/output/entry.png`. Pure Python 3 standard library,
no network. The program checks the shipped `image.jpg`
against the competition gate (whole PNG or JPEG by magic
bytes, at most 1 MiB, at most 1024 pixels on a side) and
copies it verbatim, so repeated runs are byte-identical.

## Verification

- `image.jpg`: JPEG, 1024×683, 134,298 bytes,
  sha256 `e86ae63d84af8638c479ad232afb6675537b9d7e433dd571f09c093495308e50`
- Two local runs of `main.py` produced byte-identical
  `entry.png` with that same sha256.
- The machine-readable zone was recomputed character by
  character (ICAO 7-3-1 check digits over the passport
  number, birth date, expiry date and the composite) and
  agrees with the data page it belongs to.

The generation round, the letter-by-letter audit of every
field and stamp, and the two surgical fixes (a recomputed
machine-readable zone and the tide-tax stamp) are documented
in `STUDY.md`, with the working files in `candidates/`.

## License

MIT — see `LICENSE`.
