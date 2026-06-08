from __future__ import annotations
import argparse, json, pathlib, sys
from .builder import build_blueprint, validate_blueprint, DEMO_INPUT

QUESTIONS = [
    "What action, decision, workflow, AI agent behavior, payment, access event, recommendation, or system behavior must be governed?",
    "What consequence can bind if this movement is admitted incorrectly?",
    "Who or what has authority to admit, hold, or refuse the movement?",
    "What evidence must exist before movement can bind?",
    "What must create a receipt?",
    "What must be replayable later?",
    "Where does buyer-facing scope end and Elyria Systems runtime delivery begin?"
]

def write_json(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2) + "\n", encoding="utf-8")

def main(argv=None):
    p = argparse.ArgumentParser(prog="elyria-build-tool", description="Elyria Build Tool — scope governance before movement binds consequence.")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("questions")
    b = sub.add_parser("build"); b.add_argument("--demo", action="store_true"); b.add_argument("--out", default="elyria_scope")
    v = sub.add_parser("validate"); v.add_argument("file")
    i = sub.add_parser("inspect"); i.add_argument("file")
    args = p.parse_args(argv)
    if args.cmd == "questions":
        print("Elyria Build Tool intake questions:\n")
        for n, q in enumerate(QUESTIONS, 1): print(f"{n}. {q}")
    elif args.cmd == "build":
        doc = build_blueprint(DEMO_INPUT if args.demo else {})
        out = pathlib.Path(args.out); write_json(out/"elyria_build_blueprint.json", doc)
        write_json(out/"validation_report.json", doc["build_blueprint"]["validation_report"])
        print(f"Built blueprint: {out/'elyria_build_blueprint.json'}")
    elif args.cmd == "validate":
        doc = json.loads(pathlib.Path(args.file).read_text(encoding="utf-8"))
        ok, missing = validate_blueprint(doc)
        print("VALID" if ok else "INVALID")
        if missing: print("Missing: " + ", ".join(missing)); sys.exit(1)
    elif args.cmd == "inspect":
        doc = json.loads(pathlib.Path(args.file).read_text(encoding="utf-8")); bp = doc["build_blueprint"]
        print(f"Product: {doc.get('product')}")
        print(f"Governed object: {bp.get('governed_object')}")
        print(f"Protected scope: {bp.get('protected_scope')}")
        print(f"Validation: {bp.get('validation_report',{}).get('status')}")
if __name__ == "__main__": main()
