import os
from os.path import exists
from pathlib import Path
import shutil
import subprocess

BUILD_PATH = './build'
DIST_PATH = './dist'
SRC_PATH = './root'

ignored_files = ['README.md']

def check_mpy_cross():
    possible_paths = [
        './circuitpython/mpy-cross/mpy-cross',
        './circuitpython/mpy-cross/mpy-cross.exe'
    ]
    for p in possible_paths:
        if os.path.exists(p):
            return p
    return False


mpy_binary = check_mpy_cross()
if not mpy_binary:
    print("Please compile mpy-cross. Refer to the building section in the README")
    exit()

# Cleanup build directory
try:
    shutil.rmtree(BUILD_PATH)
except OSError as e:
    pass

# Copy Source files to build directory
destination = shutil.copytree(SRC_PATH, BUILD_PATH, ignore=shutil.ignore_patterns('*.pyc', '__pycache__'))

# Generate mpy files from src
for subdir, dirs, files in os.walk(BUILD_PATH):
    for filename in files:
        filepath = os.path.join(subdir, filename)
        if filename in ignored_files:
            os.remove(filepath)
        elif filename.endswith(".py"):
                filepath = os.path.join(subdir, filename)
                subprocess.check_output([mpy_binary, filepath])
                os.remove(filepath)

shutil.make_archive(os.path.join(DIST_PATH, 'swarm-feathers2'), 'zip', BUILD_PATH)
