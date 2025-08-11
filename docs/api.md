# REST API

## POST /torrents
Add a torrent from a magnet link.

Request body:
```json
{"magnet": "magnet:?xt=urn:btih:..."}
```

Response:
```json
{"id": "<info-hash>"}
```

## GET /torrents
List torrents in the session.

Response:
```json
[{"id": "<info-hash>"}]
```

## POST /torrents/{id}/pause
Pause a torrent.

Response:
```json
{"id": "<info-hash>"}
```
