#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import glob
import os
import shutil

for file_name in glob.glob('*.txt'):
    new_path = os.path.join('archive', file_name)
    shutil.move(file_name, new_path)