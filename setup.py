import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = []

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    # icon="icon.ico"
)

# SETUP CX FREEZE
setup(
    name = "Ipa Software",
    version = "1.0",
    description = "Analysis program",
    author = "Dariusz Makarewicz",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
)