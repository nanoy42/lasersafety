# Examples

## Example 1

We consider a 1550 nm pulsed laser, with an average optical power of 3 W. Each pulse has a duration of 50 ps and is produced at a rate of 80 MHz. The beam diameter is 2 mm.

The command line below performs the EN207 analysis for this laser.

```{command-output} lasersafety -w 1550e-9 -p 3 -r 80e6 -t 50e-12 -d 2e-3 en207
```

The code displays all the parameters of the laser, included the one that were computed. It also provides the result of the analysis, requiring a scale number of LB3 for the D mode and no protection (scale number of -2) for the M mode.

Now let us suppose, that in the consider setup, the second harmonic might be generated, using a Second Harmonic Generation (SHG) stage. This generates light at a wavelength of 775 nm. Assuming that this process does not change the parameter of the beam (same pulse duration, same beam diameter, same repetition rate), and assuming a maximal efficiency of 100 % (each 2 photon for the initial beam produce 1 output photon in the output beam, or said otherwise the energy is fully conserved), meaning that the output power of the beam remains the same.

In this case, the script must be run a second time:

```{command-output} lasersafety -w 775e-9 -p 3 -r 80e6 -t 50e-12 -d 2e-3 en207
```

At the end the required eyewear must have : 
1550 D LB3
775 D LB5 + M LB5

## Example 2

We consider a 10 Watt continuous wave (CW) laser, with a single wavelength of 1064 nm and a beam diameter of 4 mm.

The command below performs the EN207 analysis for this laser.

```{command-output} lasersafety -w 1064e-9 -p 10 -r 0 -d 4e-3 en207
```

Note that the repetition rate was set to 0 to indicate that the laser is continuous.

This requires a scale number of LB5 for D at 1064 nm.

## Example 3

We consider a laser that produces a CW power of 5 W at 532 nm (green) with a beam diameter of 2 mm, and we want to consider alignment glasses for this laser.

The command below performs the EN208 analysis for this laser.

```{command-output} lasersafety -w 532e-9 -p 5 -r 0 -d 2e-3 en208
```

This requires a RB4 at 525 nm.

## Example 4

We need to find the full attenuation laser protective eyewear for a pulsed laser that produces 4.5 µJ per pulse at 800 nm with a pulse repetition frequency of 200 kHz. The duration of each pulse is 200 fs. The accessible beam diameter is 3 mm.

```{command-output} lasersafety -w 800e-9 -r 200e3 -t 200e-12 -e 4.5e-6 -d 3e-3 en207
```

This requires 800 D LB5 + M LB6