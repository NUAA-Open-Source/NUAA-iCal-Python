class Lesson:
    def __init__(self, year, semester, student_number, lesson_order_number,
                 lesson_number, name, teacher_number, teacher_name,
                 school_distinct, day_of_week, unit, lsjs, room_number, weeks):
        self.year = year
        self.semester = semester
        self.student_number = student_number
        self.lesson_order_number = lesson_order_number
        self.lesson_number = lesson_number
        self.name = name
        self.teacher_number = teacher_number
        self.teacher_name = teacher_name
        self.school_distinct = school_distinct
        self.day_of_week = day_of_week
        self.unit = unit
        self.lsjs = lsjs # what is this?
        self.room_number = room_number
        self.weeks = weeks

    def print(self):
        print('=====================================')
        print("学年：" + self.year)
        print("学期：" + self.semester)
        print("学号：" + self.student_number)
        print("课程序号：" + self.lesson_order_number)
        print("课程号：" + self.lesson_number)
        print("课程名：" + self.name)
        print("教师号：" + self.teacher_number)
        print("教师名：" + self.teacher_name)
        print("校区：" + self.school_distinct)
        print("week：" + self.day_of_week)
        print("学分：" + self.unit)
        print("lsjs：" + self.lsjs)
        print("教室号：" + self.room_number)
        print("上课周：" + ','.join(map(str, self.weeks)))
