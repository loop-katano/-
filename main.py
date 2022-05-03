# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import tkinter as tk
import tkinter.filedialog
import os


# path = tk.filedialog.askdirectory(title='选择一个文件夹',)
# filename = tk.filedialog.askopenfilename(title='选择一个文件夹', filetypes=('所有文件', '.*'))

def rename():
    path = input("请输入要重命名的文件夹路径：")  # 获取当前文件的相对路径
    target = input("请输入重命名的规则：")
    file_list = os.listdir(path)  # 用列表存储，该文件夹下的所有文件名
    i = 0
    for file in file_list:
        i = i + 1
        former_file = os.path.join(path, file)  # 当前文件原名称(含扩展名)
        filetype = os.path.splitext(file)[1]  # 当前文件扩展名
        # 获取新的文件夹路径
        os.rename(former_file, os.path.join(path, target + '_' + str(i) + filetype))
        # 重命名前后都必须包含路径+文件名


rename()

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
