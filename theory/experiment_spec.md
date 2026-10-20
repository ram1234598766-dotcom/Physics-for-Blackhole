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

## 6. Multi-Observable Joint Inversion (simulations/exp_inversion.py)

Added two model-dependent observables to break the Page-time degeneracy:
  1. Page-time slope C          = eta * K(alpha) / r0        (K(alpha) = alpha^1.5/(1+alpha))
  2. Graybody peak frequency    = alpha / r0
  3. OTOC scrambling rate       = (2*pi/eta) * (1 - 0.1*r0)^alpha

Ground truth (conjectured, NOT measured): eta = 0.5000, r0 = 1.2000,
alpha = 0.8500. Derived observables: C = 0.17650, w_peak = 0.70833,
lambda_L = 11.27250. 2% Gaussian noise, random.seed(42), N = 1000 trials.

Execution (pure Python, standard library; results differ from any numpy
run because Python's RNG differs from numpy's even with the same seed):

  Reconstructed eta   : 0.5142 +/- 0.0242  (True: 0.5000)
  Reconstructed r0    : 1.0220 +/- 0.2996  (True: 1.2000)
  Reconstructed alpha : 0.7245 +/- 0.2172  (True: 0.8500)
  Degeneracy Broken! Absolute bias in eta: 2.83%

**[WARNING] eta bias above 1% — degeneracy not cleanly broken.**

Interpretation (honest):
- eta is recovered within ~1 standard deviation of its conjectured truth
  (0.5142 vs 0.5000; difference 0.0142 < eta_std 0.0242), so the
  point estimate is statistically consistent, but the 2.83% point-estimate
  bias exceeds the script's 1% success threshold.
- r0 and alpha are POORLY constrained: r0_std = 0.2996 (~25% relative) and
  alpha_std = 0.2172 (~25% relative), both biased low. The alpha scan
  coupled with r0 = alpha / w_obs leaves strong residual correlation.
- Conclusion: adding ω_peak and λ_L narrows eta relative to Page-time-only
  (where eta was wholly unidentifiable), but r0 and alpha remain weakly
  identified, and eta is only recovered to a few percent. The degeneracy is
  *reduced*, not eliminated, within this synthetic model.

Caveats (honesty):
- omega_peak and lambda_L are MODEL-DEPENDENT synthetic observables; neither
  has been measured in any real analog-horizon or black-hole experiment.
- Ground-truth values are conjectured ("Conjectured Nature"), not measured.
- This breaks the degeneracy INSIDE THE MODEL on SYNTHETIC data only. It does
  not establish OM = eta*c as a constant of nature.

## 7. Honest status

- eta is a [CONJECTURE] free parameter; it is NOT a constant of nature.
- No experiment above has been performed; no value of eta has been measured.
- The universality test in simulations/test_om.py used SYNTHETIC data only.
- Claiming OM as a constant of nature before an experiment like this reports
  eta < 1 with controlled systematics would be fabrication.

