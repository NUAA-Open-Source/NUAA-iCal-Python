# NUAA iCal Python

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/NUAAiCal.svg)
[![Build Status](https://travis-ci.org/NUAA-Open-Source/NUAA-iCal-Python.svg)](https://travis-ci.org/NUAA-Open-Source/NUAA-iCal-Python)
[![pypi package](https://img.shields.io/pypi/v/NUAAiCal.svg)](https://pypi.python.org/pypi/NUAAiCal/)
![PyPI - Status](https://img.shields.io/pypi/status/NUAAiCal.svg)
![PyPI - License](https://img.shields.io/pypi/l/NUAAiCal.svg)

:us: [English](/README.md) | :cn: 简体中文

⚠️ **由于南京航空航天大学教务处接口变化，该程序使用的接口已无效。请使用其它方式获得课表的程序如 [miaotony/NUAA_ClassSchedule](https://github.com/miaotony/NUAA_ClassSchedule)。感谢你们的支持！**

将南京航空航天大学的课程表（不含体育、实验等课程）导出成 `.ics` 日历格式，以将课程事件导入其他日历软件（如 Google Calendar）。

欢迎贡献代码，提交 `PR`！

## 快速使用

[![DEMO](https://asciinema.org/a/HNivm2Ax5PpuUx6e5LwMwxffA.png)](https://asciinema.org/a/HNivm2Ax5PpuUx6e5LwMwxffA)

## 安装

### PyPI 安装

安装 `NUAAiCal` python 软件包:

```bash
$ pip install NUAAiCal
```

> 若有权限问题，请使用 `pip install NUAAiCal --user` 。

### 源码安装

从源码构建安装:

```bash
$ git clone https://github.com/Triple-Z/NUAA-iCal-Python.git
$ cd NUAA-iCal-Python
$ python setup.py install
```

## 启动程序

```bash
$ nuaaical
```

你将会看到课程表日历 `.ics` 文件的导出路径, 你可以将其导入至 Google 日历等日历程序。

## 疑难解答

### 未找到命令

> nuaaical: command not found

可能系统环境变量 `PATH` 缺失了值 `~/.local/bin` ， 尝试运行下面的命令后再重新运行 `nuaaical` :

```bash
$ export PATH=${HOME}/.local/bin:$PATH
``` 

## 版权声明

本项目采用 [MIT 许可协议](/LICENSE.md) 。

Copyright &copy; 2018 [TripleZ](https://github.com/Triple-Z)
