# Elyria Build Tool

**Scope it. Layer it. Prove it before it moves.**

Elyria Build Tool is a customer-facing governance intake and blueprint generator. It helps a buyer describe what they need governed, then produces a build-ready handoff package for Elyria Systems to implement the actual runtime/proof corridor.

## What it governs

Actions, decisions, workflows, AI agents, payment events, access events, recommendations, and system behaviors where invalid movement can bind consequence.

## Core outputs

- Build blueprint
- Governed object
- Consequence description
- Authority requirements
- Evidence requirements
- Admit / hold / refuse matrix
- Failure modes
- Receipt requirements
- Replay requirements
- Pilot corridor plan
- Protected scope
- Commercial access boundary
- Validation report

## Install for local use

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e .
```

## Commands

```bash
python -m elyria_build_tool questions
python -m elyria_build_tool build --demo --out sample_scope
python -m elyria_build_tool validate sample_scope/elyria_build_blueprint.json
python -m elyria_build_tool inspect sample_scope/elyria_build_blueprint.json
python -m pytest -q
```

## Commercial boundary

The tool produces buyer-facing scope and blueprint artifacts. Runtime implementation, validators, enforcement logic, proof corridor design, and replay infrastructure remain Elyria Systems delivery assets unless contracted separately.
