import os
import subprocess
from scanfs.fsscanner import FileSystemScanner
from scanfs.fsscannerex import FSScannerException


def callback(fpath, node):
    try:
        path = os.path.join(fpath, node.name)
        completed_process = subprocess.run(
            ["checksec", "--format=json", "--file=" + str(path)],
            capture_output=True,
            check=True,
        )
        print(completed_process)
    except Exception as e:
        print("An exception occurred: " + str(e))


fss = FileSystemScanner("/usr/bin")
fss.checksec_on_elfs()
