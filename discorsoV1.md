# Thesis Defense Speech (English) — target 10 minutes

*Legend: `[PAUSE]`, `[SLOW DOWN HERE]`, `[SHOW SLIDE: ...]` are stage directions for you — do not read them aloud. Section headers (`##`) are navigation aids only.*

---

## 1. Opening (30 sec)

Good afternoon to the members of the committee and to everyone here. My name is Jacopo Garau. [PAUSE]

Today I will present my Master's thesis in Electronic Engineering. The work was carried out at Mid Sweden University during my Erasmus for Traineeship program, under the supervision of Professor Alessandro Pozzebon, Professor Sebastian Bader, and Doctor Ye Xu.

The goal of my project was to design and implement an interface able to extract the maximum power from a six-phase energy harvester. [SHOW SLIDE: Title]

---

## 2. Context and motivation

Wireless sensor networks and IoT devices have grown very fast in recent years. This creates a simple but important problem: how do we power millions of small devices without constantly replacing their batteries? Batteries are expensive to maintain, and are often not even possible to replace, and also they are not good for the planet.

Energy harvesting comes as a solution to those problems.
What does energy harvesting mean? It means capturing small amounts of ambient energy — vibration, heat, or light — and turning it into electricity. [SHOW SLIDE: Energy harvesting overview]

My thesis focuses on collecting electric power from rotating motion using a specific electromagnetic technology: variable reluctance energy harvesting or VREH.

Here is the idea behind it. [PAUSE] In a VREH device, both the magnet and the coil stay completely still. Only a toothed metal wheel rotates nearby. As the teeth pass, the magnetic flux through the coil changes, and this induces a voltage. There are no moving electrical parts, it can be scaled easily to shafts of different sizes, and, notably, it's designed to produce a very small counter torque. [SHOW SLIDE: VREH principle]

This technology evolved from early single-unit prototypes for railway monitoring, to an optimized design with a six-phase system proposed for large vehicles, like buses.

---

## 3. Research question and objectives

The six coils are designed to be phase-shifted by 60 degrees from each other. More phases mean more power, but they also mean a harder electronics problem: six AC signals, all shifted in time, all needing rectification. Nobody has studied how to do this properly.

This gap defines my research question: which interface circuit extracts the most power from this six-phase harvester, across its entire speed range? [PAUSE]

[SHOW SLIDE: Voltage vs. speed specification plot]

To answer it, I followed a complete path: from theoretical modeling, to circuit simulation, to building and testing a real prototype. [SHOW SLIDE: Research objectives]

---

## 4. Methodology

Now, how did I approach this? [PAUSE]

I started from theory. I built an electrical model of each coil: a voltage source in series with a resistance and an inductance. At low speed, a simple resistive load is enough to extract the maximum power. But as speed increases, so frequency increases the coil's inductance starts to matter, and the matched load condition is no longer valid. To simplest way to recover it is addibng a compensation capacitor in series with the load. This cancels out the inductive component and restores maximum power transfer. [SHOW SLIDE: Electrical model] [SLOW DOWN HERE]

then, I extended it to all six phases of the harvester.

Then I proposed two rectifier strategies. [PAUSE] The first groups the six phases into two three-phase bridges — a standard, diode-based rectifier I call the FWR — tested in two wiring configurations, star and delta. Star wiring gives a higher voltage from the same coils, which turns out to matter a lot at low speed. The second groups the six phases into three pairs of opposite phases, connected so their voltages add up, and rectifies them with a self-driven MOSFET bridge. I call this the NVC. It avoids most of the voltage loss that diodes cause, which matters a lot at low voltage. [SHOW SLIDE: Two rectifier topologies]

I simulated both strategies in Simulink, using real measured waveforms rather than ideal sine waves, to keep the simulation realistic.

Then came the hardware. [PAUSE] I designed a custom circuit board where every configuration can be tested on the very same six coils, just by moving jumpers. I built a test bench with a motor and a variable-speed drive, to control rotation speed precisely. And to measure power accurately, I calibrated every current sensor individually, using precision instruments and lookup tables, instead of trusting datasheet values. [SHOW SLIDE: Test bench and board]

---

## 5. Main results

Let's look at what I found. [PAUSE]

In simulation, the NVC was the clear winner. It delivered up to six times more power than the delta connection, and almost double the star connection, at low speed. It was also the most efficient topology overall.

But the real prototype told a more interesting story. [SLOW DOWN HERE] At low speed, the NVC still won. But above roughly 250 rotations per minute, the star connection actually overtook it in raw output power. The NVC kept the best efficiency at every speed — up to seventy percent, against fifty-six percent for the star connection at top speed — but it no longer delivered the most power everywhere. This is a result that simulation alone did not predict. In practice, this matters: a bus does not run at one constant speed, so the best circuit choice depends on the typical speed profile of the vehicle. [SHOW SLIDE: Measured power comparison]

Why the gap between simulation and measurement? Mainly two reasons. The real coil inductance was somewhat lower than the datasheet value. And the compensation capacitors lose some of their capacitance under real operating voltage. Both effects push the best design point higher than simulation suggested.

Finally, I checked compatibility with five real, commercial power-management chips. [PAUSE] The delta and NVC configurations stayed under about four volts across the whole speed range, so they work safely with every chip I tested. The star connection, however, climbs up to seven volts at top speed. That is too high for most of these chips: it would need either a wide-input converter or a protection circuit in front of it — extra cost and complexity that the delta and NVC designs simply avoid. [SHOW SLIDE: PMIC compatibility]

---

## 6. Original contribution

So, what does this thesis actually add? [PAUSE]

First, this is the first systematic study of power conditioning specifically for a six-phase harvester. Previous work only compared rectifiers for a single phase.

Second, I adapted and validated two different ways to combine six phases into working rectifier circuits — something not demonstrated before for this type of harvester.

Third, I built a single, reconfigurable test platform. This let me compare every topology on the exact same hardware, under the exact same mechanical conditions: a fair, controlled comparison that is rare in this field.

Fourth, my current-sensing methodology, with individual calibration for every sensor, made it possible to trust power measurements down to the milliwatt level.

And finally, my most important finding refines what simulation alone would suggest. [SLOW DOWN HERE] There is no single best topology. The NVC wins on efficiency and at low speed; the star connection wins on raw power at high speed. This nuance only appears once you measure the real hardware, and it directly shapes which topology should be chosen for a given application. [SHOW SLIDE: Key contributions]

---

## 7. Conclusions, limitations, and future work

To conclude. [PAUSE]

The NVC and the star connection emerge as the two strongest candidates, each better suited to a different part of the speed range. The delta connection is consistently the weakest choice.

In practice, the NVC and delta configurations connect safely to any power-management chip I tested. The star connection needs extra protection at high speed, despite giving the most power there.

This work has two main limitations. My coil model does not capture losses that grow with frequency. And my prototype housing, being 3D-printed, is sensitive to vibration, which limits how repeatable the measurements can be.

For future work, I suggest an adaptive compensation network that tracks the optimal capacitance as speed changes, and a full hardware test of the harvester connected to a real power-management chip, to measure the true end-to-end efficiency. [SHOW SLIDE: Conclusions]

---

## 8. Acknowledgments (20 sec)

Before I finish, I want to thank my supervisor, Professor Pozzebon, and my co-supervisors, Professor Bader and Doctor Xu, for their guidance throughout this work. [PAUSE]

Thank you to the committee for your attention. I am happy to answer your questions.

---

## Word count and timing

**Spoken word count: 1319 words** (stage directions and headers excluded).

At 130 words/minute: **~10.1 minutes**. At 140 words/minute: **~9.4 minutes**. Comfortably within the 10-minute target — practice it once out loud with a timer to find your own natural pace, and trim a sentence or two from Section 4 or 5 if you consistently run long.
