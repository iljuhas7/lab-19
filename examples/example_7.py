#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pathlib
from datetime import datetime

directory = pathlib.Path.cwd()

print("Найти последний измененный файл")

time, file_path = max((f.stat().st_mtime, f) for f in directory.iterdir())
print(datetime.fromtimestamp(time), file_path)
print(max((f.stat().st_mtime, f) for f in directory.iterdir())[1].read_text())
