# __author: TungShine
# __date: 2017/9/13
# __description:


import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

school_db_file = "%s\\%s" % (BASE_DIR, "db\\school")

print(school_db_file)
