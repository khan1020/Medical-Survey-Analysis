import re

html_file = r'c:\Users\AfzalTAS\Desktop\survey\research_paper_complete.html'
with open(html_file, 'r', encoding='utf-8') as f:
    text = f.read()

# Methodology
meth_old = r'<h2 id="methodology">3\. Materials and Methods</h2>.*?(?=<!-- ══════════════════════════════════════════════ -->\n        <!--                 RESULTS                       -->)'
meth_new = '''<h2 id="methodology">3. Materials and Methods</h2>

        <h3 id="design">3.1 Study Design</h3>
        <p>We set this up as a descriptive cross-sectional study. Essentially, we wanted a snapshot of what LUMHS nurses knew about infection prevention, what their actual daily practices looked like, and what roadblocks were stopping them from doing their jobs properly.</p>

        <h3 id="setting">3.2 Study Setting and Duration</h3>
        <p>The research took place at Liaquat University of Medical &amp; Health Sciences (LUMHS), covering both the main Jamshoro campus hospital and the Hyderabad branch. We hit the ground running for data collection between January and February 2026. Since LUMHS is a massive public sector tertiary teaching hospital, we were able to pull nurses from everywhere—Medicine, Surgery, ER, Pediatrics, the ICUs, Cardiology, Gynecology, and the Operation Theaters.</p>

        <h3 id="sample">3.3 Sample Size Calculation</h3>
        <p>To figure out exactly how many people we needed to talk to, we used Slovin\'s formula:</p>
        <p style="text-align:center; font-style:italic; font-size:12pt; margin:15px 0;"><strong>n = N / (1 + N × e²)</strong></p>
        <p>With a total nursing population (N) hovering around 140 across the two hospital campuses, and plugging in a standard 5% margin of error (e = 0.05), the math looked like this: 140 / (1 + 140 × 0.0025) = 140 / 1.35. That gave us an ideal target of roughly <strong>103 participants</strong>.</p>

        <h3 id="sampling">3.4 Sampling Method</h3>
        <p>We went with convenience sampling. Given the crazy rotating shifts and heavy workloads on the wards, we basically approached whoever was on duty, available, and willing to spare a few minutes.</p>

        <h3 id="criteria">3.5 Inclusion and Exclusion Criteria</h3>
        <p><strong>Inclusion:</strong> Any registered staff nurse currently pulling shifts and handling direct patient care at LUMHS was welcome to join. <strong>Exclusion:</strong> We skipped over student nurses, interns, anyone on leave, and administrative staff who weren\'t working directly with patients. And obviously, anyone who was too busy or just didn\'t want to participate was left alone.</p>

        <h3 id="instrument">3.6 Data Collection Instrument</h3>
        <p>We put together a structured, printed questionnaire drawing heavily from WHO guidelines and previous local studies.<sup>[<a href="#ref5" title="Reference 5">5</a>,<a href="#ref9" title="Reference 9">9</a>]</sup> It was split into two straightforward parts:</p>

        <p><strong>Section A (Demographics):</strong> Just the basics—five questions asking for gender, age bracket, marital status, latest nursing degree, and what department they were currently assigned to.</p>

        <p><strong>Section B (Knowledge, Practice, and Barriers):</strong> This was the meat of the survey, featuring 15 items designed for quick "Yes/No/Don\'t Know" answers to save time. We tested their <strong>Knowledge</strong> (asking about WHO hand hygiene moments, universal precautions, and basic water disinfection facts), their <strong>Practice</strong> (if they actually wash their hands, wear PPE, and handle body fluids safely), and the <strong>Barriers</strong> holding them back (like missing guidelines, skipped annual workshops, or empty supply closets).</p>

        <h3 id="procedure">3.7 Data Collection Procedure</h3>
        <p>Instead of sending out links, we physically walked the wards during active shifts at both the Jamshoro and Hyderabad campuses. We explained the point of the study, handed out the papers, and stuck around to clear up any confusing questions. Everyone managed to finish and hand them back the very same day.</p>

        <h3 id="ethics">3.8 Ethical Considerations</h3>
        <p>We made sure to get both verbal and written consent before handing out a single survey. We promised nobody would be named or tracked, keeping all responses entirely anonymous. Participation was completely and strictly voluntary—anyone could walk away with zero consequences. We cleared everything through hospital administration and stuck to the Declaration of Helsinki rules.</p>

        <h3 id="analysis">3.9 Data Analysis</h3>
        <p>Once all the papers were back, everything was fed into IBM SPSS (Version 23). We ran basic descriptive statistics like frequencies and mean scores to get a feel for the demographics. Then, we ran Chi-square (χ²) tests to see if things like age or gender actually impacted knowledge or practice scores, keeping our significance cutoff at the standard p ≤ 0.05.</p>

        '''
text = re.sub(meth_old, meth_new, text, flags=re.DOTALL)


with open(html_file, 'w', encoding='utf-8') as f:
    f.write(text)

print("Part 2.1 Methodology Complete")
