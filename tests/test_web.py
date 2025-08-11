from fastapi.testclient import TestClient

from yetx.web.app import create_app
from yetx.core.session import TorrentSession


class DummySession(TorrentSession):
    def __init__(self) -> None:  # pragma: no cover - uses fake
        pass

    def add_magnet(self, magnet_uri: str) -> str:  # type: ignore[override]
        return "abc123"

    def list_torrents(self) -> list[str]:  # type: ignore[override]
        return ["abc123"]

    def pause(self, info_hash: str) -> None:  # type: ignore[override]
        self.paused = info_hash


def test_api_add_and_pause() -> None:
    session = DummySession()
    app = create_app(session)
    client = TestClient(app)
    r = client.post("/torrents", json={"magnet": "magnet:?xt=urn:btih:abc123"})
    assert r.status_code == 200
    assert r.json()["id"] == "abc123"
    r = client.post("/torrents/abc123/pause")
    assert r.status_code == 200
    assert session.paused == "abc123"
