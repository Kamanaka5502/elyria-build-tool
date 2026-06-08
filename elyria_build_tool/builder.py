from __future__ import annotations
from datetime import datetime, timezone
from .schema import REQUIRED_FIELDS

DEMO_INPUT = {
    "governed_object": "AI agent approval of customer refund requests above $500",
    "consequence_description": "Unauthorized refund approval can create financial loss, audit exposure, and customer-service inconsistency.",
    "authority_requirements": ["Requester identity", "Refund threshold authority", "Policy version", "Escalation owner"],
    "evidence_requirements": ["Original request", "Customer account state", "Policy match", "Approval path", "Decision receipt"],
    "protected_scope": "Refund approval movement from recommendation into binding payment action.",
    "commercial_access_boundary": "Blueprint may be shared with buyers; runtime implementation, validators, and proof corridor remain Elyria Systems delivery assets."
}

def build_blueprint(data: dict | None = None) -> dict:
    data = {**DEMO_INPUT, **(data or {})}
    return {
        "product": "Elyria Build Tool",
        "tagline": "Scope it. Layer it. Prove it before it moves.",
        "version": "1.1.0",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "build_blueprint": {
            "governed_object": data["governed_object"],
            "consequence_description": data["consequence_description"],
            "authority_requirements": data["authority_requirements"],
            "evidence_requirements": data["evidence_requirements"],
            "admit_hold_refuse_matrix": {
                "admit": ["Authority verified", "Evidence complete", "Consequence path classified", "Replay receipt available"],
                "hold": ["Missing evidence", "Authority conflict", "Unclassified consequence", "Policy version mismatch"],
                "refuse": ["Unauthorized actor", "Protected movement outside scope", "Receipt cannot be produced", "Replay cannot verify decision path"]
            },
            "failure_modes": ["Silent approval", "Evidence drift", "Authority bypass", "Receipt gap", "Replay failure", "Scope creep"],
            "receipt_requirements": ["Actor", "Authority basis", "Evidence hash", "Decision state", "Timestamp", "Replay pointer"],
            "replay_requirements": ["Same inputs reproduce same classification", "Receipt binds to evidence", "Authority checks remain inspectable"],
            "pilot_corridor_plan": ["Define protected movement", "Load policy/evidence fixtures", "Run admit/hold/refuse cases", "Generate validation report", "Review buyer handoff"],
            "protected_scope": data["protected_scope"],
            "commercial_access_boundary": data["commercial_access_boundary"],
            "validation_report": {"status": "blueprint_ready", "missing_fields": [], "next_step": "Elyria runtime/proof corridor scoping"}
        }
    }

def validate_blueprint(doc: dict) -> tuple[bool, list[str]]:
    bp = doc.get("build_blueprint", {})
    missing = [f for f in REQUIRED_FIELDS if f not in bp or bp[f] in (None, "", [], {})]
    return not missing, missing
