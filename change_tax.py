# -*- coding: utf-8 -*-
from frozen_dir import app_path
from tkinter import Tk, Label, StringVar, Button, Entry
import pickle


def change_tax_main():
    tax_dict = dict()
    info_all = round(float(var_info_all.get().strip()), 2)
    info_no_tax = round(float(var_info_no_tax.get().strip()), 2)
    info_tax = round(float(var_info_tax.get().strip()), 2)

    tax_dict['all_0695'] = [info_all, info_no_tax, info_tax]

    with open(app_path()+'/bin/data/tax_info.pkl', 'wb') as f:
        pickle.dump(tax_dict, f)
        
    window_change_tax.destroy()


def change_tax_gui():
    global window_change_tax, var_info_all, var_info_no_tax, var_info_tax

    with open(app_path()+'/bin/data/tax_info.pkl', 'rb') as f:
        tax_dict = pickle.load(f)

    info_all = tax_dict['all_0695'][0]
    info_no_tax = tax_dict['all_0695'][1]
    info_tax = tax_dict['all_0695'][2]

    window_change_tax = Tk()
    window_change_tax.title('更改保费')
    window_change_tax.resizable(0, 0)  # 设置窗口宽高固定
    window_change_tax.iconbitmap(app_path() + '/bin/aic_logo.ico')
    screenWidth = window_change_tax.winfo_screenwidth()  # 获取显示区域的宽度
    screenHeight = window_change_tax.winfo_screenheight()  # 获取显示区域的高度
    width = 300  # 设定窗口宽度
    height = 110  # 设定窗口高度
    left = int((screenWidth - width) / 2)
    top = int((screenHeight - height) / 2)-100
    window_change_tax.geometry('{width}x{height}+{left}+{top}'.format(width=width, height=height, left=left, top=top))
    Label(window_change_tax, text='金额：').place(x=20, y=30)
    Label(window_change_tax, text='含税保费').place(x=76, y=5)
    Label(window_change_tax, text='不含税保费').place(x=140, y=5)
    Label(window_change_tax, text='税额').place(x=227, y=5)

    var_info_all = StringVar(value=info_all)
    Entry(window_change_tax, textvariable=var_info_all, width=6).place(x=80,y=32)
    var_info_no_tax = StringVar(value=info_no_tax)
    Entry(window_change_tax, textvariable=var_info_no_tax, width=6).place(x=150,y=32)
    var_info_tax = StringVar(value=info_tax)
    Entry(window_change_tax, textvariable=var_info_tax, width=6).place(x=220,y=32)

    btn_start = Button(window_change_tax, text='确认', width=10, command=change_tax_main)
    btn_start.place(x=112, y=65)

    window_change_tax.mainloop()


if __name__ == '__main__':
    change_tax_gui()