import pandas as pd

df = pd.read_csv(r'Intimate Hygiene Practices Survey (Responses) - Form Responses 1.csv', skiprows=1, header=None)
df.columns = ['Timestamp','Consent','Sec1','Age','Education','Occupation','AgeAtMenarche','Sec2',
              'K1','K2','K3','K4','InfoSource','Sec3','Att1','Att2','Sec4','P1','P2','P3','P4','P5','P6','P7','P8','Email']

print(f'Total rows in CSV (including any headers): {len(df)}')
print()
print('Checking all Age values:')
excluded = []
for i, v in enumerate(df['Age'].values):
    s = str(v).strip().lower().replace(' years','').replace('years','')
    try:
        val = float(s)
        if val < 10 or val > 80:
            print(f'  Row {i+2}: Age="{v}"  *** SUSPICIOUS VALUE ***')
    except:
        print(f'  Row {i+2}: Age="{v}"  *** EXCLUDED - cannot convert to number ***')
        excluded.append((i+2, v))

print()
print(f'Total rows: {len(df)}')
print(f'Excluded rows: {len(excluded)}')
print(f'Valid n = {len(df) - len(excluded)}')
