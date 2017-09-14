# __author: TungShine
# __date: 2017/9/13
# __description:

from module.course import Course
from module.classes import Classes
from module.teacher import Teacher
from module.student import Student


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

    def show_course(self):
        for key in self.school_course:
            course = self.school_course[key]
            print(("\33[32;1m课程：%s\t价格：%s\t周期：%s月\33[0m"
                   % (course.course_name, course.course_price, course.course_time,)))

    def create_classes(self, classes_name, course_obj):
        classes = Classes(classes_name, course_obj)
        self.school_classes[classes_name] = classes

    def show_classes(self):
        for key in self.school_classes:
            classes = self.school_classes[key]
            print("\33[32;1m班级：%s\t关联课程：%s\33[0m" % (classes.class_name, classes.class_courese.course_name))

    def create_teacher(self, teacher_name, teacher_salary, classes_name, classes_obj):
        teacher = Teacher(teacher_name, teacher_salary)
        # teacher.teacher_add_classes(classes_name, classes_obj)
        teacher.teacher_classes[classes_name] = classes_obj

    def show_teacher(self):
        print()