# NOTES — news-image-20261124 research (24 Nov 2026, WIB)

Prep + build in this session (started after the competition opened).
Competition: free, deadline 26 Nov 2026 07:00 WIB (entries close
2026-11-26T00:00:00Z), $100 shared by top 50 (1st $20, 2nd $12, 3rd $6,
4th–10th $2, 11th–50th $1.20). Blind rounds: next round cutoff
2026-11-24T12:00:00Z (19:00 WIB today). Quota checked 24 Nov: 0 entries
made, day cap 6, can_submit true, blind-round slot available.
Kit: ~/workspace/makefun/news-image-20261124-kit/ (RULES.txt read).
Image: PNG, ≤1 MiB, ≤1024×1024, deterministic, no network.
Judge: z-ai/glm-5.3-flash, no news feed, does not know the day. Criteria
in order: (1) names the day + specific events of that day, date shown;
(2) breadth across regions/fields; (3) readable from the image alone;
(4) faithful, no hype/speculation as fact; (5) clean craft, legible
~300px, no garbled text. Front page must say "TUESDAY 24 NOVEMBER 2026".

## Stories verified (each against ≥2 sources, 24 Nov 2026 news cycle)

1. **HERO — Russian jets spark air-raid alert off Korea.**
   Several Russian military aircraft entered the Korea Air Defense
   Identification Zone (KADIZ) over the East Sea on Tuesday morning
   24 Nov and approached Ulleung Island; South Korea issued an air-raid
   alert at 07:52 local, told islanders to take shelter, scrambled
   fighter jets; alert lifted ~07:57; Joint Chiefs: no violation of
   sovereign airspace; Seoul to summon Russia's defence attaché to
   protest. Sources: Reuters, AP, Yonhap (via JKN), AJU Press.
2. **Iran — Tehran demands $290bn from the US.**
   Iranian courts awarded $290bn in damages against the US, judiciary
   official Hassan Abdolianpour announced on state TV; claims cover US
   actions over decades; lawsuits also filed against Gulf Arab states
   for letting the US use their territory; Iran vows to end the US naval
   blockade "by all available means". Sources: AFP (via South Punjab
   News), Trust Radio (24 Nov), DailyFoxNews / Reuters daily brief.
3. **Indonesia — 26 dead named, 28 still missing after factory fire.**
   Banten DVI identified 26 body bags on Tuesday 24 Nov from the
   PT Fonusa Agung Mulia candy factory fire in Cikande, Serang (fire
   Sat 21 Nov, ~300 inside); 28 workers still missing; DNA samples
   taken from relatives. Sources: thedaily.id (24 Nov), r24.mv
   (24 Nov), People (24 Nov).
4. **Nvidia — Huang back as CEO; shares soar.**
   Nvidia's board unanimously reinstated Jensen Huang as president, CEO
   and director on Monday 23 Nov, 11 days after his resignation, after
   pressure from Trump; the US Commerce Department blacklisted
   Megaspeed the same day; Nvidia shares jumped 30%+ in pre-market
   trading. Sources: NY Post, Reuters (24 Nov), CNN, The Times,
   CEOWORLD (published 24 Nov).
5. **Mexico — El Chapo Isidro to be tried at home.**
   Attorney General Ernestina Godoy said Monday 23 Nov that Mexico will
   try Fausto Isidro Meza Flores ("El Chapo Isidro") in Mexico despite
   a US extradition request; captured Fri 20 Nov in Guasave, Sinaloa,
   in an operation that killed 4 soldiers and 16 gunmen; held at
   Altiplano prison. Sources: Reuters, Al Jazeera, Devdiscourse
   (published 24 Nov).
6. **Footer — also today.**
   Car bomb hits the Meta governor's office in Villavicencio, Colombia
   (Monday night; injured toll rises to 23 on Tuesday) — Al Jazeera,
   El Tiempo (via Global Incident Tracker), QNC News. UN chief
   Guterres calls for a global AI risk framework within a year at the
   Bridgetown summit — AFP, QNC News, NewsCentralTV (24 Nov). Final
   Spain polls put PP+Vox on course for a majority in the 29 Nov
   election — Reuters, Breitbart.

## Timing note (honest)

The Korea air scare and the Banten identification update happened on
Tuesday 24 Nov itself. The Iran $290bn announcement, the Nvidia
reinstatement, the El Chapo Isidro trial decision, the Colombia bombing
and the UN/Spain items were announced on Monday 23 Nov (US/Europe
daytime) and are Tuesday 24 Nov's news cycle in world outlets — the
same convention as the 23 Nov entry (Saturday strikes counted for
Monday). Nothing in the image predates 13 November 2026. Label the
image "TUESDAY 24 NOVEMBER 2026".

## Design plan (fresh builder, not a copy of the 23 Nov draw script)

Front page, 1024×1024 PNG, drawn from scratch with PIL (flat vector,
Montserrat Bold/ExtraBold — no photos, no screenshots, no copied
artwork). Masthead "THE WORLD TODAY" + date. Hero panel: Korea air
scare — text on the LEFT, illustration on the RIGHT (island, radar
rings, jets, red alert triangle; the 23 Nov hero had art left, text
right). 2×2 grid: Iran, Indonesia, Nvidia, Mexico — icon box on the
RIGHT of each card this time. Bottom ticker: Colombia + UN AI + Spain
polls. Re-read the render twice; watch for headline/deck overflow in
cards and footer cutoff (the two defects fixed on 21 Nov). Keep text
short, large, high contrast.
