# -*- coding:utf-8 -*-

from __future__ import unicode_literals

from NUAAiCal.FindFirstDayofSemester import get_semester_start_date
import pytest
from zeep import Client
from datetime import datetime
from pytz import timezone


class TestFFDoS:
    def test_get_semester_start_date(self):
        client = Client(
            'http://ded.nuaa.edu.cn/NetEa/Services/WebService.asmx?WSDL')
        assert get_semester_start_date([2017, 2018], '2', client) == \
            datetime(2018, 2, 26, 0, 0, 0, tzinfo=timezone('Asia/Shanghai'))
