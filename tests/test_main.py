from app.main import create_app


def test_root_returns_contract_as_json(monkeypatch):
    monkeypatch.setenv("APP_VERSION", "1.0.0")
    monkeypatch.setenv("APP_ENVIRONMENT", "dev")
    client = create_app().test_client()

    response = client.get("/", headers={"Accept": "application/json"})

    assert response.status_code == 200
    assert response.get_json() == {
        "application": "argocd-demo",
        "version": "1.0.0",
        "environment": "dev",
    }


def test_version_1_renders_blue_page(monkeypatch):
    monkeypatch.setenv("APP_VERSION", "1.0.0")
    client = create_app().test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"#0f62fe" in response.data
    assert b"1.0.0" in response.data


def test_version_2_renders_green_page(monkeypatch):
    monkeypatch.setenv("APP_VERSION", "2.0.0")
    client = create_app().test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"#198038" in response.data
    assert b"2.0.0" in response.data


def test_healthz():
    client = create_app().test_client()

    response = client.get("/healthz")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}
