
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pycgettb',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.1.2',

    description='convert guided form excel to text data by template base',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/hrsano645/pycgettb',

    # Author details
    author='Hiroshi Sano',
    author_email='hrs.sano645@gmail.com',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],

    # What does your project relate to?
    keywords='excel xlsx convert jinja2 template',

    packages=["pycgettb"],

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    py_modules=["pycgettbcli"],

    install_requires=['jinja2', 'click', 'openpyxl'],

    entry_points={
        'console_scripts': [
            'pycgettbcli=pycgettbcli:main',
        ],
    },
)
