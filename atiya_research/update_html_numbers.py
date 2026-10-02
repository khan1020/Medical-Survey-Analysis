import re

with open('atiya_research_paper.html', 'r', encoding='utf-8') as f:
    text = f.read()

replacements = {
    # Text changes
    '99 valid responses': '100 valid responses',
    '99 complete and valid responses': '100 complete and valid responses',
    'among 99 women': 'among 100 women',
    'Ninety-nine responses were valid': 'One hundred responses were valid',
    '99 women': '100 women',
    'One hundred women submitted responses. However, one entry had to be excluded  the age field was entered as a letter rather than a number, making it impossible to classify. The final sample used in all analysis was therefore <strong>n = 99</strong>.': 'One hundred women submitted responses. One age entry ("I3") was identified as a typographical error for 13, supported by corresponding adolescent data points, and was normalized for analysis. The final valid sample was <strong>n = 100</strong>.',
    '(n=99)': '(n=100)',
    '(n = 99)': '(n = 100)',
    'n = 99': 'n = 100',
    'n=99': 'n=100',

    # Table 1: Demographics
    '20–25 years (61.6%)': '20–25 years (61.0%)',
    'mean age of 21.5': 'mean age of 21.4',
    '(63.6%)': '(63.0%)',
    '6.1%': '6.0%',
    
    '<td>26</td>\n                    <td>26.3%</td>': '<td>27</td>\n                    <td>27.0%</td>',
    '<td>61</td>\n                    <td>61.6%</td>': '<td>61</td>\n                    <td>61.0%</td>',
    '<td>11</td>\n                    <td>11.1%</td>': '<td>11</td>\n                    <td>11.0%</td>',
    '<td>1</td>\n                    <td>1.0%</td>': '<td>1</td>\n                    <td>1.0%</td>',

    '<td>35</td>\n                    <td>35.4%</td>': '<td>35</td>\n                    <td>35.0%</td>',
    '<td>29</td>\n                    <td>29.3%</td>': '<td>29</td>\n                    <td>29.0%</td>',
    '<td>13</td>\n                    <td>13.1%</td>': '<td>13</td>\n                    <td>13.0%</td>',
    '<td>11</td>\n                    <td>11.1%</td>': '<td>12</td>\n                    <td>12.0%</td>',
    '<td>6</td>\n                    <td>6.1%</td>': '<td>6</td>\n                    <td>6.0%</td>',
    
    '<td>63</td>\n                    <td>63.6%</td>': '<td>63</td>\n                    <td>63.0%</td>',
    '<td>20</td>\n                    <td>20.2%</td>': '<td>21</td>\n                    <td>21.0%</td>',
    '<td>12</td>\n                    <td>12.1%</td>': '<td>12</td>\n                    <td>12.0%</td>',
    '<td>3</td>\n                    <td>3.0%</td>': '<td>3</td>\n                    <td>3.0%</td>',

    # Table 2: Knowledge
    '97.0%': '96.0%',
    '40.4%': '41.0%',
    '56.6%': '56.0%',
    '50.5%': '51.0%',
    '18.2%': '18.0%',
    '16.2%': '16.0%',
    '<td>96</td>\n                    <td>97.0%</td>': '<td>96</td>\n                    <td>96.0%</td>',
    '<td>2</td>\n                    <td>2.0%</td>': '<td>3</td>\n                    <td>3.0%</td>',
    
    '<td>71</td>\n                    <td>71.7%</td>': '<td>71</td>\n                    <td>71.0%</td>',
    '<td>19</td>\n                    <td>19.2%</td>': '<td>20</td>\n                    <td>20.0%</td>',
    '<td>8</td>\n                    <td>8.1%</td>': '<td>8</td>\n                    <td>8.0%</td>',
    
    '<td>56</td>\n                    <td>56.6%</td>': '<td>56</td>\n                    <td>56.0%</td>',
    '<td>25</td>\n                    <td>25.3%</td>': '<td>26</td>\n                    <td>26.0%</td>',
    '<td>14</td>\n                    <td>14.1%</td>': '<td>14</td>\n                    <td>14.0%</td>',
    '<td>4</td>\n                    <td>4.0%</td>': '<td>4</td>\n                    <td>4.0%</td>',

    '<td>40</td>\n                    <td>40.4%</td>': '<td>41</td>\n                    <td>41.0%</td>',
    '<td>31</td>\n                    <td>31.3%</td>': '<td>31</td>\n                    <td>31.0%</td>',
    '*40.4% (n=40)': '*41.0% (n=41)',

    # Table 3: Info Source
    '<td>50</td>\n                    <td>50.5%</td>': '<td>51</td>\n                    <td>51.0%</td>',
    '<td>18</td>\n                    <td>18.2%</td>': '<td>18</td>\n                    <td>18.0%</td>',
    '<td>16</td>\n                    <td>16.2%</td>': '<td>16</td>\n                    <td>16.0%</td>',
    '<td>7</td>\n                    <td>7.1%</td>': '<td>7</td>\n                    <td>7.0%</td>',
    '<td>6</td>\n                    <td>6.1%</td>': '<td>6</td>\n                    <td>6.0%</td>',

    # Table 4: Attitudes
    '38.4%': '39.0%',
    '35.3%': '35.0%',
    '73.8%': '74.0%',
    '<td>11 (11.1%)</td>': '<td>11 (11.0%)</td>',
    '<td>27 (27.3%)</td>': '<td>28 (28.0%)</td>',
    '<td>25 (25.3%)</td>': '<td>25 (25.0%)</td>',
    '<td>22 (22.2%)</td>': '<td>22 (22.0%)</td>',
    '<td>13 (13.1%)</td>': '<td>13 (13.0%)</td>',
    
    '<td>45 (45.5%)</td>': '<td>46 (46.0%)</td>',
    '<td>28 (28.3%)</td>': '<td>28 (28.0%)</td>',
    '<td>8 (8.1%)</td>': '<td>8 (8.0%)</td>',
    '<td>7 (7.1%)</td>': '<td>7 (7.0%)</td>',

    # Table 5: Practices
    '79.8%': '80.0%',
    '63.6%': '63.0%',
    '20.2%': '21.0%',
    '55.6%': '55.0%',
    '9.1%': '10.0%',
    '32.3%': '32.0%',
    '17.2%': '17.0%',
    '49.5%': '50.0%',
    
    '<td>79</td>\n                    <td>79.8%</td>': '<td>80</td>\n                    <td>80.0%</td>',
    '<td>11</td>\n                    <td>11.1%</td>': '<td>11</td>\n                    <td>11.0%</td>',
    '<td>8</td>\n                    <td>8.1%</td>': '<td>8</td>\n                    <td>8.0%</td>',
    
    '<td>63</td>\n                    <td>63.6%</td>': '<td>63</td>\n                    <td>63.0%</td>',
    '<td>20</td>\n                    <td>20.2%</td>': '<td>21</td>\n                    <td>21.0%</td>',
    '<td>14</td>\n                    <td>14.1%</td>': '<td>14</td>\n                    <td>14.0%</td>',

    '<td>55</td>\n                    <td>55.6%</td>': '<td>55</td>\n                    <td>55.0%</td>',
    '<td>35</td>\n                    <td>35.4%</td>': '<td>35</td>\n                    <td>35.0%</td>',
    '<td>9</td>\n                    <td>9.1%</td>': '<td>10</td>\n                    <td>10.0%</td>',

    '<td>41</td>\n                    <td>41.4%</td>': '<td>41</td>\n                    <td>41.0%</td>',
    '<td>34</td>\n                    <td>34.3%</td>': '<td>34</td>\n                    <td>34.0%</td>',
    '<td>23</td>\n                    <td>23.2%</td>': '<td>24</td>\n                    <td>24.0%</td>',

    '<td>49</td>\n                    <td>49.5%</td>': '<td>50</td>\n                    <td>50.0%</td>',
    '<td>32</td>\n                    <td>32.3%</td>': '<td>32</td>\n                    <td>32.0%</td>',
    '<td>17</td>\n                    <td>17.2%</td>': '<td>17</td>\n                    <td>17.0%</td>',

    '<td>55</td>\n                    <td>55.6%</td>': '<td>56</td>\n                    <td>56.0%</td>',
    '<td>44</td>\n                    <td>44.4%</td>': '<td>44</td>\n                    <td>44.0%</td>',

    '<td>45</td>\n                    <td>45.5%</td>': '<td>45</td>\n                    <td>45.0%</td>',
    '<td>39</td>\n                    <td>39.4%</td>': '<td>40</td>\n                    <td>40.0%</td>',
    '<td>15</td>\n                    <td>15.2%</td>': '<td>15</td>\n                    <td>15.0%</td>',

    # Bullet points / Summary / Figures 
    '75.7%': '75.0%',
    '41.4%': '41.0%',
    '34.3%': '34.0%',
    '8.1%': '8.0%',
    '45.5%': '45.0%',
    '39.4%': '40.0%',
    '15.2%': '15.0%',
}

for old, new in replacements.items():
    text = text.replace(old, new)

with open('atiya_research_paper.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated HTML percentages and n logic.')
