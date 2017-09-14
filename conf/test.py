# __author: TungShine
# __date: 2017/9/14
# __description:
import pickle
from conf import setting

print(setting.school_db_file)

ret = pickle.load(setting.read_school_file)
print(ret)
