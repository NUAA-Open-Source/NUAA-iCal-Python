# NUAA iCal Python

![Python Version](https://img.shields.io/badge/python-3.6-blue.svg)
[![pypi package](https://img.shields.io/pypi/v/NUAAiCal.svg)](https://pypi.python.org/pypi/NUAAiCal/)
![PyPI - Status](https://img.shields.io/pypi/status/NUAAiCal.svg)
![PyPI - License](https://img.shields.io/pypi/l/NUAAiCal.svg)

Export the curriculum of NUAA to a `.ics` calendar file, in order to import 
class events to other calendars (e.g. Google Calendar).

:us: English | :cn: [简体中文](/README_zh-hans.md)

## Installation

### PyPI

Install `NUAAiCal` python package:

```bash
$ pip3 install NUAAiCal
```

### Source

Built it from source code:

```bash
$ git clone https://github.com/Triple-Z/NUAA-iCal-Python.git
$ cd NUAA-iCal-Python
$ python3 setup.py install
```

## Start Application

```bash
$ nuaaical
```

You will get the `.ics` file path, you can import it to Google 
Calendar etc.

# TroubleShoot

## Command Not Found

> nuaaical: command not found

Maybe your system `PATH` environment variable lacks of the value of `~/
.local/bin` . Try the command following, then run `nuaaical` again:

```bash
$ export PATH=${HOME}/.local/bin:$PATH
``` 

## TODO

- [x] Get course table data
- [x] Generate iCal file
- [x] Input Variables
- [x] Pack
- [ ] GUI
- [ ] Export to Google Calendar
- [ ] WSGI server

## Copyright

This project is licensed by [The MIT License](/LICENSE.md).

Copyright &copy; 2018 [TripleZ](https://github.com/Triple-Z)
