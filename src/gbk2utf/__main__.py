import argparse
import sys

from gbk2utf.gbk2utf import BackupFailException, convert

ap = argparse.ArgumentParser(
    description='Convert GBK coded file to UTF-8 coded.',
    allow_abbrev=False
)

ap.add_argument(
    'files',
    metavar='files',
    type=str,
    nargs='+',
    help='file(s) to proceed',
)

ap.add_argument(
    '-i', '--in-place',
    action='store_true',
    help='convert file in place, do not save backup.',
)

ap.add_argument(
    '-o', '--overwrite',
    action='store_true',
    help='overwrite the existing backup file if it exists.',
)

args = vars(ap.parse_args())

for file in list(args['files']):
    try:
        convert(
            file,
            in_place=bool(args['in_place']),
            overwrite=bool(args['overwrite'])
        )
    except BackupFailException:
        print(f'Failed: Could not save backup: "{file}"', file=sys.stderr)
    except FileNotFoundError:
        print(f'Failed: Not found: "{file}"', file=sys.stderr)
    except PermissionError:
        print(f'Failed: Permission denied: "{file}"', file=sys.stderr)
    except IsADirectoryError:
        print(f'Failed: Input is a directory: "{file}"', file=sys.stderr)
    except UnicodeDecodeError as e:
        print(f'Failed: Unable to decode as GBK: "{file}": {e}')
    else:
        print(f'Converted: "{file}"', file=sys.stderr)
    finally:
        pass
