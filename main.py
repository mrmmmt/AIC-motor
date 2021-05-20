# -*- coding: utf-8 -*-
import create_update0695, create_total_sheet_super
import download_super
from calc_earned_premium import calc_earned_premium
from change_policy_number import change_policy_number_gui
from change_tax import ChangeTax
from tkinter import Tk, Label, StringVar, Button, PhotoImage, Radiobutton, Menu, messagebox
from frozen_dir import app_path
import sys
import os


def about():
    about_info = '版本 2.01\nBuild 20210520\nmrmmmt_ 制作\nE-mail：mmmt123321@126.com'
    messagebox.showinfo('关于', about_info)


def close_the_window():
    global selected_menu_option
    selected_menu_option = False
    window_root.destroy()

def close_the_window_2():
    global selected_menu_option
    selected_menu_option = '计算满期保费'
    window_root.destroy()

def close_the_window_3():
    global selected_menu_option
    selected_menu_option = '0695投保单号修改'
    window_root.destroy()

def close_the_window_4():
    global selected_menu_option
    selected_menu_option = '0695保费（税）修改'
    window_root.destroy()

def my_close():
    # True or False
    res = messagebox.askokcancel('提示', '是否关闭程序')
    if res == True:
        sys.exit(0)


if __name__ == '__main__':

    if not os.path.exists(app_path()+'/汇总表'):
        os.makedirs(app_path()+'/汇总表')

    while True:
        window_root = Tk()
        window_root.title('aic-motor')
        screenWidth = window_root.winfo_screenwidth()  # 获取显示区域的宽度
        screenHeight = window_root.winfo_screenheight()  # 获取显示区域的高度
        width = 300  # 设定窗口宽度
        height = 220  # 设定窗口高度
        left = int((screenWidth - width) / 2)
        top = int((screenHeight - height) / 2)-100
        window_root.geometry('{width}x{height}+{left}+{top}'.format(width=width, height=height, left=left, top=top))
        window_root.resizable(0, 0)  # 设置窗口宽高固定
        # 为右上角的关闭事件添加一个响应函数
        window_root.protocol('WM_DELETE_WINDOW', my_close)
        window_root.iconbitmap(app_path() + '/bin/aic_logo.ico')
        window_root["background"] = "white"
        logo_image_file = PhotoImage(file=app_path()+'/bin/background.png')
        Label(window_root, image=logo_image_file).pack()
        Button(window_root, text='关于', bg='white', bd=0, font=('Msyh', 8), command=about).place(x=270, y=180)
        var_option_select = StringVar()
        Radiobutton(window_root, text='0695批量导入数据生成', bg='white', variable=var_option_select, value='Option_1').place(x=70, y=60)
        Radiobutton(window_root, text='截止每日汇总表生成', bg='white', variable=var_option_select, value='Option_2').place(x=70, y=85)
        Radiobutton(window_root, text='电子保单批量下载', bg='white', variable=var_option_select, value='Option_3').place(x=70, y=110)
        Button(window_root, text='确定', bg='white', width=15, command=close_the_window).place(x=93, y=155)

        ## 菜单栏
        menubar = Menu(window_root)
        window_root.configure(menu=menubar)
        menu_1 = Menu(menubar, tearoff = False)  # 从属于 menubar
        
        menubar.add_cascade(label='Menu', menu=menu_1)
        menu_1.add_cascade(label='计算满期保费', command=close_the_window_2)
        menu_1.add_cascade(label='0695投保单号修改', command=close_the_window_3)
        menu_1.add_cascade(label='0695保费（税）修改', command=close_the_window_4)
        menu_1.add_separator()  # 添加分割线
        menu_1.add_cascade(label='退出程序', command=my_close)

        window_root.mainloop()

        if var_option_select.get() == 'Option_1':
            create_update0695.create_0695update_gui()
        elif var_option_select.get() == 'Option_2':
            create_total_sheet_super.create_total_sheet_gui()
        elif var_option_select.get() == 'Option_3':
            download_super.Download_Policy()
        elif selected_menu_option == '计算满期保费':
            calc_earned_premium()
        elif selected_menu_option == '0695投保单号修改':
            change_policy_number_gui()
        elif selected_menu_option == '0695保费（税）修改':
            ChangeTax()
            
