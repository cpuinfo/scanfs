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
