# -*- coding: utf-8 -*-
# CREATED: 2023/2/10
# AUTHOR : NOAH YOUNG
# EMAIL  : noah227@foxmail.com
from src.main import JsonAbstractGenerator


def __test():
    generator = JsonAbstractGenerator("./", include="**.txt")
    generator.generate()
    pass


if __name__ == "__main__":
    __test()
