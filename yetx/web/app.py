from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel
from yetx.core.session import TorrentSession


class AddTorrentRequest(BaseModel):
    magnet: str


class TorrentActionResponse(BaseModel):
    id: str


def create_app(session: TorrentSession | None = None) -> FastAPI:
    session = session or TorrentSession()
    app = FastAPI(title="YetX API")

    @app.post("/torrents", response_model=TorrentActionResponse)
    def add_torrent(
        req: AddTorrentRequest,
    ) -> TorrentActionResponse:  # type: ignore[valid-type]
        tid = session.add_magnet(req.magnet)
        return TorrentActionResponse(id=tid)

    @app.get("/torrents")
    def list_torrents() -> list[TorrentActionResponse]:
        return [TorrentActionResponse(id=i) for i in session.list_torrents()]

    @app.post("/torrents/{tid}/pause")
    def pause_torrent(tid: str) -> TorrentActionResponse:
        session.pause(tid)
        return TorrentActionResponse(id=tid)

    return app


try:
    app = create_app()
except ModuleNotFoundError:  # pragma: no cover - libtorrent missing in tests
    app = FastAPI(title="YetX API")
