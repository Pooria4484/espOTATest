import sys
# Remove current dir from sys.path, otherwise setuptools will peek up our
# module instead of system's.
sys.path.pop(0)
from setuptools import setup
sys.path.append("..")
import sdist_upip

setup(name='upiptest',
      version='0.0.1',
      description='Minimalistic file shell using native Python syntax.',
      long_description='Minimalistic file shell using native Python syntax.',
      url='https://github.com/Pooria4484/espOTATest/app',
      author='pooria-lib Developers',
      author_email='info@msb-co.ir',
      maintainer='pooria-lib Developers',
      maintainer_email='info@msb-co.ir',
      license='/MSB',
      cmdclass={'sdist': sdist_upip.sdist},
      py_modules=['upiptest'])
