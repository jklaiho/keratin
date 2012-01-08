import os
from setuptools import setup
from keratin import VERSION

f = open(os.path.join(os.path.dirname(__file__), 'README.md'))
readme = f.read()
f.close()

setup(
    name = 'Keratin',
    version = ".".join(map(str, VERSION)),
    description = 'Keratin is a static site generator that tries very hard '
        'not to suck.',
    long_description = readme,
    author = 'JK Laiho',
    author_email = 'jklaiho@iki.fi',
    url = 'https://github.com/jklaiho/keratin',
    packages = ['keratin', 'keratin.tests'],
    zip_safe = False,
    test_suite = 'keratin.tests',
    entry_points = {
        'console_scripts': ['keratin = keratin.cli:main']
    },
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Text Processing :: Markup',
        'Topic :: Text Processing :: Markup :: HTML'
    ],
)
