"""Resoup
=========

Resoup Installation
"""
import setuptools

requires = []

setuptools.setup(
    name='Resoup',
    version='0.0.1',
    url='http://hardtack.me/resoup',
    author='GunWoo Choi',
    description='Simple LISP dialect implemented with Python',
    long_description=__doc__,
    packages=setuptools.find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=requires,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
    ]
)
