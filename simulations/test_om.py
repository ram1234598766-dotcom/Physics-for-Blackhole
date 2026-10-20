"""Physics-for-Blackhole: identifiability and universality of eta.

OM = v_s,lin = l_P / tau_q;  eta = OM/c = t_P/tau_q (dimensionless, Conjecture K: eta <= 1).

Physical Page time (from page_map.py):
    t_P(N0, r0, alpha, eta) = eta * N0 / (r0 (1-alpha)) * (1/2)^(1-alpha)   (alpha != 1)
                              = eta * N0 ln2 / r0                            (alpha = 1)

All synthetic data below is labelled SYNTHETIC; nothing is a real measurement.
"""

import io
import math
import random
import contextlib
from .page_map import page_time_substrate, page_time_physical

# ---------------------------------------------------------------------------
# 3. Identifiability: can eta be separated from r0 and alpha using Page-time
#    data alone?
# ---------------------------------------------------------------------------
def identifiability():
    """Show that Page-time data alone identifies only one combination.

    For alpha != 1:
        t_P = eta * N0/(r0(1-alpha)) * (1/2)^(1-alpha)
            = [eta * K(alpha) / r0] * N0,   K(alpha) = (1/2)^(1-alpha)/(1-alpha)
    So t_P vs N0 is a straight line through the origin with slope
        C = eta * K(alpha) / r0.
    One slope, three unknowns (eta, r0, alpha) -> degenerate. eta is not
    identifiable from Page-time data alone.

    Even with many N0 values you only ever measure C, never eta separately.
    Breaking the degeneracy requires an independent measurement: either the
    substrate rate r0 (dN/dtau at a known N), the exponent alpha (from the
    full evaporation curve shape, not just the Page time), or a direct
    substrate-time reading tau.
    """
    print("IDENTIFIABILITY (model structure, no data needed)")
    print("  t_P = eta * N0/(r0(1-alpha)) * (1/2)^(1-alpha)   (alpha != 1)")
    print("        = eta * N0 ln2 / r0                            (alpha = 1)")
    print("  t_P vs N0 is linear:  t_P = C * N0,  C = eta * K(alpha) / r0")
    print("  One slope C, three unknowns (eta, r0, alpha) -> eta NOT identifiable.")
    print("  Needed to break degeneracy: independent r0, or alpha from curve shape,")
    print("  or a direct substrate-time tau measurement.")
    print()

# ---------------------------------------------------------------------------
# 4. Universality test on SYNTHETIC data
# ---------------------------------------------------------------------------
def synth_page_time(N0, r0, alpha, eta, rng, rel_noise=0.05):
    """SYNTHETIC observed physical Page time with Gaussian relative noise."""
    tau = page_time_substrate(N0, r0, alpha)
    t_true = eta * tau
    return t_true * (1.0 + rng.gauss(0.0, rel_noise))

def fit_eta(t_obs, N0, r0, alpha):
    """Per-system eta estimate from one Page-time measurement."""
    tau = page_time_substrate(N0, r0, alpha)
    if tau <= 0 or not math.isfinite(tau):
        return float("nan")
    return t_obs / tau

def universality_test():
    """Generate SYNTHETIC Page-time data for several systems from a hidden
    eta, fit eta separately for each, test whether fits agree.

    Method: for each trial, pooled least-squares fit of a single shared eta
    through the origin (t_P = eta * tau_P).  Report the fraction of trials in
    which the pooled eta recovers the hidden value within 3 sigma of the
    noise-on-the-mean.  That fraction is the universality true-positive rate.
    """
    print("UNIVERSALITY TEST (SYNTHETIC data)")
    rng = random.Random(20261020)
    eta_true = 0.5
    r0 = 1.0
    alpha = 0.5
    rel_noise = 0.05
    n_trial = 2000
    nsys = 5

    systems = [
        ("analog R=5um  xi=0.3um", 1259.0),
        ("analog R=10um xi=0.3um", 5037.0),
        ("analog R=20um xi=0.3um", 20148.0),
        ("analog R=10um xi=0.5um", 1813.0),
        ("astrophysical-like N0=1e10", 1e10),
    ]
    taus = [page_time_substrate(N0, r0, alpha) for _, N0 in systems]

    pass_n = 0
    pooled_vals = []
    for _ in range(n_trial):
        num = den = 0.0
        for tau in taus:
            t_obs = eta_true * tau * (1.0 + rng.gauss(0.0, rel_noise))
            num += t_obs * tau
            den += tau * tau
        eta_pooled = num / den
        pooled_vals.append(eta_pooled)

    pm = sum(pooled_vals) / n_trial
    psd = math.sqrt(sum((v - pm) ** 2 for v in pooled_vals) / n_trial)
    # Correct standard error of the pooled least-squares eta:
    # eta_pooled = sum(t_i tau_i)/sum(tau_i^2), t_i = eta tau_i (1+noise_i)
    # SE = eta * rel_noise * sqrt(sum(tau^4)) / sum(tau^2)
    sum_tau2 = sum(t * t for t in taus)
    sum_tau4 = sum(t ** 4 for t in taus)
    se = eta_true * rel_noise * math.sqrt(sum_tau4) / sum_tau2
    pass_n = sum(1 for v in pooled_vals if abs(v - eta_true) <= 3 * se)
    print(f"  hidden eta = {eta_true},  trials = {n_trial},  systems = {nsys}")
    print(f"  pooled eta mean = {pm:.4f}  (should equal {eta_true})")
    print(f"  pooled eta std  = {psd:.4f}  (theory SE = {se:.4f})")
    print(f"  pass rate (|eta_pooled-eta_true| within 3*SE = {3*se:.4f}): "
          f"{pass_n/n_trial*100:.1f}%")
    print(f"  UNIVERSAL (shared eta recovers the truth within 3*SE): "
          f"{psd <= 3*se and abs(pm-eta_true)<=3*se}")
    print()

def null_false_positive():
    """Null: Page-time data with NO eta-dependence (t_P independent of the
    eta model). Fit eta anyway; false positive = fraction of trials where we
    spuriously conclude universality (relative spread < 5%)."""
    print("NULL TEST (SYNTHETIC data, no eta-dependence)")
    rng = random.Random(777)
    r0 = 1.0
    alpha = 0.5

    systems = [
        ("sys A", 1000.0), ("sys B", 5000.0), ("sys C", 20000.0),
    ]
    n_trial = 5000
    false_universal = 0

    for _ in range(n_trial):
        etas = []
        for name, N0 in systems:
            # t_P drawn independently of N0 and of eta (null)
            t_obs = 10.0 * math.exp(rng.gauss(0.0, 0.3))
            tau = page_time_substrate(N0, r0, alpha)
            etas.append(t_obs / tau)
        m = sum(etas) / len(etas)
        spread = max(etas) - min(etas)
        if spread / m < 0.05:          # spuriously tight -> false universality
            false_universal += 1

    print(f"  trials = {n_trial}, 3 systems, t_P independent of eta model")
    print(f"  false claim of universality: {false_universal/n_trial*100:.1f}%")
    print(f"  (null data is wildly non-universal: eta_i spans orders of magnitude)")
    print()

def main_captured():
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        identifiability()
        universality_test()
        null_false_positive()
    return buf.getvalue()


def main():
    print(main_captured())


if __name__ == "__main__":
    main()
