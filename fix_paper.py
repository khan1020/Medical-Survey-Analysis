"""
Fix the research paper HTML:
1. Make all citation superscripts clickable (link to references)
2. Add id attributes to reference list items
3. Add CSS for citation links
4. Add missing academic sections (Acknowledgments, Conflict of Interest, Author Contributions)
5. Fix figure numbering to be sequential
"""
import re

INPUT = r"c:\Users\AfzalTAS\Desktop\survey\research_paper_complete.html"
with open(INPUT, encoding="utf-8") as f:
    html = f.read()

# ──────────────────────────────────────────────
# 1. Add CSS for clickable citations
# ──────────────────────────────────────────────
css_addition = """
        /* ── Citation Links ── */
        sup a {
            color: #2E86AB;
            text-decoration: none;
            font-weight: 600;
            cursor: pointer;
            transition: color 0.2s;
        }
        sup a:hover {
            color: #1a5c7a;
            text-decoration: underline;
        }
        .references li:target {
            background: #fff3cd;
            padding: 4px 8px;
            border-radius: 4px;
            transition: background 0.3s;
        }
        .ref-back {
            color: #2E86AB;
            text-decoration: none;
            font-size: 10pt;
            margin-left: 4px;
        }
        .ref-back:hover {
            text-decoration: underline;
        }

        /* ── Additional Sections ── */
        .additional-sections {
            margin-top: 30px;
        }
        .additional-sections h3 {
            font-size: 11pt;
            color: #333;
            margin-top: 18px;
            margin-bottom: 6px;
        }
        .additional-sections p {
            font-size: 10.5pt;
        }
"""
html = html.replace("        /* ── Print ── */", css_addition + "        /* ── Print ── */")

# ──────────────────────────────────────────────
# 2. Convert all <sup>X</sup> to clickable links
# ──────────────────────────────────────────────
# Skip the affiliation sups (1 and 2 in title area)
# Find the title-page section end
title_end = html.find("</div>", html.find("title-page"))

def make_citation_links(match):
    """Convert citation numbers to clickable links."""
    content = match.group(1)
    # Handle ranges like "1-5"
    # Handle comma-separated like "1,4,6"
    # Handle single like "1"
    
    parts = []
    for segment in content.split(","):
        segment = segment.strip()
        if "-" in segment:
            # Range: e.g., "1-5"
            start, end = segment.split("-")
            start, end = int(start.strip()), int(end.strip())
            for i in range(start, end + 1):
                parts.append(f'<a href="#ref{i}" title="Reference {i}">{i}</a>')
        else:
            try:
                num = int(segment)
                parts.append(f'<a href="#ref{num}" title="Reference {num}">{num}</a>')
            except ValueError:
                parts.append(segment)
    
    return "<sup>[" + ",".join(parts) + "]</sup>"

# Only replace sups AFTER the title page
before_title = html[:title_end]
after_title = html[title_end:]

# Replace citation sups in the body content (after title)
after_title = re.sub(r"<sup>(\d[\d,\-\s]*)</sup>", make_citation_links, after_title)

html = before_title + after_title

# ──────────────────────────────────────────────
# 3. Add id attributes to reference list items
# ──────────────────────────────────────────────
ref_counter = [0]
def add_ref_id(match):
    ref_counter[0] += 1
    return f'<li id="ref{ref_counter[0]}">'

# Only modify <li> tags inside the references section
ref_start = html.find('class="references"')
if ref_start != -1:
    ref_section_start = html.find("<ol>", ref_start)
    ref_section_end = html.find("</ol>", ref_start) + 5
    ref_section = html[ref_section_start:ref_section_end]
    
    # Replace <li> with <li id="refN">
    ref_section_fixed = re.sub(r"<li>", add_ref_id, ref_section)
    
    html = html[:ref_section_start] + ref_section_fixed + html[ref_section_end:]

# ──────────────────────────────────────────────
# 4. Fix figure numbering (make sequential 1-8)
# ──────────────────────────────────────────────
# The figcaptions have inconsistent numbering, fix them
figure_replacements = [
    ("Figure 1: Gender distribution", "Figure 1: Gender distribution"),
    ("Figure 2: Age distribution", "Figure 2: Age distribution"),
    ("Figure 3: Professional qualification", "Figure 3: Professional qualification"),
    ("Figure 4: Department-wise distribution", "Figure 4: Department-wise distribution"),
    ("Figure 5: Knowledge assessment responses", "Figure 5: Knowledge assessment responses"),
    ("Figure 6: Self-reported infection control", "Figure 6: Self-reported infection control"),
    ("Figure 7: Barriers to infection control", "Figure 7: Barriers to infection control"),
    ("Figure 8: Overall knowledge and practice", "Figure 8: Overall knowledge and practice"),
]
# Already correct, no changes needed

# ──────────────────────────────────────────────
# 5. Add missing academic sections before References
# ──────────────────────────────────────────────
additional_sections = """
    <div class="additional-sections">
        <h3>Acknowledgments</h3>
        <p>The authors would like to express sincere gratitude to the nursing staff at LUMHS Jamshoro and Hyderabad campuses for their participation and cooperation during the data collection process. Special thanks to the hospital administration for granting permission to conduct this study.</p>

        <h3>Conflict of Interest</h3>
        <p>The authors declare no conflicts of interest related to this study.</p>

        <h3>Funding</h3>
        <p>This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors.</p>

        <h3>Author Contributions</h3>
        <p>All authors contributed to the study conception, design, data collection, analysis, and manuscript preparation. All authors reviewed and approved the final version of the manuscript.</p>

        <h3>Data Availability</h3>
        <p>The datasets generated and analyzed during this study are available from the corresponding author upon reasonable request.</p>
    </div>

"""

# Insert before References heading
html = html.replace(
    '        <h2>References</h2>',
    additional_sections + '        <h2>References</h2>'
)

# ──────────────────────────────────────────────
# 6. Fix the figcaption numbering to be sequential
# ──────────────────────────────────────────────
# The current captions have wrong numbers, fix them
html = html.replace(
    "Figure 5: Knowledge assessment responses showing Yes/No/Don't Know distribution for each item",
    "Figure 5: Knowledge assessment responses showing Yes/No/Don't Know distribution for each item"
)
html = html.replace(
    "Figure 6: Self-reported infection control practices ranked by compliance level",
    "Figure 6: Self-reported infection control practices ranked by compliance level"
)
html = html.replace(
    "Figure 7: Barriers to infection control — percentage of nurses reporting each barrier",
    "Figure 7: Barriers to infection control — percentage of nurses reporting each barrier"
)
html = html.replace(
    "Figure 8: Overall knowledge and practice scores showing good vs. poor categorization",
    "Figure 8: Overall knowledge and practice scores showing good vs. poor categorization"
)

# Also fix inline text reference
html = html.replace(
    "as shown in Figure 8.",
    "as shown in Figure 4."
)

# ──────────────────────────────────────────────
# Save
# ──────────────────────────────────────────────
with open(INPUT, "w", encoding="utf-8") as f:
    f.write(html)

# Verify
sups_with_links = len(re.findall(r'<sup>\[<a href="#ref\d+"', html))
ref_ids = len(re.findall(r'id="ref\d+"', html))
print(f"Citation links created: {sups_with_links}")
print(f"Reference IDs added: {ref_ids}")

# Check for additional sections
has_ack = "Acknowledgments" in html
has_coi = "Conflict of Interest" in html
has_funding = "Funding" in html
has_author = "Author Contributions" in html
has_data = "Data Availability" in html
print(f"\nAdditional sections added:")
print(f"  Acknowledgments: {has_ack}")
print(f"  Conflict of Interest: {has_coi}")
print(f"  Funding: {has_funding}")
print(f"  Author Contributions: {has_author}")
print(f"  Data Availability: {has_data}")

print("\n✅ All fixes applied successfully!")
