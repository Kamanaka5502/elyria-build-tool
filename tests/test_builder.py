from elyria_build_tool.builder import build_blueprint, validate_blueprint

def test_demo_blueprint_valid():
    doc = build_blueprint()
    ok, missing = validate_blueprint(doc)
    assert ok
    assert missing == []

def test_required_branding():
    doc = build_blueprint()
    assert doc["product"] == "Elyria Build Tool"
    assert "Prove it before it moves" in doc["tagline"]
