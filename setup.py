from distutils.core import setup
import py2exe

setup(windows=[{"script": "render.py", "icon_resources": [(1, "source/main.ico")]}],
      data_files=[("source",
                   ["source/background.png", "source/board.png", "source/mark_black.png", "source/mark_white.png", "source/victory_black.png", "source/victory_white.png", "source/next.png"])
                  ,
                  ]
      ,
      options = { "py2exe": { "dll_excludes": ["MSVCP90.dll"] } }
                  
)