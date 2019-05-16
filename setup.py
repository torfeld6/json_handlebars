from setuptools import setup, find_packages

from json_handlebars import __author__
from json_handlebars  import __email__
from json_handlebars  import __version__

setup(
    name='jars',
    author=__author__,
    author_email=__email__,
    version=__version__,
    description='A deployment command line program in Python.',
    url='https://github.com/torfeld6/json_handlebars',
    license='BSD',
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='cli',
    packages=find_packages(),
    install_requires=['click'],
    entry_points={
        'console_scripts': [
            'jars = json_handlebars.__main__:cli',
        ],
    },
)
