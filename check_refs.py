import re

with open(r"c:\Users\AfzalTAS\Desktop\survey\research_paper_complete.html", encoding="utf-8") as f:
    html = f.read()

# Find all sup tags
sups = re.findall(r'<sup>([^<]+)</sup>', html)
print("All citation numbers used:")
for s in sups:
    print(f"  [{s}]")

# Check if there are any anchor links
anchors = re.findall(r'<a href=[^>]+>', html)
print(f"\nAnchor links found: {len(anchors)}")

ref_ids = re.findall(r'id="ref\d+"', html)
print(f"Reference IDs found: {len(ref_ids)}")

# Find affiliation sups
aff_sups = re.findall(r'<sup>\d+</sup>', html[:2000])
print(f"\nAffiliation sups in title area: {len(aff_sups)}")
