#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pathlib
import collections

print("Подсчет файлов")
print(collections.Counter(p.suffix for p in pathlib.Path.cwd().iterdir()))
print(collections.Counter(p.suffix for p in pathlib.Path.cwd().glob('*.p*')))
