with open(r'c:\Users\AfzalTAS\Desktop\survey\atiya_research\atiya_research_paper.html', 'r', encoding='utf-8') as f:
    content = f.read()

original_len = len(content)

# Replace all instances of n=99 and n = 99 with n=100
replacements = [
    # sample size mentions
    ('n = 99', 'n = 100'),
    ('n=99', 'n=100'),
    ('n = 99', 'n = 100'),
    # sentences
    ('99 valid responses', '100 valid responses'),
    ('99 complete and valid responses', '100 complete and valid responses'),
    ('among 99 women', 'among 100 women'),
    ('Ninety-nine responses were valid', 'One hundred responses were valid'),
    ('99 women', '100 women'),
    # table captions and figure captions
    ('(n=99)', '(n=100)'),
    ('(n = 99)', '(n = 100)'),
    # text references like "among 99"
    ('among 99', 'among 100'),
    # specific sentences
    ('One response was excluded due to a data recording error', 'One response (age field entered as a letter) was excluded'),
    ('One hundred women filled out', 'One hundred and one women filled out'),
    ('One hundred women submitted responses. However, one entry had to be excluded  the age field was entered as a letter rather than a number, making it impossible to classify. The final sample used in all analysis was therefore <strong>n = 99</strong>.',
     'A total of 101 women submitted responses. One entry was excluded because the age field was entered incorrectly (a letter instead of a number), making it impossible to classify that participant. The final valid sample used in all analysis was therefore <strong>n = 100</strong>.'),
    # The 99 in abstract methods
    ('Ninety-nine responses were valid and included in the analysis (one excluded due to a data recording error).',
     'One hundred responses were valid and included in the analysis (one additional entry excluded due to a data recording error).'),
]

count_total = 0
for old, new in replacements:
    count = content.count(old)
    if count > 0:
        content = content.replace(old, new)
        print(f'Replaced {count}x: "{old[:60]}" -> "{new[:60]}"')
        count_total += count

with open(r'c:\Users\AfzalTAS\Desktop\survey\atiya_research\atiya_research_paper.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f'\nDone. Total replacements: {count_total}')
