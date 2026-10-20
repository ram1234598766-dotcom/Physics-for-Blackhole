# Experimental specification: measuring eta = OM/c

**Purpose.** Pin down the framework's single free parameter
    eta = OM/c = v_s,lin/c = t_P/tau_q
or show it cannot be pinned. Nothing here has been measured; all numbers
below are requirements, not results. No existing dataset is claimed to
support the framework.

## 1. What must be measured

The observable is the Page-time shift of the radiation entropy staircase
in an analog horizon (BEC, water wave, optical fiber, ion ring, ...).

For N = A/Delta_a area quanta remaining (Delta_a = 4 ln2 xi^2, one bit
per quantum; xi = healing length = analog Planck scale), a half-quantum
misplacement of the Page time gives

    Delta t / t = 3 / (4 N)

and a full quantum gives 3/(2N). With R = 5–20 µm and xi = 0.3 µm,
N ~ 1.3×10^3 – 2×10^4, so Delta t/t ~ 4×10^-5 – 4×10^-4 (half quantum)
— small but potentially resolvable if the radiation entropy can be
tracked to sub-per-cent precision over the evaporation window.

Physical Page time (Conjecture N time map t = eta·tau):

    t_P(N0, r0, alpha, eta) = eta · N0 / (r0 (1-alpha)) · (1/2)^(1-alpha)    (alpha != 1)
                              = eta · N0 ln2 / r0                            (alpha = 1)

So eta is read off as eta = t_P_observed / tau_P(N0, r0, alpha).

## 2. The identifiability problem (task 3, honest statement)

Page-time data alone measures only the slope C = eta·K(alpha)/r0 in
t_P = C·N0. One slope, three unknowns (eta, r0, alpha) => eta is NOT
identifiable from Page-time data alone.

**Degeneracy-breaking requirement — at least one of:**
- (a) independent measurement of r0 = dN/dtau at a known N (substrate
  reconfiguration rate per quantum), or
- (b) alpha from the *shape* of the full evaporation curve N(tau), not
  just the Page time, or
- (c) a direct substrate-time reading tau (not physical time t).

Without (a), (b), or (c), eta cannot be separated from r0 and alpha,
and the parameter is empirically meaningless ([F14]).
[F14 decision rule: relative error on eta > 100% after degeneracy-breaking
=> eta not identifiable.]

## 3. Required experimental program

System: analog horizon with tunable R and xi so that N spans at least
3–5 distinct values (e.g. R = 5, 10, 20 µm at xi = 0.3 µm; plus xi = 0.5 µm).
For each system:
- measure N0 = pi R^2 / (ln2 xi^2) from geometry;
- measure the physical Page time t_P from the radiation entropy staircase;
- resolve entropy steps of one logical qunit (k_B ln 2);
- timing precision better than Delta t/t ~ 3/(4N) for the smallest N.

## 4. Decision rules

**[F13] Causal bound.** Conjecture K: eta <= 1 (v_s,lin <= c).
- fitted eta with lower error bar > 1 => Conjecture K falsified;
- eta = 1 => framework reduces to the standard light-speed story;
- only eta < 1 leaves the framework standing.

**[F15] Universality.** The same eta must describe every system.
- Fit eta separately for each system (after breaking the degeneracy).
- max_i |eta_i − eta_pooled| > 3·SE_pooled => universality fails, no single OM.
- On null data (no eta-dependence), a false claim of universality above the
  nominal rate also invalidates the test.

**[F14] Identifiability.** See section 2.

## 5. Honest status

- eta is a [CONJECTURE] free parameter; it is NOT a constant of nature.
- No experiment above has been performed; no value of eta has been measured.
- The universality test in simulations/test_om.py used SYNTHETIC data only.
- Claiming OM as a constant of nature before an experiment like this reports
  eta < 1 with controlled systematics would be fabrication.
