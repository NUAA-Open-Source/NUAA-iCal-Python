from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='NUAAiCal',
    version='0.3.3',
    description='Generate NUAA curriculum to iCalendar file.',
    url='https://github.com/Triple-Z/NUAA-iCal-Python',
    author='TripleZ',
    author_email='me@triplez.cn',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='NUAA iCalendar ics curriculum iCal schedule calendar',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'nuaaical=NUAAiCal.main:main',
        ],
    },
    install_requires=[
        'lxml==4.1.1',
        'pytz==2018.3',
        'zeep==2.5.0',
    ],
    project_urls={
        'Bug Reports': 'https://github.com/Triple-Z/NUAA-iCal-Python/issues',
        'Donate': 'https://blog.triplez.cn/index.php/about',
        'Source': 'https://github.com/Triple-Z/NUAA-iCal-Python',
    },
)
