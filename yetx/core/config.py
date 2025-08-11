from __future__ import annotations

from pathlib import Path
from pydantic import BaseModel, Field
import tomllib


class CoreSettings(BaseModel):
    """Application configuration loaded from TOML."""

    download_dir: Path = Field(default_factory=lambda: Path.cwd() / "downloads")
    listen_port: int = 6881


def load_config(path: Path | None = None) -> CoreSettings:
    """Load configuration from *path* or the default location."""
    cfg_path = path or Path.home() / ".config" / "yetx" / "config.toml"
    data = {}
    if cfg_path.exists():
        data = tomllib.loads(cfg_path.read_text())
    return CoreSettings(**data)
