import re

html_file = r'c:\Users\AfzalTAS\Desktop\survey\research_paper_complete.html'
with open(html_file, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Abstract
abs_old = r'<div class="abstract">.*?</div>'
abs_new = '''<div class="abstract">
            <h2 id="abstract">Abstract</h2>
            <p><strong>Background:</strong> Hospital-acquired infections (HAIs) are a massive burden on healthcare facilities globally. Since nurses are constantly at the bedside, they act as the primary defense line for infection prevention and control (IPC). Yet, across Pakistan, we keep seeing a disconnect between what nurses know and what they actually do on the ward.</p>
            <p><strong>Objective:</strong> We wanted to figure out the real level of knowledge, daily practices, and institutional roadblocks tied to infection control among the nursing staff at Liaquat University of Medical &amp; Health Sciences (LUMHS) in Jamshoro and Hyderabad.</p>
            <p><strong>Methods:</strong> We ran a descriptive cross-sectional survey involving 103 LUMHS nurses. They filled out a 15-item questionnaire covering what they knew, what they practiced, and what was stopping them. We then crunched the numbers in SPSS 23, looking at basic frequencies and running chi-square tests to spot correlations.</p>
            <p><strong>Results:</strong> Most of our nurses were female (61.2%), firmly in their mid-to-late twenties (46.6%), and had a BSN degree (65.0%). They scored reasonably well on knowledge, averaging 3.61 out of 5, which means about 60.2% had a solid grasp of the basics. Practice scores looked even better on paper (mean 7.31/9, 73.8% "good practice"). But down in the details, we found some startling issues: half (50.5%) genuinely thought plain clean water could kill microbes. Roughly 30.1% admitted to touching body fluids without wearing gloves, and 28.2% hadn't been to an IPC workshop in over a year. Demographics like age and gender didn't really swing the results (p&gt;0.05).</p>
            <p><strong>Conclusion:</strong> Overall, the nurses know what they are supposed to do, but putting it into practice is hit or miss. The biggest hurdles aren't related to individual ignorance—they are systemic. Fixing things like irregular training, hidden guidelines, and empty glove boxes will probably do much more good than just another lecture on hand-washing.</p>
            <div class="keywords">
                <strong>Keywords:</strong> Infection control, nurses, healthcare-associated infections, hand hygiene,
                personal protective equipment, nosocomial infections, tertiary hospital, Pakistan
            </div>
        </div>'''
text = re.sub(abs_old, abs_new, text, flags=re.DOTALL)

# 2. Introduction
intro_old = r'<h2 id="introduction">1\. Introduction</h2>.*?(?=<h2 id="literature">)'
intro_new = '''<h2 id="introduction">1. Introduction</h2>

        <p>Nobody wants to go to the hospital and leave sicker than when they arrived. Yet, hospital-acquired infections (HAIs) are a massive, ongoing crisis worldwide. When patients pick up a new bug during treatment, everything gets worse—recoveries stall, hospital stays stretch on, and medical bills pile up. Because nurses are the ones stationed at the bedside around the clock, they are right in the line of fire for capturing and transmitting these infections.<sup>[<a href="#ref1" title="Reference 1">1</a>]</sup> This risk spikes dramatically in tertiary care centers. Think about it: you have wards packed with immunocompromised patients, lines and tubes everywhere, and constant foot traffic. It\'s essentially the perfect storm for bugs to spread.<sup>[<a href="#ref2" title="Reference 2">2</a>]</sup></p>

        <p>We know exactly how to stop this. According to the World Health Organization, plain old hand hygiene is still the absolute best tool we have to block HAIs.<sup>[<a href="#ref3" title="Reference 3">3</a>]</sup> You pair that with proper masks and gowns, safe needle disposal, and sterile equipment, and infection rates plummet.<sup>[<a href="#ref4" title="Reference 4">4</a>]</sup> But knowing the rules and following them are two very different things. The reality on the ground—especially in under-funded, resource-strapped hospitals—is that staff often miss the mark on these golden standards.<sup>[<a href="#ref5" title="Reference 5">5</a>]</sup></p>

        <p>Time and again, research turns up the same frustrating pattern: a massive gap between what nurses know they should do, and what they actually do during a chaotic shift.<sup>[<a href="#ref1" title="Reference 1">1</a>,<a href="#ref4" title="Reference 4">4</a>,<a href="#ref6" title="Reference 6">6</a>]</sup> A nurse can easily check the right boxes on a protocol exam, while quietly admitting that they skip steps on the ward. Why? The usual suspects: terrible workloads, chronic supply shortages, and a lack of ongoing training.<sup>[<a href="#ref7" title="Reference 7">7</a>,<a href="#ref8" title="Reference 8">8</a>]</sup></p>

        <p>In Pakistan, these challenges hit even harder. The public healthcare system is overwhelmed. Wards are overcrowded, and you frequently see just a handful of nurses managing dozens of patients. Protective supplies run out mid-shift, and administrative oversight is often sketchy at best.<sup>[<a href="#ref2" title="Reference 2">2</a>,<a href="#ref5" title="Reference 5">5</a>]</sup> Picture a nurse grinding through a 12-hour shift, juggling double the normal patient load, staring at an empty glove box, with no manager in sight. That\'s a universe away from the pristine, controlled clinics where international guidelines are drafted. Given that tertiary hospitals deal with the absolute sickest patients in the country, one slip-up can be disastrous. Despite this, we still have very little targeted research looking into these specific high-stakes environments in Pakistan.</p>

        <h3 id="gaps">1.1 Gaps in Current Research</h3>

        <p>While local studies do confirm that Pakistani nurses struggle to match their actions to their knowledge, there are still some glaring blind spots. Most papers treat "knowledge" and "practice" as two separate scores, rarely digging into the actual roadblocks standing in the nurses\' way.<sup>[<a href="#ref1" title="Reference 1">1</a>,<a href="#ref2" title="Reference 2">2</a>,<a href="#ref3" title="Reference 3">3</a>,<a href="#ref4" title="Reference 4">4</a>,<a href="#ref5" title="Reference 5">5</a>]</sup> Plus, nearly everyone relies on self-reported surveys. Naturally, people want to look good on paper, so we are probably seeing inflated compliance rates. Very few researchers are actually standing there to observe what happens.</p>

        <p>Tertiary teaching hospitals are also slipping through the cracks. These massive centers take on regional referrals and house massive ICUs where infection risks hit the ceiling. We still don\'t fully know if the hurdles here are completely different from a rural district hospital. Most critically, researchers tend to treat things like "broken sinks" or "empty supply closets" as minor background noise rather than the primary culprit. When the WHO manual assumes you always have running water and endless sterile gloves, how is a resource-starved nurse actually supposed to prioritize their tasks?</p>

        <h3 id="objectives">1.2 Study Objectives</h3>
        <p>This research examines infection control among nurses in tertiary care settings through four objectives:</p>
        <ol>
            <li>Assess current knowledge levels regarding infection prevention protocols</li>
            <li>Evaluate reported infection control practices during patient care</li>
            <li>Identify institutional, environmental, and individual barriers impeding adherence</li>
            <li>Analyze relationships between demographics, knowledge, practices, and barriers</li>
        </ol>

        <!-- ══════════════════════════════════════════════ -->
        <!--            LITERATURE REVIEW                  -->
        <!-- ══════════════════════════════════════════════ -->
        '''
text = re.sub(intro_old, intro_new, text, flags=re.DOTALL)

# 3. Literature
lit_old = r'<h2 id="literature">2\. Review of Related Literature</h2>.*?(?=<h2 id="methodology">)'
lit_new = '''<h2 id="literature">2. Review of Related Literature</h2>

        <p>When you look back at recent local research, a very distinct pattern emerges. Take Khowaja\'s team, for instance, who surveyed 30 nurses over at the Liaquat Institute in Thatta.<sup>[<a href="#ref1" title="Reference 1">1</a>]</sup> Their findings were pretty clear: the nurses understood the core concepts of infection control perfectly well, but their day-to-day compliance missed the mark. The usual suspects took the blame—not enough continuing education and constantly empty supply closets. What they didn\'t really figure out, though, was the nuance. If you miraculously stocked the hospital with endless gloves, would compliance actually jump? Or is the issue deeper than that?</p>

        <p>Over in Baluchistan, Batool and her colleagues looked at a much larger group—138 nurses stationed across two major Quetta hospitals.<sup>[<a href="#ref2" title="Reference 2">2</a>]</sup> They found some worrying gaps in basic hand hygiene, though oddly, almost everyone claimed to use gloves (99.3%) and masks (97.8%). Interestingly, they looked into attitudes too. Most nurses felt that catching a cold meant you shouldn\'t step foot on the ward, and over three-quarters admitted that local cultural habits speed up the spread of disease. A major takeaway here was the total lack of oversight; poor sanitation and absent ward managers were devastating factors. Interestingly enough, things like age or years on the job made virtually zero difference to how safely someone practiced (p&gt;0.05).</p>

        <p>Meanwhile, Kousar\'s research at Aziz Bhatti Shaheed Hospital in Gujrat found a similar "know-do" gap.<sup>[<a href="#ref3" title="Reference 3">3</a>]</sup> They used the Health Belief Model to unpick why aware nurses still tripped up. Their big push was for dedicated infection control committees. They also found a gender split—female nurses scored significantly higher on knowing when to use antiseptics, use an autoclave, and wash their hands. The catch? The study kind of assumed that hospital committees actually wield power in public Pakistani wards, which isn\'t always reality.</p>

        <p>Right next door in Hyderabad, Soomro\'s team checked on 60 nurses at Isra University Hospital.<sup>[<a href="#ref4" title="Reference 4">4</a>]</sup> The basics looked great—85% routine hand hygiene. But when the stakes got higher, compliance plummeted. Barely half the staff (56.7%) bothered to wear gowns or contact gear when explicitly required, and shockingly, mostly everyone skipped gloves when drawing blood (only 45% complied). It paints a picture of staff handling the easy, routine stuff fine, but dropping the ball entirely during specialized procedures.</p>

        <p>Perhaps the most eye-opening piece of evidence comes from Baqar\'s observational work in Khairpur with 111 nurses.<sup>[<a href="#ref5" title="Reference 5">5</a>]</sup> Surveys are one thing, but actually watching people work tells another story. While 88.3% of the nurses confidently stated that staff need vaccinations, two-thirds of them were actively recapping dirty needles—a massive hazard. Because Baqar directly observed the staff, the truth came out: actual handwashing compliance before an aseptic task was effectively zero (0.9%), and only 19.8% washed up after pulling off gloves. It proved that self-reported surveys are incredibly biased. Much like Kousar, Baqar found that female staff were far stricter with protocol (p=0.000) than their male counterparts.</p>

        <h3 id="synthesis">2.1 Synthesis of Evidence</h3>

        <p>When you stack these five studies together, the narrative is completely unanimous. Pakistani nurses know what to do. They can rattle off the protocols. But walk into almost any ward—whether in Quetta, Gujrat, or Khairpur—and the actual practice on the floor is desperately lagging behind. Everyone points the finger at the same few culprits: crushing workloads, zero resources, and missing training. Yet almost no one has tried to figure out which of those hurdles is the most damaging. Worse still, because nearly every paper relies on nurses self-reporting their own good behavior, the data is heavily padded. As Baqar\'s sneaky observations forcefully proved, what nurses say they do is vastly different from what happens at 2 AM on a chaotic shift.<sup>[<a href="#ref5" title="Reference 5">5</a>]</sup></p>

        <p>This is exactly why the current study matters. By digging into the tertiary setup at LUMHS, we are trying to drag those institutional background barriers into the foreground to see exactly what is crippling our nursing staff\'s ability to protect their patients.</p>

        <!-- ══════════════════════════════════════════════ -->
        <!--              METHODOLOGY                      -->
        <!-- ══════════════════════════════════════════════ -->
        '''
text = re.sub(lit_old, lit_new, text, flags=re.DOTALL)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(text)

print("Part 1 Humanization Complete")
