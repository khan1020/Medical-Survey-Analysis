"""
Enhance all figure and table captions in the research paper to be
detailed, self-explanatory, and follow academic standards.
"""

INPUT = r"c:\Users\AfzalTAS\Desktop\survey\research_paper_complete.html"
with open(INPUT, encoding="utf-8") as f:
    html = f.read()

# ── TABLE CAPTIONS ──
# Table 1
html = html.replace(
    "<caption>Table 1: Demographic Characteristics of Participants (n=103)</caption>",
    "<caption>Table 1: Demographic characteristics of study participants including gender, age, marital status, and professional qualification distribution among nurses at LUMHS tertiary care hospital (n=103)</caption>"
)

# Table 2
html = html.replace(
    "<caption>Table 2: Knowledge Assessment Responses (n=103)</caption>",
    "<caption>Table 2: Distribution of responses to knowledge assessment items on infection prevention and control, showing frequency and percentage of Yes, No, and Don't Know responses among nurses at LUMHS (n=103)</caption>"
)

# Table 3
html = html.replace(
    "<caption>Table 3: Practice Assessment Responses (n=103)</caption>",
    "<caption>Table 3: Distribution of self-reported infection control practice responses among nurses, showing compliance levels for each practice item including training participation, hand hygiene, PPE use, and waste handling (n=103)</caption>"
)

# Table 4
html = html.replace(
    "<caption>Table 4: Barriers to Infection Control (n=103)</caption>",
    "<caption>Table 4: Institutional barriers to infection control as identified by nurses, showing percentage reporting each barrier based on negative responses to relevant questionnaire items (n=103)</caption>"
)

# Table 5
html = html.replace(
    "<caption>Table 5: Association Between Gender and Key Responses (Chi-Square Test)</caption>",
    '<caption>Table 5: Association between gender and key knowledge/practice responses using Pearson Chi-Square test with Yates\' correction. Statistical significance set at p &le; 0.05 (n=103; Male=40, Female=63)</caption>'
)

# Table 6
html = html.replace(
    "<caption>Table 6: Association Between Age and Key Responses (Chi-Square Test)</caption>",
    "<caption>Table 6: Association between age groups and key knowledge/practice responses using Pearson Chi-Square test. Four age categories were compared across selected questionnaire items (n=103)</caption>"
)

# Table 7
html = html.replace(
    "<caption>Table 7: Association Between Qualification and Key Responses (Chi-Square Test)</caption>",
    '<caption>Table 7: Association between professional qualification and key knowledge/practice responses using Pearson Chi-Square test. Statistically significant results (p &le; 0.05) are highlighted. Diploma=29, BSN=67, Post RN BSCN=5 (n=103)</caption>'
)

# ── FIGURE CAPTIONS ──
# Figure 1
html = html.replace(
    "<figcaption>Figure 1: Gender distribution of study participants (n=103)</figcaption>",
    "<figcaption>Figure 1: Pie chart showing gender distribution of study participants. Female nurses constituted the majority (61.2%, n=63) compared to male nurses (38.8%, n=40), reflecting the gender composition typical of the nursing profession at LUMHS tertiary care hospital (n=103)</figcaption>"
)

# Figure 2
html = html.replace(
    "<figcaption>Figure 2: Age distribution of study participants (n=103)</figcaption>",
    "<figcaption>Figure 2: Pie chart showing age distribution of participants. The largest age group was 26-30 years (46.6%, n=48), followed by 31-40 years (23.3%, n=24), indicating a predominantly young nursing workforce at LUMHS (n=103)</figcaption>"
)

# Figure 3
html = html.replace(
    "<figcaption>Figure 3: Professional qualification distribution (n=103)</figcaption>",
    "<figcaption>Figure 3: Horizontal bar chart showing professional qualification distribution. BSN was the most common qualification (65.0%, n=67), followed by Diploma in Nursing (28.2%, n=29) and Post RN BSCN (4.9%, n=5) (n=103)</figcaption>"
)

# Figure 4 (departments)
html = html.replace(
    "<figcaption>Figure 4: Department-wise distribution of participants</figcaption>",
    "<figcaption>Figure 4: Bar chart showing department-wise distribution of participating nurses across clinical departments at LUMHS Jamshoro and Hyderabad campuses, illustrating the variety of clinical settings represented in the study (n=103)</figcaption>"
)

# Figure 5 (knowledge)
html = html.replace(
    "Figure 5: Knowledge assessment responses showing Yes/No/Don't Know distribution for each item",
    "Figure 5: Grouped bar chart showing response distribution for five knowledge assessment items. Notably, 50.5% of nurses incorrectly believed clean water alone destroys microorganisms (marked with asterisk), representing the most critical knowledge gap identified in the study"
)

# Figure 6 (practice)
html = html.replace(
    "Figure 6: Self-reported infection control practices ranked by compliance level (n=103)",
    "Figure 6: Horizontal bar chart showing self-reported infection control practices ranked by compliance level. Items are color-coded: green (good, above 85%), orange (moderate, 75-84%), and red (needs improvement, below 75%). Body fluid handling without gloves (66.0%) was the lowest-scoring practice item (n=103)"
)

# Figure 7 (barriers)
html = html.replace(
    "Figure 7: Barriers to infection control - percentage of nurses reporting each barrier (n=103)",
    "Figure 7: Bar chart showing the five main institutional barriers to infection control identified by nurses. Lack of annual IPC training (28.2%) and inaccessible IC guidelines (25.2%) were the most frequently reported barriers, highlighting systemic gaps in institutional support (n=103)"
)

# Figure 8 (scores donut)
html = html.replace(
    "Figure 8: Overall knowledge and practice scores showing good vs. poor categorization (n=103)",
    "Figure 8: Donut charts comparing overall knowledge and practice scores. Knowledge: 60.2% scored good (4 or above out of 5, mean=3.6). Practice: 73.8% scored good (7 or above out of 9, mean=7.3). The higher self-reported practice scores may reflect social desirability bias (n=103)"
)

# Save
with open(INPUT, "w", encoding="utf-8") as f:
    f.write(html)

print("All captions enhanced successfully!")
print("  - 7 table captions updated")
print("  - 8 figure captions updated")
