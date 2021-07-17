# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os.path
import sys
import hashlib


def get_sha1sum(buffer):
    BUFFERSIZE = 128*1024
    sha1 = hashlib.sha1()
    sha1128ksum = None
    while True:
        data = buffer.read(BUFFERSIZE)
        if not data:
            break
        sha1.update(data)
        if not sha1128ksum:
            sha1128ksum = hashlib.sha1(data).hexdigest().upper()
    sha1sum = sha1.hexdigest().upper()
    return sha1sum, sha1128ksum



def create_url(filename):
    name = os.path.basename(filename)
    size = os.stat(filename).st_size
    with open(filename, "rb") as f:
        sha1sum, sha1128ksum = get_sha1sum(f)
    return "115://%s|%s|%s|%s" % (name, size, sha1sum, sha1128ksum)


def main():
    path = sys.argv[1]
    if os.path.isdir(path):
        filenames = [
            os.path.join(path, filename)
            for filename in os.listdir(path)
        ]
    else:
        filenames = [path]
    for filename in filenames:
        url = create_url(filename)
        print(url, end="\n")


if "__main__" == __name__:
    main()
