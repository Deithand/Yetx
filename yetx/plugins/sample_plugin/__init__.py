"""Sample plugin demonstrating the plugin API.

Plugins expose a ``register`` function accepting a :class:`TorrentSession`.
"""

from yetx.core.session import TorrentSession


def register(session: TorrentSession) -> None:
    """Entry point called on start.

    Parameters
    ----------
    session:
        Active :class:`~yetx.core.session.TorrentSession` instance.
    """

    # Example plugin logic: log the number of torrents.
    count = len(session.list_torrents())
    print(f"Sample plugin loaded, {count} torrents present")
