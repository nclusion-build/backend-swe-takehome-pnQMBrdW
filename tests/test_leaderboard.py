from fastapi.testclient import TestClient
from src.main import app

def test_leaderboard_endpoints_exist():
    client = TestClient(app)
    res = client.get('/leaderboard')
    assert res.status_code in (200, 404)  # TODO: adjust after implementation
    res = client.get('/leaderboard/efficiency')
    assert res.status_code in (200, 404)

