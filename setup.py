import os
from setuptools import setup, find_packages
from median_voting import __version__


setup(
    name='median_voting',
    version=__version__,
    description='A python implementation for median votings with the possibility to have weighted votes.',
    url='https://github.com/FabianWe/median_voting',
    author='Fabian Wenzelmann',
    author_email='fabianwen@posteo.eu',
    license='MIT',
    keywords='voting median',
    packages=find_packages(exclude=('docs', 'tests', 'env')),
    include_package_data=True,
    install_requires=['pytest'],
)
