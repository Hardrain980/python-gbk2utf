import os


class BackupFailException(Exception):
    pass


def convert(
    file: str,
    in_place: bool = False,
    overwrite: bool = False,
) -> None:
    with open(file, 'rb') as fh:
        co = fh.read()

    cn = co.decode('CP936').encode('utf-8')

    if not in_place:
        if os.path.exists(f"{file}.old") and not overwrite:
            raise BackupFailException()

        os.rename(file, f"{file}.old")

    with open(file, 'wb') as fh:
        fh.write(cn)
