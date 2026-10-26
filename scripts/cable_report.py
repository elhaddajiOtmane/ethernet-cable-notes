#!/usr/bin/env python3
"""Summarize a personal cable-test CSV. No claims about instrument accuracy."""
import csv, sys
from collections import Counter

def main(path):
    with open(path, newline='', encoding='utf-8') as fh:
        rows=list(csv.DictReader(fh))
    if not rows:
        print('No tests recorded yet. Add REAL cable test rows first.');return
    counts=Counter(r['result'].strip().upper() for r in rows)
    for label,count in sorted(counts.items()):
        print(f'{label}: {count}')
    print(f'Total cables logged: {len(rows)}')
    for row in rows:
        if row['result'].strip().upper() != 'PASS':
            print(f"Review {row['cable_id']}: {row.get('notes','')}")

if __name__=='__main__':
    if len(sys.argv)!=2: raise SystemExit('Usage: python3 cable_report.py cable_tests.csv')
    main(sys.argv[1])
