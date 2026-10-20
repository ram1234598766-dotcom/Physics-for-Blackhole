"""Physics-for-Blackhole: multi-observable joint inversion of eta.

Breaks the structural degeneracy C = eta * K(alpha) / r0 by adding two
independent observables:
  1. Page-time slope C          = eta * K(alpha) / r0
  2. Graybody peak frequency    = alpha / r0
  3. OTOC scrambling rate       = (2*pi/eta) * (1 - 0.1*r0)**alpha

All numbers below are SYNTHETIC: ground-truth values are conjectured
("Conjectured Nature"), noise is Gaussian with np.random.seed(42), and
neither omega_peak nor lambda_L has been measured in any real experiment.
This demonstrates identifiability INSIDE THE MODEL only. It does not
establish OM = eta*c as a constant of nature.
"""

import numpy as np


def K_alpha(alpha):
    """Model shape function K(alpha) = alpha**1.5 / (1.0 + alpha)."""
    return (alpha ** 1.5) / (1.0 + alpha)


def run_multi_observable_experiment(n_trials=1000):
    print("=== Multi-Observable Joint Inversion Experiment ===")
    print("(SYNTHETIC data — ground truth conjectured, Gaussian noise, seed=42)")

    # Ground Truth Physical Parameters (Conjectured Nature — not measured)
    eta_true = 0.5000
    r0_true = 1.2000
    alpha_true = 0.8500

    # True Observables derived from physics model
    C_true = eta_true * K_alpha(alpha_true) / r0_true
    w_peak_true = alpha_true / r0_true
    lambda_L_true = (
        (2.0 * np.pi / eta_true) * (1.0 - 0.1 * r0_true) ** alpha_true
    )

    print(
        f"[TRUTH] eta: {eta_true:.4f} | r0: {r0_true:.4f} | alpha: {alpha_true:.4f}"
    )
    print(
        f"[DERIVED OBS] C: {C_true:.5f} | w_peak: {w_peak_true:.5f} | "
        f"lambda_L: {lambda_L_true:.5f}\n"
    )

    # Simulate Experimental Measurements with 2% Gaussian Noise
    np.random.seed(42)
    noise_level = 0.02

    C_obs = C_true * (1 + np.random.normal(0, noise_level, n_trials))
    w_obs = w_peak_true * (1 + np.random.normal(0, noise_level, n_trials))
    lambda_obs = lambda_L_true * (1 + np.random.normal(0, noise_level, n_trials))

    # Inversion Pipeline to recover parameters independently
    eta_reconstructed = []
    r0_reconstructed = []
    alpha_reconstructed = []

    for i in range(n_trials):
        # Step 1: recover r0 from w_obs and approximate alpha scan;
        # use lambda_L and w_peak coupling to isolate alpha numerically
        best_alpha = None
        min_err = 1e9

        for alpha_candidate in np.linspace(0.1, 3.0, 1000):
            r0_candidate = alpha_candidate / w_obs[i]
            if r0_candidate >= 10.0:  # physical horizon boundary
                continue

            eta_candidate = C_obs[i] * r0_candidate / K_alpha(alpha_candidate)

            # Predict lambda_L under candidate parameters
            lambda_pred = (
                (2.0 * np.pi / eta_candidate)
                * (1.0 - 0.1 * r0_candidate) ** alpha_candidate
            )
            err = (lambda_pred - lambda_obs[i]) ** 2

            if err < min_err:
                min_err = err
                best_alpha = alpha_candidate

        r0_rec = best_alpha / w_obs[i]
        eta_rec = C_obs[i] * r0_rec / K_alpha(best_alpha)

        alpha_reconstructed.append(best_alpha)
        r0_reconstructed.append(r0_rec)
        eta_reconstructed.append(eta_rec)

    eta_mean, eta_std = np.mean(eta_reconstructed), np.std(eta_reconstructed)
    r0_mean, r0_std = np.mean(r0_reconstructed), np.std(r0_reconstructed)
    alpha_mean, alpha_std = np.mean(alpha_reconstructed), np.std(alpha_reconstructed)

    print("=== Joint Inversion Results (N = 1000 noisy measurements) ===")
    print(
        f"Reconstructed eta   : {eta_mean:.4f} +/- {eta_std:.4f} "
        f"(True: {eta_true:.4f})"
    )
    print(
        f"Reconstructed r0    : {r0_mean:.4f} +/- {r0_std:.4f} "
        f"(True: {r0_true:.4f})"
    )
    print(
        f"Reconstructed alpha : {alpha_mean:.4f} +/- {alpha_std:.4f} "
        f"(True: {alpha_true:.4f})"
    )

    bias_eta = abs(eta_mean - eta_true) / eta_true * 100
    print(f"\nDegeneracy Broken! Absolute bias in eta: {bias_eta:.2f}%")

    if bias_eta < 1.0:
        print(
            "[SUCCESS] eta is identifiable as an empirical parameter "
            "(within this synthetic model)."
        )
    else:
        print(
            "[WARNING] eta bias above 1% — degeneracy not cleanly broken."
        )

    return {
        "eta_mean": eta_mean,
        "eta_std": eta_std,
        "r0_mean": r0_mean,
        "r0_std": r0_std,
        "alpha_mean": alpha_mean,
        "alpha_std": alpha_std,
        "bias_eta": bias_eta,
    }


def main_captured():
    import io
    import contextlib

    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        run_multi_observable_experiment()
    return buf.getvalue()


def main():
    print(main_captured())


if __name__ == "__main__":
    run_multi_observable_experiment()
