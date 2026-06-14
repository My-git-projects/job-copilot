from app.services.ats_engine import analyze_candidate

def test_pipeline():
    res = analyze_candidate(
        "Python AWS developer",
        "Backend engineer Python AWS Docker"
    )
    assert "match_score" in res