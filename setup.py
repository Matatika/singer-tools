#!/usr/bin/env python

from setuptools import setup

setup(name='singer-tools',
      version='0.4.1',
      description='Tools for working with Singer.io Taps and Targets',
      author='Stitch',
      url='http://singer.io',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      install_requires=[
          'attrs==17.4.0',
          'jsonschema==3.2.0',
          'singer-python',
          'strict-rfc3339==0.7',
          'terminaltables==3.1.0',
          'python-dateutil>=2.6.0',
      ],
      extras_require={
          'dev': [
              'pylint==2.5.3',
              'pynose'
          ]
      },
      packages=['singertools'],
      entry_points='''
          [console_scripts]
          singer-infer-schema=singertools.infer_schema:main
          singer-check-tap=singertools.check_tap:main
          singer-release=singertools.release:main
          diff-jsonl=singertools.diff_jsonl:main
      ''',
      include_package_data=True,
)
