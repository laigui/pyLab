# coding:utf-8
import os


def get_latest_log_file():
    base_dir = '/Users/mikeqin/Workspace/python_work/wirelessUART/src'
    #列出目录下文件
    list = os.listdir(base_dir)
    #排序
    #sorted([(x,os.path.getctime(os.path.join(p,x)))   实际是获取文件名的元祖 os.path.join只是拼接该文件
    #  p 为路径 x为文件名  getctime是文件创建时间 getmtime为文件修改时间 getatime是文件访问时间
    #        for x in os.listdir(p) if os.path.isfile(os.path.join(p,x))  判断在改路径下的文件 os.path.isfile
    #        ],
    #       key = lambda  i: i[-1]          可参见 sorted(d.items(), key=lambda x: x[1])   d是一个元祖 这可通value排序
    #       )
    try:
        file=sorted(
            [
                (x, os.path.getctime(os.path.join(base_dir, x)))  # 生成一个列表，列表的每个元素是一个元组（文件，文件创建时间）
                for x in list if os.path.isfile(os.path.join(base_dir, x)) and os.path.splitext(x)[1] == '.log'  # p是文件夹路径，对p下的所有内容，只将文件的信息加入列表
            ],
            key=lambda i: i[1])[-1]  # 对列表进行排序，排序的依据是每一个元组元素的第二个元素，排序后取最后一个元素
        # 输出排序最新的文件
        print("The latest file is " + file[0])
        return file[0]
    except IndexError:
        print("no such file in base folder!")
        return 'null'


if __name__=="__main__":
    dir_p = get_latest_log_file()                                         # 获取最新文档名
