# YetX

YetX is a cross‑platform BitTorrent client built on top of
[`libtorrent-rasterbar`](https://libtorrent.org). It consists of a core daemon,
a desktop GUI written in Qt/QML and a FastAPI based web service.

This repository contains the minimal MVP implementation and scaffolding for
further development.

## Features

- Add torrents via magnet links
- Simple REST API powered by FastAPI
- Qt/QML based GUI
- Plugin system using Python entry points

## Development

```bash
poetry install
poetry run pre-commit install
poetry run pre-commit run --files <files>
poetry run pytest
```

## Running

Start the web API:

```bash
poetry run uvicorn yetx.web.app:app
```

Launch the GUI:

```bash
poetry run python -m yetx.gui.main
```

## License

GPLv3 – see [LICENSE](LICENSE).
