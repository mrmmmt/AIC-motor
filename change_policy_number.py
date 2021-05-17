# -*- coding: utf-8 -*-
from frozen_dir import app_path
from tkinter import Tk, Label, StringVar, Button, Entry, CENTER
import pickle


def change_policy_number_main():
    policy_number_dict = dict()
    policy_number_dict['all_0695_1'] = var_all_0695_1.get().strip()
    policy_number_dict['all_0695_2'] = var_all_0695_2.get().strip()
    policy_number_dict['all_0695_3'] = var_all_0695_3.get().strip()
    policy_number_dict['all_0695_4'] = var_all_0695_4.get().strip()
    policy_number_dict['all_0695_5'] = var_all_0695_5.get().strip()
    policy_number_dict['all_0695_6'] = var_all_0695_6.get().strip()
    policy_number_dict['all_0695_7'] = var_all_0695_7.get().strip()
    policy_number_dict['all_0695_8'] = var_all_0695_8.get().strip()
    policy_number_dict['all_0695_9'] = var_all_0695_9.get().strip()

    with open(app_path()+'/bin/data/policy_number.pkl', 'wb') as f:
        pickle.dump(policy_number_dict, f)
        
    window_change_policy_number.destroy()


def change_policy_number_gui():
    global var_all_0695_1, var_all_0695_2, var_all_0695_3, var_all_0695_4, var_all_0695_5, var_all_0695_6, var_all_0695_7, var_all_0695_8, var_all_0695_9, window_change_policy_number

    with open(app_path()+'/bin/data/policy_number.pkl', 'rb') as f:
        policy_number_dict = pickle.load(f)

    all_0695_1 = policy_number_dict['all_0695_1']
    all_0695_2 = policy_number_dict['all_0695_2']
    all_0695_3 = policy_number_dict['all_0695_3']
    all_0695_4 = policy_number_dict['all_0695_4']
    all_0695_5 = policy_number_dict['all_0695_5']
    all_0695_6 = policy_number_dict['all_0695_6']
    all_0695_7 = policy_number_dict['all_0695_7']
    all_0695_8 = policy_number_dict['all_0695_8']
    all_0695_9 = policy_number_dict['all_0695_9']

    window_change_policy_number = Tk()
    window_change_policy_number.title('更改投保单号')
    window_change_policy_number.resizable(0, 0)  # 设置窗口宽高固定
    window_change_policy_number.iconbitmap(app_path() + '/bin/aic_logo.ico')
    screenWidth = window_change_policy_number.winfo_screenwidth()  # 获取显示区域的宽度
    screenHeight = window_change_policy_number.winfo_screenheight()  # 获取显示区域的高度
    width = 310  # 设定窗口宽度
    height = 280  # 设定窗口高度
    left = int((screenWidth - width) / 2)
    top = int((screenHeight - height) / 2)-100
    window_change_policy_number.geometry('{width}x{height}+{left}+{top}'.format(width=width, height=height, left=left, top=top))
    Label(window_change_policy_number, text='投保单号 - 1：').place(x=20, y=19)
    Label(window_change_policy_number, text='投保单号 - 2：').place(x=20, y=39)
    Label(window_change_policy_number, text='投保单号 - 3：').place(x=20, y=59)
    Label(window_change_policy_number, text='投保单号 - 4：').place(x=20, y=79)
    Label(window_change_policy_number, text='投保单号 - 5：').place(x=20, y=99)
    Label(window_change_policy_number, text='投保单号 - 6：').place(x=20, y=119)
    Label(window_change_policy_number, text='投保单号 - 7：').place(x=20, y=139)
    Label(window_change_policy_number, text='投保单号 - 8：').place(x=20, y=159)
    Label(window_change_policy_number, text='投保单号 - 9：').place(x=20, y=179)

    var_all_0695_1 = StringVar(value=all_0695_1)
    Entry(window_change_policy_number, textvariable=var_all_0695_1, width=25, justify=CENTER).place(x=105,y=20)

    var_all_0695_2 = StringVar(value=all_0695_2)
    Entry(window_change_policy_number, textvariable=var_all_0695_2, width=25, justify=CENTER).place(x=105,y=40)

    var_all_0695_3 = StringVar(value=all_0695_3)
    Entry(window_change_policy_number, textvariable=var_all_0695_3, width=25, justify=CENTER).place(x=105,y=60)

    var_all_0695_4 = StringVar(value=all_0695_4)
    Entry(window_change_policy_number, textvariable=var_all_0695_4, width=25, justify=CENTER).place(x=105,y=80)

    var_all_0695_5 = StringVar(value=all_0695_5)
    Entry(window_change_policy_number, textvariable=var_all_0695_5, width=25, justify=CENTER).place(x=105,y=100)

    var_all_0695_6 = StringVar(value=all_0695_6)
    Entry(window_change_policy_number, textvariable=var_all_0695_6, width=25, justify=CENTER).place(x=105,y=120)

    var_all_0695_7 = StringVar(value=all_0695_7)
    Entry(window_change_policy_number, textvariable=var_all_0695_7, width=25, justify=CENTER).place(x=105,y=140)

    var_all_0695_8 = StringVar(value=all_0695_8)
    Entry(window_change_policy_number, textvariable=var_all_0695_8, width=25, justify=CENTER).place(x=105,y=160)

    var_all_0695_9 = StringVar(value=all_0695_9)
    Entry(window_change_policy_number, textvariable=var_all_0695_9, width=25, justify=CENTER).place(x=105,y=180)

    btn_start = Button(window_change_policy_number, text='确认', width=10, command=change_policy_number_main)
    btn_start.place(x=112, y=220)

    window_change_policy_number.mainloop()


if __name__ == '__main__':
    change_policy_number_gui()