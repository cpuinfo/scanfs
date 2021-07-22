import os
import filetype
import magic
from filesystemscannerexception import FileSystemScannerException


class FileSystemScanner:

    """
    FileSystemScanner

    This scanner scans the folder in the filesystem
    with various filetype filters and provides a hook
    whenever the filetype is found in the provided path

    Attributes:
        fpath (str): Folder in the filesytem to scan

    Raises:
        FileSystemScannerException: [Exception when the
        folder path fpath is empty or not valid]
    """

    def __init__(self, fpath: str) -> None:
        super().__init__()
        self._check_str_param(fpath)
        self.fpath = fpath

    def scan_for(self, filetype, callback):
        """
        Scans for specific filetype in the nested folder

        Args:
            filetype ([type]): Filetype
            callback (function): Function called when the filetype
            is found
        """
        nodes = os.scandir(self.fpath)
        for node in nodes:
            callback(self.fpath, node)

    def _check_str_param(self, param):
        if not isinstance(param, str) or not param:
            raise FileSystemScannerException(
                f'Firmware path "{param}" is empty or not valid string!!!'
            )


if __name__ == "__main__":

    files = []

    def callback(fpath, node):
        try:
            path = os.path.join(fpath, node.name)
            # statinfo = os.stat(path)
            print("#")
            if not node.is_dir() and not node.is_symlink():
                files.append(magic.from_file(path))
        except:
            print("An exception occurred")

    fss = FileSystemScanner("/usr/bin")
    # fss = FileSystemScanner("/home/maker/Downloads")
    fss.scan_for("elf", callback)
    print(files)
