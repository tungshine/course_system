# __author: TungShine
# __date: 2017/9/13
# __description:


import os
import pickle
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
        if os.path.exists(setting.school_db_file):
            self.school_db = pickle.load(setting.read_school_file)
            self.school_manage()
            self.school_db.close()
        else:
            print("\33[31;1m系统信息：初始化数据库\33[0m")
            self.initialize_school()
            self.school_manage()
            self.school_db.close()

    def initialize_school(self):
        self.school_db = dict()
        self.school_db['北京'] = School('北京', '中国.北京')
        self.school_db['上海'] = School('上海', '中国.上海')
        pickle.dump(self.school_db, setting.write_school_file)

    def school_manage(self):
        while True:
            for key in self.school_db:
                print("学校名称：", key)
            choice_school = input("\33[34;0m输入选择管理的学校名:\33[0m").strip()
            if choice_school in self.school_db:
                self.choice_school = choice_school
                self.school_obj = self.school_db[choice_school]
                print(self.school_obj)
                while True:
                    print("\n欢迎来到%s校区\n"
                          "1 添加课程 add_course\n"
                          "2 增加班级 add_classes\n"
                          "3 招聘讲师 add_teacher\n"
                          "4 查看课程 show_course\n"
                          "5 查看班级 show_classes\n"
                          "6 查看讲师 show_teacher\n"
                          "q 退出程序 exit" % self.school_obj.school_name)
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
            self.school_obj.create_course(course_name, course_time, course_price)
            print("\33[32;1m课程更新完成\33[0m")
        else:
            self.school_obj.create_course(course_name, course_time, course_price)
            print("\33[32;1m课程添加成功\33[0m")
            self.school_db[self.choice_school] = self.school_obj
            pickle.dump(self.school_db, setting.write_school_file)

    def show_course(self):
        self.school_obj.show_course()

    def add_classes(self):
        classes_name = input('''\033[34;0m输入要添加班级的名称：\033[0m''').strip()
        course_name = input('''\033[34;0m输入要关联的课程：\033[0m''').strip()
        if classes_name not in self.school_obj.school_classes:
            if course_name in self.school_obj.school_course:
                self.school_obj.create_classes(classes_name, self.school_obj.school_course[course_name])
                self.school_db.update({self.choice_school: self.school_obj})
            else:
                print("\33[31;1m系统错误：关联的课程不存在\33[0m")
        else:
            print("\33[31;1m系统错误：班级已经存在\33[0m")

    def show_classes(self):
        self.school_obj.show_classes()

    def add_teacher(self):
        teacher_name = input('''\033[34;0m输入要添加教师的名称：\033[0m''').strip()
        teacher_salary = input('''\033[34;0m输入要添加教师的薪资：\033[0m''').strip()
        classes_name = input('''\033[34;0m输入要关联的班级：\033[0m''').strip()
        if teacher_name not in self.school_obj.school_teacher:
            if classes_name in self.school_obj.school_classes:
                self.school_obj.create_teacher(teacher_name, teacher_salary, classes_name,
                                               self.school_obj.school_classes[classes_name])
            else:
                self.school_obj.create_teacher(teacher_name, teacher_salary, classes_name,
                                               self.school_obj.school_classes[classes_name])
                print("\33[32;1m讲师已经存在，信息更新完成\33[0m")

        else:
            print("\33[31;1m系统错误：教师已经存在\33[0m")

    def show_teacher(self):
        self.school_obj.show_teacher()


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
