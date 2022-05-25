#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pathlib

path = pathlib.Path.cwd() / 'test.md'

with open(path, mode='r', encoding='utf-8') as fid:
    headers = [line.strip() for line in fid if line.startswith('#')]
    
print('\n'.join(headers))
