# __author: TungShine
# __date: 2017/9/13
# __description:

from module.course import Course


class School:
    def __init__(self, school_name, school_address):
        self.school_name = school_name
        self.school_address = school_address
        self.school_course = {}
        self.school_classes = {}
        self.school_teacher = {}
        self.school_student = {}

    def create_course(self, course_name, course_time, course_price):
        course = Course(course_name, course_time, course_price)
        self.school_course[course_name] = course
