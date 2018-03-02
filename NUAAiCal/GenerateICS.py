# -*- coding: utf-8 -*-

from icalendar import Calendar, Event, vText
from datetime import datetime, timedelta
from pytz import timezone
import os


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
            event.add('dtstamp', datetime.now(tz=timezone('Asia/Shanghai')))
            event.add('location', lesson.room_number.rstrip() + '@' +
                      lesson.school_distinct.rstrip())
            event.add('description', "教师：" + lesson.teacher_name.rstrip() +
                      "\n" +
                      "课程序号：" + lesson.lesson_order_number.rstrip()
                      + "\n\nPowered by <a href=\"https://github.com/Triple-Z/NUAA-iCal-Python\">NUAA-iCal-Python</a>")

            cal.add_component(event)

    return cal


def export_ics(cal, xn, xq, xh):

    if os.path.exists('NUAAiCal-Data'):
        # print('Directory exists.')
        pass
    else:
        os.mkdir('NUAAiCal-Data')
    filename = 'NUAAiCal-Data/NUAA-curriculum-' + xn + '-' + xq + '-' + xh + '.ics'
    f = open(os.path.join(filename), 'wb')
    f.write(cal.to_ical())
    f.close()
    # print('ICS file has successfully exported to \"' + filename + '\".')

    print("日历文件已导出到 \"" + os.path.abspath(filename) + "\"。")
