# Thesis Defense Speech (English) — target 10 minutes

---

## 1. Opening (30 sec) — Slides 1

Good afternoon to the members of the committee and to everyone here. My name is Jacopo Garau.

Today I will present my Master's thesis in Electronic Engineering. The work was carried out at Mid Sweden University during my Erasmus for Traineeship program, under the supervision of Professor Alessandro Pozzebon, Professor Sebastian Bader, and Doctor Ye Xu.

The goal of my project was to design and implement an interface able to extract the maximum power from a six-phase energy harvester. [SHOW SLIDE: Title]

---

## 2. Context and motivation — Slides 2-3

Wireless sensor networks and IoT devices have grown very fast in recent years. They are widely used to collect data, which can then be processed for many different purposes. This creates a simple but important problem: how do we power millions of small devices without constantly replacing their batteries? 

Energy harvesting comes as a solution to those problems. [SHOW SLIDE: Energy harvesting overview]

My thesis focuses on generating electric power from rotating motion using a specific electromagnetic technology: variable reluctance energy harvesting, or VREH.

How does this system work? In a VREH device, both the magnet and the coil stay completely still. Only a toothed metal wheel rotates nearby. As the teeth pass, the magnetic flux through the coil changes, and this induces a voltage across each coil. [SHOW SLIDE: VREH principle]

What is the convenience of using this system? There are no moving electrical parts, it can be scaled easily to shafts of different sizes, and, notably, it's designed to produce a very small counter torque. 

This system is designed to be mounted around a shaft in large vehicles, for example buses. It operates in the 100 to 400 RPM range, corresponding to typical driving speeds of 20 to 80 kilometers per hour.

---

## 3. Research question and objectives — Slides 6-7

The six coils are designed to be phase-shifted by 60 degrees from each other. More phases mean more power, but they also mean a harder electronics problem: six AC signals, all shifted in time, all needing rectification. Nobody has studied how to do this properly.

This gap defines my research question: which interface circuit extracts the most power from this six-phase harvester, across its entire speed range?

[SHOW SLIDE: Voltage vs. speed specification plot]

To answer it, I followed a complete path: from theoretical modeling, to circuit simulation, to designing, building and testing a real prototype. [SHOW SLIDE: Research objectives]

---

## 4. Methodology — Slides 8-15

Now, how did I approach this?

I started from theory. I built an electrical model of each coil: a voltage source in series with a resistance and an inductance. At low speed, a simple resistive load is enough to extract the maximum power. But as speed — and therefore frequency — increases, the coil's inductance starts to matter and can no longer be neglected, so the matched-load condition is no longer valid. The simplest way to recover it is adding a compensation capacitor in series with the load. This helps to cancel out the inductive component and increase power transfer. [SHOW SLIDE: Electrical model]

This model can be extended to all six phases of the harvester. [SHOW SLIDE: Fig. 4.2 — six real phase-shifted waveforms]
Here you can see the six real coil voltages, shifted by 60deg from each other, and we can notice that they are different from ideal sine waves.

Then I proposed two rectifier strategies.

Since the system is composed of six coils phase shifted by 60deg one to each other, we can divide the six-phase system into two three-phase subsystems.
Now I could approach this problem using two standard full bridge rectifiers. For these configurations I tested Star and Delta connections of the coils. [SHOW SLIDE: Delta and Star Connection]
What would I expect from these configurations? I expect the Star connection to have a higher open-circuit voltage than the Delta connection.

The second strategy I decided to follow was to divide the main system into 3 subsystems of two phases each, coupling two coils phase shifted by 180deg in antiseries connection. [SHOW SLIDE: Antiseries connection]
This way I expect to have, in ideal conditions, the same signal with double the voltage. 
These two voltage sources are then connected to a Negative Voltage Converter, or NVC. This device combines 4 mosfets with cross coupled gates that activate two at a time, bypassing the diodes to avoid their voltage drop and increasing the overall bridge efficiency.

I simulated both strategies in Matlab Simulink. But the real coil voltage is not a perfect sine wave. [SHOW SLIDE: Fig. 4.3 — measured vs. ideal waveform]
So I computed the RMS voltage of the coil as a function of rpm, and based on that I ran the simulation with an equivalent sinusoid, scaled using the real crest factor, that produces the same power as the measured waveform.

After the simulations I designed a custom PCB (using Altium Designer) where every configuration can be tested just by moving jumpers. I also soldered by hand every single component using a soldering iron and a hot plate. [SHOW SLIDE: Fig. 5.7 soldered transistors]

Here is my test bench, with a motor connected to its inverter to control rotation speed precisely. [SHOW SLIDE: Fig. 6.1 testbench]
To measure voltage I used the acquisition board, and to measure currents I used current sensors based on differential measurement of a shunt resistor. Every current sensor was calibrated individually, using precision instruments to create the lookup tables.

---

## 5. Main results — Slides 16-20

Let's look at what I found. [SHOW SLIDE: Fig. 4.8, 4.15, 4.22 — total power vs. speed for the three topologies]

The simulations are performed doing a sweep of the matching capacitor.

As we can see, the NVC was the clear winner, especially at low speed and low speed is what matters the most, since it's the worst-case condition that sets the lower bound on the power we can deliver to the load. The NVC delivered up to six times more power than the delta connection, and almost double the star connection, at low speed. It was also the most efficient topology overall.

But the real prototype told a more interesting story. [SHOW SLIDE: Fig. 7.6, 7.14, 7.23 — total power vs. speed for the three topologies]

At low speed, the NVC still wins. But above roughly 250 rotations per minute, the star connection actually overtook the NVC in output power. 

Looking ant the eficiency we can see that [SHOW SLIDE: Fig. 7.7, 7.16, 7.24 — total efficiency vs. speed for the three topologies]
The NVC has the best efficiency at every speed and it goes up to seventy percent, against fiftyfive percent for the star connection at top speed. The Dela connection instead is the worst performer as expected. This is a result that simulation alone did not predict.

On average, across all topologies and speeds, measured power differed from 8% for star configuration to almost 30% for NVC.
Why the gap between simulation and measurement?  The compensation capacitors lose some of their capacitance under real operating voltage expecially wiht voltage rising with rpm, real components in general, bridge parasitic resistance and because of non ideal sinusoidal sources.

Finally, I checked compatibility with five real, commercial power-management chips. these IC can be used to manage the power and to produce a stable voltage to deliver power to the load.
Which kind of load we are talking about? we can for examples power some circuitds that by means of various sensors are capable to detect and prevent malfunxionamenti al systema o al veicolo dove sono isnstallati.

## 6. Conclusions, limitations, and future work — Slide 21

To conclude.

The NVC and the star connection emerge as the two strongest candidates ans the delta connection is consistently the weakest choice.

In practice, the NVC and delta configurations connect safely to any power-management chip I tested. The star connection needs extra protection at high speed because of an higher open circuit votage that can damage the Powerv managment IC.

The biggest limitation of this work was that the Vriable reluctace energu harvester was a 3d printed prototpe that is sensitive to vibration execially at high speeds, which limits la ripetibilità delle misure.

For future work, I suggest an adaptive compensation network that tracks the optimal capacitance as speed changes, and a full hardware test of the harvester connected to a real power-management chip, to measure the true efficiency form the harvester to the final load. [SHOW SLIDE: Conclusions]

---

## 7. Acknowledgments (20 sec) — Slide 22

Before I finish, I want to thank my supervisor, Professor Pozzebon, and my two co-supervisors, Professor Bader and Doctor Xu, for their guidance throughout this work.

Thank you to the committee for your attention. I am happy to answer your questions.

---

## Word count and timing

**Spoken word count: 1319 words** (stage directions and headers excluded).

At 130 words/minute: **~10.1 minutes**. At 140 words/minute: **~9.4 minutes**. Comfortably within the 10-minute target — practice it once out loud with a timer to find your own natural pace, and trim a sentence or two from Section 4 or 5 if you consistently run long.
