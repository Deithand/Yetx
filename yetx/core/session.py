from __future__ import annotations

import logging
from typing import Any, List

from .config import CoreSettings, load_config

logger = logging.getLogger(__name__)


class TorrentSession:
    """Thin wrapper around ``libtorrent.session``.

    Parameters
    ----------
    lt_module:
        Optional injected ``libtorrent`` module for testing.
    config:
        Optional configuration for the session.
    """

    def __init__(
        self,
        lt_module: Any | None = None,
        config: CoreSettings | None = None,
    ) -> None:
        self.lt = lt_module or __import__("libtorrent")
        self.config = config or load_config()
        self.config.download_dir.mkdir(parents=True, exist_ok=True)
        self.session = self.lt.session()
        logger.debug("Torrent session initialized at %s", self.config.download_dir)

    def add_magnet(self, magnet_uri: str) -> str:
        """Add a torrent from a magnet link and return its info hash."""
        params = self.lt.parse_magnet_uri(magnet_uri)
        save_path = str(self.config.download_dir)
        if hasattr(params, "save_path"):
            params.save_path = save_path  # type: ignore[attr-defined]
        else:  # parse_magnet_uri may return a dict
            params["save_path"] = save_path
        handle = self.session.add_torrent(params)
        info_hash = str(handle.info_hash())
        logger.info("Added magnet %s", info_hash)
        return info_hash

    def list_torrents(self) -> List[str]:
        """Return list of torrent info hashes currently in the session."""
        return [str(h.info_hash()) for h in self.session.get_torrents()]

    def pause(self, info_hash: str) -> None:
        """Pause a torrent by info hash if present."""
        for h in self.session.get_torrents():
            if str(h.info_hash()) == info_hash:
                h.pause()
                logger.info("Paused %s", info_hash)
                break
