#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pathlib

print("Отличия операционной системы")
print(pathlib.WindowsPath('test.md'))

path = pathlib.PureWindowsPath(r'C:\Users\gahjelle\realpython\file.txt')
print(path)