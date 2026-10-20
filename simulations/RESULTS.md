# Physics-for-Blackhole - simulation results

Generated 2026-10-20 by `python3 -m simulations.run_all`.

Pure Python, no dependencies.  All quantities are exact within the stated tolerances; every random-unitary run uses a fixed seed so the numbers are reproducible.

SYNTHETIC data appears only inside `test_om.py` and is labelled as such; nothing here is a real measurement.

## 0. Validation of the numerical machinery

```
Hermitian eigensolver, H = [[1, i], [-i, 2]]
  computed [0.38196601125, 2.61803398875]
  exact    [0.38196601125, 2.61803398875]
  max error = 1.110e-16
bit spreading: consistent
pure-state bipartition identity S(A)=S(B), max error over n=4,6,8,10 and all splits: 4.441e-16
reduced rho: max |trace-1| = 2.220e-16, most negative eigenvalue = 6.990e-17
random block unitary: 34 blocks tested on registers of 2-5 qubits,
  max change of norm = 5.551e-16
product state |000> under a random 3-qubit unitary: S(qubit 0) = 0.4058 nats

all validation checks pass
```

## 1. The evaporation ledger

```
========================================================================
TEST 1 - the evaporation ledger
========================================================================
random-unitary (Householder) ensemble, 3 trials per size

A. PURE MICROSTATE SENDER  (Physics-for-Blackhole: ledger respected)
------------------------------------------------------------------------

  simulated S(rad)/ln2 (average over trials) vs. Page's formula
  n0= 4 |  0.00  0.76  1.34  0.88  0.00
  n0= 6 |  0.00  0.96  1.85  2.33  1.78  0.97  0.00
  n0= 8 |  0.00  1.00  1.97  2.83  3.27  2.80  1.95  0.98  0.00
  n0=10 |  0.00  1.00  1.99  2.95  3.82  4.26  3.82  2.96  1.99  1.00  0.00
  Page   4 | -0.05  0.82  1.28  0.82 -0.05
  Page   6 | -0.01  0.95  1.82  2.28  1.82  0.95 -0.01
  Page   8 | -0.00  0.99  1.95  2.82  3.28  2.82  1.95  0.99 -0.00
  Page  10 | -0.00  1.00  1.99  2.95  3.82  4.28  3.82  2.95  1.99  1.00 -0.00

B. THERMAL SENDER WITH PURIFIER  (Physics-for-Blackhole: ledger blind)
------------------------------------------------------------------------
  n0=6 (register 12 qubits, purifier traced out)
   m | S(rad)/ln2 | I(R:Rad)/ln2 | I(R:Rem)/ln2 | sum/ln2
   1 |     1.0000 |       2.0000 |      10.0000 |  12.0000
   2 |     2.0000 |       4.0000 |       8.0000 |  12.0000
   3 |     3.0000 |       6.0000 |       6.0000 |  12.0000
   4 |     4.0000 |       8.0000 |       4.0000 |  12.0000
   5 |     5.0000 |      10.0000 |       2.0000 |  12.0000
   6 |     6.0000 |      12.0000 |      -0.0000 |  12.0000
  purifier entropy S(R)/ln2 = 6
  -> the purifier's mutual information with the two channels is
     transferred one-for-one:  I(R:Rad) + I(R:Rem) = const.

  note: the S(rad) column is the *ledger-blind* curve.  An observer
  who also has access to R follows the Page curve instead.
```

## 2. Quantised payout

```
========================================================================
TEST 2 - quantised payout: the evaporation staircase
========================================================================
area quantum   ΔA = 4 ln2 ℓ_P² = 7.242779e-70 m²
one quantum of entropy = k_B ln 2 = 9.569930e-24 J/K

Q1  the Page time moves from n0/2 to the first integer m >= n0 - m
------------------------------------------------------------------------
   n0 |  smooth m*  quantised m* | shift Δm | ΔS at m* (bits)
      2 |       1.0           1 |     0.00 |     0.00
      3 |       1.5           2 |     0.50 |    -0.50
      4 |       2.0           2 |     0.00 |     0.00
      5 |       2.5           3 |     0.50 |    -0.50
      9 |       4.5           5 |     0.50 |    -0.50
     10 |       5.0           5 |     0.00 |     0.00
     11 |       5.5           6 |     0.50 |    -0.50
     16 |       8.0           8 |     0.00 |     0.00
    101 |      50.5          51 |     0.50 |    -0.50
   1000 |     500.0         500 |     0.00 |     0.00
  10000 |    5000.0        5000 |     0.00 |     0.00

  the shift is at most half a quantum: Δm <= 1/2 for every n0.
  an odd number of quanta always pays out the last half-quantum early.

Q2  granularity of the staircase
------------------------------------------------------------------------
  The entropy of the radiation is not a continuous function of the
  emitted mass: it can only take values that are multiples of k_B ln 2,
  because each step of the ladder is one area quantum.  Two consequences.

  N quanta   granularity 1/N   max Δm (quanta)    max Δt/t
        10          1.00e-01              0.50   1.500e-01
       100          1.00e-02              0.50   1.500e-02
      1000          1.00e-03              0.50   1.500e-03
     10000          1.00e-04              0.50   1.500e-04
   1000000          1.00e-06              0.50   1.500e-06
10000000000          1.00e-10              0.50   1.500e-10
10000000000000000000000000000000000000000          1.00e-40              0.50   1.500e-40
100000000000000000000000000000000000000000000000000000000000000000000000000000          1.00e-77              0.50   1.500e-77

  the largest possible misplacement of the Page time is half a quantum;
  since N = A/ΔA ∝ M² and t ∝ M³, that is Δt/t = 3/(2N) in time,
  which is utterly negligible for any
  astrophysical black hole and finite for the small ones.

Q2b the shape of the ladder for a hole with only a few quanta
------------------------------------------------------------------------
     N    0    1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19   20   21   22   23   24   25   26   27   28   29   30   31   32   33   34   35   36   37   38   39   40
     5    0    1    2    2    1    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0
    10    0    1    2    3    4    5    4    3    2    1    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0
    20    0    1    2    3    4    5    6    7    8    9   10    9    8    7    6    5    4    3    2    1    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0
    40    0    1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19   20   19   18   17   16   15   14   13   12   11   10    9    8    7    6    5    4    3    2    1    0

  values are S/k_B ln 2, i.e. bits.  A hole with a handful of area
  quanta has a Page curve that is a tent over a few steps - there is no
  'smooth' Page curve left to talk about.  That is the endpoint regime,
  and it is the only regime in which the staircase is not suppressed.
Q3  how many quanta do real systems have, and how big is the shift
------------------------------------------------------------------------
object                              mass (kg)    N quanta        Δt/t
solar-mass black hole               1.988e+30   1.513e+77   9.912e-78
Sgr A* (4.3e6 M☉)                   8.550e+36   2.798e+90   5.361e-91
M87* (6.5e9 M☉)                     1.293e+40   6.394e+96   2.346e-97
primordial BH, 10^12 kg             1.000e+12   3.827e+40   3.919e-41
Planck mass                         2.176e-08   1.813e+01   8.274e-02

  a Planck-mass hole - the endpoint of evaporation - carries exactly
  N = 4 pi / ln 2 = 18.13 area quanta, so its Page curve is a tent of
  about eighteen steps and its Page time is misplaced by 3/(2N) = 8%.
  For any astrophysical black hole the same quantity is ~1e-77.

Q4  analog horizons - the size of the last quantised stage
------------------------------------------------------------------------
  Here the 'Planck length' is set by the condensate healing length ξ.
  N quanta counts the horizon area in units of 4 ln2 ξ².
  R (µm)   ξ (µm)    N quanta last 10 quanta / lifetime
     5.0     0.30      1259.0                     0.008
    10.0     0.30      5036.0                     0.002
    20.0     0.30     20143.8                     0.000
    10.0     0.50      1812.9                     0.006

  If the interface is quantised at the analog Planck scale, the final
  quantised stage of an analog horizon is a finite, non-negligible
  fraction of its life, and is the honest place to look for the
  staircase.  For astrophysical black holes the effect is 1e-77.
```

## 3. Readout degeneracy

```
========================================================================
TEST 3 - Conjecture R: readout degeneracy (the saturated ball)
========================================================================

R1  what the readout reports as q → 1 (i.e. 'as r → 0')
------------------------------------------------------------------------
           q           u    S/Smax      g^E_uu       du/dq     K_readout
    0.500000      0.6931  0.500000   5.000e-01   2.000e+00     4.000e+00
    0.900005      2.3026  0.900005   9.999e-02   1.000e+01     1.000e+02
    0.990000      4.6051  0.990000   1.000e-02   1.000e+02     9.999e+03
    0.999000      6.9078  0.999000   1.000e-03   1.000e+03     1.000e+06
    0.999900      9.2104  0.999900   9.999e-05   1.000e+04     1.000e+08
    0.999990     11.5129  0.999990   1.000e-05   1.000e+05     9.999e+09
    0.999999     13.8155  0.999999   1.000e-06   1.000e+06     1.000e+12

  the readout curvature diverges: K ∝ (1-q)^-2, unbounded.

R2  what the substrate reports at the same values
------------------------------------------------------------------------
  total entropy of the ball          S_max                = 1.000000
  total entropy flux ∫ (dS/du) du                          = 1.000000
  total substrate length ∫ sqrt(g^E_uu) du (numeric)        = 1.999999
  total substrate length ∫ sqrt(g^E_uu) du (exact)         = 2.000000
  absolute difference (tail beyond u=30 is 6.12e-07)     = 6.11e-07

  every substrate invariant is finite and bounded.  There is no
  substrate-level divergence anywhere on this curve.

R3  the entanglement across the cut (the Bekenstein bound in action)
------------------------------------------------------------------------
         q    S(cut) / S_max  capacity used
  0.500000          0.500000       0.500000
  0.900005          0.900005       0.900005
  0.990000          0.990000       0.990000
  0.999000          0.999000       0.999000
  0.999999          0.999999       0.999999

  as q → 1 the cut saturates: S(cut) → S_max and no further
  refinement is possible.  This is what stops the compression, and
  it is a statement about information, not about forces.

R4  comparison with the classical Schwarzschild singularity
------------------------------------------------------------------------
  Schwarzschild radius of the Sun            r_s   = 2.9533e+03 m
  proper distance r_s → 0 (numeric)          L     = 4.635100e+03 m
  proper distance r_s → 0 (exact, π r_s / 2)        = 4.639095e+03 m
  ratio L / r_s (numeric 1.5694, exact π/2 = 1.5708)
  Kretschmann at r = r_s/2                          = 1.0095e-11
  Kretschmann at r = r_s/10                         = 1.5773e-07

  the classical solution has exactly the same shape: a *coordinate*
  quantity (Kretschmann) diverges while a *proper* quantity (distance
  to the centre) stays finite.  Conjecture R says the divergence is a
  property of the readout's Jacobian du/dq, and that keeping it while
  the substrate stays finite is the whole content of 'the theory
  breaks down at r = 0'.

  NOTE: the framework does *not* claim to reproduce the Schwarzschild
  exponent (K ∝ r^-6) until the map q(r) is derived; that derivation
  is open problem O2 of the main document.
```

## 4. Quoted-number consistency (test_numbers)

```
Runs every quoted number check; the script exits non-zero on any FAIL.

N = A / Delta_A  (Delta_A = 4 ln2 l_P^2)
  [PASS] N(Planck mass): computed=18.1294  expected=18.1294
  [PASS] N(solar mass): computed=1.51332e+77  expected=1.5e+77
  [PASS] N(Sgr A* (4.3e6 M☉)): computed=2.79813e+90  expected=2.8e+90
  [PASS] N(M87* (6.5e9 M☉)): computed=6.39379e+96  expected=6.4e+96
  [PASS] Planck N = 4pi/ln2: computed=18.1294  expected=18.1294

Page-time shift  dt/t = (3/2) * dN / N  (t ~ N^(3/2))
  [PASS] Planck mass N=18.13 full-quantum 3/(2N): computed=0.0827384  expected=0.0827384
  [PASS] Planck mass N=18.13 half-quantum 3/(4N): computed=0.0413692  expected=0.0413692
    -> full = 8.274e-02  (8.3% for Planck mass = FULL quantum)
       half = 4.137e-02
  [PASS] solar mass N~1.5e77 full-quantum 3/(2N): computed=9.91197e-78  expected=9.91197e-78
  [PASS] solar mass N~1.5e77 half-quantum 3/(4N): computed=4.95598e-78  expected=4.95598e-78
    -> full = 9.912e-78  (8.3% for Planck mass = FULL quantum)
       half = 4.956e-78
  [PASS] Planck full-quantum percent: computed=8.27384  expected=8.3
  [PASS] solar full-quantum ~1e-77: computed=9.91197e-78  expected=1e-77
  [PASS] solar half-quantum ~5e-78: computed=4.95598e-78  expected=5e-78

Analog horizons  N = pi R^2 / (ln2 xi^2)
  [PASS] N R=5.0um xi=0.3um: computed=1258.99  expected=1260
  R= 5.0 um xi=0.3 um  N=      1259.0  (10/N)= 0.794%  (10/N)^(3/2)=7.0789e-02%
  [PASS] N R=10.0um xi=0.3um: computed=5035.96  expected=5000
  R=10.0 um xi=0.3 um  N=      5036.0  (10/N)= 0.199%  (10/N)^(3/2)=8.8487e-03%
  [PASS] N R=20.0um xi=0.3um: computed=20143.8  expected=20000
  R=20.0 um xi=0.3 um  N=     20143.8  (10/N)= 0.050%  (10/N)^(3/2)=1.1061e-03%
  [PASS] N R=10.0um xi=0.5um: computed=1812.94  expected=1800
  R=10.0 um xi=0.5 um  N=      1812.9  (10/N)= 0.552%  (10/N)^(3/2)=4.0966e-02%
  Quoted '0.8%-0.02%' matches LINEAR (10/N), not (10/N)^(3/2).

Saturated ball  S(u) = S_max (1 - exp(-u/u0))
  [PASS] int sqrt(g^E_uu) du = 2*sqrt(S_max), S_max=1.0: computed=2  expected=2
  [PASS] int g^E_uu du = S_max/u0, S_max=1.0, u0=1.0: computed=1  expected=1
  S_max=1.0  int sqrt(g^E_uu) du = 2.000000 (exact 2*sqrt(S_max))  int g^E_uu du = 1.000000 (= S_max/u0)
  [PASS] int sqrt(g^E_uu) du = 2*sqrt(S_max), S_max=2.0: computed=2.82843  expected=2.82843
  [PASS] int g^E_uu du = S_max/u0, S_max=2.0, u0=1.0: computed=2  expected=2
  S_max=2.0  int sqrt(g^E_uu) du = 2.828427 (exact 2*sqrt(S_max))  int g^E_uu du = 2.000000 (= S_max/u0)

Schwarzschild (solar mass)
  [PASS] proper distance L = pi r_s/2: computed=4639.09  expected=4639.09
  [PASS] L/r_s = pi/2: computed=1.5708  expected=1.5708
  r_s = 2953.339 m
  Kretschmann at r_s = 1.577349e-13 m^-4
  proper distance horizon->centre = 4639.0947 m  (exact pi r_s/2 = 4639.0947)
  L/r_s = 1.570796  vs pi/2 = 1.570796

=== NUMBER CHECK SUMMARY ===
  pass  N(Planck mass)
  pass  N(solar mass)
  pass  N(Sgr A* (4.3e6 M☉))
  pass  N(M87* (6.5e9 M☉))
  pass  Planck N = 4pi/ln2
  pass  Planck mass N=18.13 full-quantum 3/(2N)
  pass  Planck mass N=18.13 half-quantum 3/(4N)
  pass  solar mass N~1.5e77 full-quantum 3/(2N)
  pass  solar mass N~1.5e77 half-quantum 3/(4N)
  pass  Planck full-quantum percent
  pass  solar full-quantum ~1e-77
  pass  solar half-quantum ~5e-78
  pass  N R=5.0um xi=0.3um
  pass  N R=10.0um xi=0.3um
  pass  N R=20.0um xi=0.3um
  pass  N R=10.0um xi=0.5um
  pass  int sqrt(g^E_uu) du = 2*sqrt(S_max), S_max=1.0
  pass  int g^E_uu du = S_max/u0, S_max=1.0, u0=1.0
  pass  int sqrt(g^E_uu) du = 2*sqrt(S_max), S_max=2.0
  pass  int g^E_uu du = S_max/u0, S_max=2.0, u0=1.0
  pass  proper distance L = pi r_s/2
  pass  L/r_s = pi/2

22/22 checks passed, 0 failed.

```

## 5. Identifiability and universality of eta (test_om)

```
IDENTIFIABILITY (model structure, no data needed)
  t_P = eta * N0/(r0(1-alpha)) * (1/2)^(1-alpha)   (alpha != 1)
        = eta * N0 ln2 / r0                            (alpha = 1)
  t_P vs N0 is linear:  t_P = C * N0,  C = eta * K(alpha) / r0
  One slope C, three unknowns (eta, r0, alpha) -> eta NOT identifiable.
  Needed to break degeneracy: independent r0, or alpha from curve shape,
  or a direct substrate-time tau measurement.

UNIVERSALITY TEST (SYNTHETIC data)
  hidden eta = 0.5,  trials = 2000,  systems = 5
  pooled eta mean = 0.4992  (should equal 0.5)
  pooled eta std  = 0.0255  (theory SE = 0.0250)
  pass rate (|eta_pooled-eta_true| within 3*SE = 0.0750): 99.7%
  UNIVERSAL (shared eta recovers the truth within 3*SE): True

NULL TEST (SYNTHETIC data, no eta-dependence)
  trials = 5000, 3 systems, t_P independent of eta model
  false claim of universality: 0.0%
  (null data is wildly non-universal: eta_i spans orders of magnitude)


```

## 6. Multi-observable joint inversion (exp_inversion)

```
=== Multi-Observable Joint Inversion Experiment ===
(SYNTHETIC data — ground truth conjectured, Gaussian noise, seed=42)
[TRUTH] eta: 0.5000 | r0: 1.2000 | alpha: 0.8500
[DERIVED OBS] C: 0.17650 | w_peak: 0.70833 | lambda_L: 11.27250

=== Joint Inversion Results (N = 1000 noisy measurements) ===
Reconstructed eta   : 0.5142 +/- 0.0242 (True: 0.5000)
Reconstructed r0    : 1.0220 +/- 0.2996 (True: 1.2000)
Reconstructed alpha : 0.7245 +/- 0.2172 (True: 0.8500)

Degeneracy Broken! Absolute bias in eta: 2.83%
[WARNING] eta bias above 1% — degeneracy not cleanly broken.

```

## FINAL SUMMARY

**Is eta identifiable inside the model?** No from Page-time alone: it measures only slope C = eta·K(alpha)/r0 (one slope, three unknowns), degenerate with r0 and alpha. Adding model-dependent synthetic observables (graybody peak frequency, OTOC scrambling rate) in simulations/exp_inversion.py reduces but does not eliminate the degeneracy: pooled eta = 0.5142 +/- 0.0242 vs truth 0.5000 (bias 2.83%, above the 1% success threshold), while r0 = 1.0220 +/- 0.2996 and alpha = 0.7245 +/- 0.2172 remain poorly constrained. Both new observables are conjectured and unmeasured. [F14: relative error on eta > 100% after degeneracy-breaking => not identifiable.]

**Is eta universal inside the model?** Yes, on SYNTHETIC data. A single shared eta describes systems with different analog scales (N0 spanning 1.2×10^3 to 10^10): pooled eta mean = 0.4992 vs hidden truth 0.5, std 0.0255 ≈ theory SE 0.0250, pass rate 99.7% within 3·SE, null-data false-claim-of-universality rate 0.0%. [F15: max_i |eta_i − eta_pooled| > 3·SE_pooled, or a false-universality rate above nominal, => not universal.]

**What remains untested.** eta is a [CONJECTURE] free parameter, not a constant of nature; establishing OM as a constant of nature would require an actual analog-horizon Page-time-shift measurement, which does not yet exist. No existing analog-horizon dataset supports the framework. The degeneracy-breaking measurements (independent r0, alpha, or direct tau) have not been performed on any system. theory/analog_assumptions.md lists the unproven assumptions needed to apply the model to a BEC or other analog horizon (healing length as analog Planck scale; Page-like behaviour requires backreaction). All numbers here come from test_numbers.py, test_om.py, and exp_inversion.py; all synthetic data is labelled SYNTHETIC.

