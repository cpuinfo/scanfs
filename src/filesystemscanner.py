class FileSystemScannerException(Exception):
    pass


class FileSystemScanner:
    def __init__(self, fwpath: str) -> None:
        super().__init__()
        self._check_str_param(fwpath)
        self.fwpath = fwpath

    def _check_str_param(self, param):
        if not isinstance(param, str) or not param:
            raise FileSystemScannerException(
                f'Firmware path "{param}" is empty or not valid string!!!'
            )


if __name__ == "__main__":
    fss = FileSystemScanner("/")
