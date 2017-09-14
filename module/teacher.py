# __author: TungShine
# __date: 2017/9/13
# __description:


class Teacher:
    def __init__(self, teacher_name, teacher_salary):
        self.teacher_name = teacher_name
        self.teacher_salary = teacher_salary
        self.teacher_classes = []

    def teacher_add_classes(self, classes_name, classes_obj):
        self.teacher_calsses[classes_name] = classes_obj
