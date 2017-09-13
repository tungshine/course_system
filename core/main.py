# __author: TungShine
# __date: 2017/9/13
# __description:


import os
import shelve
from conf import setting
from module.school import School


class ManageCenter:
    def __init__(self):
        pass

    @staticmethod
    def run():
        while True:
            print("\n欢迎进入CLASS_SYSTEM系统\n"
                  "1 学生视图\n"
                  "2 教师视图\n"
                  "3 学校视图\n"
                  "q 退出学员管理系统\n")
            user_choice = input("\033[34;0m请输入您要登录的视图:\033[0m")
            if user_choice == '1':
                StudentManage()
            elif user_choice == '2':
                TeacherManage()
            elif user_choice == '3':
                SchoolManage()
            elif user_choice == 'q':
                print("\033[34;1m感谢使用学员管理系统,退出\033[0m")
                break
            else:
                print("\033[31;1m请输入正确的选项\033[0m")


class SchoolManage:
    """学校管理视图"""

    def __init__(self):
        if os.path.exists(setting.school_db_file + '.dat'):
            self.school_db = shelve.open(setting.school_db_file)
            self.school_manage()
            self.school_db.close()
        else:
            print("\33[31;1m系统信息：初始化数据库\33[0m")
            self.initialize_school()
            self.school_manage()
            self.school_db.close()

    def initialize_school(self):
        self.school_db = shelve.open(setting.school_db_file)
        self.school_db['北京'] = School('北京', '中国.北京')
        self.school_db['上海'] = School('上海', '中国.上海')

    def school_manage(self):
        while True:
            for key in self.school_db:
                print("学校名称：", key)
            choice_school = input("\33[34;0m输入选择管理的学校名:\33[0m").strip()
            if choice_school in self.school_db:
                self.choice_school = choice_school
                self.school_obj = self.school_db[choice_school]
                while True:
                    print("\n欢迎来到%s校区\n"
                          "添加课程 add_course\n"
                          "增加班级 add_classes\n"
                          "招聘讲师 add_teacher\n"
                          "查看课程 check_course\n"
                          "查看班级 check_classes\n"
                          "查看讲师 check_teacher\n"
                          "退出程序 exit" % self.school_obj.school_name)
                    user_func = input('''\033[34;0m输入要操作的命令：\033[0m''').strip()
                    if hasattr(self, user_func):
                        getattr(self, user_func)()
            else:
                print("\33[31;1m输入错误：请输入正确的学校名\33[0m")

    def add_course(self):
        course_name = input('''\033[34;0m输入要添加课程的名称：\033[0m''').strip()
        course_price = input('''\033[34;0m输入要添加课程的价格：\033[0m''').strip()
        course_time = input('''\033[34;0m输入要添加课程的时长：\033[0m''').strip()

        if course_name in self.school_obj.school_course:
            print("\33[32;1m课程存在\33[0m")
            pass

    def add_classes(self):
        print('add_classes')

    def add_teacher(self):
        print('add_teacher')

    def check_course(self):
        print('check_course')

    def check_classes(self):
        print('check_classes')

    def check_teacher(self):
        print('check_teacher')


class CourseManage:
    """课程管理视图"""

    def __init__(self):
        pass


class StudentManage:
    """学员管理视图"""

    def __init__(self):
        pass


class TeacherManage:
    """教师管理视图"""

    def __init__(self):
        pass
