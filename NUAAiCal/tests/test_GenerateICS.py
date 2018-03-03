# -*- coding:utf-8 -*-

from __future__ import unicode_literals

from NUAAiCal.GenerateICS import create_ics, export_ics
from NUAAiCal.Lesson import Lesson
import pytest
from zeep import Client
from icalendar import Calendar, Event
from datetime import datetime
from pytz import timezone


class TestGenerateICS:
    def test_create_ics(self):
        new_lesson = Lesson('2017-2018', '2', '161540121',
                            '03103270_70205111_6', '03103270', '全球导航卫星系统',
                            '70205111', '曾庆化', '将军路', '3', '3', '2', '2205',
                            [10, 11, 12, 13, 14, 15, 16, 17])
        lessons = [new_lesson]
        assert type(create_ics(lessons, datetime(2018, 2, 26, 0, 0, 0,
                    tzinfo=timezone('Asia/Shanghai'))) is Calendar)

    def test_export_ics(self):
        # test cal
        cal = Calendar()
        cal.add('prodid', '-//TripleZ//NUAA-iCal-Python//CN')
        cal.add('version', '2.0')
        cal.add('X-WR-TIMEZONE', 'Asia/Shanghai')
        event = Event()
        event.add('summary', '全球导航卫星系统')
        event.add('dtstart', datetime(2018, 5, 2, 10, 15, 0,
                    tzinfo=timezone('Asia/Shanghai')))
        event.add('dtend', datetime(2018, 5, 2, 12, 0, 0,
                    tzinfo=timezone('Asia/Shanghai')))
        event.add('dtstamp', datetime.now(tz=timezone('Asia/Shanghai')))
        event.add('location', '2205' + '@' + '将军路')
        try:
            event.add('description', "教师：" + '曾庆化' +
                      "\n" +
                      "课程序号：03103270_70205111_6"
                      + "\n\nPowered by <a href=\"https://github.com/Triple-Z/NUAA-iCal-Python\">NUAA-iCal-Python</a>")
        except UnicodeDecodeError:
            details = "教师：".decode('utf-8') + '曾庆化' \
                      + "\n".decode('utf-8') + \
                      "课程序号：03103270_70205111_6".decode('utf-8') \
                      + "\n\nPowered by  <a href=\"https://github.com/Triple-Z/NUAA-iCal-Python\">NUAA-iCal-Python</a>".decode(
                'utf-8')
            event.add('description', details)

        cal.add_component(event)

        assert export_ics(cal, '2017-2018', '2', '161540121')
