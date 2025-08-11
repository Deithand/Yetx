# Plugin API

Plugins are discovered via the `yetx.plugins` entry point group. Each plugin
must expose a `register(session)` function. The function receives a
[`TorrentSession`](../yetx/core/session.py) instance and can interact with the
running session.

## Example

```python
from yetx.core.session import TorrentSession

def register(session: TorrentSession) -> None:
    print("session has", len(session.list_torrents()), "torrents")
```
