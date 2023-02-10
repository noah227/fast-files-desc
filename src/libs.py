# -*- coding: utf-8 -*-
# CREATED: 2023/2/10
# AUTHOR : NOAH YOUNG
# EMAIL  : noah227@foxmail.com

import hashlib
import json
import os

from wcmatch import fnmatch


class JsonAbstractGenerator:
    def __init__(self, inputSourceDir, include=None, exclude=None, minimized=False, fileSizeLimit=0):
        """
        初始化
        :param str inputSourceDir: 输入源文件夹
        :param minimized: 输出结果是否压缩
        :param fileSizeLimit: 文件大小限制（字节）
        :param include: 要包含的（通配符）匹配
        :param exclude: 要排除的（通配符）匹配
        """
        self.inputSourceDir = inputSourceDir
        self.include = include or []
        self.exclude = exclude or ["*.exe", "*.json"]
        self.minimized = minimized
        self.fileSizeLimit = fileSizeLimit
        self.fileList = []
        self.__initFileList()
        pass

    def __initFileList(self):
        files = []
        # 遍历文件（一级）
        for i in os.listdir(self.inputSourceDir):
            if os.path.isfile(os.path.join(self.inputSourceDir, i)):
                files.append(i)

        if self.include or self.exclude:
            indexCurrent = len(files) - 1
            while indexCurrent >= 0:
                # 匹配包含
                if self.include:
                    isCurrentMatched = False
                    for iPattern in self.include:
                        if fnmatch.fnmatch(files[indexCurrent], iPattern):
                            isCurrentMatched = True
                            break
                    if not isCurrentMatched:
                        files.pop(indexCurrent)
                # 匹配排除
                if self.exclude:
                    for ePattern in self.exclude:
                        if fnmatch.fnmatch(files[indexCurrent], ePattern):
                            files.pop(indexCurrent)
                            break
                indexCurrent -= 1

        # 排除超过大小限制的文件
        if self.fileSizeLimit:
            indexCurrent = len(files) - 1
            while indexCurrent >= 0:
                if os.path.getsize(os.path.join(self.inputSourceDir, files[indexCurrent])) > self.fileSizeLimit:
                    files.pop(indexCurrent)
                indexCurrent -= 1

        self.fileList = files
        pass

    def generate(self, outputPath=""):
        outputPath = outputPath or os.path.join(self.inputSourceDir, "export.json")
        exportData = []
        for i in self.fileList:
            filePath = os.path.join(self.inputSourceDir, i)
            exportData.append({
                "id": self.__getFileMd5(filePath),
                "name": i
            })
        with open(outputPath, "w+", encoding="utf8") as f:
            f.write(json.dumps(exportData, indent="" if self.minimized else "\t", ensure_ascii=False))
        pass

    @staticmethod
    def __getFileMd5(filePath):
        m = hashlib.md5()
        with open(filePath, "rb") as f:
            while True:
                data = f.read(4096)
                if not data:
                    break
                m.update(data)
        return m.hexdigest()
        pass
