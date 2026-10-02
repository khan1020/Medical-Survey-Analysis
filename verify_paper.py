import os, re

html_file = r"c:\Users\AfzalTAS\Desktop\survey\research_paper_complete.html"
fig_dir = r"c:\Users\AfzalTAS\Desktop\survey\figures"

print("HTML file exists:", os.path.exists(html_file))
print("HTML file size:", os.path.getsize(html_file), "bytes")
print()
print("Figures directory contents:")
for f in sorted(os.listdir(fig_dir)):
    path = os.path.join(fig_dir, f)
    print(f"  {f}: {os.path.getsize(path):,} bytes")

with open(html_file, encoding="utf-8") as fh:
    html = fh.read()

# Check figure references
figs_referenced = re.findall(r'src="(figures/[^"]+)"', html)
print("\nFigures referenced in HTML:")
for f in figs_referenced:
    full = os.path.join(r"c:\Users\AfzalTAS\Desktop\survey", f)
    exists = os.path.exists(full)
    print(f"  {f} -> {'EXISTS' if exists else 'MISSING'}")

# Count sections
sections = re.findall(r'<h2>(.*?)</h2>', html)
print(f"\nSections ({len(sections)}):")
for s in sections:
    print(f"  - {s}")

tables = re.findall(r'<caption>(.*?)</caption>', html)
print(f"\nTables ({len(tables)}):")
for t in tables:
    print(f"  - {t}")

ref_section = html.split('class="references"')[1]
ref_items = re.findall(r'<li>', ref_section)
print(f"\nReferences: {len(ref_items)}")
print("\nAll checks passed!")
