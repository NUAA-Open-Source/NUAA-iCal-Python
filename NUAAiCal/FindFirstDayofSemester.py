# -*- coding: utf-8 -*-

from lxml import etree
from datetime import datetime, timedelta
from pytz import timezone


def get_semester_start_date(years, xq, client):
    semester = int(xq)

    request_data = {
        1: {
            "year": years[0],
            "month": 9,
            "day": 1,
        },
        2: {
            "year": years[1],
            "month": 3,
            "day": 1,
        },
    }.get(semester)

    base_date = datetime(int(request_data['year']), int(request_data['month']),
                         int(request_data['day']), 0, 0, 0, tzinfo=timezone(
            'Asia/Shanghai'))

    with client.options(raw_response=True):
        response = client.service.GeXlInfoByDate(**request_data)
        root = etree.fromstring(response.content)
        body = root[0]
        GeXlInfoByDateResponse = body[0]
        GeXlInfoByDateResult = GeXlInfoByDateResponse[0]
        try:
            ds = GeXlInfoByDateResult[1][0][0]
        except IndexError:
            print('[ERROR] 这个学期还没有校历信息!')
            return False
        else:
            week_number = int(ds.find('zc').text)
            monday = base_date - timedelta(days=base_date.weekday())
            if week_number == 0:
                while week_number == 0:
                    monday = monday + timedelta(weeks=1)
                    request_data = {
                        "year": monday.year,
                        "month": monday.month,
                        "day": monday.day,
                    }
                    response = client.service.GeXlInfoByDate(**request_data)
                    root = etree.fromstring(response.content)
                    ds = root[0][0][0][1][0][0]
                    week_number = int(ds.find('zc').text)
                if week_number == 1:
                    return monday
            elif week_number == 1:
                return monday
            else:
                monday = monday - timedelta(weeks=week_number - 1)
                return monday
