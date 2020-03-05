import sys
from cx_Freeze import setup, Executable
import ftplib
import json
import datetime
from datetime import datetime, date
import time
import shutil


base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
        Executable("MarcacaoFTP.py", base=base)
]

buildOptions = dict(
        packages = [],
        includes = ["ftplib", "json","datetime","time","shutil"],
        include_files = ["config.json"],
        excludes = []
)




setup(
    name = "MarcacaoFTP",
    version = "1.0",
    description = "Tranfere a marcacao via FTP",
    options = dict(build_exe = buildOptions),
    executables = executables
 )

