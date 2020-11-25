#!/c/Users/leyan/AppData/Local/Programs/Python/Python38/python
# **********************************************
# pyinstaller -F -w 你的文件名.py
# v 2.5
#
# **********************************************

import tkinter as tk
from tkinter import filedialog
import os
from tkinter import *  # 导入tkinter的所有组件
import tkinter.messagebox  # 弹出消息框

stg_changelist = {
    'wss': ' 		"endpoint": "wss://agent.stg.lain.leyanbot.com/ws",\n',
    'authority":': '		"authority": "https://stg-api.leyanbot.com/dice/v1",\n',
    'flashcard":': '		"flashcard": "https://stg-api.leyanbot.com/flashcard/v1",\n',
    '"wingman":': '		"wingman": "http://stg-pip-boy.infra.leyantech.com",\n',
    'endpoint": "https://api': '				"endpoint": "https://stg-api.leyanbot.com/dice/v1"\n',
    'bipolar-prokaryote': '			"endpoint": "https://staging-taobao-bipolar-prokaryote.ftest.leyantech.com/",\n'
}
prd_changelist = {
    'wss': ' 		"endpoint": "wss://agentproxy.leyanbot.com/ws",\n',
    'authority":': '		"authority": "https://api.leyanbot.com/dice/v1",\n',
    'flashcard":': '		"flashcard": "https://api.leyanbot.com/flashcard/v1",\n',
    '"wingman":': '		"wingman": "https://wingman.leyantech.com",\n',
    'endpoint": "https://stg-api': '				"endpoint": "https://api.leyanbot.com/dice/v1"\n',
    'bipolar-prokaryote': '			"endpoint": "https://bipolar-prokaryote.leyantech.com/",\n'
}

preview_changelist = {
    'wss': ' 		"endpoint": "wss://agentproxy.leyanbot.com/ws",\n',
    'authority":': '		"authority": "https://api.leyanbot.com/dice/v1",\n',
    'flashcard":': '		"flashcard": "https://api.leyanbot.com/flashcard/v1",\n',
    '"wingman":': '		"wingman": "https://wingman.leyantech.com",\n',
    'endpoint": "https://stg-api': '				"endpoint": "https://api.leyanbot.com/dice/v1"\n',
    'bipolar-prokaryote': '			"endpoint": "https://preview-taobao-bipolar-prokaryote.ftest.leyantech.com/",\n'
}

env_dice = {0: 'stg', 1: 'prd', 2: 'preview'}


def selectPath():
    path_ = filedialog.askopenfilename()
    path.set(path_)


def action():
    env_flag = v.get()
    entry_content = e_path.get()
    if len(entry_content) == 0:
        if os.path.isfile(file_path):
            dice_path = file_path
            change_dice(env_flag, dice_path)
        else:
            tk.messagebox.showinfo(title='提示', message="默认路径未找到dice.json")
    else:
        if entry_content.endswith('dice.json') and os.path.isfile(entry_content):
            dice_path = entry_content
            change_dice(env_flag, dice_path)
        else:
            tk.messagebox.showinfo(title='提示', message="未找到dice.json")


def change_dice(env_flag, dice_path):
    dicejson_path = dice_path
    content = open(dicejson_path, 'r', encoding='utf-8').readlines()
    changelist_name = env_dice[env_flag] + '_changelist'
    print(changelist_name)
    env_list = globals()[changelist_name]
    for change in env_list:
        for line_con in content:
            if change in line_con:
                line_num = content.index(line_con)
                content[line_num] = env_list[change]

    open(dicejson_path, 'w', encoding='utf-8').writelines(content)
    tk.messagebox.showinfo(title='提示', message="dice.josn 修改成功！！！")


root = Tk()
root.title('修改dice.json')
root.geometry('500x130+400+200')  # 尺寸位置
root.minsize(500, 130)  # 最小尺寸
root.maxsize(500, 130)  # 最大尺寸
path = StringVar()

Label(root, text="env:").grid(row=0, column=0)
# 显示操作界面
v = tk.IntVar()  # 设置关联变量
# 每一个选项都设置一个单一值
for flag in env_dice:
    Radiobutton(root, text=env_dice[flag], variable=v, value=flag).grid(row=0, column=flag + 1)

l_path = Label(root, text="文件路径:").grid(row=1, column=0)
# Entry是获取输入
e_path = Entry(root, textvariable=path, width=50)
e_path.grid(row=1, column=1, columnspan=4)
# 操作按钮
b_path = Button(root, text="选择", command=selectPath).grid(row=1, column=5)

username = os.getenv('username')
file_path = 'C:/Users/' + username + '/AppData/Roaming/dice/dice.json'
l_default = Label(root, text="default:").grid(row=2, column=0)
l_default_path = Label(root, text=file_path).grid(row=2, column=1, columnspan=4)

b_change = Button(root, text="修改", width=15, command=action).grid(row=3, column=2)

root.mainloop()
