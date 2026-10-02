"""
Update dates - write to new file, user can rename after closing original.
"""
import csv
import random

random.seed(42)

INPUT = r"c:\Users\AfzalTAS\Desktop\survey\expanded_dataset_103.csv"
OUTPUT = r"c:\Users\AfzalTAS\Desktop\survey\expanded_dataset_fixed.csv"

with open(INPUT, encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)
    rows = list(reader)

rows = [r for r in rows if len(r) > 1]
n = len(rows)

jan27_count = 45
feb4_count = 40

indices = list(range(n))
random.shuffle(indices)

jan27_indices = set(indices[:jan27_count])
feb4_indices = set(indices[jan27_count:jan27_count + feb4_count])

online_dates = ["01/28/2026", "01/29/2026", "01/30/2026", "01/31/2026", 
                "02/01/2026", "02/02/2026", "02/03/2026"]

def random_time(date_str, is_physical=True):
    month, day, year = date_str.split("/")
    if is_physical:
        hour = random.randint(9, 16)
    else:
        hour = random.choice([8,9,10,11,14,15,16,17,18,19,20,21,22])
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    return f"{int(month)}/{int(day)}/{year} {hour}:{minute:02d}:{second:02d}"

for i in range(n):
    if i in jan27_indices:
        date_str = "01/27/2026"
        rows[i][2] = date_str
        rows[i][0] = random_time(date_str, is_physical=True)
    elif i in feb4_indices:
        date_str = "02/04/2026"
        rows[i][2] = date_str
        rows[i][0] = random_time(date_str, is_physical=True)
    else:
        date_str = random.choice(online_dates)
        rows[i][2] = date_str
        rows[i][0] = random_time(date_str, is_physical=False)

with open(OUTPUT, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)

from collections import Counter
date_counts = Counter(r[2] for r in rows)
print(f"Total rows: {n}")
print("\nDate distribution:")
for date in sorted(date_counts.keys()):
    count = date_counts[date]
    label = "PHYSICAL" if date in ("01/27/2026", "02/04/2026") else "ONLINE"
    print(f"  {date}: {count:3d} responses  ({label})")
print(f"\nTotal: {sum(date_counts.values())}")
print(f"\nSaved to: {OUTPUT}")
print("Close the original CSV in your editor, then delete it and rename this one.")
