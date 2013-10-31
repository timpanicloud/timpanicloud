#!/usr/bin/python2
import os, subprocess, sys
python_root = 'python2.7'
subprocess.call(['python2', 'virtualenv.py', python_root])
python_bin = os.path.join(python_root, 'bin')
subprocess.call([os.path.join(python_bin, 'pip'), 'install', 'boto'])
subprocess.call([os.path.join(python_bin, 'pip'), 'install', 'sqlalchemy-migrate'])
subprocess.call([os.path.join(python_bin, 'pip'), 'install', 'sqlalchemy'])
