# Building
## Prerequisites
- `python 3`
- `git submodule init`
- `git submodule update`
- `pip install huffman`
- `cd circuitpython/mpy-cross && make`

## Generating Binary
Running `python build.py` will generate `.mpy` release files in `./build` and a zip file in `./dist`.
