import os
from src.filesystemscannerexception import FileSystemScannerException


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
        """Scans for specific filetype in the nested folder

        Args:
            filetype ([type]): Filetype
            callback (function): Function called when the filetype
            is found
        """
        nodes = os.scandir(self.fpath)
        for node in nodes:
            callback(node)

    def _check_str_param(self, param):
        if not isinstance(param, str) or not param:
            raise FileSystemScannerException(
                f'Firmware path "{param}" is empty or not valid string!!!'
            )


def callback(node):
    print(node.name)


if __name__ == "__main__":
    fss = FileSystemScanner("/home/maker")
    fss.scan_for("elf", callback)
