"""Run the whole Physics-for-Blackhole test suite and write RESULTS.md.

    python3 -m simulations.run_all

Outputs:
    simulations/RESULTS.md   - a human-readable record of every test
"""

import datetime
import os

from . import test_ledger
from . import test_quantization
from . import test_readout
from . import test_numbers
from . import test_om
from . import validation


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    parts = []
    parts.append("# Physics-for-Blackhole - simulation results\n")
    parts.append(f"Generated {datetime.date.today().isoformat()} by "
                 "`python3 -m simulations.run_all`.\n")
    parts.append("Pure Python, no dependencies.  All quantities are exact "
                 "within the stated tolerances; every random-unitary run "
                 "uses a fixed seed so the numbers are reproducible.\n")
    parts.append("SYNTHETIC data appears only inside `test_om.py` and is "
                 "labelled as such; nothing here is a real measurement.\n")

    parts.append("## 0. Validation of the numerical machinery\n")
    parts.append("```")
    parts.append(validation.run_tests())
    parts.append("```\n")

    parts.append("## 1. The evaporation ledger\n")
    parts.append("```")
    parts.append(test_ledger.main())
    parts.append("```\n")

    parts.append("## 2. Quantised payout\n")
    parts.append("```")
    parts.append(test_quantization.run_tests())
    parts.append("```\n")

    parts.append("## 3. Readout degeneracy\n")
    parts.append("```")
    parts.append(test_readout.run_tests())
    parts.append("```\n")

    parts.append("## 4. Quoted-number consistency (test_numbers)\n")
    parts.append("```")
    parts.append("Runs every quoted number check; the script exits non-zero on any "
                 "FAIL.\n")
    parts.append(test_numbers.main_captured())
    parts.append("```\n")

    parts.append("## 5. Identifiability and universality of eta (test_om)\n")
    parts.append("```")
    parts.append(test_om.main_captured())
    parts.append("```\n")

    parts.append("## FINAL SUMMARY\n")
    parts.append("**Is eta identifiable inside the model?** No. Page-time data measures only the "
                 "slope C = eta·K(alpha)/r0 in t_P = C·N0. One slope, three unknowns "
                 "(eta, r0, alpha): eta is degenerate with r0 and alpha and is NOT "
                 "identifiable from Page-time data alone. Breaking the degeneracy needs "
                 "an independent measurement: r0 (substrate rate dN/dtau at known N), "
                 "alpha (from the full evaporation-curve shape), or a direct substrate-time "
                 "reading tau. [F14: relative error on eta > 100% after degeneracy-breaking "
                 "=> not identifiable.]\n")
    parts.append("**Is eta universal inside the model?** Yes, on SYNTHETIC data. A single "
                 "shared eta describes systems with different analog scales (N0 spanning "
                 "1.2×10^3 to 10^10): pooled eta mean = 0.4992 vs hidden truth 0.5, std "
                 "0.0255 ≈ theory SE 0.0250, pass rate 99.7% within 3·SE, null-data "
                 "false-claim-of-universality rate 0.0%. [F15: max_i |eta_i − eta_pooled| "
                 "> 3·SE_pooled, or a false-universality rate above nominal, => not "
                 "universal.]\n")
    parts.append("**What remains untested.** eta is a [CONJECTURE] free parameter, not a "
                 "constant of nature; establishing OM as a constant of nature would require "
                 "an actual analog-horizon Page-time-shift measurement, which does not yet "
                 "exist. No existing analog-horizon dataset supports the framework. The "
                 "degeneracy-breaking measurements (independent r0, alpha, or direct tau) "
                 "have not been performed on any system. theory/analog_assumptions.md lists "
                 "the unproven assumptions needed to apply the model to a BEC or other "
                 "analog horizon (healing length as analog Planck scale; Page-like behaviour "
                 "requires backreaction). All numbers here come from test_numbers.py and "
                 "test_om.py; all synthetic data is labelled SYNTHETIC.\n")

    text = "\n".join(parts) + "\n"
    path = os.path.join(here, "RESULTS.md")
    with open(path, "w") as fh:
        fh.write(text)
    print(text)
    print(f"\nwritten to {path}")


if __name__ == "__main__":
    main()
