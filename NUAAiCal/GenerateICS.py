# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

from icalendar import Calendar, Event, vText
from datetime import datetime, timedelta
from pytz import timezone
import tempfile
import hashlib
import os
from sys import getsizeof

def create_ics(lessons, semester_start_date):

    cal = Calendar()
    cal.add('prodid', '-//TripleZ//NUAA-iCal-Python//CN')
    cal.add('version', '2.0')
    cal.add('X-WR-TIMEZONE', 'Asia/Shanghai')

    for lesson in lessons:
        for week in lesson.weeks:

            event = Event()
            event.add('summary', lesson.name)

            # Lesson start time
            lesson_start_hour = {
                '1': 8,
                '3': 10,
                '5': 14,
                '7': 16,
                '9': 18,
            }.get(lesson.unit)
            lesson_start_minute = {
                '1': 0,
                '3': 15,
                '5': 0,
                '7': 15,
                '9': 45,
            }.get(lesson.unit)

            lesson_start_time = semester_start_date \
                + timedelta(weeks=week-1, days=int(lesson.day_of_week)-1,
                            hours=lesson_start_hour-semester_start_date.hour,
                            minutes=lesson_start_minute-semester_start_date.minute,
                            seconds=-semester_start_date.second,
                            milliseconds=-semester_start_date.microsecond)

            lesson_end_time = lesson_start_time + timedelta(minutes=105)

            event.add('dtstart', lesson_start_time)
            event.add('dtend', lesson_end_time)
            # event.add('dtstamp', datetime.now(tz=timezone('Asia/Shanghai')))
            event.add('location', lesson.room_number.rstrip() + '@' +
                      lesson.school_distinct.rstrip())
            try:
                event.add('description', "教师：" + lesson.teacher_name.rstrip() +
                      "\n" + \
                      "当前周次：%d" % week + \
                      "\n上课周次：%d-%d" % (lesson.weeks[0], lesson.weeks[-1]) +
                      "\n课程序号：" + lesson.lesson_order_number.rstrip() + \
                      "\n\nPowered by <a href=\"https://github.com/Triple-Z/NUAA-iCal-Python\">NUAA-iCal-Python</a>")
            except UnicodeDecodeError:
                details = "教师：".decode('utf-8') + lesson.teacher_name.rstrip()\
                          + "\n".decode('utf-8') + \
                          "当前周次：".decode('utf-8') + week + \
                          "\n上课周次：".decode('utf-8') + weeks[0] + "-".decode('utf-8') + week[-1] + \
                          "\n课程序号：".decode('utf-8') +\
                      lesson.lesson_order_number.rstrip() + "\n\nPowered by  <a href=\"https://github.com/Triple-Z/NUAA-iCal-Python\">NUAA-iCal-Python</a>".decode('utf-8')
                event.add('description', details)

            cal.add_component(event)

    return cal


def export_ics(cal, xn, xq, xh):
    filename = 'NUAAiCal-Data/NUAA-curriculum-' + xn + '-' + xq + '-' + xh + '.ics'

    if os.path.exists('NUAAiCal-Data'):
        # print('Directory exists.')
        if os.path.isfile(filename):
            # File exists, check whether need to be updated.

            tem = open('.temp', 'w+b')
            tem_path = os.path.abspath(tem.name)
            tem.write(cal.to_ical())
            tem_filename = tem.name
            tem.read()  # fix a py2.7 bug... issue#2
            tem.close()
            # print(getsizeof(tem.read()))
            is_update = not is_same(tem_path, filename)
            # print("Temp file name is %s, in %s" % (tem_filename, os.path.abspath(tem_filename)))
            os.remove(tem_path)

            if is_update:
                print('有更新的课程！')
                f = open(os.path.join(filename), 'wb')
                f.write(cal.to_ical())
                f.close()
                print("更新的日历文件已导出到 \"" + os.path.abspath(filename) + "\"。")
            else:
                print('没有需要更新的课程！')
                print("原有的日历文件位置为 \"" + os.path.abspath(filename) + "\"。")

        else:
            f = open(os.path.join(filename), 'wb')
            f.write(cal.to_ical())
            f.close()
            print("日历文件已导出到 \"" + os.path.abspath(filename) + "\"。")
    else:
        os.mkdir('NUAAiCal-Data')

        f = open(os.path.join(filename), 'wb')
        f.write(cal.to_ical())
        f.close()
        # print('ICS file has successfully exported to \"' + filename + '\".')
        print("日历文件已导出到 \"" + os.path.abspath(filename) + "\"。")

    return True


def is_same(file1, file2):
    hash1 = hashlib.md5()
    with open(file1, 'rb') as f1:
        f1_data = f1.read()
    # print(getsizeof(f1_data))
    hash1.update(f1_data)
    md5_1 = hash1.hexdigest()
    # print(f1_data)
    # print(file1.name)
    # print(md5_1)

    hash2 = hashlib.md5()
    with open(file2, 'rb') as f2:
        f2_data = f2.read()
        # print(getsizeof(f2_data))
    hash2.update(f2_data)
    md5_2 = hash2.hexdigest()
    # print(f2_data)
    # print(f2.name)
    # print(md5_2)

    # print(f1_data == f2_data)

    if md5_1 == md5_2:
        return True
    else:
        return False
