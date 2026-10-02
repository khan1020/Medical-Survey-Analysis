import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

out = r'c:\Users\AfzalTAS\Desktop\survey\atiya_research\figures'
os.makedirs(out, exist_ok=True)

COLORS = ['#2E86AB','#A23B72','#F18F01','#C73E1D','#3B1F2B','#44BBA4','#E94F37','#393E41']
TEAL = '#2E86AB'
ROSE = '#A23B72'
ORANGE = '#F18F01'

def save(name):
    plt.tight_layout()
    plt.savefig(os.path.join(out, name), dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"Saved {name}")

# ── Fig 1: Age Distribution ──────────────────────────────────────────
labels = ['13–19\n(Adolescent)', '20–25\n(Young Adult)', '26–35\n(Adult)', '36+\n(Older Adult)']
vals   = [27, 61, 11, 1]
pcts   = [f'{v} ({v/100*100:.1f}%)' for v in vals]
fig, ax = plt.subplots(figsize=(8,5))
bars = ax.bar(labels, vals, color=[TEAL, ROSE, ORANGE, '#44BBA4'], edgecolor='white', linewidth=1.5)
for bar, pct in zip(bars, pcts):
    ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.5, pct, ha='center', va='bottom', fontsize=10, fontweight='bold')
ax.set_title('Figure 1: Age Distribution of Participants (n=100)', fontsize=13, fontweight='bold')
ax.set_ylabel('Number of Participants')
ax.set_ylim(0, 75)
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
save('fig1_age.png')

# ── Fig 2: Education Level (Pie) ─────────────────────────────────────
ed_labels = ['Higher Secondary\n(Intermediate)', 'Graduate &\nAbove', 'Secondary\n(High School)', 'Primary\nEducation', 'No Formal\nEducation', 'Not\nSpecified']
ed_vals   = [35, 29, 13, 12, 6, 5]
fig, ax = plt.subplots(figsize=(8,6))
wedges, texts, autotexts = ax.pie(ed_vals, labels=None, autopct='%1.1f%%', colors=COLORS[:6], startangle=140, pctdistance=0.75)
for at in autotexts: at.set_fontsize(9); at.set_fontweight('bold')
ax.legend(wedges, [f'{l} (n={v})' for l,v in zip(ed_labels, ed_vals)], loc='lower center', bbox_to_anchor=(0.5,-0.15), ncol=2, fontsize=9)
ax.set_title('Figure 2: Education Level Distribution (n=100)', fontsize=13, fontweight='bold')
save('fig2_education.png')

# ── Fig 3: Occupation ────────────────────────────────────────────────
occ_labels = ['Student','Housewife','Employed','Unemployed/Other']
occ_vals   = [63, 21, 12, 3]
fig, ax = plt.subplots(figsize=(7,5))
bars = ax.barh(occ_labels, occ_vals, color=[TEAL, ROSE, ORANGE, '#44BBA4'], edgecolor='white')
for bar, v in zip(bars, occ_vals):
    ax.text(bar.get_width()+0.5, bar.get_y()+bar.get_height()/2, f'{v} ({v/100*100:.1f}%)', va='center', fontsize=10, fontweight='bold')
ax.set_title('Figure 3: Occupation Distribution (n=100)', fontsize=13, fontweight='bold')
ax.set_xlabel('Number of Participants')
ax.set_xlim(0, 80)
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
save('fig3_occupation.png')

# ── Fig 4: Knowledge - Menstruation ──────────────────────────────────
k_labels = ['Normal\nPhysiological\nProcess', 'Disease\nor Illness', 'Do Not\nKnow']
k_vals   = [96, 3, 1]
fig, ax = plt.subplots(figsize=(7,5))
bars = ax.bar(k_labels, k_vals, color=[TEAL, '#C73E1D', ORANGE], edgecolor='white', linewidth=1.5)
for bar, v in zip(bars, k_vals):
    ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.3, f'{v} ({v/100*100:.1f}%)', ha='center', fontsize=10, fontweight='bold')
ax.set_title('Figure 4: Knowledge About Menstruation (n=100)', fontsize=13, fontweight='bold')
ax.set_ylabel('Number of Participants')
ax.set_ylim(0, 110)
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
save('fig4_knowledge_menstruation.png')

# ── Fig 5: Information Source ─────────────────────────────────────────
src_labels = ['Mother','Doctor','Teacher/\nSchool','Media','Family','Do Not\nKnow']
src_vals   = [51, 18, 16, 7, 6, 2]
fig, ax = plt.subplots(figsize=(8,5))
bars = ax.bar(src_labels, src_vals, color=COLORS[:6], edgecolor='white', linewidth=1.5)
for bar, v in zip(bars, src_vals):
    ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.3, f'{v}\n({v/100*100:.1f}%)', ha='center', fontsize=9, fontweight='bold')
ax.set_title('Figure 5: Primary Sources of Hygiene Information (n=100)', fontsize=13, fontweight='bold')
ax.set_ylabel('Number of Participants')
ax.set_ylim(0, 62)
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
save('fig5_info_source.png')

# ── Fig 6: Pad Material Used ──────────────────────────────────────────
pm_labels = ['Disposable\nSanitary Pads', 'Reusable\nCloth', 'Homemade\nPads', 'Other']
pm_vals   = [80, 11, 8, 1]
fig, ax = plt.subplots(figsize=(7,5))
wedges, texts, autotexts = ax.pie(pm_vals, labels=None, autopct='%1.1f%%', colors=[TEAL, ROSE, ORANGE, '#44BBA4'], startangle=90, pctdistance=0.75)
for at in autotexts: at.set_fontsize(10); at.set_fontweight('bold')
ax.legend(wedges, [f'{l} (n={v})' for l,v in zip(pm_labels, pm_vals)], loc='lower center', bbox_to_anchor=(0.5,-0.15), ncol=2, fontsize=9)
ax.set_title('Figure 6: Primary Menstrual Material Used (n=100)', fontsize=13, fontweight='bold')
save('fig6_pad_material.png')

# ── Fig 7: Key Practice Items (Grouped Bar) ───────────────────────────
practice_items = [
    'Change Frequency\n(Recommended)',
    'Cleaning Method\n(Soap & Water)',
    'Avoid Physical\nActivity',
    'Vaginal\nDouching (Yes)',
    'Dry in Sunlight\n(Recommended)',
    'Sought Medical\nHelp',
    'Discuss Openly'
]
correct_pcts  = [63.0, 35.0, 41.0+34.0, 32.0+17.0, 36.0, 56.0, 45.0]
# simplified: correct/positive practice %
correct_n = [63, 35, 75, 49, 36, 56, 45]
incorrect_n = [37, 65, 25, 51, 64, 44, 55]

x = np.arange(len(practice_items))
width = 0.35
fig, ax = plt.subplots(figsize=(13,6))
b1 = ax.bar(x - width/2, correct_n, width, label='Correct/Positive Practice', color=TEAL, edgecolor='white')
b2 = ax.bar(x + width/2, incorrect_n, width, label='Incorrect/Negative Practice', color='#C73E1D', edgecolor='white')
for bar in b1:
    ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.5, str(int(bar.get_height())), ha='center', fontsize=8, fontweight='bold')
for bar in b2:
    ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.5, str(int(bar.get_height())), ha='center', fontsize=8, fontweight='bold')
ax.set_title('Figure 7: Practice Assessment – Correct vs. Incorrect Responses (n=100)', fontsize=13, fontweight='bold')
ax.set_xticks(x); ax.set_xticklabels(practice_items, fontsize=9)
ax.set_ylabel('Number of Participants')
ax.set_ylim(0, 110)
ax.legend()
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
save('fig7_practices.png')

# ── Fig 8: Attitudes ──────────────────────────────────────────────────
att_cats = ['Strongly\nAgree', 'Agree', 'Neutral', 'Disagree', 'Strongly\nDisagree']
dirty    = [11, 28, 25, 22, 13]
religious= [46, 28, 8, 7, 11]

x = np.arange(len(att_cats))
width = 0.35
fig, ax = plt.subplots(figsize=(10,5))
b1 = ax.bar(x - width/2, dirty, width, label='Menstruation is Dirty', color=ROSE, edgecolor='white')
b2 = ax.bar(x + width/2, religious, width, label='Should Avoid Religious Activities', color=TEAL, edgecolor='white')
for bar in b1:
    ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.3, str(int(bar.get_height())), ha='center', fontsize=9, fontweight='bold')
for bar in b2:
    ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.3, str(int(bar.get_height())), ha='center', fontsize=9, fontweight='bold')
ax.set_title('Figure 8: Attitudes Toward Menstruation (n=100)', fontsize=13, fontweight='bold')
ax.set_xticks(x); ax.set_xticklabels(att_cats)
ax.set_ylabel('Number of Participants')
ax.set_ylim(0, 58)
ax.legend()
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
save('fig8_attitudes.png')

# ── Fig 9: Discuss hygiene (Pie) ──────────────────────────────────────
dh_labels = ['Yes, Openly\n& Comfortably', 'Rarely, Only\nWhen Necessary', 'No, Keep\nIt Private']
dh_vals   = [45, 40, 15]
fig, ax = plt.subplots(figsize=(7,5))
wedges, texts, autotexts = ax.pie(dh_vals, labels=None, autopct='%1.1f%%', colors=[TEAL, ORANGE, '#C73E1D'], startangle=120, pctdistance=0.75)
for at in autotexts: at.set_fontsize(11); at.set_fontweight('bold')
ax.legend(wedges, [f'{l} (n={v})' for l,v in zip(dh_labels, dh_vals)], loc='lower center', bbox_to_anchor=(0.5,-0.12), ncol=1, fontsize=10)
ax.set_title('Figure 9: Willingness to Discuss Intimate Hygiene (n=100)', fontsize=13, fontweight='bold')
save('fig9_discuss.png')

print("All figures saved!")
