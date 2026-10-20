# Physics-for-Blackhole

A research framework whose object is **the black hole as a whole** — one
substrate, one law, one set of objects, from first compression to last emitted
distinction.

> **Status:** speculative research framework (research proposal, not a
> published theory).  Everything specific to the framework is labelled
> `[CONJECTURE]` or `[PREDICTION]` and is *not* established physics.  The
> established-physics parts are real and cited.

## What is in this repo

| path | contents |
|---|---|
| `PARTITIONISM.md` | the theory document: postulates, the five phases, the singularity resolution, the paradoxes, predictions, falsifiers, novelty audit, open problems, research program, and the simulation results |
| `theory/` | the proceedings PDF and its build/audit toolchain (pure Python, no third-party PDF library) |
| `simulations/` | the numerical verification suite (pure Python, standard library only) |

## Run the simulations

```
python3 -m simulations.run_all
```

Writes `simulations/RESULTS.md` and prints the same text.  Individual tests:

```
python3 -m simulations.validation
python3 -m simulations.test_ledger
python3 -m simulations.test_quantization
python3 -m simulations.test_readout
```

`test_ledger` accepts `--nmax` (largest register, default 10) and `--trials`.

## Build the proceedings PDF

```
python3 -m theory.build_paper            # -> theory/partitionism.pdf
python3 -m theory.verify_pdf            # structural check
python3 -m theory.audit_pdf             # render check (needs Adobe AFM files)
```

## Honest scope

The simulations test the *internal consistency and quantitative
consequences* of the framework's claims in controlled quantum systems.  They
do not show that the substrate exists, and they are not observational tests of
black holes.  See the falsifiers in `PARTITIONISM.md` section 11.

## Origin

This repository is the successor to `BlackHole-Physics`.  The earlier repo has
been deleted; everything it contained was copied here verbatim and then
rebranded and reorganised (the `paper/` directory became `theory/`, and the
name "Partitionism" became "Physics-for-Blackhole").  No theory content was
changed in the move — only names and paths.
