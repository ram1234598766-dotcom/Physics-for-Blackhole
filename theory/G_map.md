# Appendix G map — physical vs substrate time, and the physical Page time

## Conventions (all [CONJECTURE] unless marked)

- OM = v_s,lin = l_P / tau_q, the framework's single free parameter.
- eta = OM / c = t_P / tau_q, dimensionless, Conjecture K: eta <= 1.
  t_P = l_P / c is the physical Planck time; tau_q is substrate time per quantum.
- Physical time t and substrate time tau (CONJECTURE N, the time map):
      t = eta * tau
  This is the minimal map consistent with P4 (the readout is the metric):
  physical time is a linear functional of substrate time with one
  dimensionless conversion factor eta. Nothing in P1-P5 fixes eta.

## Evaporation law (model input)

    dN/dtau = -r0 * (1 - N/N0)^alpha,   N(0) = N0

N = number of area quanta remaining; N0 = initial quanta; r0 = rate; alpha = shape.
alpha = 0 is constant substrate-rate evaporation; alpha -> 1 slows as N -> N0.

## Solution

Separable. With u = 1 - N/N0 (u: 0 at tau=0, N=N0; u -> 1 at N=0):

    dN/(1-N/N0)^alpha = -r0 dtau
    -N0 du/u^alpha = -r0 dtau   =>   N0 du/u^alpha = r0 dtau

Integrating u:0 -> (1-N/N0):

  alpha != 1:
      tau(N) = N0 / (r0 (1-alpha)) * (1 - N/N0)^(1-alpha)
  alpha = 1:
      tau(N) = -(N0/r0) * ln(1 - N/N0)
  alpha > 1: reaches N=0 at finite tau
      tau_evap = N0 / (r0 (alpha-1))
  alpha <= 1: N->0 only as tau->inf (asymptotic evaporation)

## Physical Page time

Page time = turnover at N = N0/2 (where the two channel capacities cross).

  tau_P = tau(N0/2)
  alpha != 1:
      tau_P = N0 / (r0 (1-alpha)) * (1/2)^(1-alpha)
  alpha = 1:
      tau_P = N0 ln2 / r0

Physical Page time:

    t_P(N0, r0, alpha, eta) = eta * tau_P

So:

  alpha != 1:
      t_P = eta * N0 / (r0 (1-alpha)) * (1/2)^(1-alpha)
  alpha = 1:
      t_P = eta * N0 ln2 / r0

## Identifiability (consequence)

t_P vs N0 is a straight line through the origin:

    t_P = C * N0,   C = eta * K(alpha) / r0,   K(alpha) = (1/2)^(1-alpha)/(1-alpha)

One measurable slope C, three unknowns (eta, r0, alpha) => eta is NOT
identifiable from Page-time data alone. Breaking the degeneracy requires an
independent measurement of r0 (substrate rate dN/dtau at known N), of alpha
(from the full evaporation-curve shape, not just the Page time), or a direct
substrate-time reading tau. See simulations/test_om.py.

## Code

simulations/page_map.py  — substrate_time(), page_time_substrate(),
page_time_physical(), evaporation_time_substrate().
simulations/test_om.py   — identifiability + universality on SYNTHETIC data.

## Honesty

eta is a [CONJECTURE] free parameter, not a constant of nature. No existing
dataset supports it; the universality test in test_om.py uses SYNTHETIC data.
