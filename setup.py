from distutils.core import setup
import py2exe

setup(console=["render.py"],
      data_files=[("source",
                   ["source/background.png", "source/board.png", "source/mark_black.png", "source/mark_white.png"])
                  ,
                  ]
                  
)