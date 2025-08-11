# PyInstaller spec for YetX GUI
block_cipher = None

a = Analysis([
    'yetx/gui/main.py',
], pathex=['.'],
    binaries=[],
    datas=[('yetx/gui/main.qml', 'yetx/gui')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={})
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='yetx-gui',
          debug=False)
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='yetx-gui')
