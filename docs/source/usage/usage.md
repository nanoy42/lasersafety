# Usage

## Using the CLI

Once the package is installed, you can use the lasersafety entrypoint. If the python site-packages installation directory is in the path, the `lasersafety` command should be available. You can check this with 


```{command-output} lasersafety --version
```

If it is not in the path, commands can be executed by replacing `lasersafety` by `python3 -m lasersafety`:


```{command-output} python3 -m lasersafety --version
```

Two functions are available through the command line interface: the first one provides the computation with respect to the EN207 standard and the second one with respect to the EN208 standard (they have now been superseeded by the ISO 19818:2021 standard). For more details on these standards, see {doc}`/understanding/choosing_eyewear`.

The commands can be executed with `lasersafety en207` and `lasersafety en208`. Note that several parameters must be passed to the command line for the beam parameters. The table below explain parameters must be, must not be or could passed depending on the type of laser (continuous or pulses).

| Parameter          | CLI                        | Continuous | Pulsed             | Unit                  |
| ------------------ | -------------------------- | ---------- | ------------------ | --------------------- |
| Wavelength         | `-w` or `--wavelength`     | Must       | Must               | Meter (m)             |
| Repetition rate    | `-r` or `--rep-rate`       | Must be 0  | Must               | Hertz (Hz)            |
| Average power (*)  | `-p` or `--avg-power`      | Must       | Exactly two of (*) | Watt (W)              |
| Peak power (*)     | `-s` or `--peak-power`     | Must not   | Exactly two of (*) | Watt (W)              |
| Pulse duration (*) | `-t` or `--pulse-duration` | Must not   | Exactly two of (*) | Second (s)            |
| Pulse energy (*)   | `-e` or `--pulse-energy`   | Must not   | Exactly two of (*) | Joule (J)             |
| Beam diameter      | `-d` or `--beam-diameter`  | Must       | Must               | Meter (m)             |
| Beam divergence    | `--divergence`             | Can        | Can                | Unitless/radian (rad) |

Hence, for continuous lasers, the user has to pass the wavelength, the average optical power and the beam diameter. The value 0 must also be passed as the repetition rate for the script to understand that the laser is continuous. The beam divergence may also be passed.

For pulsed lasers, the user has to pass the wavelength, the repetition rate and the beam diameter. Additionally, exactly two parameters between the average power, the peak power, the pulse duration and the pulse energy must be passed (except the average power and pulse energy couple that is not enough).

For more details, see {doc}`/understanding/beam_parameters`.

Depending on the chosen standard, and if the parameters of the laser fall inside the standard, then the script outputs the scale(s) number(s) for the required wavelength and modes.

```{warning} All parameters must be passed in the units given above. The script will not be able to detect a mistake on the unit.
```

For more details on the CLI, see {doc}`/cli/cli_usage` and {doc}`/cli/examples`. Taking the first example of a 3 W 1550 nm laser with 50 ps pulses, and repetition rate of 80 MHz for a beam diameter of 2 mm:

```{command-output} lasersafety -p 3 -r 80e6 -t 50e-12 -w 1550e-9 -d 2e-3 en207
```

## Using the API

It is possible to also use the API directly. The functions from the modules {py:mod}`lasersafety.en207` and {py:mod}`lasersafety.en208`.

For instance, taking the example from above of computing the EN207 scale number for a 3 W 1550 nm laser with 50 ps pulses, and repetition rate of 80 MHz for a beam diameter of 2 mm:


```{eval-rst}
.. exec_code::

    import numpy as np

    from lasersafety.en207 import continuous_scale_number, pulsed_scale_number

    average_power = 3
    repetition_rate = 80e6
    beam_diameter = 2e-3
    wavelength = 1550e-9
    pulse_duration = 50e-12

    area = np.pi*(beam_diameter/2)**2
    pulse_energy = average_power / repetition_rate
    peak_power = pulse_energy / pulse_duration

    res_continuous = continuous_scale_number(average_power=average_power, area=area, wavelength=wavelength)

    res_pulsed = pulsed_scale_number(peak_power=peak_power,pulse_energy=pulse_energy,area=area, pulse_duration=pulse_duration, repetition_rate=repetition_rate, wavelength=wavelength)

    print("Continuous: ", res_continuous)
    print("Pulsed: ", res_pulsed)
```

As we see, this method requires additional computation and knowledge about the relations between beam parameters. It also requires some knowledge about the standard as both the continuous and pulsed scale numbers must be computer independently.

Another option is hence to use the {py:class}`lasersafety.laser.LaserBeam` class. This class takes the same parameters as the script (see the previous section), and directly has the methods to compute the EN207 and EN208 scale numbers.

```{eval-rst}
.. exec_code::

    from lasersafety.laser import LaserBeam

    laser = LaserBeam(
        average_power=3,
        repetition_rate=80e6,
        beam_diameter=2e-3,
        wavelength=1550e-9,
        pulse_duration=50e-12
    )

    print(laser)

    print(laser.en207_analysis())
```
