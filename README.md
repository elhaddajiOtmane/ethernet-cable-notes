# Ethernet cable notes

A place for my Ethernet wiring notes, cable labeling ideas, and a small CSV reporting script. I kept forgetting the wire order when switching between diagrams, so I put the pinout and test-log format in one place.

## Wiring I refer to
T568B (pins 1–8): white/orange, orange, white/green, blue, white/blue, green, white/brown, brown. For a straight-through patch cable, use the same scheme on both ends.

## What is here
- `scripts/cable_report.py` summarizes rows from a cable test CSV.
- `cable_tests.csv` is an empty log ready for readings.
- `examples/SYNTHETIC_cable_tests.csv` contains made-up examples to test the parser, **not real cable readings**.

```bash
python3 scripts/cable_report.py examples/SYNTHETIC_cable_tests.csv
```

## Reference photos
[Ethernet cables on Wikimedia Commons](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=ethernet%20cable) · [RJ45 connectors](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=RJ45%20connector)

Those links are reference images from the web, not photos of my own setup. Check each photo's license before reusing it.
