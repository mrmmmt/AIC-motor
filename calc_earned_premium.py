# -*- coding: utf-8 -*-
import os
import pandas as pd
from frozen_dir import app_path
from datetime import datetime, timedelta
from tkinter import Tk, Label, StringVar, Button, ttk, scrolledtext, END


def print_result(total_sheet_name, selected_date):
    df = pd.read_excel(total_sheet_name, dtype='str')
    df = df.loc[:, ['起保日期', '三责险-保费总计', '驾意险-保费总计', '是否退保', '三责险-退款金额', '驾意险-退款金额']]
    df['起保年份'] = df['起保日期'].str[:4]
    years = list(df['起保年份'].unique())
    years.sort(reverse=False)
    df['起保日期'] = df['起保日期'].apply(pd.to_datetime)
    df['三责险-保费总计'] = df['三责险-保费总计'].apply(pd.to_numeric)
    df['驾意险-保费总计'] = df['驾意险-保费总计'].apply(pd.to_numeric)
    df['三责险-退款金额'] = df['三责险-退款金额'].apply(pd.to_numeric)
    df['驾意险-退款金额'] = df['驾意险-退款金额'].apply(pd.to_numeric)
    df['selected_date'] = selected_date
    df['selected_date'] = df['selected_date'].apply(pd.to_datetime)
    df_cancel = df[df['是否退保'].isin(['是', 'T', 'True', 'TRUE', '退保'])]
    df = df[~df['是否退保'].isin(['是', 'T', 'True', 'TRUE', '退保'])]

    df['已用期数_day'] = (df['selected_date'] - df['起保日期'])
    df['已用期数_day'] = [x.days if x.days <= 365 else 365 for x in df['已用期数_day']]
    df = df[df['已用期数_day'] > 0]
    df['三责险-已赚保费'] = df['三责险-保费总计'] / 365 * df['已用期数_day']
    df['驾意险-已赚保费'] = df['驾意险-保费总计'] / 365 * df['已用期数_day']

    df_cancel['三责险-已赚保费'] = df_cancel['三责险-保费总计'] - df_cancel['三责险-退款金额']
    df_cancel['驾意险-已赚保费'] = df_cancel['驾意险-保费总计'] - df_cancel['驾意险-退款金额']
    
    result = []
    
    for i in range(len(years)):
        df_oneYear = df[df['起保年份']==years[i]]
        df_cancel_oneYear = df_cancel[df_cancel['起保年份']==years[i]]
        result_temp = [
            '-*- {0} 在保保单 -*-'.format(years[i]),
            '三责险-保费总计：{:.2f}'.format(df_oneYear['三责险-保费总计'].sum()),
            '驾意险-保费总计：{:.2f}'.format(df_oneYear['驾意险-保费总计'].sum()),
            '三责险-已赚保费：{:.2f}'.format(df_oneYear['三责险-已赚保费'].sum()),
            '驾意险-已赚保费：{:.2f}'.format(df_oneYear['驾意险-已赚保费'].sum()),
            '总起保单量：{}'.format(df_oneYear.shape[0]),
            '-------------------------------------------',
            '-*- {0} 退保保单 -*-'.format(years[i]),
            '三责险-已赚保费：{:.2f}'.format(df_cancel_oneYear['三责险-已赚保费'].sum()),
            '驾意险-已赚保费：{:.2f}'.format(df_cancel_oneYear['驾意险-已赚保费'].sum()),
            '已退保单量：{}'.format(df_cancel_oneYear.shape[0]),
            '-------------------------------------------',
            '-*- {0} 共计 -*-'.format(years[i]),
            '三责险-已赚保费：{:.2f}'.format(df_oneYear['三责险-已赚保费'].sum() + df_cancel_oneYear['三责险-已赚保费'].sum()),
            '驾意险-已赚保费：{:.2f}'.format(df_oneYear['驾意险-已赚保费'].sum() + df_cancel_oneYear['驾意险-已赚保费'].sum()),
            ''
        ]
    
        result += result_temp
        
    result += [
        '-*- {0} 在保保单 -*-'.format('+'.join(years)),
        '三责险-保费总计：{:.2f}'.format(df['三责险-保费总计'].sum()),
        '驾意险-保费总计：{:.2f}'.format(df['驾意险-保费总计'].sum()),
        '三责险-已赚保费：{:.2f}'.format(df['三责险-已赚保费'].sum()),
        '驾意险-已赚保费：{:.2f}'.format(df['驾意险-已赚保费'].sum()),
        '总起保单量：{}'.format(df.shape[0]),
        '-------------------------------------------',
        '-*- {0} 退保保单 -*-'.format('+'.join(years)),
        '三责险-已赚保费：{:.2f}'.format(df_cancel['三责险-已赚保费'].sum()),
        '驾意险-已赚保费：{:.2f}'.format(df_cancel['驾意险-已赚保费'].sum()),
        '已退保单量：{}'.format(df_cancel.shape[0]),
        '-------------------------------------------',
        '-*- {0} 共计 -*-'.format('+'.join(years)),
        '三责险-已赚保费：{:.2f}'.format(df['三责险-已赚保费'].sum() + df_cancel['三责险-已赚保费'].sum()),
        '驾意险-已赚保费：{:.2f}'.format(df['驾意险-已赚保费'].sum() + df_cancel['驾意险-已赚保费'].sum())
        ]
        
    return result


def print_result_gui():
    window_earned_premium.destroy()
    total_sheet_name, selected_date = app_path() + '/汇总表/' + var_total_sheet_nme.get(), var_cur_date.get()
    window_show_info = Tk()
    screenWidth = window_show_info.winfo_screenwidth()  # 获取显示区域的宽度
    screenHeight = window_show_info.winfo_screenheight()  # 获取显示区域的高度
    width = 300  # 设定窗口宽度
    height = 295  # 设定窗口高度
    left = int((screenWidth - width) / 2)
    top = int((screenHeight - height) / 2)-100
    window_show_info.title('满期保费')
    window_show_info.geometry('{width}x{height}+{left}+{top}'.format(width=width, height=height, left=left, top=top))
    window_show_info.iconbitmap(app_path() + '/bin/aic_logo.ico')
    text = scrolledtext.ScrolledText(window_show_info, font=('微软雅黑', 10), fg='blue')
    text.pack()
    text.insert(END, '\n')
    for info in print_result(total_sheet_name, selected_date):
        text.insert(END, info+'\n')
        window_show_info.update()

    window_show_info.mainloop()
    

def calc_earned_premium():
    global var_total_sheet_nme, var_cur_date, window_earned_premium
    window_earned_premium = Tk()
    window_earned_premium.title('满期保费计算')
    window_earned_premium.resizable(0, 0)  # 设置窗口宽高固定
    window_earned_premium.iconbitmap(app_path() + '/bin/aic_logo.ico')
    screenWidth = window_earned_premium.winfo_screenwidth()  # 获取显示区域的宽度
    screenHeight = window_earned_premium.winfo_screenheight()  # 获取显示区域的高度
    width = 400  # 设定窗口宽度
    height = 150  # 设定窗口高度
    left = int((screenWidth - width) / 2)
    top = int((screenHeight - height) / 2)-100
    window_earned_premium.geometry('{width}x{height}+{left}+{top}'.format(width=width, height=height, left=left, top=top))
    Label(window_earned_premium, text='摩托车汇总表:', font=('Msyh', 12)).place(x=20, y=19)
    Label(window_earned_premium, text='截止日期:', font=('Msyh', 12)).place(x=20, y=55)

    var_total_sheet_nme = StringVar()
    comboxlist = ttk.Combobox(window_earned_premium, width=25, textvariable=var_total_sheet_nme, font=('Msyh', 12))
    list_value = [item for item in os.listdir(app_path() + '/汇总表/') if item.split('.')[-1] == 'xlsx']
    list_value.sort(reverse=True)
    comboxlist["values"] = list_value
    try:
        comboxlist.current(0)
    except:
        pass
    comboxlist.place(x=150,y=20)

    var_cur_date = StringVar()
    comboxlist_2 = ttk.Combobox(window_earned_premium, width=25, textvariable=var_cur_date, font=('Msyh', 12))
    list_value_2 = [datetime.now().strftime('%Y-%m-%d'), (datetime.now()-timedelta(days=1)).strftime('%Y-%m-%d'), (datetime.now()-timedelta(days=2)).strftime('%Y-%m-%d'), (datetime.now()-timedelta(days=3)).strftime('%Y-%m-%d'), (datetime.now()-timedelta(days=4)).strftime('%Y-%m-%d'), (datetime.now()-timedelta(days=5)).strftime('%Y-%m-%d')]
    comboxlist_2["values"] = list_value_2
    comboxlist_2.current(0)
    comboxlist_2.place(x=150,y=56)

    btn_start = Button(window_earned_premium, text='开始计算', command=print_result_gui)
    btn_start.place(x=165, y=100)

    window_earned_premium.mainloop()


if __name__ == '__main__':
    calc_earned_premium()
