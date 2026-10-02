"""Add Table of Contents with hyperlinks and anchor IDs to all sections."""

INPUT = r"c:\Users\AfzalTAS\Desktop\survey\research_paper_complete.html"
with open(INPUT, encoding="utf-8") as f:
    html = f.read()

# 1. Add IDs to all section headings
heading_ids = {
    "<h2>Abstract</h2>": '<h2 id="abstract">Abstract</h2>',
    "<h2>1. Introduction</h2>": '<h2 id="introduction">1. Introduction</h2>',
    "<h3>1.1 Gaps in Current Research</h3>": '<h3 id="gaps">1.1 Gaps in Current Research</h3>',
    "<h3>1.2 Study Objectives</h3>": '<h3 id="objectives">1.2 Study Objectives</h3>',
    "<h2>2. Review of Related Literature</h2>": '<h2 id="literature">2. Review of Related Literature</h2>',
    "<h3>2.1 Synthesis of Evidence</h3>": '<h3 id="synthesis">2.1 Synthesis of Evidence</h3>',
    "<h2>3. Materials and Methods</h2>": '<h2 id="methodology">3. Materials and Methods</h2>',
    "<h3>3.1 Study Design</h3>": '<h3 id="design">3.1 Study Design</h3>',
    "<h3>3.2 Study Setting and Duration</h3>": '<h3 id="setting">3.2 Study Setting and Duration</h3>',
    "<h3>3.3 Sample Size Calculation</h3>": '<h3 id="sample">3.3 Sample Size Calculation</h3>',
    "<h3>3.4 Sampling Method</h3>": '<h3 id="sampling">3.4 Sampling Method</h3>',
    "<h3>3.5 Inclusion and Exclusion Criteria</h3>": '<h3 id="criteria">3.5 Inclusion and Exclusion Criteria</h3>',
    "<h3>3.6 Data Collection Instrument</h3>": '<h3 id="instrument">3.6 Data Collection Instrument</h3>',
    "<h3>3.7 Data Collection Procedure</h3>": '<h3 id="procedure">3.7 Data Collection Procedure</h3>',
    "<h3>3.8 Ethical Considerations</h3>": '<h3 id="ethics">3.8 Ethical Considerations</h3>',
    "<h3>3.9 Data Analysis</h3>": '<h3 id="analysis">3.9 Data Analysis</h3>',
    "<h2>4. Results</h2>": '<h2 id="results">4. Results</h2>',
    "<h3>4.1 Demographic Characteristics</h3>": '<h3 id="demographics">4.1 Demographic Characteristics</h3>',
    "<h3>4.2 Knowledge Assessment</h3>": '<h3 id="knowledge">4.2 Knowledge Assessment</h3>',
    "<h3>4.3 Practice Assessment</h3>": '<h3 id="practice">4.3 Practice Assessment</h3>',
    "<h3>4.4 Barriers to Infection Control</h3>": '<h3 id="barriers">4.4 Barriers to Infection Control</h3>',
    "<h3>4.5 Overall Knowledge and Practice Scores</h3>": '<h3 id="scores">4.5 Overall Knowledge and Practice Scores</h3>',
    "<h3>4.6 Chi-Square Analysis</h3>": '<h3 id="chisquare">4.6 Chi-Square Analysis</h3>',
    "<h2>5. Discussion</h2>": '<h2 id="discussion">5. Discussion</h2>',
    "<h3>5.1 Knowledge Assessment</h3>": '<h3 id="disc-knowledge">5.1 Knowledge Assessment</h3>',
    "<h3>5.2 Practice Assessment</h3>": '<h3 id="disc-practice">5.2 Practice Assessment</h3>',
    "<h3>5.3 Barriers Analysis</h3>": '<h3 id="disc-barriers">5.3 Barriers Analysis</h3>',
    "<h3>5.4 Comparison with International Literature</h3>": '<h3 id="disc-intl">5.4 Comparison with International Literature</h3>',
    "<h3>5.5 Limitations</h3>": '<h3 id="limitations">5.5 Limitations</h3>',
    "<h2>6. Conclusion</h2>": '<h2 id="conclusion">6. Conclusion</h2>',
    "<h3>6.1 Recommendations</h3>": '<h3 id="recommendations">6.1 Recommendations</h3>',
    "<h2>References</h2>": '<h2 id="references">References</h2>',
}

for old, new in heading_ids.items():
    html = html.replace(old, new)

# 2. Add CSS for TOC
toc_css = """
        /* ── Table of Contents ── */
        .toc {
            background: #f9f9f6;
            border: 1px solid #e0e0e0;
            border-radius: 6px;
            padding: 20px 30px;
            margin: 25px 0;
            page-break-after: always;
        }
        .toc h2 {
            font-size: 14pt;
            color: #1a1a1a;
            margin-bottom: 15px;
            border-bottom: 2px solid #2E86AB;
            padding-bottom: 8px;
            text-align: center;
        }
        .toc ul {
            list-style: none;
            margin: 0;
            padding: 0;
        }
        .toc > ul > li {
            margin-bottom: 8px;
            font-family: 'Source Sans 3', sans-serif;
            font-size: 11pt;
        }
        .toc > ul > li > a {
            color: #1a1a1a;
            text-decoration: none;
            font-weight: 600;
            display: block;
            padding: 4px 0;
            border-bottom: 1px dotted #ccc;
        }
        .toc > ul > li > a:hover {
            color: #2E86AB;
        }
        .toc ul ul {
            margin-left: 25px;
            margin-top: 4px;
        }
        .toc ul ul li {
            margin-bottom: 3px;
            font-size: 10pt;
            font-weight: 400;
        }
        .toc ul ul li a {
            color: #555;
            text-decoration: none;
        }
        .toc ul ul li a:hover {
            color: #2E86AB;
            text-decoration: underline;
        }
"""
html = html.replace("        /* ── Citation Links ── */", toc_css + "        /* ── Citation Links ── */")

# 3. Insert the TOC after the Abstract section
toc_html = """
        <!-- ══════════════════════════════════════════════ -->
        <!--             TABLE OF CONTENTS                 -->
        <!-- ══════════════════════════════════════════════ -->
        <div class="toc">
            <h2>Table of Contents</h2>
            <ul>
                <li><a href="#abstract">Abstract</a></li>
                <li><a href="#introduction">1. Introduction</a>
                    <ul>
                        <li><a href="#gaps">1.1 Gaps in Current Research</a></li>
                        <li><a href="#objectives">1.2 Study Objectives</a></li>
                    </ul>
                </li>
                <li><a href="#literature">2. Review of Related Literature</a>
                    <ul>
                        <li><a href="#synthesis">2.1 Synthesis of Evidence</a></li>
                    </ul>
                </li>
                <li><a href="#methodology">3. Materials and Methods</a>
                    <ul>
                        <li><a href="#design">3.1 Study Design</a></li>
                        <li><a href="#setting">3.2 Study Setting and Duration</a></li>
                        <li><a href="#sample">3.3 Sample Size Calculation</a></li>
                        <li><a href="#sampling">3.4 Sampling Method</a></li>
                        <li><a href="#criteria">3.5 Inclusion and Exclusion Criteria</a></li>
                        <li><a href="#instrument">3.6 Data Collection Instrument</a></li>
                        <li><a href="#procedure">3.7 Data Collection Procedure</a></li>
                        <li><a href="#ethics">3.8 Ethical Considerations</a></li>
                        <li><a href="#analysis">3.9 Data Analysis</a></li>
                    </ul>
                </li>
                <li><a href="#results">4. Results</a>
                    <ul>
                        <li><a href="#demographics">4.1 Demographic Characteristics</a></li>
                        <li><a href="#knowledge">4.2 Knowledge Assessment</a></li>
                        <li><a href="#practice">4.3 Practice Assessment</a></li>
                        <li><a href="#barriers">4.4 Barriers to Infection Control</a></li>
                        <li><a href="#scores">4.5 Overall Knowledge and Practice Scores</a></li>
                        <li><a href="#chisquare">4.6 Chi-Square Analysis</a></li>
                    </ul>
                </li>
                <li><a href="#discussion">5. Discussion</a>
                    <ul>
                        <li><a href="#disc-knowledge">5.1 Knowledge Assessment</a></li>
                        <li><a href="#disc-practice">5.2 Practice Assessment</a></li>
                        <li><a href="#disc-barriers">5.3 Barriers Analysis</a></li>
                        <li><a href="#disc-intl">5.4 Comparison with International Literature</a></li>
                        <li><a href="#limitations">5.5 Limitations</a></li>
                    </ul>
                </li>
                <li><a href="#conclusion">6. Conclusion</a>
                    <ul>
                        <li><a href="#recommendations">6.1 Recommendations</a></li>
                    </ul>
                </li>
                <li><a href="#references">References</a></li>
            </ul>
        </div>

"""

# Insert TOC right after the keywords div (end of abstract)
insert_after = "        </div>\n\n        <!-- "
# More specifically, after the abstract closing div
abstract_end = html.find("</div>", html.find('class="keywords"'))
abstract_end = html.find("\n", abstract_end) + 1

# Find the next comment block after abstract
next_section = html.find("        <!-- ══", abstract_end)

html = html[:next_section] + toc_html + html[next_section:]

# 4. Add smooth scrolling to HTML
html = html.replace('<html lang="en">', '<html lang="en" style="scroll-behavior: smooth;">')

# Save
with open(INPUT, "w", encoding="utf-8") as f:
    f.write(html)

print("Table of Contents added successfully!")
print("  - 32 section headings given IDs")
print("  - TOC with clickable links inserted after Abstract")
print("  - Smooth scrolling enabled")
print("  - TOC CSS styles added")
