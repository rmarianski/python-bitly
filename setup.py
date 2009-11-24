from setuptools import setup, find_packages
import sys, os

install_requires = []

version_info = sys.version_info
if version_info[0:1] == (2,) and version_info[1:2] < (6,):
    install_requires.append('simplejson')

version = '0.1'

setup(name='python-bitly',
      version=version,
      description="python wrapper for bitly api",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='',
      author_email='',
      url='',
      license='apache2',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
