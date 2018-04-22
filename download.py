#!/usr/bin/env python
import argparse
import os

from download.outputs.file_output import FileOutput
from download.inputs.exception import InvalidHttpInputAddress
from download.cmd.copy import Copy
from download.inputs.http_input import HttpInput


def pars_args():
    parser = argparse.ArgumentParser(description='Downloads some file from web.')
    parser.add_argument('src', help='path to the file containing urls')
    parser.add_argument('dst', help='path to the folder to store images')
    args = parser.parse_args()
    src, dst = args.src, args.dst
    return dst, src


def inputs(src):
    with open(src, 'r') as urls:
        for url in urls:
            url = url.strip()
            yield HttpInput(url), os.path.basename(url)


def main():
    dst, src = pars_args()
    if not os.path.exists(src):
        print 'Source file does not exist!'
        exit(1)
    if not os.path.exists(dst):
        print 'Destination folder does not exist!'
        exit(1)

    download_files(dst, src)


def download_files(dst, src):
    try:
        for input, file_name in inputs(src):
            output = FileOutput(os.path.join(dst, file_name))
            copy = Copy(input, output)
            copy.execute()

    except InvalidHttpInputAddress:
        print 'Source file contains invalid url'


if __name__ == '__main__':
    main()