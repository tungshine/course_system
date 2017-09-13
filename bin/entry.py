# __author: TungShine
# __date: 2017/9/13
# __description:

import os
from core import main

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    obj = main.ManageCenter()
    obj.run()
