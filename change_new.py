#!/c/Users/leyan/AppData/Local/Programs/Python/Python38/python
# **********************************************
# pip install pyinstaller
# pyinstaller -F -w 你的文件名.py
# v 3.0
#
# **********************************************

import tkinter as tk
from tkinter import filedialog
import os
from tkinter import *  # 导入tkinter的所有组件
import tkinter.messagebox  # 弹出消息框

dice_stg_changelist = {
    'wss': ' 		"endpoint": "wss://stg-agent.leyanbot.com/ws",\n',
    'authority":': '		"authority": "https://stg-api.leyanbot.com/dice/v1",\n',
    'flashcard":': '		"flashcard": "https://stg-api.leyanbot.com/flashcard/v1",\n',
    '"wingman":': '		"wingman": "http://stg-pip-boy.infra.leyantech.com",\n',
    'endpoint": "https://api': '				"endpoint": "https://stg-api.leyanbot.com/dice/v1"\n',
    'bipolar-prokaryote': '			"endpoint": "https://staging-taobao-bipolar-prokaryote.ftest.leyantech.com/",\n',
    'serviceMode": "http': '		"serviceMode": "https://stg-gw-api.leyanbot.com/v1/client_info",\n'
}
dice_prd_changelist = {
    'wss': ' 		"endpoint": "wss://agentproxy.leyanbot.com/ws",\n',
    'authority":': '		"authority": "https://api.leyanbot.com/dice/v1",\n',
    'flashcard":': '		"flashcard": "https://api.leyanbot.com/flashcard/v1",\n',
    '"wingman":': '		"wingman": "https://wingman.leyantech.com",\n',
    'endpoint": "https://stg-api': '				"endpoint": "https://api.leyanbot.com/dice/v1"\n',
    'bipolar-prokaryote': '			"endpoint": "https://bipolar-prokaryote.leyantech.com/",\n',
    'serviceMode": "http': '		"serviceMode": "https://apiproxy.leyanbot.com/v1/client_info",\n'
}

dice_preview_changelist = {
    'wss': ' 		"endpoint": "wss://agentproxy.leyanbot.com/ws",\n',
    'authority":': '		"authority": "https://api.leyanbot.com/dice/v1",\n',
    'flashcard":': '		"flashcard": "https://api.leyanbot.com/flashcard/v1",\n',
    '"wingman":': '		"wingman": "https://wingman.leyantech.com",\n',
    'endpoint": "https://stg-api': '				"endpoint": "https://api.leyanbot.com/dice/v1"\n',
    'bipolar-prokaryote': '			"endpoint": "https://preview-taobao-bipolar-prokaryote.ftest.leyantech.com/",\n',
    'serviceMode": "http': '		"serviceMode": "https://apiproxy.leyanbot.com/v1/client_info",\n'

}

fishpond_stg_changelist = {
    'ws': '		"endpoint": "wss://stg-agent.leyanbot.com/ws",\n',
    'authority":': '		"authority": "https://stg-api.leyanbot.com/dice/v1",\n',
    'anneau":': '		"anneau": "http://staging-anneau.infra.leyantech.com",\n',
    'endpoint": "https://': '			"endpoint": "https://stg-api.leyanbot.com/dice/v1"\n'
}

fishpond_prd_changelist = {
    'ws': '		"endpoint": "ws://106.12.165.199:8000/ws",\n',
    'authority":': '		"authority": "http://106.12.159.229:8000/dice/v1",\n',
    'anneau":': '		"anneau": "http://180.76.234.49:8000",\n',
    'endpoint": "https://': '			"endpoint": "http://106.12.159.229:8000/dice/v1"\n'
}

mulberry_stg_changelist = {
    'wss': '			"endpoint": "wss://stg-agent.leyanbot.com/ws",\n',
    'authority":': '		"authority": "https://stg-api.ganjutech.com/flashcard/v1/lxk",\n',
    'anneau":': '		"anneau": "http://staging-yx-allele.ftest.leyantech.com",\n',
    'endpoint": "https://': '			"endpoint": "https://stg-api.ganjutech.com/dice/v1",\n'
}

mulberry_prd_changelist = {
    'wss': '			"endpoint": "wss://lxk-agentproxy.ganjutech.com/ws",\n',
    'authority":': '		"authority": "https://api.ganjutech.com/flashcard/v1/lxk",\n',
    'anneau":': '		"anneau": "https://lxk.ganjutech.com",\n',
    'endpoint": "https://': '			"endpoint": "https://api.ganjutech.com/dice/v1",\n'
}
project_map = {0: ['dice', {0: 'stg', 1: 'prd', 2: 'preview'}],
               1: ['fishpond', {0: 'stg', 1: 'prd'}],
               2: ['mulberry', {0: 'stg', 1: 'prd'}]}


# env_map = {0: 'stg', 1: 'prd', 2: 'preview'}


def project_choose(project_name, env_map):
    print(project_name, env_map)
    global env_button
    #### 清空env 单选框
    if env_button:
        for e_b in env_button:
            e_b.destroy()
    ### 根据porject 单选框 设置env 单选框
    for flag in env_map:
        env = Radiobutton(root, text=env_map[flag], variable=v_env, value=flag)
        env.grid(row=1, column=flag + 1)
        env_button.append(env)
    #### 根据project 单选框 修改默认路径
    username = os.getenv('username')
    file_path = 'C:/Users/' + username + '/AppData/Roaming/' + project_name + '/' + project_name + '.json'
    l_default_path.config(text=file_path)
    return file_path


def selectPath():
    ###  获取自定义路径
    path_ = filedialog.askopenfilename()
    path.set(path_)


def action():
    ### 校验自定义路径和默认路径文件是否合法
    project_flag = v_project.get()
    env_flag = v_env.get()
    entry_content = e_path.get()
    default_path = l_default_path['text']
    if len(entry_content) == 0:
        if os.path.isfile(default_path):
            project_path = default_path
            change_profile(project_flag, env_flag, project_path)
        else:
            tk.messagebox.showinfo(title='提示', message="默认路径未找到配置文件")
    else:
        if entry_content.endswith(project_map[project_flag][0] + '.json') and os.path.isfile(entry_content):
            project_path = entry_content
            change_profile(project_flag, env_flag, project_path)
        else:
            tk.messagebox.showinfo(title='提示', message="指定路径未找到配置文件")


def change_profile(project_flag, env_flag, project_path):
    ### 读取配置修改配置文件
    json_path = project_path
    content = open(json_path, 'r', encoding='utf-8').readlines()
    changelist_name = project_map[project_flag][0] + '_' + project_map[project_flag][1][env_flag] + '_changelist'
    print(changelist_name)
    project_env_list = globals()[changelist_name]
    for change in project_env_list:
        for line_con in content:
            if change in line_con:
                line_num = content.index(line_con)
                content[line_num] = project_env_list[change]
    open(json_path, 'w', encoding='utf-8').writelines(content)
    tk.messagebox.showinfo(title='提示', message="配置修改成功！！！")


if __name__ == "__main__":
    root = Tk()
    root.title('修改配置文件')
    root.geometry('500x150+400+200')  # 尺寸位置
    root.minsize(500, 150)  # 最小尺寸
    root.maxsize(500, 150)  # 最大尺寸
    path = StringVar()

    Label(root, text="project:").grid(row=0, column=0)
    v_project = tk.IntVar()  # 设置porject 关联变量
    v_env = tk.IntVar()  # 设置env 关联变量

    p0 = Radiobutton(root, text=project_map[0][0], variable=v_project, value=0,
                     command=lambda: project_choose(project_map[0][0], project_map[0][1])).grid(row=0, column=0 + 1)
    p1 = Radiobutton(root, text=project_map[1][0], variable=v_project, value=1,
                     command=lambda: project_choose(project_map[1][0], project_map[1][1])).grid(row=0, column=1 + 1)
    p2 = Radiobutton(root, text=project_map[2][0], variable=v_project, value=2,
                     command=lambda: project_choose(project_map[2][0], project_map[2][1])).grid(row=0, column=2 + 1)

    Label(root, text="env:").grid(row=1, column=0)
    env_button = []

    ### 自定义路径获取
    l_path = Label(root, text="文件路径:").grid(row=2, column=0)
    # Entry是获取输入
    e_path = Entry(root, textvariable=path, width=50)
    e_path.grid(row=2, column=1, columnspan=4)
    # 操作按钮
    b_path = Button(root, text="选择", command=selectPath).grid(row=2, column=5)

    ### 默认路径显示
    l_default = Label(root, text="default:").grid(row=3, column=0)
    l_default_path = Label(root, text='')
    project_choose(project_map[0][0], project_map[0][1])
    l_default_path.grid(row=3, column=1, columnspan=4)

    b_change = Button(root, text="修改", width=15, command=action).grid(row=4, column=2)

    root.mainloop()
