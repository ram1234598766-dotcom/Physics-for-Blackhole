"""Physics-for-Blackhole: physical/substrate time map.

CONJECTURE N (time map): physical time t and substrate time tau are related by
t = eta * tau, where eta = OM/c = t_P/tau_q is the single dimensionless free
parameter. This is the minimal map consistent with P4 (the readout is the
metric): physical time is a linear functional of substrate time with one
dimensionless conversion factor.

Evaporation law (model input):
    dN/dtau = -r0 * (1 - N/N0)**alpha,   N(0) = N0
N = number of area quanta remaining; N0 initial quanta; r0 rate; alpha shape.

Physical Page time t_P: when N = N0/2 (turnover of the Page curve).
"""

import math

# ---------------------------------------------------------------------------
# tau(N): substrate time to reach quantum count N
# ---------------------------------------------------------------------------
def substrate_time(N, N0, r0, alpha):
    """Substrate time tau(N) for N quanta remaining, starting from N0 at tau=0.

    Returns None for alpha >= 1 when N -> 0 (infinite substrate time to
    evaporate the last quantum in that regime).
    """
    if N < 0 or N > N0:
        raise ValueError("N must be in [0, N0]")
    if r0 <= 0:
        raise ValueError("r0 must be positive")
    if alpha == 1.0:
        # dN/dtau = -r0 (1 - N/N0)  ->  N = N0 (1 - exp(-r0 tau / N0))
        return -(N0 / r0) * math.log(1.0 - N / N0)
    if alpha < 1.0:
        return (N0 / (r0 * (1.0 - alpha))) * (1.0 - N / N0) ** (1.0 - alpha)
    # alpha > 1: reaches N=0 at finite tau
    return (N0 / (r0 * (alpha - 1.0))) * (
        1.0 - (1.0 - N / N0) ** (1.0 - alpha)
    )

def page_time_substrate(N0, r0, alpha):
    """Substrate time tau_P at turnover N = N0/2."""
    return substrate_time(N0 / 2.0, N0, r0, alpha)

def page_time_physical(N0, r0, alpha, eta):
    """Physical Page time t_P = eta * tau_P."""
    return eta * page_time_substrate(N0, r0, alpha)

def evaporation_time_substrate(N0, r0, alpha):
    """Substrate time to evaporate all quanta (N -> 0)."""
    if alpha <= 1.0:
        return float("inf")   # asymptotic: never fully evaporates
    return (N0 / (r0 * (alpha - 1.0)))
