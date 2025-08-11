from __future__ import annotations

import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine


def main() -> int:
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()
    qml_file = Path(__file__).with_name("main.qml")
    engine.load(qml_file)
    if not engine.rootObjects():
        return -1
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
