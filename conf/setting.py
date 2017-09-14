# __author: TungShine
# __date: 2017/9/13
# __description:


import os
import pickle

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

school_db_file = "%s\\%s" % (BASE_DIR, "db\\school")
course_db_file = "%s\\%s" % (BASE_DIR, "db\\course")
student_db_file = "%s\\%s" % (BASE_DIR, "db\\student")
classes_db_file = "%s\\%s" % (BASE_DIR, "db\\classes")

write_school_file = open(school_db_file, 'wb')
read_school_file = open(school_db_file, 'rb')

data = {
    "school": {
        "study": "day"
    },
}

pickle.dump(data, write_school_file)
