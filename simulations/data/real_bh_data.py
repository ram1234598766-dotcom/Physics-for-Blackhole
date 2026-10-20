"""Real astronomical black hole data (measured, not synthetic).

Every entry below is a REAL, published measurement with a citation.
These are used as inputs to the Physics-for-Blackhole simulations so that
the astrophysical cases (solar mass, Sgr A*, M87*) are grounded in
observation rather than arbitrary numbers.

Sources:
  - M87*: EHT Collaboration 2019, ApJL 875, L1 (6.5e9 M_sun)
  - Sgr A*: EHT Collaboration 2022, ApJL 930, L12 (4.0e6 M_sun)
  - Milky Way BH: Ghez et al. 2008, ApJ 689, 1044 (4.1e6 M_sun)
  - Solar mass: IAU 2015 nominal (1.98847e30 kg)
  - Schwarzschild radius, Hawking temperature, etc. are derived.

No claim is made that any of these measurements support the
Physics-for-Blackhole framework. They are real inputs only.
"""

# Masses in solar masses (measured)
M87_MASS_MSUN = 6.5e9          # EHT 2019: 6.5 +/- 0.7e9 M_sun
SGR_A_MASS_MSUN = 4.0e6        # EHT 2022: 4.0 +1.1/-0.6 e6 M_sun
MILKY_WAY_MASS_MSUN = 4.1e6    # Ghez et al. 2008: 4.1 +/- 0.6 e6 M_sun
SOLAR_MASS_KG = 1.98847e30    # IAU 2015 nominal

# Distance to Sgr A* (measured)
SGR_A_DISTANCE_KPC = 8.0       # EHT 2022: ~8 kpc

# Distance to M87 (measured)
M87_DISTANCE_MPC = 16.8        # EHT 2019: 16.8 +0.8/-0.7 Mpc

# EHT ring diameters (measured, microarcseconds)
M87_RING_DIAMETER_UAS = 42.0   # EHT 2019: 42 +/- 3 uas
SGR_A_RING_DIAMETER_UAS = 51.8 # EHT 2022: 51.8 +/- 2.3 uas

# Angular gravitational radius (measured)
M87_ANGULAR_GR = 3.8           # EHT 2019: 3.8 +/- 0.4 uas
SGR_A_ANGULAR_GR = 4.8         # EHT 2022: 4.8 +1.4/-0.7 uas

# Citations
CITATIONS = {
    "M87": "EHT Collaboration 2019, ApJL 875, L1 (doi:10.3847/2041-8213/ab0ec7)",
    "Sgr_A": "EHT Collaboration 2022, ApJL 930, L12 (doi:10.3847/2041-8213/ac6674)",
    "Milky_Way": "Ghez et al. 2008, ApJ 689, 1044 (doi:10.1086/592738)",
    "Solar_Mass": "IAU 2015 Resolution B3 (nominal solar mass)",
}


def mass_to_kg(mass_msun):
    """Convert solar masses to kg using IAU nominal solar mass."""
    return mass_msun * SOLAR_MASS_KG


def schwarzschild_radius(mass_msun):
    """Schwarzschild radius in meters for a given mass in solar masses."""
    G = 6.67430e-11
    c = 299792458.0
    M = mass_to_kg(mass_msun)
    return 2.0 * G * M / c ** 2


def hawking_temperature(mass_msun):
    """Hawking temperature in Kelvin."""
    import math
    G = 6.67430e-11
    c = 299792458.0
    hbar = 1.054571817e-34
    k_B = 1.380649e-23
    M = mass_to_kg(mass_msun)
    return hbar * c ** 3 / (8.0 * math.pi * G * M * k_B)


def evaporation_time_years(mass_msun):
    """Estimated evaporation time in years (power-law)."""
    G = 6.67430e-11
    c = 299792458.0
    hbar = 1.054571817e-34
    M = mass_to_kg(mass_msun)
    t_seconds = M ** 3 * 5120.0 * math.pi * G ** 2 / (hbar * c ** 4)
    return t_seconds / (365.25 * 24 * 3600)


if __name__ == "__main__":
    import math
    print("Real astronomical black hole data (measured)")
    print("=" * 60)
    for name, mass in [("M87*", M87_MASS_MSUN),
                       ("Sgr A*", SGR_A_MASS_MSUN),
                       ("Milky Way BH", MILKY_WAY_MASS_MSUN)]:
        r_s = schwarzschild_radius(mass)
        T_H = hawking_temperature(mass)
        t_evap = evaporation_time_years(mass)
        print(f"{name}: M = {mass:.3e} M_sun")
        print(f"  r_s = {r_s:.3e} m = {r_s/1e3:.1f} km")
        print(f"  T_H = {T_H:.3e} K")
        print(f"  t_evap ~ {t_evap:.3e} years")
        cite_key = name.replace(" ", "_").replace("*", "").replace("Way", "Way")
        if cite_key == "Milky_Way_BH":
            cite_key = "Milky_Way"
        print(f"  citation: {CITATIONS[cite_key]}")
        print()
    print("These are REAL measured values, not synthetic.")
    print("No claim is made that they support the Physics-for-Blackhole framework.")
