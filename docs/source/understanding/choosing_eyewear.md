# Choosing eyewear

On this page we review the process for choosing eyewear protection according to the EN207 (full attenuation) and EN208 (alignement) standards.

```{warning} What is described on this page of my own understanding of the standards, and could be wrong. All this computations should be performed and/or checked by the trained competent personal. I decline any responsibility in case the explanation described below brings to dangerous situations.
```

## EN207

The EN207 standard applies to beams with wavelength between 180 nm and 1 mm. For the purpose of the standard, the mode of a laser is defined based on the pulse duration $\tau$:

| Mode              | Letter | Pulse duration (s)                        |
| ----------------- | ------ | ----------------------------------------- |
| Continuous Wave   | D      | $0.25\text{ s} < \tau$                    |
| Pulsed Mode       | I      | $1\mu\text{ s} < \tau \leq 0.25\text{ s}$ |
| Giant Pulsed Mode | R      | $1\text{ ns} < \tau \leq 1\mu\text{ s}$   |
| Modelocked        | D      | $\tau < 1\text{ ns}$                      |

The base working table can be summarized in the following table (please refer to the EN207 standard for the official table):

| Working mode | Wavelength range | Max power or energy density    | Minimal protection level          |
| ------------ | ---------------- | ------------------------------ | --------------------------------- |
| D            | 180 - 315 nm     | $1\times 10^{n-3}$ W/m${}^2$   | $\log(P^{\star})+3$               |
|              | > 315 - 1400 nm  | $1\times 10^{n+1}$ W/m${}^2$   | $\log(P^{\star})-1$               |
|              | > 1400 nm - 1 mm | $1\times 10^{n+3}$ W/m${}^2$   | $\log(P^{\star})-3$               |
| I,R          | 180 - 315 nm     | $3\times 10^{n+1}$ J/m${}^2$   | $\log(E^{\star}/3)-1$             |
|              | > 315 - 1400 nm  | $5\times 10^{n-3}$ J/m${}^2$   | $\log({E^{\star}}'/5)-3$          |
|              | > 1400 nm - 1 mm | $1\times 10^{n+2}$ J/m${}^2$   | $\log(E^{\star})-2$               |
| M            | 180 - 315 nm     | $3\times 10^{n+10}$ W/m${}^2$  | $\log(P^{\star}_{\rm peak}/3)-10$ |
|              | > 315 - 1400 nm  | $1.5\times 10^{n-4}$ J/m${}^2$ | $\log({E^{\star}}'/1.5)+4$        |
|              | > 1400 nm - 1 mm | $1\times 10^{n+11}$ W/m${}^2$  | $\log(P^{\star}_{\rm peak})-11$   |

For the formulas, power densities must be expressed in W/m${}^2$ and energy densities must be expressed in J/m${}^2$. All scale numbers must be rounded upwards.

### Continuous laser

The steps for choosing the required scale number for a continuous wave laser are as follows: 

1. Compute the cross-section area of the beam, rounding down if needed;
2. Compute the (average) power density by diving the average power by the cross-section area, rounding up if needed. This should be expressed in W/m${}^2$;
3. From the summarized table, choose the "D" lines and the line associated to the working wavelength;
4. Compute the minimal scale number required, rounding up to the nearest integer. If the scale number is less or equal than 0, no eyewear protection is required.

### Pulsed laser

The steps for choosing the required scale number for a pulsed laser are two-fold: first one should compute the scale number as if the laser was continuous, using the average power, and then for the pulsed case. In addition, for lasers with a wavelength between 400 nm and 1400 nm, a correction factor should be applied.

The chosen eyewear protection must meet both scale numbers.

**Continuous scale number**

1. Compute the cross-section area of the beam, rounding down if needed;
2. Compute the (average) power density by diving the average power by the cross-section area, rounding up if needed. This should be expressed in W/m${}^2$;
3. From the summarized table, choose the "D" lines and the line associated to the working wavelength;
4. Compute the minimal scale number required, rounding up to the nearest integer. If the scale number is less or equal than 0, no eyewear protection is required for this mode.

**Pulsed scale number**

For I,R lasers:

1. Compute the cross-section area of the beam, rounding down if needed ;
2. Compute the energy density by dividing the energy per pulse by the cross-section area, rounding up if needed. This should be expressed in J/m${}^2$;
3. If the wavelength is between 400 nm and 1400 nm, compute the number of pulses in a reference interval of 10 s $N$ by multiplying the repetition rate by 10 s. Then compute the corrected energy density by multiplying the energy density by the correction factor $N^{1/4}$;
4. From the summarized table, choose the "I,R" lines and the line associated to the working wavelength;
5. Compute the minimal scale number required, rounding up to the nearest integer. If the scale number is less or equal than 0, no eyewear protection is required for this mode.

For M lasers:

1. Compute the cross-section area of the beam, rounding down if needed ;
2. Compute the peak power density by dividing the peak power by the cross-section area, rounding up if needed. This should be expressed in W/m${}^2$;
3. If the wavelength is between 400 nm and 1400 nm, compute the energy density by diving the energy per pulse by the cross-section area, rounding up if needed. Then compute the number of pulses in a reference interval of 10 s $N$ by multiplying the repetition rate by 10 s. Finally, compute the corrected energy density by multiplying the energy density by the correction factor $N^{1/4}$;
4. From the summarized table, choose the "M" lines and the line associated to the working wavelength;
5. Compute the minimal scale number required, rounding up to the nearest integer. If the scale number is less or equal than 0, no eyewear protection is required for this mode.

### Examples

Examples are from https://www.ucc.ie/en/media/training/workthings/UCCLaserSafetyGuidelines.pdf

#### Continuous laser example

Consider a continuous wave laser with average output power of $P = 10$ W with a wavelength of $\lambda = 1064$ nm and a beam diameter of $d = 4$ mm.

The beam area is computed with $A = \pi (d/2)^2$ and expressed in m${}^2$. This gives a cross-section area of approximately $1.25\times 10^{-5}$ m${}^2$.

Then we compute the power density as $P^{\star} = P/A$, giving $P^{\star} \simeq 8 \times 10^5$ W/m${}^2$.

Finally, we use the formula associated with D lasers between 315 nm and 1400 nm which is 

$$
n = \lceil \log_{10}(P^{\star}) - 1\rceil
$$

giving $n=5$. This means that we require at least 1064 D LB5.

We check that the lasersafety package brings the same answer:

```{command-output} lasersafety -w 1064e-9 -p 10 -r 0 -d 4e-3 en207
```

#### Pulsed laser example

We first consider a laser producing pulses with energy of $E = 4.5$ μJ per pulse at a wavelength of $\lambda = 800$ nm and a repetition rate of $R = 200$ kHz. The duration of each pulse is $\tau = 200$ fs. The beam diameter is $d = 3$ mm.

First, we work out the mode of the laser. Since the pulse duration is 200 fs, we are below the 1 ns limit and hence we consider the M case.

As we will need for both cases, we start by computing the cross-section area $A = \pi (d/2)^2$, which is approximately $7.06\times 10^{-6}$ m${}^2$.

The first step is to get the protection level in the equivalent continuous mode. For this, we need to compute the average power of the laser. As we saw previously, the average power can be computed by multiplying the pulse energy by the repetition rate $P_{\rm avg} = E\cdot R$, giving an average power of 0.9 W.

We then compute the average power density as $P^{\star} = P/A$, giving $P^{\star} \simeq 1.3 \times 10^5$ W/m${}^2$.

Finally, we use the formula associated with D lasers between 315 nm and 1400 nm which is 

$$
n = \lceil \log_{10}(P^{\star}) - 1\rceil
$$

giving $n=5$.

Then we need to compute the scale number for the pulse mode. Since the wavelength is between 400 nm and 1400 nm, we need to use the energy density even if we are in the M regime. 

We start by compute the energy density by dividing the pulse energy by the cross-section area, $E^{\star} = E / A$ giving $E^{\star} = 0.637$ J/m${}^2$.

Since the wavelength is between 400 nm and 1400 nm, we then need to correct the energy density. We start by computing the number of pulses in a 10 s reference interval, $N = R\cdot 10$ s, giving $N = 2\times 10^6$ and we then compute the corrected pulse energy ${E^{\star}}' = N^{1/4}\cdot E^{\rm star}$ giving ${E^{\star}}' = 23.95$ J/m${}^2$.

We finally can compute the required scale number by using the formula for M lasers between 315 nm and 1400 nm which is 

$$
n = \lceil \log_{10}({E^{\star}}' / 1.5) + 4\rceil
$$

giving $n=6$.

Finally, we require at least 800 D LB5 M LB6.

We check that the lasersafety package brings the same answer:

```{command-output} lasersafety -w 800e-9 -e 4.5e-6 -r 200e3 -d 3e-3 -t 200e-15 en207
```

In the source of the example, they then consider that the laser might be driving an OPA and the light is converted to a longer wavelength, in this case 1500 nm. They assume that the efficiency of the process is such that the output power in 1500 nm light is 20 mW on average, and that there is no effect on the temporal or spatial mode such that the pulse duration and the beam diameter stay unchanged. The repetition rate is also the same.

We consider this as a new beam, and start the process from the beginning. Since the pulse duration is the same, it still falls in the M mode. We start by looking at the equivalent continuous mode.

The cross-section area is still the same as the beam diameter is unchanged, and the average power is 20 mW. Hence the average power density is $P^{\star} = P_{\rm avg} / A = 2.9\times 10^3$ W/m${}^2$.

We then use the formula from the D lines with the line corresponding the > 1400 nm wavelength, which is

$$
n = \lceil \log_{10}(P^{\star}) - 3\rceil
$$

giving $n=1$.

Next, we do the steps for the pulsed case. The wavelength is now away from the 400 nm to 1400 nm range and we must use the peak power to derive the peak power density. The peak power can be obtained from the average power, repetition rate and pulse duration as $P_{\rm peak} = P_{\rm avg} / (\tau\cdot R)$ giving a peak power of $P_{\rm peak} = 5\times 10^5$ W.

We then compute the peak power density by diving the peak power by the cross-section area giving $P^{\star}_{\rm peak} = P_{\rm peak} / A \simeq 7.1\times 10^{10}$ W/m${}^2$.

We use the formula for the M case with > 1400 nm wavelength, which is 

$$
n = \lceil \log_{10}(P^{\star}_{\rm peak}) - 11\rceil
$$

giving $n=0$. In this case, no eyewear protection is in theory required to be protected. Note in the example, the authors take the smallest protection available LB1.

We check that the lasersafety package brings the same answer:

```{command-output} lasersafety -w 1500e-9 -p 20e-3 -r 200e3 -d 3e-3 -t 200e-15 en207
```

At the end, the requirement for the eyewear protection for this experiment is 800 D LB5 M LB6 + 1500 D LB1.

## E208

The EN208 can be used for laser in the visible range, to choose glasses that don't fully attenuate the laser, but leave some for alignment. For validity, the wavelength of the laser must be between 400 and 700 nm.

The base working table is the following:

| Scale number | Power density             | Energy density         |
| ------------ | ------------------------- | ---------------------- |
| Condition    | CW and $\tau \geq 0.2$ ms | 1 ns $< \tau < 0.2$ ms |
|              |                           |                        |
| RB1          | $10^4$ W/m${}^2$          | 2 J/m${}^2$            |
| RB2          | $10^5$ W/m${}^2$          | 20 J/m${}^2$           |
| RB3          | $10^6$ W/m${}^2$          | 200 J/m${}^2$          |
| RB4          | $10^7$ W/m${}^2$          | 2000 J/m${}^2$         |
| RB5          | $10^8$ W/m${}^2$          | 20000 J/m${}^2$        |

This can be summarized in the following way: 

* for CW lasers and pulsed lasers with $\tau \geq 0.2$ ms, the scale number is given by $\lceil \log(P^{\star}) - 3\rceil$;
* for pulsed lasers with $1 \text{ ns} < \tau < 0.2 \text{ ms}$, the scale number is given by $\lceil \log({E^{\star}}'/2)+1\rceil$.

### Continuous lasers

For continuous lasers and pulsed lasers with a pulse duration above 0.2 ms:

1. Compute the cross-section area of the beam, rounding down if needed;
2. Compute the (average) power density by diving the average power by the cross-section area, rounding up if needed. This should be expressed in W/m${}^2$;
3. Use the summarized formula, rounding up if needed.

### Pulsed lasers

For pulsed lasers below 0.2 ms (and above 1 ns):

1. Compute the cross-section area of the beam, rounding down if needed;
2. Compute the energy density by dividing the energy per pulse by the cross-section area, rounding up if needed. This should be expressed in J/m${}^2$;
3. Compute the number of pulses in a reference interval of 10 s $N$ by multiplying the repetition rate by 10 s. Then compute the corrected energy density by multiplying the energy density by the correction factor $N^{1/4}$;
4. Used the summarized formula, rounding up if needed.


### Example

The example is again from https://www.ucc.ie/en/media/training/workthings/UCCLaserSafetyGuidelines.pdf

Consider a continuous laser with a power of 5 W at 532 nm (green) with a beam diameter of 2 mm.

The beam area is computed with $A = \pi (d/2)^2$ and expressed in m${}^2$. This gives a cross-section area of approximately $3.14\times 10^{-6}$ m${}^2$.

Then we compute the power density as $P^{\star} = P/A$, giving $P^{\star} \simeq 1.6 \times 10^6$ W/m${}^2$.

Finally, we use the formula associated with continuous lasers which is 

$$
n = \lceil \log_{10}(P^{\star}) - 3\rceil
$$

giving $n=4$. This means that we require at least 532 RB4.

We check that the lasersafety package brings the same answer:

```{command-output} lasersafety -w 532e-9 -p 5 -r 0 -d 2e-3 en208
```