from setuptools import setup, find_packages
from codecs import open
from os import path
from NUAAiCal.settings import VERSION

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()
setup(
    name='NUAAiCal',
    version=VERSION,
    description='Generate NUAA curriculum to iCalendar file.',
    url='https://github.com/Triple-Z/NUAA-iCal-Python',
    author='TripleZ',
    author_email='me@triplez.cn',
    license='MIT',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        # 'Programming Language :: Python :: 2',
        # 'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.4',
        # 'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='NUAA iCalendar ics curriculum iCal schedule calendar',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    entry_points={
        'console_scripts': [
            'nuaaical = NUAAiCal.main:main',
        ],
    },
    install_requires=[
        'future;python_version<"3"',
        'six',
        'lxml',
        'pytz',
        'zeep==2.5.0',
        'icalendar',
    ],
    # Use pytest
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)

