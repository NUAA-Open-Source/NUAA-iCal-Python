from zeep import Client
from lxml import etree
from Lesson import Lesson
from datetime import datetime, timedelta

client = Client('http://ded.nuaa.edu.cn/NetEa/Services/WebService.asmx?WSDL')

# xn = input('学年: ')
# xq = input('学期: ')
# xh = input('学号: ')

# DEBUG MODE
xn = '2017-2018'
xq = '2'
xh = '161540121'

request_data = {
    'xn': xn,
    'xq': xq,
    'xh': xh,
}

with client.options(raw_response=True):
    response = client.service.GetCourseTableByXh(**request_data)
    # response = client.service.GetCurrentXlInfo()
    root = etree.fromstring(response.content)
    # print(etree.tostring(root, pretty_print=True))
    body = root[0]
    GetCourseTableByXhResponse = body[0]
    GetCourseTableByXhResult = GetCourseTableByXhResponse[0]
    NewDataSet = list(GetCourseTableByXhResult[1][1])
    print(len(NewDataSet))

    lessons = list()

    for ds in NewDataSet:
        year = ds.find('xn').text
        semester = ds.find('xq').text
        student_number = ds.find('xh').text
        lesson_order_number = ds.find('kcxh').text
        lesson_number = ds.find('kch').text
        name = ds.find('kcm').text
        teacher_number = ds.find('jsh').text
        teacher_name = ds.find('jsm').text
        school_distinct = ds.find('xiaoqu').text
        day_of_week = ds.find('week').text
        unit = ds.find('unit').text
        lsjs = ds.find('lsjs').text # what is this???
        room_number = ds.find('roomid').text
        weeks = list(map(int, ds.find('weeks').text.split(',')))

        new_lesson = Lesson(year, semester, student_number, lesson_order_number,
                 lesson_number, name, teacher_number, teacher_name,
                 school_distinct, day_of_week, unit, lsjs, room_number, weeks)

        lessons.append(new_lesson)

    for lesson in lessons:
        lesson.print()
