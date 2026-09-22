# Thesis Defense Speech - target 10 minutes - Current time 13 min 40 sec

---

## 1. Opening (45 sec) - Slide 1

Good afternoon to the members of the committee and to everyone here. My name is Jacopo Garau.

Today I will present my Master's thesis in Electronic Engineering. The work was carried out at Mid Sweden University during my Erasmus for Traineeship program, under the supervision of Professor Alessandro Pozzebon, Professor Sebastian Bader, and Doctor Ye Xu.

The goal of my project was to design and implement an interface able to extract the maximum power from a six-phase energy harvester.

## 2. Context and motivation (2 min) - Slides 2-3

Wireless sensor networks and IoT devices have grown very fast in recent years. They are widely used to collect data, which can then be processed for many different purposes. This creates a simple but important problem: how do we power millions of small devices without constantly replacing their batteries?

Energy harvesting comes as a solution to those problems.

A variable reluctance energy harvester, or VREH from here on, converts mechanical energy into electrical energy. It is made of two parts: a pickup unit, composed of a magnet and a coil, and a toothed wheel, made of ferromagnetic material. The pickup unit stays still while the toothed wheel rotates. This relative motion changes the magnetic flux over time, and that induces a voltage across the coil.

This system is designed to be mounted around a shaft in large vehicles, for example buses. It operates in the 100 to 400 RPM range, corresponding to typical driving speeds of 20 to 80 kilometers per hour.


## 3. Research question and objectives (50 sec) - Slides 4-5

This harvester has six coils, each shifted by 60 degrees from the next. That means six AC signals to rectify instead of one.

So, my research question was: which interface circuit extracts the most power from this six-phase harvester, across its entire speed range? 

To answer it, I followed a complete path: from theoretical modeling, to circuit simulation, to designing, building and testing a real prototype.


## 4. Methodology (3 min 45sec) - Slides 6-8

Let's start with the coil model: a voltage source in series with a resistance and an inductance. At low speed, with a resistive load, the phase shift between voltage and current can be negligible, but as speed increases the power factor decreases. In order to have a high power factor and a perfect matching condition, a capacitor is placed in series with the load.

We will see later that the best capacitor choice is the one that guarantees the matching condition at the lowest frequency, since that's what sets the lower-bound power extraction.

This model can be extended to all six phases of the harvester.

Then I proposed two rectifier strategies.

Since the system is composed of six coils phase shifted by 60 degrees from each other, we can divide the six-phase system into two three-phase subsystems.
Now I could approach this problem using two standard full bridge rectifiers. For these configurations I tested Star and Delta connections of the coils.

The second strategy I decided to follow was to divide the main system into three subsystems of two phases each, coupling two coils phase shifted by 180 degrees in antiseries connection.

This way I expect to have, in ideal conditions, the same signal with double the voltage.
These two voltage sources are then connected to a Negative Voltage Converter, or NVC. This device combines four MOSFETs with cross coupled gates that activate two at a time, bypassing the diodes to avoid their voltage drop and increasing the overall bridge efficiency.

## 5. Simulations Results (30 sec) - Slide 9

Let's look at what I found.
As we can see, the NVC was the clear winner, especially at low speed, and low speed is what matters the most, since it's the worst-case condition that sets the lower bound on the power we can deliver to the load. The NVC delivered up to six times more power than the Delta connection, and almost double the Star connection, at low speed. It was also the most efficient topology overall.

## 6. Prototype and testbench (30 sec) - Slide 11

After the simulations I designed a custom PCB (using Altium Designer) where every configuration can be tested just by moving jumpers. I also soldered by hand every single component using a soldering iron and a hot plate.

Here is my test bench, with a motor connected to its inverter to control rotation speed precisely.
The VREH is connected on the motor shaft.

## 7. Main results - (3 min 30sec) Slides 12-15

But the real prototype told a more interesting story.

At low speed, the NVC still wins. But above roughly 250 rotations per minute, the Star connection overtakes the NVC in output power.

Looking at the efficiency, the NVC has the best efficiency at every speed and it goes up to seventy percent, against fifty-five percent for the Star connection at top speed. The Delta connection instead is the worst performer, as expected. This is a result that simulation alone did not predict.

On average, across all topologies and speeds, the measured power differed from simulation by about eight percent for the Star configuration, up to almost thirty percent for the NVC.
Why the gap between simulation and measurement? The compensation capacitors lose some of their capacitance under the real operating voltage, especially as the voltage rises with rpm. On top of that there are the tolerances of the real components, the parasitic resistance of the bridges, and sources that are not perfectly sinusoidal.

Finally, I checked compatibility with five real, commercial power-management chips. These ICs manage the harvested power and produce a stable voltage to deliver power to the load.
What kind of load are we talking about? For example, they can power circuits whose sensors detect and prevent malfunctions in the system or the vehicle where they are installed.

## 8. Conclusions, limitations, and future work (1 min 30 sec) - Slide 16

To conclude.

The NVC and the Star connection emerge as the two strongest candidates, and the Delta connection is consistently the weakest choice.

In practice, the NVC and Delta configurations connect safely to any power-management chip I tested. The Star connection needs extra protection at high speed, because of a higher open-circuit voltage that can damage the power management IC.

The biggest limitation of this work was that the variable reluctance harvester was a 3D-printed prototype, sensitive to vibration especially at high speed, which limits how repeatable the measurements are.

For future work, I suggest an adaptive compensation network that tracks the optimal capacitance as speed changes, and a full hardware test of the harvester connected to a real power-management chip, to measure the true efficiency from the harvester to the final load.

## 9. Acknowledgments (20 sec) - Slide 17

Before I finish, I want to thank my supervisor for this amazing experience in Sweden, without whom none of this would have been possible.

Thank you to the committee for your attention. I am happy to answer your questions.


























Here you can see the six real coil voltages, shifted by 60 degrees from each other, and we can notice that they are different from ideal sine waves.

here we have the peak to peak voltages of a single coil, the blue line comes from a comsol simulation, the red line is derived form measurements and the yellow is relatet to a sine wave source that generates the same power of the source in red.

To measure voltage I used the acquisition board, and to measure currents I used current sensors based on differential measurement of a shunt resistor. Every current sensor was calibrated individually, using precision instruments to create the lookup tables. [SHOW SLIDE: Current sensing]
