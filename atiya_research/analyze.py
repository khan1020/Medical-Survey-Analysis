import pandas as pd
from collections import Counter

df = pd.read_csv(r'c:\Users\AfzalTAS\Desktop\survey\atiya_research\Intimate Hygiene Practices Survey (Responses) - Form Responses 1.csv', skiprows=1)
df.columns = [
    'Timestamp','Consent','Sec1','Age','Education','Occupation','AgeAtMenarche','Sec2',
    'KnowledgeMenstruation','CleaningFrequency','ReusableClothSafe','AvoidBathing',
    'InfoSource','Sec3','AttitudeDirty','AttitudeReligious','Sec4','PadMaterial',
    'ChangeFrequency','CleaningMethod','AvoidPhysical','Douching','DryingPlace',
    'SoughtMedicalHelp','DiscussHygiene','Email'
]
df = df.dropna(subset=['Age'])  # remove header/blank rows

# Clean age
def clean_age(x):
    try:
        x = str(x).strip().lower().replace(' years','').replace('years','')
        if x == 'i3': return 13  # Assume typo for 13
        elif x.startswith('i'): return None
        return int(float(x))
    except:
        return None

df['Age_num'] = df['Age'].apply(clean_age)
df = df[df['Age_num'].notna()]
df['Age_num'] = df['Age_num'].astype(int)

n = len(df)
print(f"Total valid responses: {n}")

# Age groups
def age_group(a):
    if a <= 19: return '13-19 (Adolescent)'
    elif a <= 25: return '20-25 (Young Adult)'
    elif a <= 35: return '26-35 (Adult)'
    else: return '36+ (Older Adult)'

df['AgeGroup'] = df['Age_num'].apply(age_group)
print("\n--- Age Distribution ---")
ag = df['AgeGroup'].value_counts().reindex(['13-19 (Adolescent)','20-25 (Young Adult)','26-35 (Adult)','36+ (Older Adult)'])
for k,v in ag.items(): print(f"  {k}: {v} ({v/n*100:.1f}%)")

print(f"\nAge: Min={df['Age_num'].min()}, Max={df['Age_num'].max()}, Mean={df['Age_num'].mean():.1f}")

print("\n--- Education Level ---")
ed = df['Education'].value_counts()
for k,v in ed.items(): print(f"  {k}: {v} ({v/n*100:.1f}%)")

print("\n--- Occupation ---")
oc = df['Occupation'].value_counts()
for k,v in oc.items(): print(f"  {k}: {v} ({v/n*100:.1f}%)")

# education grouping
def edu_group(e):
    e = str(e).strip()
    if e in ['No formal education','Primary education']: return 'Low Education'
    elif e in ['Secondary education (High School)','Higher secondary education (Intermediate/A-Levels)']: return 'Moderate Education'
    elif e in ['Graduate or above (Bachelor\'s degree or higher)']: return 'High Education'
    else: return 'Unknown'

df['EduGroup'] = df['Education'].apply(edu_group)
print("\n--- Education Groups ---")
eg = df['EduGroup'].value_counts()
for k,v in eg.items(): print(f"  {k}: {v} ({v/n*100:.1f}%)")

print("\n--- Knowledge: Menstruation ---")
km = df['KnowledgeMenstruation'].value_counts()
for k,v in km.items(): print(f"  {k}: {v} ({v/n*100:.1f}%)")

print("\n--- Knowledge: Cleaning Frequency ---")
cf = df['CleaningFrequency'].value_counts()
for k,v in cf.items(): print(f"  {k}: {v} ({v/n*100:.1f}%)")

print("\n--- Knowledge: Reusable Cloth Safe? ---")
rc = df['ReusableClothSafe'].value_counts()
for k,v in rc.items(): print(f"  {k}: {v} ({v/n*100:.1f}%)")

print("\n--- Knowledge: Avoid Bathing? ---")
ab = df['AvoidBathing'].value_counts()
for k,v in ab.items(): print(f"  {k}: {v} ({v/n*100:.1f}%)")

print("\n--- Information Source ---")
inf = df['InfoSource'].value_counts()
for k,v in inf.items(): print(f"  {k}: {v} ({v/n*100:.1f}%)")

print("\n--- Attitude: Menstruation is Dirty ---")
ad = df['AttitudeDirty'].value_counts()
for k,v in ad.items(): print(f"  {k}: {v} ({v/n*100:.1f}%)")

print("\n--- Attitude: Avoid Religious Activities ---")
ar = df['AttitudeReligious'].value_counts()
for k,v in ar.items(): print(f"  {k}: {v} ({v/n*100:.1f}%)")

print("\n--- Practice: Pad Material Used ---")
pm = df['PadMaterial'].value_counts()
for k,v in pm.items(): print(f"  {k}: {v} ({v/n*100:.1f}%)")

print("\n--- Practice: Change Frequency ---")
chf = df['ChangeFrequency'].value_counts()
for k,v in chf.items(): print(f"  {k}: {v} ({v/n*100:.1f}%)")

print("\n--- Practice: Cleaning Method ---")
cm = df['CleaningMethod'].value_counts()
for k,v in cm.items(): print(f"  {k}: {v} ({v/n*100:.1f}%)")

print("\n--- Practice: Avoid Physical Activity ---")
ap = df['AvoidPhysical'].value_counts()
for k,v in ap.items(): print(f"  {k}: {v} ({v/n*100:.1f}%)")

print("\n--- Practice: Douching ---")
do = df['Douching'].value_counts()
for k,v in do.items(): print(f"  {k}: {v} ({v/n*100:.1f}%)")

print("\n--- Practice: Drying Place ---")
dp = df['DryingPlace'].value_counts()
for k,v in dp.items(): print(f"  {k}: {v} ({v/n*100:.1f}%)")

print("\n--- Practice: Sought Medical Help ---")
smh = df['SoughtMedicalHelp'].value_counts()
for k,v in smh.items(): print(f"  {k}: {v} ({v/n*100:.1f}%)")

print("\n--- Practice: Discuss Hygiene ---")
dh = df['DiscussHygiene'].value_counts()
for k,v in dh.items(): print(f"  {k}: {v} ({v/n*100:.1f}%)")

# Age at Menarche
df['Menarche_num'] = pd.to_numeric(df['AgeAtMenarche'], errors='coerce')
valid_m = df['Menarche_num'].dropna()
print(f"\n--- Age at Menarche ---")
print(f"  Mean: {valid_m.mean():.1f}, Min: {valid_m.min()}, Max: {valid_m.max()}, n={len(valid_m)}")
