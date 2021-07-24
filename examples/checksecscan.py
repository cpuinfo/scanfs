import os
import subprocess
from scanfs.fsscanner import FileSystemScanner
from scanfs.scanners.checksecscanner import CheckSecScanner

css = CheckSecScanner("/usr/bin", "/tmp/checksec_results.json")
css.checksec_on_elfs()

css = CheckSecScanner("/usr/bin", "/tmp/checksec_results.csv", fformat="csv")
css.checksec_on_elfs()
