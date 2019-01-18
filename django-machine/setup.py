import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-machine',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    description='Machine is a Testing task from Intive, for patronage 2019 Machine Learning & Big Data.',
    long_description=README,
    author='Patryk Woźniak',
    author_email='wozniakxyz@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.1.5', 
        'Operating System :: Windows 7 64-bit',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6.5',
    ],
)