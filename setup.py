#!/usr/bin/env python

from distutils.core import setup

# from https://docs.python.org/3.11/distutils/introduction.html#distutils-simple-example
# setup(name='foo',
#       version='1.0',
#       py_modules=['foo'],
#       )

# from https://docs.python.org/3.11/distutils/setupscript.html
setup(name='timetable_announcer',
      version='1.0',
      description='Announcer for timetable entries',
      author='John Sturdy',
      author_email='jcg.sturdy@gmail.com',
      # url='https://www.python.org/sigs/distutils-sig/',
      packages=['src/timetable_announcer'],
     )
