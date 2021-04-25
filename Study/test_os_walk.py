def fileListFunc(filePathList):
    fileList = []
    for top, dirs, nondirs in os.walk(filePathList):
        print('这是top目录：', top)
        for item in nondirs:
            # print('这是nodirs目录：', item)
            fileList.append(os.path.join(top, item))

    return fileList

 def search_file(self, root, searchname,temp):         #定义一个文件查找的功能,并把值传递给temp
        items = os.walk(root)    # 把路径所有的目录和文件赋值给files
        print('看看walk有啥不一样的额', items)
        for item in items:      # 遍历目录或文件
            path = os.path.join(root, item)
            if os.path.isdir(path):
                # print('这是一个文件目录：' + item)
                # print('立即跟踪进入，调用函数本身')
                self.search_inFilelist(path, searchname, temp)
            elif os.path.isfile(path) and searchname in item:
                # print('[+]   发现一个目标文件', path)
                temp.append(item)

import os
# fileListFunc('H:\ZB_tools')
print(fileListFunc('H:\ZB_tools'))
