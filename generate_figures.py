"""
Generate all research figures/charts for the paper.
Saves PNG images to the survey folder.
"""

import csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from collections import Counter
import os

# Style
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 11
plt.rcParams['figure.dpi'] = 200

OUTPUT_DIR = r"c:\Users\AfzalTAS\Desktop\survey\figures"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load data
INPUT = r"c:\Users\AfzalTAS\Desktop\survey\expanded_dataset_103.csv"
with open(INPUT, encoding='utf-8') as f:
    reader = csv.reader(f)
    headers = next(reader)
    rows = list(reader)
N = len(rows)

# Color palette - professional academic colors
COLORS_PIE = ['#2E86AB', '#A23B72', '#F18F01', '#C73E1D', '#3B1F2B']
COLORS_BAR = ['#2E86AB', '#E8505B']
COLORS_BAR3 = ['#2E86AB', '#E8505B', '#F4A261']
COLORS_MULTI = ['#264653', '#2A9D8F', '#E9C46A', '#F4A261', '#E76F51']

COL = {
    'gender': headers.index('1. Gender'),
    'age': headers.index('2. Age (Years)'),
    'marital': headers.index('3. Marital Status'),
    'qual': headers.index('4. Professional Qualification'),
    'dept': headers.index('5. Department'),
}

# ============================================================
#  FIGURE 1: Gender Distribution (Pie Chart)
# ============================================================
fig, ax = plt.subplots(figsize=(6, 5))
vals = Counter([r[COL['gender']] for r in rows])
labels = ['Female', 'Male']
sizes = [vals.get(l, 0) for l in labels]
pcts = [s/N*100 for s in sizes]
wedges, texts, autotexts = ax.pie(sizes, labels=None, autopct='%1.1f%%',
    colors=['#A23B72', '#2E86AB'], startangle=90, 
    wedgeprops={'edgecolor': 'white', 'linewidth': 2},
    textprops={'fontsize': 13, 'fontweight': 'bold'})
ax.legend([f'{l} (n={s})' for l, s in zip(labels, sizes)], 
    loc='lower center', ncol=2, fontsize=11, frameon=False,
    bbox_to_anchor=(0.5, -0.05))
ax.set_title('Figure 1: Gender Distribution of Participants (n=103)', 
    fontsize=13, fontweight='bold', pad=15)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'fig1_gender.png'), bbox_inches='tight', facecolor='white')
plt.close()
print("✅ Figure 1: Gender distribution saved")

# ============================================================
#  FIGURE 2: Age Distribution (Pie Chart)
# ============================================================
fig, ax = plt.subplots(figsize=(6, 5))
age_labels = ['≤25', '26-30', '31-40', 'Above 40']
age_keys = ['<=25', '26-30', '31-40', 'Above 40']
vals = Counter([r[COL['age']] for r in rows])
sizes = [vals.get(k, 0) for k in age_keys]
explode = (0, 0.05, 0, 0)
wedges, texts, autotexts = ax.pie(sizes, labels=None, autopct='%1.1f%%',
    colors=COLORS_PIE[:4], startangle=90, explode=explode,
    wedgeprops={'edgecolor': 'white', 'linewidth': 2},
    textprops={'fontsize': 12, 'fontweight': 'bold'})
ax.legend([f'{l} years (n={s})' for l, s in zip(age_labels, sizes)],
    loc='lower center', ncol=2, fontsize=10, frameon=False,
    bbox_to_anchor=(0.5, -0.08))
ax.set_title('Figure 2: Age Distribution of Participants (n=103)',
    fontsize=13, fontweight='bold', pad=15)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'fig2_age.png'), bbox_inches='tight', facecolor='white')
plt.close()
print("✅ Figure 2: Age distribution saved")

# ============================================================
#  FIGURE 3: Qualification Distribution (Horizontal Bar)
# ============================================================
fig, ax = plt.subplots(figsize=(8, 4))
qual_labels = ['BSN', 'Diploma in Nursing', 'Post RN BSCN']
vals = Counter([r[COL['qual']].strip() for r in rows])
sizes = [vals.get(k, 0) for k in qual_labels]
pcts = [s/N*100 for s in sizes]
bars = ax.barh(qual_labels, pcts, color=['#2E86AB', '#A23B72', '#F18F01'],
    edgecolor='white', height=0.5)
for bar, s, p in zip(bars, sizes, pcts):
    ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
        f'{p:.1f}% (n={s})', va='center', fontsize=11, fontweight='bold')
ax.set_xlabel('Percentage (%)', fontsize=12)
ax.set_xlim(0, 85)
ax.set_title('Figure 3: Professional Qualification Distribution (n=103)',
    fontsize=13, fontweight='bold')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'fig3_qualification.png'), bbox_inches='tight', facecolor='white')
plt.close()
print("✅ Figure 3: Qualification distribution saved")

# ============================================================
#  FIGURE 4: Knowledge Assessment (Grouped Bar Chart)
# ============================================================
Q_KNOWLEDGE = {
    10: 'HAIs via\ncontaminated\nequipment',
    11: 'Nosocomial\ninfection\ndefinition',
    13: 'WHO Five\nMoments\nawareness',
    14: 'All HCWs\npotentially\ninfectious',
    15: 'Clean water\ndestroys\nmicroorganisms*',
}

fig, ax = plt.subplots(figsize=(10, 6))
x = np.arange(len(Q_KNOWLEDGE))
width = 0.28

yes_vals, no_vals, dk_vals = [], [], []
for col_idx in Q_KNOWLEDGE:
    c = Counter([r[col_idx].strip() for r in rows])
    yes_vals.append(c.get('Yes', 0)/N*100)
    no_vals.append(c.get('No', 0)/N*100)
    dk_vals.append(c.get("Don't Know", 0)/N*100)

b1 = ax.bar(x - width, yes_vals, width, label='Yes', color='#2A9D8F', edgecolor='white')
b2 = ax.bar(x, no_vals, width, label='No', color='#E76F51', edgecolor='white')
b3 = ax.bar(x + width, dk_vals, width, label="Don't Know", color='#E9C46A', edgecolor='white')

for bars in [b1, b2, b3]:
    for bar in bars:
        h = bar.get_height()
        if h > 3:
            ax.text(bar.get_x() + bar.get_width()/2, h + 1, f'{h:.0f}%',
                ha='center', va='bottom', fontsize=9, fontweight='bold')

ax.set_ylabel('Percentage (%)', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(list(Q_KNOWLEDGE.values()), fontsize=9)
ax.set_ylim(0, 105)
ax.legend(fontsize=11, loc='upper right')
ax.set_title('Figure 4: Knowledge Assessment Responses (n=103)',
    fontsize=13, fontweight='bold')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.figtext(0.12, 0.01, '*Correct answer is "No" — 50.5% answered incorrectly',
    fontsize=9, fontstyle='italic', color='#666')
plt.tight_layout()
plt.subplots_adjust(bottom=0.08)
plt.savefig(os.path.join(OUTPUT_DIR, 'fig4_knowledge.png'), bbox_inches='tight', facecolor='white')
plt.close()
print("✅ Figure 4: Knowledge assessment saved")

# ============================================================
#  FIGURE 5: Practice Assessment (Horizontal Bar Chart)
# ============================================================
Q_PRACTICE = {
    12: 'Hand washing before/after patient contact',
    22: 'Proper IPC improves patient outcomes',
    18: 'PPE always available when needed',
    19: 'Masks/eye protection during invasive procedures',
    8:  'Periodic IPC training conducted',
    21: 'PPE when handling contaminated waste',
    9:  'IC guidelines available and accessible',
    20: 'Attend IPC training at least once/year',
    16: 'Body fluids never handled with bare hands',
}

fig, ax = plt.subplots(figsize=(10, 7))
labels_p = list(Q_PRACTICE.values())
yes_pcts = []
for col_idx in Q_PRACTICE:
    c = Counter([r[col_idx].strip() for r in rows])
    yes_pcts.append(c.get('Yes', 0)/N*100)

# Sort by percentage (ascending for horizontal bar)
sorted_data = sorted(zip(labels_p, yes_pcts), key=lambda x: x[1])
labels_sorted = [d[0] for d in sorted_data]
pcts_sorted = [d[1] for d in sorted_data]

colors = ['#E76F51' if p < 75 else '#F4A261' if p < 85 else '#2A9D8F' for p in pcts_sorted]
bars = ax.barh(labels_sorted, pcts_sorted, color=colors, edgecolor='white', height=0.6)
for bar, p in zip(bars, pcts_sorted):
    ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2,
        f'{p:.1f}%', va='center', fontsize=10, fontweight='bold')

# Legend
legend_patches = [
    mpatches.Patch(color='#2A9D8F', label='≥85% (Good)'),
    mpatches.Patch(color='#F4A261', label='75-84% (Moderate)'),
    mpatches.Patch(color='#E76F51', label='<75% (Needs Improvement)'),
]
ax.legend(handles=legend_patches, loc='lower right', fontsize=10)
ax.set_xlabel('Percentage Responding "Yes" (%)', fontsize=12)
ax.set_xlim(0, 110)
ax.set_title('Figure 5: Self-Reported Infection Control Practices (n=103)',
    fontsize=13, fontweight='bold')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'fig5_practice.png'), bbox_inches='tight', facecolor='white')
plt.close()
print("✅ Figure 5: Practice assessment saved")

# ============================================================
#  FIGURE 6: Barriers to Infection Control (Bar Chart)
# ============================================================
BARRIER_ITEMS = {
    20: 'Lack of annual\nIPC training',
    9:  'IC guidelines\nnot accessible',
    17: 'Inadequate personal\nHAI knowledge',
    8:  'No periodic\nIPC training',
    18: 'PPE not always\navailable',
}

fig, ax = plt.subplots(figsize=(9, 5))
barrier_labels = list(BARRIER_ITEMS.values())
barrier_pcts = []
for col_idx in BARRIER_ITEMS:
    c = Counter([r[col_idx].strip() for r in rows])
    no_pct = c.get('No', 0)/N*100
    barrier_pcts.append(no_pct)

colors_b = ['#C73E1D' if p > 25 else '#E8505B' if p > 18 else '#F4A261' for p in barrier_pcts]
bars = ax.bar(barrier_labels, barrier_pcts, color=colors_b, edgecolor='white', width=0.6)
for bar, p in zip(bars, barrier_pcts):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
        f'{p:.1f}%', ha='center', va='bottom', fontsize=11, fontweight='bold')

ax.set_ylabel('Percentage Reporting Barrier (%)', fontsize=12)
ax.set_ylim(0, 38)
ax.set_title('Figure 6: Barriers to Infection Control (n=103)',
    fontsize=13, fontweight='bold')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'fig6_barriers.png'), bbox_inches='tight', facecolor='white')
plt.close()
print("✅ Figure 6: Barriers saved")

# ============================================================
#  FIGURE 7: Knowledge vs Practice Scores (Donut Chart)
# ============================================================
CORRECT_ANSWERS = {10: 'Yes', 11: 'Yes', 13: 'Yes', 14: 'Yes', 15: 'No'}
PRACTICE_Qs = [8, 9, 12, 16, 18, 19, 20, 21, 22]

k_scores = []
p_scores = []
for row in rows:
    ks = sum(1 for ci, ca in CORRECT_ANSWERS.items() if row[ci].strip() == ca)
    ps = sum(1 for ci in PRACTICE_Qs if row[ci].strip() == 'Yes')
    k_scores.append(ks)
    p_scores.append(ps)

k_good = sum(1 for s in k_scores if s >= 4)
k_poor = N - k_good
p_good = sum(1 for s in p_scores if s >= 7)
p_poor = N - p_good

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Knowledge donut
sizes_k = [k_good, k_poor]
colors_k = ['#2A9D8F', '#E76F51']
wedges, texts, autotexts = ax1.pie(sizes_k, labels=None, autopct='%1.1f%%',
    colors=colors_k, startangle=90, pctdistance=0.75,
    wedgeprops={'width': 0.4, 'edgecolor': 'white', 'linewidth': 2},
    textprops={'fontsize': 13, 'fontweight': 'bold'})
ax1.text(0, 0, f'Mean\n{np.mean(k_scores):.1f}/5', ha='center', va='center',
    fontsize=14, fontweight='bold', color='#333')
ax1.legend([f'Good ≥4 (n={k_good})', f'Poor <4 (n={k_poor})'],
    loc='lower center', fontsize=10, frameon=False, bbox_to_anchor=(0.5, -0.08))
ax1.set_title('Knowledge Score', fontsize=13, fontweight='bold')

# Practice donut
sizes_p = [p_good, p_poor]
wedges2, texts2, autotexts2 = ax2.pie(sizes_p, labels=None, autopct='%1.1f%%',
    colors=colors_k, startangle=90, pctdistance=0.75,
    wedgeprops={'width': 0.4, 'edgecolor': 'white', 'linewidth': 2},
    textprops={'fontsize': 13, 'fontweight': 'bold'})
ax2.text(0, 0, f'Mean\n{np.mean(p_scores):.1f}/9', ha='center', va='center',
    fontsize=14, fontweight='bold', color='#333')
ax2.legend([f'Good ≥7 (n={p_good})', f'Poor <7 (n={p_poor})'],
    loc='lower center', fontsize=10, frameon=False, bbox_to_anchor=(0.5, -0.08))
ax2.set_title('Practice Score', fontsize=13, fontweight='bold')

fig.suptitle('Figure 7: Overall Knowledge and Practice Scores (n=103)',
    fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'fig7_scores.png'), bbox_inches='tight', facecolor='white')
plt.close()
print("✅ Figure 7: Knowledge vs Practice scores saved")

# ============================================================
#  FIGURE 8: Department-wise Distribution (Bar Chart)
# ============================================================
fig, ax = plt.subplots(figsize=(12, 5))
dept_vals = Counter([r[COL['dept']].strip() for r in rows if r[COL['dept']].strip()])
dept_sorted = dept_vals.most_common(15)  # Top 15 departments
dept_names = [d[0] for d in dept_sorted]
dept_counts = [d[1] for d in dept_sorted]

bars = ax.bar(dept_names, dept_counts, color='#2E86AB', edgecolor='white', width=0.7)
for bar, c in zip(bars, dept_counts):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2,
        str(c), ha='center', va='bottom', fontsize=9, fontweight='bold')

ax.set_ylabel('Number of Participants', fontsize=12)
ax.set_title('Figure 8: Department-wise Distribution of Participants',
    fontsize=13, fontweight='bold')
plt.xticks(rotation=45, ha='right', fontsize=9)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'fig8_departments.png'), bbox_inches='tight', facecolor='white')
plt.close()
print("✅ Figure 8: Department distribution saved")

print(f"\n✅ All 8 figures saved to: {OUTPUT_DIR}")
