# Analog-horizon assumptions

Every assumption below is required to apply the Physics-for-Blackhole model
to a BEC or other analog horizon. All are [CONJECTURE]; none is established
physics for any real analog system. No existing dataset is claimed to support
the framework.

## A1. The healing length is the analog Planck scale
The analog horizon's minimum resolvable length is the condensate healing
length xi (or the system's equivalent short-distance cutoff), playing the role
of l_P. The analog area quantum is then Delta_a = 4 ln2 xi^2 (one bit of
entropy per quantum, adopting the published Bekenstein-Mukhanov/Landauer
spacing as input, not as a discovery of this framework).

Consequence: the number of analog area quanta is
    N = A / Delta_a = 4 pi R^2 / (4 ln2 xi^2) = pi R^2 / (ln2 xi^2)
where R is the analog horizon radius. This is why the staircase is finite and
potentially resolvable for tabletop horizons (xi/R not absurdly small) but
suppressed by (l_P/R)^2 ~ 10^-77 for astrophysical holes.

## A2. Page-like behaviour requires backreaction
A Page curve (turnover and return to zero) assumes the radiation carries away
information and the remaining horizon's capacity shrinks accordingly — i.e.
backreaction of the emitted quanta on the horizon. A fixed-background
analog Hawking calculation (no backreaction) gives a monotonic thermal flux
and NO Page turnover. So observing Page-like behaviour in an analog system
requires the analog of backreaction to be operative; otherwise the framework's
staircase prediction does not apply.

## A3. The interface is a saturated cut with a code
The analog horizon is an interface (saturated cut) with N = A/Delta_a logical
degrees of freedom protected by a code of distance d. The entropy of the
radiation rises in steps of one logical qunit per Delta_a. This code structure
is assumed, not derived, for analog systems.

## A4. Substrate time and the readout map apply to the analog
The analog system has a substrate reconfiguration count tau and a readout that
produces an effective metric, with physical time t = eta * tau (Conjecture N)
and eta = OM/c the single free parameter. The same eta is assumed to
characterize the analog as the astrophysical case (universality claim —
unproven; see test_om.py SYNTHETIC universality test).

## A5. The analog Planck scale is above the condensate's own dispersion
The discreteness/line-structure signature sought (a resolved staircase or line
structure not explained by the condensate's dispersion relation) must lie
above the condensate's intrinsic dispersion. If the observed corrections can be
re-expressed entirely as the condensate's dispersion or quasi-normal-mode
structure, the framework is unfalsifiable in that system (open problem O8).

## A6. Measurability
The experiment must resolve entropy steps of one logical qunit (k_B ln 2) in
the outgoing radiation, and a Page-time shift of order 3/(4N) (half a
quantum) or 3/(2N) (full quantum). For N ~ 10^3-10^4 (R=5-20 um, xi=0.3 um)
the last-ten-quanta fraction of the lifetime is (10/N) ~ 0.05-0.8% (linear;
see test_numbers.py). Resolving this requires the analog Hawking flux to be
measured with sub-per-cent entropy precision over the relevant window.

## What is NOT claimed
- No existing analog-horizon dataset (BEC, water wave, optical fiber, ion
  ring, etc.) exhibits the staircase or line structure.
- No value of eta has been measured in any analog system.
- eta is not asserted to be a constant of nature.
