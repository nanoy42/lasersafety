# Beam parameters

## Parameters

We start this tutorial by naming and describing the different parameters that will be used for evaluating the required glasses. We also lay the different equations that relate the different parameters together.

| Parameter                    | Symbol                 | Unit (SI)      |
| ---------------------------- | ---------------------- | -------------- |
| Average power                | $P_{\rm avg}$          | W              |
| Peak power                   | $P_{\rm peak}$         | W              |
| Pulse energy                 | $E$                    | J              |
| Pulse duration               | $\tau$                 | s              |
| Wavelength                   | $\lambda$              | m              |
| Beam diameter                | $d$                    | m              |
| Cross-section area           | $A$                    | m^2            |
| Divergence (Half-Angle)      | $\theta$               | rad (unitless) |
| Repetition rate              | $R$                    | Hz             |
| Power density                | $P^{\star}$            | W/m^2          |
| Peak power density           | $P^{\star}_{\rm peak}$ | W/m^2          |
| Energy density               | $E^{\star}$            | J/m^2          |
| Number of pulses in time $T$ | $N(T)$                 | Unitless       |

## Relations

The pulse energy is related to the average power and the repetition rate:

$$
E = \frac{P_{\rm avg}}{R}
$$

The peak power is related to the pulse energy and the pulse duration:

$$
P_{\rm peak} = \frac{E}{\tau}
$$

Note that the two previous relations can be combined to get

$$
P_{\rm peak} = \frac{P_{\rm avg}}{\tau \cdot R}
$$

The cross-section area is related to the beam diameter and the beam divergence. If the beam is collimated, it is simply

$$
A = \pi \left(\frac{d}{2}\right)^2
$$

If the beam is divergent, the cross-section at distance $r$ ($r$ is the distance with respect to the other beam diameter) is given by

$$
A(r) = \pi \left(\frac{d + 2r\tan(\theta)}{2}\right)^2
$$

For laser safety calculation, if the beam is divergent we take $r=10$ cm as the default distance per EN207.

The power density is related to the average power and cross-section area by 

$$
P^{\star} = \frac{P_{\rm avg}}{A}
$$

The peak power density is related to the peak power and cross-section area by

$$
P^{\star}_{\rm peak} = \frac{P_{\rm peak}}{A}
$$

The energy density is related to the pulse energy and cross-section area by

$$
E^{\star} = \frac{E}{A}
$$

For the purpose of eyewear protection calculation, the energy density must be corrected when considering pulsed lasers with a wavelength in the visible and near-infrared regions, more specifically when the wavelength is greater than 400 nm and lower than 1400 nm. In that case, the energy density is corrected by a factor $N^{1/4}$:

$$
{E^{\star}}' = E^{\star}\cdot N^{1/4}
$$

The number of pulses in time $T$ is related to the repetition rate

$$
N(T) = T\cdot R
$$

For the purpose of eyewear protection calculation per EN207, we use $T=10$ s.