# -*- coding: utf-8 -*-
from frozen_dir import app_path
from tkinter import Tk, Label, StringVar, Button, Entry
import pickle


def change_policy_number_main():
    policy_number_dict = dict()
    policy_number_dict['all_0695'] = var_all_0695.get().strip()
    with open(app_path()+'/bin/data/policy_number.pkl', 'wb') as f:
        pickle.dump(policy_number_dict, f)
        
    window_change_policy_number.destroy()


def change_policy_number_gui():
    global var_all_0695, window_change_policy_number

    with open(app_path()+'/bin/data/policy_number.pkl', 'rb') as f:
        policy_number_dict = pickle.load(f)

    all_0695 = policy_number_dict['all_0695']

    window_change_policy_number = Tk()
    window_change_policy_number.title('更改投保单号')
    window_change_policy_number.resizable(0, 0)  # 设置窗口宽高固定
    window_change_policy_number.iconbitmap(app_path() + '/bin/aic_logo.ico')
    screenWidth = window_change_policy_number.winfo_screenwidth()  # 获取显示区域的宽度
    screenHeight = window_change_policy_number.winfo_screenheight()  # 获取显示区域的高度
    width = 300  # 设定窗口宽度
    height = 100  # 设定窗口高度
    left = int((screenWidth - width) / 2)
    top = int((screenHeight - height) / 2)-100
    window_change_policy_number.geometry('{width}x{height}+{left}+{top}'.format(width=width, height=height, left=left, top=top))
    Label(window_change_policy_number, text='投保单号：').place(x=20, y=19)

    var_all_0695 = StringVar(value=all_0695)
    Entry(window_change_policy_number, textvariable=var_all_0695, width=25).place(x=90,y=20)

    btn_start = Button(window_change_policy_number, text='确认', width=10, command=change_policy_number_main)
    btn_start.place(x=112, y=55)

    window_change_policy_number.mainloop()


if __name__ == '__main__':
    change_policy_number_gui()