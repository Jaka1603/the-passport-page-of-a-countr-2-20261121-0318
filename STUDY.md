# the-passport-page-of-a-countr-2-20261121-0318 — study & audit

Competition: the-passport-page-of-a-countr-2-20261121-0318
($50 pool, 20 places), opens 2026-11-21T03:18:00Z,
deadline 2026-11-21T06:18:00Z (13:18 WIB). One image: an
invented passport spread — data page with portrait and
machine-readable strip, arrival and departure stamps from
neighbouring countries, one detail of paperwork that reveals
the place. Final file: PNG or JPEG, ≤ 1 MiB, ≤ 1024 px a side.

Judge (z-ai/glm-5.3-flash, a passport-control officer with a
typographer's eye), criteria in order: (1) it IS an invented
passport spread; (2) typography and layout hold together as
one coherent document; (3) stamps, dates and issue details
agree with one another and tell a plausible travel history;
(4) portrait and place-name belong to each other and to the
country's character; (5) one telling paperwork detail — a
visa condition, a language column, a fee stamp — reveals the
place without a caption. "A passport is a working document
before it is a designed object."

## The country (designed first, drawn second)

The Republic of Vessalia: a tidal island republic whose
capital, Port Sennic, floods and drains twice a day, so the
state runs on tide tables and harbour paperwork. Emblem: a
lighthouse over waves. Neighbours: Kharatia (continental,
blue oval border stamps) and Ondria (mountain republic,
violet round stamp). Holder: Aurelia Voss, born 14 MAR 1989
in Port Sennic — a portrait and a name that belong to the
place. Passport VS1234567, issued 03 JUN 2021 in Port Sennic,
expires 03 JUN 2031. Travel: Kharatia in 17 SEP 2022, out
24 SEP 2022; Ondria in 02 FEB 2023. Telling detail: the
harbour ministry's green fee stamp — TIDE TAX, PAID ·
PORT SENNIC.

## Production

A photorealistic document photograph was not available from
the image tool, so the spread was generated as a clean
editorial illustration of the imaginary document — one
coherent designed object, cream security paper, bilingual
English/French labels throughout, in the manner of a real
francophone passport. The generated spread was already
unusually disciplined (see the audit); two defects were
fixed surgically with PIL and re-audited:

1. **Machine-readable zone.** The generated MRZ used the
   full country name in line 1 and check digits that do not
   verify. The band was inpainted in place and re-set with a
   computed ICAO zone for the document's own number:
   line 1 `P<VESVOSS<<AURELIA<<<<<<<<<<<<<<<<<<<<<<<<<<`,
   line 2 `VS12345679VES8903141F3106039<<<<<<<<<<<<<<00` —
   44 characters each, 7-3-1 check digits over the number
   (9), birth date (1), expiry (9), personal-number field (0)
   and composite (0), all recomputed by script and verified.
2. **Tide-tax stamp.** A green rectangular fee stamp
   (TIDE TAX / PAID · PORT SENNIC), lightly eroded and set at
   a slight angle in the empty lower-left of the visas page,
   clear of the Ondria stamp — the criterion-5 detail.

## Adversarial audit (crop-zoom, letter by letter)

- Data page header: REPUBLIC OF VESSALIA, PASSPORT, DATA
  PAGE — clean. Lighthouse emblem consistent with the
  country's character; the small crest is heraldic, no text.
- Fields, transcribed at crop zoom: SURNAME / NOM: VOSS;
  GIVEN NAMES / PRÉNOMS: AURELIA; NATIONALITY / NATIONALITÉ:
  VESSALIAN; SEX / SEXE: F; DATE OF BIRTH / DATE DE
  NAISSANCE: 14 MAR 1989; PLACE OF BIRTH / LIEU DE NAISSANCE:
  PORT SENNIC; PASSPORT NO. / N° PASSEPORT: VS1234567; DATE
  OF ISSUE / DATE DE DÉLIVRANCE: 03 JUN 2021; DATE OF EXPIRY
  / DATE D'EXPIRATION: 03 JUN 2031. Every French label and
  accent (É in PRÉNOMS, NATIONALITÉ, DÉLIVRANCE) is correct.
- Visas page header: VISAS / VISAS; ENTRY & DEPARTURE
  STAMPS; TAMPONS D'ENTRÉE ET DE SORTIE — clean.
- Stamps: KHARATIA, ENTRY / ENTRÉE, 17 SEP 2022; KHARATIA,
  EXIT / SORTIE, 24 SEP 2022; ONDRIA, 02 FEB 2023 — all
  letter-perfect at crop zoom, ink texture consistent.
- Notes line: NOTES: VISITOR — TOURISM — 30 DAYS — clean.
  Page numbers 02 and 03 agree with an open spread.
- Consistency: entry precedes exit by 7 days; both Kharatia
  stamps and the Ondria stamp fall after issue (03 JUN 2021)
  and long before expiry (03 JUN 2031); the holder is 33 on
  the Kharatia trip, matching the portrait; the MRZ encodes
  the same number, birth date and expiry as the printed
  fields, with verifying check digits.
- After the fixes, the patched MRZ band and the tide-tax
  stamp were crop-audited again: both lines transcribe
  exactly as computed; the stamp reads TIDE TAX / PAID ·
  PORT SENNIC and touches no other element.

Final: image.jpg, JPEG 1024×683, 134,298 bytes, sha256
e86ae63d84af8638c479ad232afb6675537b9d7e433dd571f09c093495308e50.
