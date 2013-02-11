### -*- coding: utf-8 -*- ####################################################
"""
Configuration file used by setuptools. It creates 'egg', install all dependencies.
"""

import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

#Dependencies - python eggs
install_requires = [
    'setuptools',
    'python-cloudfiles==1.7.10',
    'django-cumulus==1.0.5',
    'softlayer-object-storage==0.4.6',
]

#Execute function to handle setuptools functionality
setup(name="django-softlayer",
    version="0.1",
    description="Django storage for SoftLayer Cloud Storage",
    long_description=read('README'),
    author='KirillBakanov',
    author_email='kirill.bakanov@gmail.com',
    url='https://github.com/Arpaso/django-softlayer',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    classifiers=(
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        ),
)