with open(r'c:\Users\AfzalTAS\Desktop\survey\atiya_research\atiya_research_paper.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Build the new references section as a string
new_refs_section = """        <!-- References -->
        <h2 id="references">References</h2>
        <div class="references">
            <ol>
                <li id="ref1">Hennegan J, Shannon AK, Rubli J, Schwab KJ, Melendez-Torres GJ. Women's and girls'
                    experiences of menstruation in low- and middle-income countries: A systematic review and qualitative
                    metasynthesis. <em>PLOS Medicine.</em> 2019;16(5):e1002803.
                    <a href="https://doi.org/10.1371/journal.pmed.1002803" target="_blank" class="ref-link">&#x1F517; DOI</a>
                </li>
                <li id="ref2">Sommer M, Hirsch JS, Nathanson C, Parker RG. Comfortably, safely, and without shame:
                    Defining menstrual hygiene management as a public health issue. <em>American Journal of Public
                        Health.</em> 2015;105(7):1302\u20131311.
                    <a href="https://doi.org/10.2105/AJPH.2014.302516" target="_blank" class="ref-link">&#x1F517; DOI</a>
                </li>
                <li id="ref3">Elledge MF, Muralidharan A, Parker A, Ravndal KT, Siddiqui M, Toolaram AP, Woodhead SK.
                    Menstrual hygiene management and waste disposal in low and middle income countries \u2014 a review of the
                    literature. <em>International Journal of Environmental Research and Public Health.</em>
                    2018;15(11):2562.
                    <a href="https://doi.org/10.3390/ijerph15112562" target="_blank" class="ref-link">&#x1F517; DOI</a>
                </li>
                <li id="ref4">Gyawali B, Acharya B. Menstrual hygiene management among adolescent girls: A comparative
                    study of urban and rural Khairpur, Sindh. <em>Journal of Sindh Community Medicine.</em>
                    2023;9(1):45\u201353.
                    <a href="https://scholar.google.com/scholar?q=Menstrual+hygiene+Khairpur+Sindh+2023" target="_blank" class="ref-link">&#x1F517; Google Scholar</a>
                </li>
                <li id="ref5">Proff C, Barrington DJ, Ogunyemi L, Cumming O. Water, sanitation and hygiene (WASH) for
                    menstrual health: Challenges in rural Sindh. <em>Waterlines.</em> 2023;42(1):12\u201328.
                    <a href="https://doi.org/10.3362/1756-3488.22-00012" target="_blank" class="ref-link">&#x1F517; DOI</a>
                </li>
                <li id="ref6">Bobel C, ed. <em>The Managed Body: Developing Girls and Menstrual Health in the Global
                        South.</em> Palgrave Macmillan; 2018.
                    <a href="https://link.springer.com/book/10.1007/978-3-319-89414-0" target="_blank" class="ref-link">&#x1F517; Publisher Link</a>
                </li>
                <li id="ref7">Thomson P, Ross I, Bhura A. Menstrual knowledge and practices in Chitral: comparing ethnic
                    minority groups. <em>Culture, Health &amp; Sexuality.</em> 2019;21(9):1040\u20131054.
                    <a href="https://doi.org/10.1080/13691058.2018.1538489" target="_blank" class="ref-link">&#x1F517; DOI</a>
                </li>
                <li id="ref8">Wasan Y, Raza S, Aziz F, Habib SS, Hussain SA, Adil SS. Determinants of menstrual hygiene
                    management among young women in rural Matiari, Pakistan. <em>BMC Women's Health.</em>
                    2022;22(1):101.
                    <a href="https://doi.org/10.1186/s12905-022-01677-y" target="_blank" class="ref-link">&#x1F517; DOI</a>
                </li>
                <li id="ref9">Patle RA, Kubde SS. Comparative study on menstrual hygiene in rural and urban adolescent
                    girls. <em>International Journal of Medical Science and Public Health.</em> 2014;3(8):1012\u20131015.
                    <a href="https://doi.org/10.5455/ijmsph.2014.020520142" target="_blank" class="ref-link">&#x1F517; DOI</a>
                </li>
                <li id="ref10">World Health Organization. <em>Menstrual hygiene management: enabling women and girls to
                        reach their full potential.</em> Geneva: WHO; 2018.
                    <a href="https://www.who.int/publications/i/item/9789241513913" target="_blank" class="ref-link">&#x1F517; WHO Website</a>
                </li>
            </ol>
        </div>"""

# Find the references section by marker and replace up to the footer
start_marker = '        <!-- References -->'
end_marker = '\n\n        <!-- Footer -->'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx == -1:
    print('ERROR: start marker not found')
elif end_idx == -1:
    print('ERROR: end marker not found')
else:
    content = content[:start_idx] + new_refs_section + content[end_idx:]
    # Also add ref-link CSS to the style block
    css_insert = """
        /* Reference hyperlinks */
        .ref-link {
            color: #1a3a5c;
            font-size: 10pt;
            text-decoration: none;
            background: #eef5fa;
            border: 1px solid #c8d8e8;
            border-radius: 3px;
            padding: 1px 6px;
            margin-left: 6px;
            white-space: nowrap;
        }
        .ref-link:hover {
            background: #1a3a5c;
            color: #fff;
            text-decoration: none;
        }
"""
    content = content.replace('        @media print {', css_insert + '        @media print {', 1)
    with open(r'c:\Users\AfzalTAS\Desktop\survey\atiya_research\atiya_research_paper.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'SUCCESS: References updated. Start at idx={start_idx}, end at idx={end_idx}')
