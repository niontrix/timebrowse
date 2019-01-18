from setuptools import setup
import sys

setup(
  name = 'nilfs2_ss_manager',
  version = '1.0',
  author = 'Tobias Heinlein, Jiro SEKIBA',
  author_email = 'dev@tobias-heinlein.com, jir@unicus.jp',
  py_modules = ['nilfs2'],
  scripts = ['nilfs2_ss_manager'],
  description = 'nilfs2 snapshot manager',
  data_files = [('/etc', ['nilfs_ss.conf'])]
)
