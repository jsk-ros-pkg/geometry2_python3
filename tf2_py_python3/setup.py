#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['jsk_tf2_py_python3'],
    package_dir={'': 'src'},
    requires=['rospy', 'geometry_msgs', 'tf2_msgs']
)

setup(**d)
