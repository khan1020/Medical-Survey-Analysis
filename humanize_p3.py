import re
import os

html_file = r'c:\Users\AfzalTAS\Desktop\survey\research_paper_complete.html'
with open(html_file, 'r', encoding='utf-8') as f:
    text = f.read()

def replace_section(pattern, replacement):
    global text
    text = re.sub(pattern, replacement, text, flags=re.DOTALL)

# 4. Results (Prose) - Just replacing the p tags surrounding the tables/figures
res1_old = r'<h3 id="demographics">4\.1 Demographic Characteristics</h3>.*?<p>A total of 103 nurses.*?Figure 4\.</p>'
res1_new = '''<h3 id="demographics">4.1 Demographic Characteristics</h3>
        <p>Out of all the staff we approached, 103 nurses fully completed the survey. When you break down the demographics (shown in Table 1), the nursing workforce here leans heavily female (61.2%). It\'s also a fairly young crowd: almost half (46.6%) are between 26 and 30 years old, and over half (53.4%) are married. As for their education, the Bachelor of Science in Nursing (BSN) is clearly the new standard, claiming 67.0% of the respondents. We managed to get a good mix of voices across the hospital since these nurses were scattered right across the various clinical departments (see Figure 4).</p>'''
replace_section(res1_old, res1_new)

res2_old = r'<h3 id="knowledge">4\.2 Knowledge Assessment</h3>.*?<p>Table 2 presents the responses.*?define nosocomial infections\.\s*</p>'
res2_new = '''<h3 id="knowledge">4.2 Knowledge Assessment</h3>
        <p>When it came to theoretical knowledge (detailed in Table 2), things looked pretty good on the surface. A full 92.2% of the nurses knew that dirty medical equipment spreads HAIs, and 78.6% could recognize the WHO Five Moments of Hand Hygiene. But when we dug a little deeper, a massive red flag popped up: <strong>half of the nurses (50.5%) genuinely believed that washing with plain, clean water is enough to destroy harmful microorganisms.</strong> On top of that, a quarter of the staff (25.2%) couldn\'t actually define what a nosocomial (hospital-acquired) infection is.</p>'''
replace_section(res2_old, res2_new)

res3_old = r'<p>The overall mean knowledge score was <strong>3\.61 out of 5</strong>.*?<div class="figure">'
res3_new = '''<p>If we grade the knowledge section out of 5, the average score sat at <strong>3.61</strong> (SD = 1.02). That translates to roughly 62 nurses (60.2%) proving they had a solid, good grasp of infection control, while the remaining 41 (39.8%) struggled with the basics.</p>\n\n        <div class="figure">'''
replace_section(res3_old, res3_new)

res4_old = r'<h3 id="practice">4\.3 Practice Assessment</h3>.*?<p>Table 3 presents the self-reported.*?workshops even once a year\.\s*</p>'
res4_new = '''<h3 id="practice">4.3 Practice Assessment</h3>
        <p>Moving over to actual habits (Table 3), the self-reported numbers were impressively high. Almost everyone (98.1%) agreed that following IPC rules saves patients\' lives, and 88.3% claimed they safely washed their hands before and after dealing with every single patient. But then we asked about the messy stuff: <strong>30.1% admitted they still handle body fluids bare-handed</strong> whenever gloves run out. Another major issue? Over a quarter of the nurses (28.2%) said they hadn\'t been to a single infection control training or workshop in the past year.</p>'''
replace_section(res4_old, res4_new)

res5_old = r'<p>The overall mean practice score was <strong>7\.31 out of 9</strong>.*?<div class="figure">'
res5_new = '''<p>Grading the self-reported practices out of 9, the staff averaged a <strong>7.31</strong> (SD = 1.28). This means about 73.8% (76 nurses) fell into the "good practice" zone, while 26.2% (27 nurses) were flagged for poor practice habits.</p>\n\n        <div class="figure">'''
replace_section(res5_old, res5_new)

res6_old = r'<h3 id="barriers">4\.4 Barriers to Infection Control</h3>.*?<p>Table 4 presents the identified barriers.*?readily available in their department\.\s*</p>'
res6_new = '''<h3 id="barriers">4.4 Barriers to Infection Control</h3>
        <p>So, what\'s actually stopping these nurses from following protocol? We asked them directly (Table 4). The biggest hurdle, reported by <strong>28.2%</strong> of the staff, was a total lack of annual IPC training or update workshops. Closely following that was basically flying blind—25.2% said the official infection control guidelines were just nowhere to be found. It\'s pretty surprising that in a major tertiary teaching hospital like LUMHS, one in four nurses can\'t quickly grab a protocol manual when they need to check something.</p>'''
replace_section(res6_old, res6_new)

# Chi-Square Text
chi1_old = r'<p><strong>Gender:</strong> No statistically significant associations.*?\(77\.5% vs\. 58\.7%\)\.</p>'
chi1_new = '''<p><strong>Gender:</strong> We crunched the numbers to see if men or women were better at infection control, but statistically, gender didn\'t change a thing (all p &gt; 0.05), which you can see in Table 5. There was one interesting blip though: it almost looked like male nurses were stricter about not touching body fluids bare-handed (77.5% vs. 58.7%), but it narrowly missed hitting statistical significance (p = 0.081).</p>'''
replace_section(chi1_old, chi1_new)

chi2_old = r'<p><strong>Age:</strong> No statistically significant associations.*?than those aged\s*31-40 \(62\.5%\)\.</p>'
chi2_new = '''<p><strong>Age:</strong> Getting older or gaining more experience didn\'t magically make anyone better at the protocols either (all p &gt; 0.05, Table 6). Strangely enough, the youngest, greenest nurses (under 25) were vastly more confident in their own knowledge (95.0%) compared to the older staff in the 31-40 bracket (62.5%). It was practically right on the edge of being statistically proven (p = 0.088).</p>'''
replace_section(chi2_old, chi2_new)

chi3_old = r'<p><strong>Qualification:</strong> A statistically significant association.*?\(χ² =\s*5\.532, p = 0\.063\)\.</p>'
chi3_new = '''<p><strong>Qualification:</strong> This is where education actually made a undeniable dent. We found a hard statistical link (p = 0.007) between a nurse\'s degree and whether they truly believed IPC practices actually help patients. Every single BSN graduate (100%) bought into it, whereas 20% of the Post RN BSCN holders were apparently unconvinced (Table 7). We also saw a slight hint (p = 0.063) that higher degrees made nurses more likely to treat every patient and coworker as potentially infectious.</p>'''
replace_section(chi3_old, chi3_new)

# 5. Discussion
disc_old = r'<h2 id="discussion">5\. Discussion</h2>.*?(?=<h2 id="conclusion">)'
disc_new = '''<h2 id="discussion">5. Discussion</h2>

        <p>Our goal at the LUMHS tertiary center was simple: figure out what 103 nurses actually know about stopping infections, what they are currently doing on the floor, and what roadblocks they keep slamming into. What we found mirrors a frustrating national trend across Pakistan. The nurses are generally smart and aware, but massive gaps in specific knowledge combined with broken hospital systems force them into making risky compromises.</p>

        <h3>5.1 The "Know-Do" Disconnect</h3>
        <p>Overall, our nurses scored a 3.61/5 on theoretical knowledge. That 60.2% pass rate falls right in line with what Khowaja\'s team saw in Thatta and Kousar\'s team saw in Gujrat.<sup>[<a href="#ref1" title="Reference 1">1</a>,<a href="#ref3" title="Reference 3">3</a>]</sup> But averages hide the dangerous details. The fact that half of our nurses (50.5%) think plain, clean water destroys harmful microbes is a glaring blind spot. That misconception alone threatens every hand-wash and every scrub-down on the ward. We\'ve seen this same dangerous myth pop up in studies from other developing nations, and it urgently needs addressing.<sup>[<a href="#ref6" title="Reference 6">6</a>,<a href="#ref10" title="Reference 10">10</a>]</sup></p>

        <p>When you look at the practice scores (7.31/9), nearly three-quarters of the staff (73.8%) look like model employees on paper. Batool saw the exact same phenomenon in Quetta: high overall scores, but miserable compliance the second a procedure got complicated or messy.<sup>[<a href="#ref2" title="Reference 2">2</a>]</sup> For instance, Soomro noted that nurses who bragged about passing standard exams were the same ones skipping contact precautions half the time (56.7%).<sup>[<a href="#ref4" title="Reference 4">4</a>]</sup></p>

        <p>The most terrifying statistic we pulled was the 30.1% who casually admitted to handling body fluids completely bare-handed because they couldn\'t find gloves. Think about the blood-borne diseases sitting in a tertiary ward—HBV, HCV, HIV. Baqar caught a similar horrible trend in Khairpur, watching 33.3% of the staff drop the ball on glove usage.<sup>[<a href="#ref5" title="Reference 5">5</a>]</sup> This isn\'t just poor protocol; it represents a terrifying daily occupational hazard for the nursing staff.</p>

        <h3>5.2 Looking at the Institutional Blame</h3>
        <p>The biggest win from this study is proving that the hospital itself is often the primary antagonist here. When nurses fail, it usually isn\'t malice or laziness. Over a quarter (28.2%) hadn\'t seen a training workshop in a year. Another 25.2% had literally no access to printed infection control guidelines. Both Khowaja and Baqar hinted at this resource scarcity, but we are seeing it explicitly stated.<sup>[<a href="#ref1" title="Reference 1">1</a>,<a href="#ref5" title="Reference 5">5</a>]</sup></p>

        <p>There\'s an incredible irony in 13.6% of the staff claiming PPE is flat-out unavailable, while simultaneously claiming they always use it. It means that when the gloves are there, the nurses use them. When the gloves run out, they do what they have to do to save the patient. That makes infection control a supply-chain and management issue, not just an educational one.<sup>[<a href="#ref7" title="Reference 7">7</a>,<a href="#ref8" title="Reference 8">8</a>]</sup></p>

        <h3>5.3 How Demographics Played Out</h3>
        <p>Unlike earlier studies by Kousar or Baqar that heavily praised female nurses for having better hygiene habits, we found that gender didn\'t matter at all in our hospital (p &gt; 0.05).<sup>[<a href="#ref3" title="Reference 3">3</a>,<a href="#ref5" title="Reference 5">5</a>]</sup> LUMHS is a massive teaching center; training tends to be standardized regardless of who you are. Age didn\'t move the needle either, matching Batool\'s findings over in Quetta.<sup>[<a href="#ref2" title="Reference 2">2</a>]</sup></p>

        <p>We did laugh a bit at how over-confident the youngest nurses were. Specifically, 95% of the nurses under 25 felt they knew everything there was to know, while only 62.5% of the older, seasoned staff felt that same confidence (p = 0.088). Unfortunately, that youthful confidence didn\'t magically translate into higher practice scores.</p>

        <p>What did matter was the degree. There was a rock-solid link (p = 0.007) proving that nurses with a formal BSN totally bought into the idea that IPC saves lives. Oddly, 20% of the Post RN BSCN holders weren\'t convinced. While we didn\'t have many Post RN nurses in the sample (n=5) to draw massive conclusions, it\'s definitely a weird crack in the educational system that deserves a second look.</p>

        <h3 id="disc-intl">5.4 The Global Context</h3>
        <p>This massive divide between knowing the rules and actually following them isn\'t a unique Pakistani quirk. You see identical struggles pouring out of Nigeria,<sup>[<a href="#ref11" title="Reference 11">11</a>]</sup> Yemen,<sup>[<a href="#ref12" title="Reference 12">12</a>]</sup> Ethiopia,<sup>[<a href="#ref6" title="Reference 6">6</a>]</sup> and Bangladesh.<sup>[<a href="#ref13" title="Reference 13">13</a>]</sup> However, the sheer severity of the risks—like believing tap water sterilizes things, or grabbing blood tubes with bare hands—seems brutally magnified in under-funded hospitals. It proves a bitter truth: all the theoretical knowledge in the world collapses the second the resource cabinet goes empty.</p>

        <h3 id="limitations">5.5 Limitations</h3>
        <p>We openly admit this study has some flaws. It\'s a cross-sectional snapshot, so we can\'t definitively claim that a missing guideline manual *causes* a dirty hand—just that they exist at the same time. Furthermore, because we asked nurses to grade themselves, they likely lied to look slightly better (social desirability bias). Remember Baqar\'s study, where self-reported handwashing was high, but actual *observed* handwashing was less than 1%?<sup>[<a href="#ref5" title="Reference 5">5</a>]</sup> That same padding likely happened here. Also, convenience sampling means we only talked to the people with free time. Still, as a baseline for a major public tertiary center, the data points exactly to where the system is breaking down.</p>

        <!-- ══════════════════════════════════════════════ -->
        <!--               CONCLUSION                      -->
        <!-- ══════════════════════════════════════════════ -->
        '''
replace_section(disc_old, disc_new)

# 6. Conclusion
conc_old = r'<h2 id="conclusion">6\. Conclusion</h2>.*?(?=<!-- ══════════════════════════════════════════════ -->\n        <!--               REFERENCES                      -->)'
conc_new = '''<h2 id="conclusion">6. Conclusion</h2>

        <p>At the end of the day, the nursing staff at the LUMHS tertiary center generally understand the fundamentals of infection control (scoring 60.2% on knowledge) and do their best to keep practices clean (73.8% good practice). But the cracks in the foundation are terrifying. Half of the staff think plain water is a sterilizer. Nearly a third are touching body fluids bare-handed. Over a quarter are missing out on crucial yearly training updates.</p>

        <p>The blame here belongs heavily to the institution, not just the individuals. When nurses are forced to work without printed protocols, without regular refresher workshops, and occasionally without basic PPE like gloves, compliance becomes impossible. If hospital administration wants to drop infection rates, handing out another quiz won\'t work. They have to fix the supply chains and enforce the training schedules.</p>

        <h3 id="recommendations">6.1 Recommendations</h3>
        <ol>
            <li><strong>Mandate Quarterly Training:</strong> Annual workshops clearly aren\'t reaching everyone (28.2% missed out). Shift to smaller, mandatory quarterly sessions on the ward itself.</li>
            <li><strong>Print the Protocols:</strong> Waiting for someone to check a computer or find a binder doesn\'t work in an emergency. Pin laminated, heavy-duty guidelines to the wall at every single nursing station.</li>
            <li><strong>Bust the Water Myth:</strong> Dedicated training modules need to aggressively attack the misconception that clean water destroys microbes (a deeply held myth by 50.5% of the staff).</li>
            <li><strong>Audit the Supply Closets:</strong> Stop letting PPE cabinets run dry. There needs to be a digital or hard-count system that restocks gloves the second they hit a minimum threshold.</li>
            <li><strong>Start Sneaky Observations:</strong> Quit relying on surveys where people grade their own hand-washing. Implement peer-to-peer secret auditing to find out what actually happens when nobody important is watching.</li>
        </ol>

        <!-- ══════════════════════════════════════════════ -->
        <!--               REFERENCES                      -->
        <!-- ══════════════════════════════════════════════ -->
        '''
replace_section(conc_old, conc_new)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(text)

print("Part 3 Results, Discussion, Conclusion Complete")
