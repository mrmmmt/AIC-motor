# -*- coding: utf-8 -*-
from frozen_dir import app_path
from tkinter import Tk, Label, StringVar, Button, Entry
from tkinter import END, CENTER
from tkinter import scrolledtext, messagebox
import pickle


class ChangeTax:

    def __init__(self):
        self.change_tax_gui()


    def change_tax_main(self):
        self.info_1['amount_all'] = round(float(self.var_amount_all_1.get().strip()), 2)
        self.info_1['amount_no_tax'] = round(float(self.var_amount_no_tax_1.get().strip()), 2)
        self.info_1['amount_tax'] = round(float(self.var_amount_tax_1.get().strip()), 2)

        self.info_2['amount_all'] = round(float(self.var_amount_all_2.get().strip()), 2)
        self.info_2['amount_no_tax'] = round(float(self.var_amount_no_tax_2.get().strip()), 2)
        self.info_2['amount_tax'] = round(float(self.var_amount_tax_2.get().strip()), 2)

        self.info_3['amount_all'] = round(float(self.var_amount_all_3.get().strip()), 2)
        self.info_3['amount_no_tax'] = round(float(self.var_amount_no_tax_3.get().strip()), 2)
        self.info_3['amount_tax'] = round(float(self.var_amount_tax_3.get().strip()), 2)

        self.info_4['amount_all'] = round(float(self.var_amount_all_4.get().strip()), 2)
        self.info_4['amount_no_tax'] = round(float(self.var_amount_no_tax_4.get().strip()), 2)
        self.info_4['amount_tax'] = round(float(self.var_amount_tax_4.get().strip()), 2)

        self.info_5['amount_all'] = round(float(self.var_amount_all_5.get().strip()), 2)
        self.info_5['amount_no_tax'] = round(float(self.var_amount_no_tax_5.get().strip()), 2)
        self.info_5['amount_tax'] = round(float(self.var_amount_tax_5.get().strip()), 2)

        self.info_6['amount_all'] = round(float(self.var_amount_all_6.get().strip()), 2)
        self.info_6['amount_no_tax'] = round(float(self.var_amount_no_tax_6.get().strip()), 2)
        self.info_6['amount_tax'] = round(float(self.var_amount_tax_6.get().strip()), 2)

        self.info_7['amount_all'] = round(float(self.var_amount_all_7.get().strip()), 2)
        self.info_7['amount_no_tax'] = round(float(self.var_amount_no_tax_7.get().strip()), 2)
        self.info_7['amount_tax'] = round(float(self.var_amount_tax_7.get().strip()), 2)

        self.info_8['amount_all'] = round(float(self.var_amount_all_8.get().strip()), 2)
        self.info_8['amount_no_tax'] = round(float(self.var_amount_no_tax_8.get().strip()), 2)
        self.info_8['amount_tax'] = round(float(self.var_amount_tax_8.get().strip()), 2)

        self.info_9['amount_all'] = round(float(self.var_amount_all_9.get().strip()), 2)
        self.info_9['amount_no_tax'] = round(float(self.var_amount_no_tax_9.get().strip()), 2)
        self.info_9['amount_tax'] = round(float(self.var_amount_tax_9.get().strip()), 2)

        with open(app_path()+'/bin/data/tax_info.pkl', 'rb') as f:
            tax_dict = pickle.load(f)

        tax_dict['amount_1'] = self.info_1
        tax_dict['amount_2'] = self.info_2
        tax_dict['amount_3'] = self.info_3
        tax_dict['amount_4'] = self.info_4
        tax_dict['amount_5'] = self.info_5
        tax_dict['amount_6'] = self.info_6
        tax_dict['amount_7'] = self.info_7
        tax_dict['amount_8'] = self.info_8
        tax_dict['amount_9'] = self.info_9

        with open(app_path()+'/bin/data/tax_info.pkl', 'wb') as f:
            pickle.dump(tax_dict, f)
            
        self.window_change_tax.destroy()


    def close_area_info_window(self, windowName, area_info, flag):
        all_flags = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        all_flags.remove(flag)
        with open(app_path()+'/bin/data/tax_info.pkl', 'rb') as f:
            tax_dict = pickle.load(f)
        temp_lst = []
        areas = area_info.get(1.0, END)
        areas = areas.split('\n')

        for i in range(len(areas)):
            one_item = areas[i].strip()
            if len(one_item) >= 2 and one_item not in temp_lst:
                temp_lst.append(one_item)

        tax_dict['area_{}'.format(flag)] = temp_lst

        for i in range(len(temp_lst)):
            one_item = temp_lst[i]
            for j in all_flags:
                if one_item in tax_dict['area_{}'.format(j)]:
                    messagebox.showinfo('提示', '{0} 已在 地区_{1} 存在'.format(one_item, j))

        with open(app_path()+'/bin/data/tax_info.pkl', 'wb') as f:
            pickle.dump(tax_dict, f)

        windowName.destroy()


    def input_area_info(self, flag):
        with open(app_path()+'/bin/data/tax_info.pkl', 'rb') as f:
            tax_dict = pickle.load(f)
        area_list = tax_dict['area_{}'.format(flag)]
        area_info_window = Tk()
        area_info_window.title('地区 - {}'.format(flag))
        area_info_window.resizable(0, 0)  # 设置窗口宽高固定
        area_info_window.iconbitmap(app_path() + '/bin/aic_logo.ico')
        screenWidth = area_info_window.winfo_screenwidth()  # 获取显示区域的宽度
        screenHeight = area_info_window.winfo_screenheight()  # 获取显示区域的高度
        width = 200  # 设定窗口宽度
        height = 400  # 设定窗口高度
        left = int((screenWidth - width) / 2)
        top = int((screenHeight - height) / 2)-100
        area_info_window.geometry('{width}x{height}+{left}+{top}'.format(width=width, height=height, left=left, top=top))
        area_info = scrolledtext.ScrolledText(area_info_window, width=25, height=30)
        area_info.pack()

        for i in range(len(area_list)):
            area_info.insert(END, '{}\n'.format(area_list[i]))

        # 为右上角的关闭事件添加一个响应函数
        area_info_window.protocol('WM_DELETE_WINDOW', lambda: self.close_area_info_window(area_info_window, area_info, flag))
        area_info_window.iconbitmap(app_path() + '/bin/aic_logo.ico')

        area_info_window.mainloop()


    def change_tax_gui(self):

        with open(app_path()+'/bin/data/tax_info.pkl', 'rb') as f:
            tax_dict = pickle.load(f)

        self.info_1 = tax_dict['amount_1']
        self.info_2 = tax_dict['amount_2']
        self.info_3 = tax_dict['amount_3']
        self.info_4 = tax_dict['amount_4']
        self.info_5 = tax_dict['amount_5']
        self.info_6 = tax_dict['amount_6']
        self.info_7 = tax_dict['amount_7']
        self.info_8 = tax_dict['amount_8']
        self.info_9 = tax_dict['amount_9']

        self.window_change_tax = Tk()
        self.window_change_tax.title('更改保费')
        self.window_change_tax.resizable(0, 0)  # 设置窗口宽高固定
        self.window_change_tax.iconbitmap(app_path() + '/bin/aic_logo.ico')
        screenWidth = self.window_change_tax.winfo_screenwidth()  # 获取显示区域的宽度
        screenHeight = self.window_change_tax.winfo_screenheight()  # 获取显示区域的高度
        width = 315  # 设定窗口宽度
        height = 300  # 设定窗口高度
        left = int((screenWidth - width) / 2)
        top = int((screenHeight - height) / 2)-100
        self.window_change_tax.geometry('{width}x{height}+{left}+{top}'.format(width=width, height=height, left=left, top=top))
        Label(self.window_change_tax, text='金额 - 1：').place(x=15, y=30)
        Label(self.window_change_tax, text='金额 - 2：').place(x=15, y=55)
        Label(self.window_change_tax, text='金额 - 3：').place(x=15, y=80)
        Label(self.window_change_tax, text='金额 - 4：').place(x=15, y=105)
        Label(self.window_change_tax, text='金额 - 5：').place(x=15, y=130)
        Label(self.window_change_tax, text='金额 - 6：').place(x=15, y=155)
        Label(self.window_change_tax, text='金额 - 7：').place(x=15, y=180)
        Label(self.window_change_tax, text='金额 - 8：').place(x=15, y=205)
        Label(self.window_change_tax, text='金额 - 9：').place(x=15, y=230)
        Label(self.window_change_tax, text='含税保费').place(x=76, y=5)
        Label(self.window_change_tax, text='不含税保费').place(x=140, y=5)
        Label(self.window_change_tax, text='税额').place(x=227, y=5)

        self.var_amount_all_1 = StringVar(value=self.info_1['amount_all'])
        Entry(self.window_change_tax, textvariable=self.var_amount_all_1, width=6, justify=CENTER).place(x=80, y=32)
        self.var_amount_no_tax_1 = StringVar(value=self.info_1['amount_no_tax'])
        Entry(self.window_change_tax, textvariable=self.var_amount_no_tax_1, width=6, justify=CENTER).place(x=150, y=32)
        self.var_amount_tax_1 = StringVar(value=self.info_1['amount_tax'])
        Entry(self.window_change_tax, textvariable=self.var_amount_tax_1, width=6, justify=CENTER).place(x=220, y=32)
        Button(self.window_change_tax, text='地区', bd=0, command=lambda: self.input_area_info('1')).place(x=270, y=30)

        self.var_amount_all_2 = StringVar(value=self.info_2['amount_all'])
        Entry(self.window_change_tax, textvariable=self.var_amount_all_2, width=6, justify=CENTER).place(x=80, y=57)
        self.var_amount_no_tax_2 = StringVar(value=self.info_2['amount_no_tax'])
        Entry(self.window_change_tax, textvariable=self.var_amount_no_tax_2, width=6, justify=CENTER).place(x=150, y=57)
        self.var_amount_tax_2 = StringVar(value=self.info_2['amount_tax'])
        Entry(self.window_change_tax, textvariable=self.var_amount_tax_2, width=6, justify=CENTER).place(x=220, y=57)
        Button(self.window_change_tax, text='地区', bd=0, command=lambda: self.input_area_info('2')).place(x=270, y=55)

        self.var_amount_all_3 = StringVar(value=self.info_3['amount_all'])
        Entry(self.window_change_tax, textvariable=self.var_amount_all_3, width=6, justify=CENTER).place(x=80,y=82)
        self.var_amount_no_tax_3 = StringVar(value=self.info_3['amount_no_tax'])
        Entry(self.window_change_tax, textvariable=self.var_amount_no_tax_3, width=6, justify=CENTER).place(x=150,y=82)
        self.var_amount_tax_3 = StringVar(value=self.info_3['amount_tax'])
        Entry(self.window_change_tax, textvariable=self.var_amount_tax_3, width=6, justify=CENTER).place(x=220,y=82)
        Button(self.window_change_tax, text='地区', bd=0, command=lambda: self.input_area_info('3')).place(x=270, y=80)

        self.var_amount_all_4 = StringVar(value=self.info_4['amount_all'])
        Entry(self.window_change_tax, textvariable=self.var_amount_all_4, width=6, justify=CENTER).place(x=80,y=107)
        self.var_amount_no_tax_4 = StringVar(value=self.info_4['amount_no_tax'])
        Entry(self.window_change_tax, textvariable=self.var_amount_no_tax_4, width=6, justify=CENTER).place(x=150,y=107)
        self.var_amount_tax_4 = StringVar(value=self.info_4['amount_tax'])
        Entry(self.window_change_tax, textvariable=self.var_amount_tax_4, width=6, justify=CENTER).place(x=220,y=107)
        Button(self.window_change_tax, text='地区', bd=0, command=lambda: self.input_area_info('4')).place(x=270, y=105)

        self.var_amount_all_5 = StringVar(value=self.info_5['amount_all'])
        Entry(self.window_change_tax, textvariable=self.var_amount_all_5, width=6, justify=CENTER).place(x=80,y=132)
        self.var_amount_no_tax_5 = StringVar(value=self.info_5['amount_no_tax'])
        Entry(self.window_change_tax, textvariable=self.var_amount_no_tax_5, width=6, justify=CENTER).place(x=150,y=132)
        self.var_amount_tax_5 = StringVar(value=self.info_5['amount_tax'])
        Entry(self.window_change_tax, textvariable=self.var_amount_tax_5, width=6, justify=CENTER).place(x=220,y=132)
        Button(self.window_change_tax, text='地区', bd=0, command=lambda: self.input_area_info('5')).place(x=270, y=130)

        self.var_amount_all_6 = StringVar(value=self.info_6['amount_all'])
        Entry(self.window_change_tax, textvariable=self.var_amount_all_6, width=6, justify=CENTER).place(x=80,y=157)
        self.var_amount_no_tax_6 = StringVar(value=self.info_6['amount_no_tax'])
        Entry(self.window_change_tax, textvariable=self.var_amount_no_tax_6, width=6, justify=CENTER).place(x=150,y=157)
        self.var_amount_tax_6 = StringVar(value=self.info_6['amount_tax'])
        Entry(self.window_change_tax, textvariable=self.var_amount_tax_6, width=6, justify=CENTER).place(x=220,y=157)
        Button(self.window_change_tax, text='地区', bd=0, command=lambda: self.input_area_info('6')).place(x=270, y=155)

        self.var_amount_all_7 = StringVar(value=self.info_7['amount_all'])
        Entry(self.window_change_tax, textvariable=self.var_amount_all_7, width=6, justify=CENTER).place(x=80,y=182)
        self.var_amount_no_tax_7 = StringVar(value=self.info_7['amount_no_tax'])
        Entry(self.window_change_tax, textvariable=self.var_amount_no_tax_7, width=6, justify=CENTER).place(x=150,y=182)
        self.var_amount_tax_7 = StringVar(value=self.info_7['amount_tax'])
        Entry(self.window_change_tax, textvariable=self.var_amount_tax_7, width=6, justify=CENTER).place(x=220,y=182)
        Button(self.window_change_tax, text='地区', bd=0, command=lambda: self.input_area_info('7')).place(x=270, y=180)

        self.var_amount_all_8 = StringVar(value=self.info_8['amount_all'])
        Entry(self.window_change_tax, textvariable=self.var_amount_all_8, width=6, justify=CENTER).place(x=80,y=207)
        self.var_amount_no_tax_8 = StringVar(value=self.info_8['amount_no_tax'])
        Entry(self.window_change_tax, textvariable=self.var_amount_no_tax_8, width=6, justify=CENTER).place(x=150,y=207)
        self.var_amount_tax_8 = StringVar(value=self.info_8['amount_tax'])
        Entry(self.window_change_tax, textvariable=self.var_amount_tax_8, width=6, justify=CENTER).place(x=220,y=207)
        Button(self.window_change_tax, text='地区', bd=0, command=lambda: self.input_area_info('8')).place(x=270, y=205)

        self.var_amount_all_9 = StringVar(value=self.info_9['amount_all'])
        Entry(self.window_change_tax, textvariable=self.var_amount_all_9, width=6, justify=CENTER).place(x=80,y=232)
        self.var_amount_no_tax_9 = StringVar(value=self.info_9['amount_no_tax'])
        Entry(self.window_change_tax, textvariable=self.var_amount_no_tax_9, width=6, justify=CENTER).place(x=150,y=232)
        self.var_amount_tax_9 = StringVar(value=self.info_9['amount_tax'])
        Entry(self.window_change_tax, textvariable=self.var_amount_tax_9, width=6, justify=CENTER).place(x=220,y=232)
        Button(self.window_change_tax, text='地区', bd=0, command=lambda: self.input_area_info('9')).place(x=270, y=230)

        btn_start = Button(self.window_change_tax, text='确认', width=10, command=self.change_tax_main)
        btn_start.place(x=112, y=260)

        self.window_change_tax.mainloop()


if __name__ == '__main__':
    ChangeTax()