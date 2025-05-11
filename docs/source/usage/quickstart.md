# Quickstart

The lasersafety library can be installed via PyPi:

```{prompt} bash

pip install lasersafety
```

For other methods of installation, see {doc}`/usage/installation`.

You can check that the package was correctly installed with

```{command-output} lasersafety --version
```

And you can directly use to compute the required scale number. The example below is for a 3 W 1550 nm laser with 50 ps pulses, and repetition rate of 80 MHz for a beam diameter of 2 mm:

```{command-output} lasersafety -p 3 -r 80e6 -t 50e-12 -w 1550e-9 -d 2e-3 en207
```

See {doc}`/usage/usage/` for more information on how to use the package.