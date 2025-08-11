from yetx.core.config import CoreSettings
from yetx.core.session import TorrentSession


class FakeHandle:
    def __init__(self, info_hash: str) -> None:
        self._info_hash = info_hash
        self.paused = False

    def info_hash(self) -> str:  # pragma: no cover - trivial
        return self._info_hash

    def pause(self) -> None:
        self.paused = True


class FakeSession:
    def __init__(self) -> None:
        self.torrents: list[FakeHandle] = []

    def add_torrent(self, params: dict) -> FakeHandle:
        handle = FakeHandle("abc123")
        self.torrents.append(handle)
        return handle

    def get_torrents(self) -> list[FakeHandle]:
        return self.torrents


class FakeLibtorrent:
    def session(self) -> FakeSession:
        return self.fake_session

    def parse_magnet_uri(self, magnet_uri: str) -> dict:  # pragma: no cover
        return {}

    def __init__(self) -> None:
        self.fake_session = FakeSession()


def test_add_and_pause(tmp_path) -> None:
    lt = FakeLibtorrent()
    cfg = CoreSettings(download_dir=tmp_path)
    s = TorrentSession(lt_module=lt, config=cfg)
    tid = s.add_magnet("magnet:?xt=urn:btih:abc123")
    assert tid == "abc123"
    assert s.list_torrents() == ["abc123"]
    s.pause("abc123")
    assert lt.fake_session.torrents[0].paused is True
