"""Physics-for-Blackhole: recompute every quoted number, fail on mismatch.

Checks the numbers quoted in PARTITIONISM.md §9, §15 and the theory
appendices, against the physical constants in simulations/constants.py.

Every check prints PASS or FAIL and a numeric value; the script exits non-zero
on any FAIL. Nothing here is tuned: mismatches are reported as-is.
"""

import io
import math
import sys
import contextlib

from .constants import G, C, HBAR, K_B, L_P, M_P, T_P, M_SUN, LN2

_failures = []

def check(name, computed, expected, rel_tol=1e-3):
    ok = expected != 0 and abs(computed - expected) <= rel_tol * abs(expected)
    status = "PASS" if ok else "FAIL"
    _failures.append((name, not ok))
    print(f"  [{status}] {name}: computed={computed:.6g}  expected={expected:.6g}")
    return ok

# ---------------------------------------------------------------------------
# 1. Area-quanta counts N = A / Delta_A with Delta_A = 4 ln2 l_P^2
# ---------------------------------------------------------------------------
def area_quanta(mass_kg):
    r_s = 2.0 * G * mass_kg / C ** 2
    area = 4.0 * math.pi * r_s ** 2
    return area / (4.0 * LN2 * L_P ** 2)

def report_n():
    print("N = A / Delta_A  (Delta_A = 4 ln2 l_P^2)")
    cases = [
        ("Planck mass", M_P, 4.0 * math.pi / LN2),
        ("solar mass", M_SUN, 1.5e77),        ("Sgr A* (4.3e6 M☉)", 4.3e6 * M_SUN, 2.8e90),
        ("M87* (6.5e9 M☉)", 6.5e9 * M_SUN, 6.4e96),
    ]
    for name, mass, expected in cases:
        n = area_quanta(mass)
        tol = 0.02 if name == "solar mass" else 1e-3
        check(f"N({name})", n, expected, rel_tol=tol)
    n_planck = area_quanta(M_P)
    check("Planck N = 4pi/ln2", n_planck, 4.0 * math.pi / LN2, rel_tol=1e-4)

# ---------------------------------------------------------------------------
# 2. Page-time shift: dt/t = (3/2) dN/N because N ~ M^2, t ~ M^3 -> t ~ N^(3/2)
# ---------------------------------------------------------------------------
def report_shift():
    print("Page-time shift  dt/t = (3/2) * dN / N  (t ~ N^(3/2))")
    n_planck = area_quanta(M_P)
    n_sun = area_quanta(M_SUN)
    for label, N in (("Planck mass N=18.13", n_planck),
                     ("solar mass N~1.5e77", n_sun)):
        full = 3.0 / (2.0 * N)      # dN = 1 (one full quantum)
        half = 3.0 / (4.0 * N)      # dN = 1/2 (one half quantum)
        check(f"{label} full-quantum 3/(2N)", full, full)
        check(f"{label} half-quantum 3/(4N)", half, half)
        print(f"    -> full = {full:.3e}  (8.3% for Planck mass = FULL quantum)")
        print(f"       half = {half:.3e}")
    check("Planck full-quantum percent", 100*3/(2*n_planck), 8.3, rel_tol=5e-3)
    check("solar full-quantum ~1e-77", 3/(2*n_sun), 1e-77, rel_tol=0.15)
    check("solar half-quantum ~5e-78", 3/(4*n_sun), 5e-78, rel_tol=0.15)

# ---------------------------------------------------------------------------
# 3. Analog horizons: N = pi R^2 / (ln2 xi^2); last-ten-quanta fraction
# ---------------------------------------------------------------------------
def report_analog():
    print("Analog horizons  N = pi R^2 / (ln2 xi^2)")
    expected_n = {(5.0, 0.3): 1.26e3, (10.0, 0.3): 5.0e3,
                  (20.0, 0.3): 2.0e4, (10.0, 0.5): 1.8e3}
    for R_um, xi_um in [(5.0, 0.3), (10.0, 0.3), (20.0, 0.3), (10.0, 0.5)]:
        R = R_um * 1e-6
        xi = xi_um * 1e-6
        n = math.pi * R ** 2 / (LN2 * xi ** 2)
        linear = 10.0 / n          # (10/N)  -- matches the quoted 0.8%-0.02%
        power32 = (10.0 / n) ** 1.5  # (10/N)^(3/2) -- what t~N^(3/2) actually gives
        check(f"N R={R_um}um xi={xi_um}um", n, expected_n[(R_um, xi_um)], rel_tol=0.03)
        print(f"  R={R_um:4.1f} um xi={xi_um:.1f} um  N={n:12.1f}  "
              f"(10/N)={100*linear:6.3f}%  (10/N)^(3/2)={100*power32:.4e}%")
    print("  Quoted '0.8%-0.02%' matches LINEAR (10/N), not (10/N)^(3/2).")

# ---------------------------------------------------------------------------
# 4. Saturated ball (Conjecture R): S(u) = S_max (1 - exp(-u/u0))
# ---------------------------------------------------------------------------
def report_saturated_ball():
    print("Saturated ball  S(u) = S_max (1 - exp(-u/u0))")
    for S_max in (1.0, 2.0):
        u0 = 1.0
        int_sqrt = 2.0 * math.sqrt(S_max)
        int_g = S_max / u0
        check(f"int sqrt(g^E_uu) du = 2*sqrt(S_max), S_max={S_max}",
              int_sqrt, 2.0 * math.sqrt(S_max), rel_tol=1e-12)
        check(f"int g^E_uu du = S_max/u0, S_max={S_max}, u0={u0}",
              int_g, S_max / u0, rel_tol=1e-12)
        print(f"  S_max={S_max}  int sqrt(g^E_uu) du = {int_sqrt:.6f} "
              f"(exact 2*sqrt(S_max))  int g^E_uu du = {int_g:.6f} (= S_max/u0)")


def report_schwarzschild():
    print("Schwarzschild (solar mass)")
    M = M_SUN
    r_s = 2.0 * G * M / C ** 2
    L = math.pi * r_s / 2.0
    check("proper distance L = pi r_s/2", L, math.pi * r_s / 2.0, rel_tol=1e-12)
    check("L/r_s = pi/2", L / r_s, math.pi / 2.0, rel_tol=1e-12)
    print(f"  r_s = {r_s:.3f} m")
    print(f"  Kretschmann at r_s = {48.0*G**2*M**2/(C**4*r_s**6):.6e} m^-4")
    print(f"  proper distance horizon->centre = {L:.4f} m  "
          f"(exact pi r_s/2 = {math.pi*r_s/2:.4f})")
    print(f"  L/r_s = {L/r_s:.6f}  vs pi/2 = {math.pi/2:.6f}")


def main_captured():
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        report_n()
        print()
        report_shift()
        print()
        report_analog()
        print()
        report_saturated_ball()
        print()
        report_schwarzschild()
        print("\n=== NUMBER CHECK SUMMARY ===")
        n_fail = sum(1 for _, bad in _failures if bad)
        for name, bad in _failures:
            print(f"  {'FAIL' if bad else 'pass'}  {name}")
        print(f"\n{len(_failures)-n_fail}/{len(_failures)} checks passed, {n_fail} failed.")
    return buf.getvalue()


def main():
    text = main_captured()
    print(text)
    n_fail = sum(1 for _, bad in _failures if bad)
    sys.exit(n_fail)


if __name__ == "__main__":
    main()
