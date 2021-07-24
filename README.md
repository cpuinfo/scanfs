# scanfs

This module scans the filesystem and provides custom hooks to handle each file
type of your choice.

## Installation

```bash
pip install scanfs
```

## Example

### How to scan a folder with ELF files and get stat info?

```python
import os
from scanfs.fsscanner import FileSystemScanner
from scanfs.fsscannerex import FSScannerException


def callback(fpath, node):
    try:
        path = os.path.join(fpath, node.name)
        # Now do what you want on the instance of file
        # eg. stat
        statinfo = os.stat(path)
        print(statinfo)
    except FSScannerException as e:
        print("An exception occurred: " + str(e))


fss = FileSystemScanner("/usr/bin")
fss.scan_for_elfs(callback)
```

### Simple way to scan EFL for binary protection using checksec

```python
import os
import subprocess
from scanfs.fsscanner import FileSystemScanner
from scanfs.scanners.checksecscanner import CheckSecScanner

css = CheckSecScanner("/usr/bin", "/tmp/checksec_results.json")
css.checksec_on_elfs()

css = CheckSecScanner("/usr/bin", "/tmp/checksec_results.csv", fformat="csv")
css.checksec_on_elfs()
```

## Developer

```bash
python -m build
twine upload dist/*
```

> Ref: https://packaging.python.org/tutorials/packaging-projects/
