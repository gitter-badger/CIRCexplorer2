#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from circ.version import __version__

setup(name='CIRCexplorer2',
      version=__version__,
      description='Circular RNA analysis toolkits',
      author='Xiao-Ou Zhang',
      author_email='zhangxiaoou@picb.ac.cn',
      url='https://github.com/YangLab/CIRCexplorer2',
      license='MIT',
      classifiers=[
          'Development Status :: 2 - Pre-Alpha'
          'Intended Audience :: Science/Research',
          'Topic :: Scientific/Engineering :: Bio-Informatics',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
      ],
      keywords='circular RNAs',
      packages=find_packages(),
      install_requires=[
          'pysam>=0.8.2',
          'pybedtools',
          'scipy',
          'docopt'
      ],
      entry_points={
          'console_scripts': [
              'CIRCexplorer2=circ.command_parse:main',
              'fetch_ucsc.py=circ.fetch_ucsc:main'
          ],
      },
      )
