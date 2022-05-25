#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pathlib

path = pathlib.Path('test.md')

print("path:", path)
print("path.name:", path.name)
print("path.stem:", path.stem)
print("path.suffix:", path.suffix)
print("path.parent:", path.parent)
print("path.parent.parent:", path.parent.parent)
print("path.anchor:", path.anchor)
print("path.parent.parent/('new' + path.suffix):", path.parent.parent/('new' + path.suffix))