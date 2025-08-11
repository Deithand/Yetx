from __future__ import annotations

from PySide6.QtCore import QObject, Signal, Slot, QStringListModel

from ..core.session import TorrentSession


class TorrentController(QObject):
    """Expose torrent actions to QML."""

    torrentsChanged = Signal()

    def __init__(
        self, session: TorrentSession | None = None, parent: QObject | None = None
    ) -> None:
        super().__init__(parent)
        self._session = session or TorrentSession()
        self._model = QStringListModel()
        self.refresh()

    @Slot(str)
    def add_magnet(self, magnet_uri: str) -> None:
        """Add a torrent from a magnet URI and refresh the list."""
        if not magnet_uri:
            return
        self._session.add_magnet(magnet_uri)
        self.refresh()

    @Slot(result=QObject)
    def torrent_model(self) -> QObject:
        """Return the model for binding in QML."""
        return self._model

    def refresh(self) -> None:
        torrents = self._session.list_torrents()
        self._model.setStringList(torrents)
        self.torrentsChanged.emit()
