from zeep import Client
from lxml import etree
from Lesson import Lesson
from datetime import datetime, timedelta
from GenerateICS import create_ics, export_ics


if __name__ == '__main__':

    client = Client(
        'http://ded.nuaa.edu.cn/NetEa/Services/WebService.asmx?WSDL')

    # xn = input('学年: ')
    # xq = input('学期: ')
    # xh = input('学号: ')

    # DEBUG MODE
    xn = '2017-2018'
    xq = '2'
    xh = '161540121'
    semester_start_date = datetime(2018, 2, 26, 0, 0, 0)

    request_data = {
        'xn': xn,
        'xq': xq,
        'xh': xh,
    }

    with client.options(raw_response=True):
        response = client.service.GetCourseTableByXh(**request_data)
        root = etree.fromstring(response.content)
        body = root[0]
        GetCourseTableByXhResponse = body[0]
        GetCourseTableByXhResult = GetCourseTableByXhResponse[0]
        try:
            NewDataSet = list(GetCourseTableByXhResult[1][1])
        except IndexError:
            print(xn + '学年第' + xq + '学期没有课程！')
        else:
            print(len(NewDataSet))

            lessons = list()

            # Add lessons
            for ds in NewDataSet:
                # Explain XML
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
                lsjs = ds.find('lsjs').text  # what is this???
                room_number = ds.find('roomid').text
                weeks = list(map(int, ds.find('weeks').text.split(',')))

                new_lesson = Lesson(year, semester, student_number,
                                    lesson_order_number,
                                    lesson_number, name, teacher_number,
                                    teacher_name,
                                    school_distinct, day_of_week, unit, lsjs,
                                    room_number, weeks)

                lessons.append(new_lesson)

            # for lesson in lessons:
            #     lesson.print()

            cal = create_ics(lessons, semester_start_date)
            export_ics(cal)
