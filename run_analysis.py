"""
Complete Statistical Analysis of Expanded Dataset (n=103)
=========================================================
Generates all tables needed for the Results section:
- Table 1: Demographic characteristics
- Table 2: Knowledge assessment responses
- Table 3: Practice assessment responses  
- Table 4: Barrier assessment responses
- Table 5: Chi-square: Gender vs Knowledge/Practice
- Table 6: Chi-square: Age vs Knowledge/Practice
- Table 7: Chi-square: Qualification vs Knowledge/Practice
- Summary statistics
"""

import csv
import os
from collections import Counter
from scipy import stats
import numpy as np

# === LOAD DATA ===
INPUT = r"c:\Users\AfzalTAS\Desktop\survey\expanded_dataset_103.csv"
with open(INPUT, encoding='utf-8') as f:
    reader = csv.reader(f)
    headers = next(reader)
    rows = list(reader)

N = len(rows)
print(f"Total Participants: {N}")
print("=" * 80)

# Column indices
COL = {
    'gender': headers.index('1. Gender'),
    'age': headers.index('2. Age (Years)'),
    'marital': headers.index('3. Marital Status'),
    'qual': headers.index('4. Professional Qualification'),
    'dept': headers.index('5. Department'),
}

# Question columns (8 to 22)
Q_COLS = list(range(8, 23))
Q_LABELS = {
    8:  "Q1. Periodic education/training on IPC conducted in department",
    9:  "Q2. Infection control guidelines available and accessible",
    10: "Q3. HAIs transmitted through contaminated equipment",
    11: "Q4. Nosocomial infection = acquired during hospital stay",
    12: "Q5. Hand washing before/after every patient contact",
    13: "Q6. Aware of WHO Five Moments of Hand Hygiene",
    14: "Q7. All HCWs/patients considered potentially infectious",
    15: "Q8. Clean water alone destroys harmful microorganisms",
    16: "Q9. Body fluids never handled with bare hands",
    17: "Q10. Adequate knowledge of HAI prevention/control",
    18: "Q11. PPE always available when needed",
    19: "Q12. Masks/eye protection during invasive procedures",
    20: "Q13. Attend IPC training/workshops at least once/year",
    21: "Q14. Appropriate PPE when handling contaminated waste",
    22: "Q15. Proper IPC practices improve patient outcomes",
}

# Domain classification
KNOWLEDGE_Qs = [10, 11, 13, 14, 15]  # Q3, Q4, Q6, Q7, Q8
PRACTICE_Qs  = [8, 9, 12, 16, 18, 19, 20, 21, 22]  # Q1,Q2,Q5,Q9,Q11-Q15
BARRIER_Qs   = [8, 9, 17, 18, 20]  # Q1,Q2,Q10,Q11,Q13

# Correct answers for knowledge scoring
# Q8 (col 15): correct = No (clean water alone is NOT sufficient)
CORRECT_ANSWERS = {
    10: 'Yes',  # Q3: HAIs via contaminated equipment
    11: 'Yes',  # Q4: Nosocomial = hospital-acquired
    13: 'Yes',  # Q6: WHO 5 moments
    14: 'Yes',  # Q7: All potentially infectious
    15: 'No',   # Q8: Clean water NOT sufficient (correct = No)
}

output_lines = []
def p(text=""):
    print(text)
    output_lines.append(text)

# ============================================================
#  TABLE 1: DEMOGRAPHIC CHARACTERISTICS
# ============================================================
p("\n" + "=" * 80)
p("TABLE 1: DEMOGRAPHIC CHARACTERISTICS OF PARTICIPANTS (n=103)")
p("=" * 80)
p(f"{'Variable':<35} {'Category':<25} {'Frequency (n)':<15} {'Percentage (%)'}")
p("-" * 90)

demo_vars = [
    ('Gender', COL['gender'], ['Male', 'Female']),
    ('Age (Years)', COL['age'], ['<=25', '26-30', '31-40', 'Above 40']),
    ('Marital Status', COL['marital'], ['Single', 'Married', 'Widowed']),
    ('Professional Qualification', COL['qual'], ['Diploma in Nursing', 'BSN', 'Post RN BSCN']),
]

for var_name, col_idx, categories in demo_vars:
    vals = [row[col_idx].strip() for row in rows]
    c = Counter(vals)
    first = True
    for cat in categories:
        count = c.get(cat, 0)
        pct = count / N * 100
        label = var_name if first else ""
        p(f"{label:<35} {cat:<25} {count:<15} {pct:.1f}%")
        first = False
    p()

# Department breakdown
p(f"{'Department':<35} {'Category':<25} {'Frequency (n)':<15} {'Percentage (%)'}")
p("-" * 90)
dept_vals = [row[COL['dept']].strip() for row in rows]
dept_c = Counter(dept_vals)
for dept, count in dept_c.most_common():
    if dept:
        pct = count / N * 100
        p(f"{'':<35} {dept:<25} {count:<15} {pct:.1f}%")

# ============================================================
#  TABLE 2: KNOWLEDGE ASSESSMENT
# ============================================================
p("\n" + "=" * 80)
p("TABLE 2: KNOWLEDGE ASSESSMENT RESPONSES (n=103)")
p("=" * 80)
p(f"{'Question':<60} {'Yes':>8} {'No':>8} {'DK':>8}")
p("-" * 90)

for col_idx in KNOWLEDGE_Qs:
    vals = [row[col_idx].strip() for row in rows]
    c = Counter(vals)
    yes_n = c.get('Yes', 0)
    no_n = c.get('No', 0)
    dk_n = c.get("Don't Know", 0)
    label = Q_LABELS[col_idx][:58]
    p(f"{label:<60} {yes_n:>3}({yes_n/N*100:.1f}%) {no_n:>3}({no_n/N*100:.1f}%) {dk_n:>3}({dk_n/N*100:.1f}%)")

# Knowledge score
p("\nKnowledge Score Summary:")
scores = []
for row in rows:
    score = 0
    for col_idx, correct in CORRECT_ANSWERS.items():
        if row[col_idx].strip() == correct:
            score += 1
    scores.append(score)
scores = np.array(scores)
p(f"  Mean Knowledge Score: {scores.mean():.2f} / 5 (SD = {scores.std():.2f})")
p(f"  Good Knowledge (≥4/5): {sum(1 for s in scores if s >= 4)} ({sum(1 for s in scores if s >= 4)/N*100:.1f}%)")
p(f"  Poor Knowledge (<4/5): {sum(1 for s in scores if s < 4)} ({sum(1 for s in scores if s < 4)/N*100:.1f}%)")

# ============================================================
#  TABLE 3: PRACTICE ASSESSMENT
# ============================================================
p("\n" + "=" * 80)
p("TABLE 3: PRACTICE ASSESSMENT RESPONSES (n=103)")
p("=" * 80)
p(f"{'Question':<60} {'Yes':>8} {'No':>8} {'DK':>8}")
p("-" * 90)

for col_idx in PRACTICE_Qs:
    vals = [row[col_idx].strip() for row in rows]
    c = Counter(vals)
    yes_n = c.get('Yes', 0)
    no_n = c.get('No', 0)
    dk_n = c.get("Don't Know", 0)
    label = Q_LABELS[col_idx][:58]
    p(f"{label:<60} {yes_n:>3}({yes_n/N*100:.1f}%) {no_n:>3}({no_n/N*100:.1f}%) {dk_n:>3}({dk_n/N*100:.1f}%)")

# Practice score
practice_scores = []
for row in rows:
    score = sum(1 for col_idx in PRACTICE_Qs if row[col_idx].strip() == 'Yes')
    practice_scores.append(score)
practice_scores = np.array(practice_scores)
p(f"\nPractice Score Summary:")
p(f"  Mean Practice Score: {practice_scores.mean():.2f} / {len(PRACTICE_Qs)} (SD = {practice_scores.std():.2f})")
p(f"  Good Practice (≥7/9): {sum(1 for s in practice_scores if s >= 7)} ({sum(1 for s in practice_scores if s >= 7)/N*100:.1f}%)")
p(f"  Poor Practice (<7/9): {sum(1 for s in practice_scores if s < 7)} ({sum(1 for s in practice_scores if s < 7)/N*100:.1f}%)")

# ============================================================
#  TABLE 4: BARRIER ASSESSMENT
# ============================================================
p("\n" + "=" * 80)
p("TABLE 4: BARRIERS TO INFECTION CONTROL (n=103)")
p("=" * 80)
p(f"{'Barrier Item':<60} {'Yes':>8} {'No':>8} {'DK':>8}")
p("-" * 90)

barrier_labels = {
    8:  "Periodic IPC training conducted in department",
    9:  "IC guidelines available and accessible",
    17: "Adequate personal knowledge of HAI prevention",
    18: "PPE always available when needed",
    20: "Attend IPC training at least once/year",
}

for col_idx in BARRIER_Qs:
    vals = [row[col_idx].strip() for row in rows]
    c = Counter(vals)
    yes_n = c.get('Yes', 0)
    no_n = c.get('No', 0)
    dk_n = c.get("Don't Know", 0)
    label = barrier_labels[col_idx]
    # For barriers: "No" = barrier exists
    p(f"{label:<60} {yes_n:>3}({yes_n/N*100:.1f}%) {no_n:>3}({no_n/N*100:.1f}%) {dk_n:>3}({dk_n/N*100:.1f}%)")

# Barrier summary
p("\nBarrier Summary (% reporting 'No' = barrier present):")
for col_idx in BARRIER_Qs:
    vals = [row[col_idx].strip() for row in rows]
    no_pct = sum(1 for v in vals if v == 'No') / N * 100
    p(f"  {barrier_labels[col_idx]}: {no_pct:.1f}% report barrier")

# ============================================================
#  TABLE 5: CHI-SQUARE: GENDER vs KNOWLEDGE/PRACTICE
# ============================================================
p("\n" + "=" * 80)
p("TABLE 5: ASSOCIATION BETWEEN GENDER AND RESPONSES (Chi-Square Test)")
p("=" * 80)
p(f"{'Question':<50} {'Male Yes%':>10} {'Female Yes%':>12} {'χ²':>8} {'p-value':>10} {'Sig':>5}")
p("-" * 100)

gender_vals = [row[COL['gender']].strip() for row in rows]
for col_idx in Q_COLS:
    q_vals = [row[col_idx].strip() for row in rows]
    # Build contingency table
    male_yes = sum(1 for g, q in zip(gender_vals, q_vals) if g == 'Male' and q == 'Yes')
    male_no = sum(1 for g, q in zip(gender_vals, q_vals) if g == 'Male' and q != 'Yes')
    female_yes = sum(1 for g, q in zip(gender_vals, q_vals) if g == 'Female' and q == 'Yes')
    female_no = sum(1 for g, q in zip(gender_vals, q_vals) if g == 'Female' and q != 'Yes')
    
    male_total = male_yes + male_no
    female_total = female_yes + female_no
    
    male_pct = male_yes / male_total * 100 if male_total > 0 else 0
    female_pct = female_yes / female_total * 100 if female_total > 0 else 0
    
    table = np.array([[male_yes, male_no], [female_yes, female_no]])
    if table.min() >= 0 and table.sum() > 0:
        chi2, pval, dof, expected = stats.chi2_contingency(table, correction=True)
    else:
        chi2, pval = 0, 1
    
    sig = "*" if pval < 0.05 else "NS"
    label = Q_LABELS[col_idx][:48]
    p(f"{label:<50} {male_pct:>8.1f}% {female_pct:>10.1f}% {chi2:>8.3f} {pval:>10.4f} {sig:>5}")

# ============================================================
#  TABLE 6: CHI-SQUARE: AGE vs KNOWLEDGE/PRACTICE
# ============================================================
p("\n" + "=" * 80)
p("TABLE 6: ASSOCIATION BETWEEN AGE AND RESPONSES (Chi-Square Test)")
p("=" * 80)
p(f"{'Question':<50} {'≤25%':>7} {'26-30%':>8} {'31-40%':>8} {'>40%':>7} {'χ²':>8} {'p-val':>8} {'Sig':>5}")
p("-" * 105)

age_vals = [row[COL['age']].strip() for row in rows]
age_groups = ['<=25', '26-30', '31-40', 'Above 40']

for col_idx in Q_COLS:
    q_vals = [row[col_idx].strip() for row in rows]
    pcts = []
    contingency = []
    
    for ag in age_groups:
        yes = sum(1 for a, q in zip(age_vals, q_vals) if a == ag and q == 'Yes')
        no = sum(1 for a, q in zip(age_vals, q_vals) if a == ag and q != 'Yes')
        total = yes + no
        pcts.append(yes / total * 100 if total > 0 else 0)
        contingency.append([yes, no])
    
    table = np.array(contingency)
    try:
        chi2, pval, dof, expected = stats.chi2_contingency(table, correction=False)
    except:
        chi2, pval = 0, 1
    
    sig = "*" if pval < 0.05 else "NS"
    label = Q_LABELS[col_idx][:48]
    p(f"{label:<50} {pcts[0]:>5.1f}% {pcts[1]:>6.1f}% {pcts[2]:>6.1f}% {pcts[3]:>5.1f}% {chi2:>8.3f} {pval:>8.4f} {sig:>5}")

# ============================================================
#  TABLE 7: CHI-SQUARE: QUALIFICATION vs KNOWLEDGE/PRACTICE
# ============================================================
p("\n" + "=" * 80)
p("TABLE 7: ASSOCIATION BETWEEN QUALIFICATION AND RESPONSES (Chi-Square Test)")
p("=" * 80)
p(f"{'Question':<50} {'Diploma%':>10} {'BSN%':>7} {'PostRN%':>9} {'χ²':>8} {'p-val':>8} {'Sig':>5}")
p("-" * 100)

qual_vals = [row[COL['qual']].strip() for row in rows]
qual_groups = ['Diploma in Nursing', 'BSN', 'Post RN BSCN']

for col_idx in Q_COLS:
    q_vals = [row[col_idx].strip() for row in rows]
    pcts = []
    contingency = []
    
    for qg in qual_groups:
        yes = sum(1 for q, qv in zip(qual_vals, q_vals) if q == qg and qv == 'Yes')
        no = sum(1 for q, qv in zip(qual_vals, q_vals) if q == qg and qv != 'Yes')
        total = yes + no
        pcts.append(yes / total * 100 if total > 0 else 0)
        contingency.append([yes, no])
    
    table = np.array(contingency)
    try:
        chi2, pval, dof, expected = stats.chi2_contingency(table, correction=False)
    except:
        chi2, pval = 0, 1
    
    sig = "*" if pval < 0.05 else "NS"
    label = Q_LABELS[col_idx][:48]
    p(f"{label:<50} {pcts[0]:>8.1f}% {pcts[1]:>5.1f}% {pcts[2]:>7.1f}% {chi2:>8.3f} {pval:>8.4f} {sig:>5}")

# ============================================================
#  OVERALL SUMMARY
# ============================================================
p("\n" + "=" * 80)
p("OVERALL SUMMARY")
p("=" * 80)
p(f"Total Participants: {N}")
p(f"Knowledge Score: Mean = {scores.mean():.2f}/5, SD = {scores.std():.2f}")
p(f"  Good Knowledge (≥4): {sum(1 for s in scores if s >= 4)} ({sum(1 for s in scores if s >= 4)/N*100:.1f}%)")
p(f"Practice Score: Mean = {practice_scores.mean():.2f}/9, SD = {practice_scores.std():.2f}")
p(f"  Good Practice (≥7): {sum(1 for s in practice_scores if s >= 7)} ({sum(1 for s in practice_scores if s >= 7)/N*100:.1f}%)")

# Key findings
p("\nKEY FINDINGS:")
p(f"  1. {sum(1 for v in [row[10].strip() for row in rows] if v=='Yes')/N*100:.1f}% correctly identified HAI transmission via contaminated equipment")
p(f"  2. {sum(1 for v in [row[13].strip() for row in rows] if v=='Yes')/N*100:.1f}% aware of WHO Five Moments of Hand Hygiene")
p(f"  3. {sum(1 for v in [row[15].strip() for row in rows] if v=='Yes')/N*100:.1f}% INCORRECTLY believe clean water alone destroys microorganisms")
p(f"  4. {sum(1 for v in [row[12].strip() for row in rows] if v=='Yes')/N*100:.1f}% report washing hands before/after patient contact")
p(f"  5. {sum(1 for v in [row[18].strip() for row in rows] if v=='Yes')/N*100:.1f}% report PPE always available")
p(f"  6. {sum(1 for v in [row[20].strip() for row in rows] if v=='Yes')/N*100:.1f}% attend IPC training at least once/year")
p(f"  7. {sum(1 for v in [row[22].strip() for row in rows] if v=='Yes')/N*100:.1f}% agree proper IPC improves patient outcomes")

# Save to file
with open(r'c:\Users\AfzalTAS\Desktop\survey\analysis_results.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(output_lines))
print(f"\nResults saved to: analysis_results.txt")
