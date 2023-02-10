# -*- coding: utf-8 -*-
# CREATED: 2023/2/10
# AUTHOR : NOAH YOUNG
# EMAIL  : noah227@foxmail.com

import sys

from libs import JsonAbstractGenerator

if __name__ == "__main__":
    args = sys.argv
    # print(args, "<<<<<args")
    if len(args) > 1:
        pass
    else:
        # 临时测试使用
        generator = JsonAbstractGenerator("./")
        generator.generate()
        pass
