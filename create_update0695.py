# -*- coding: utf-8 -*-
import pandas as pd
from datetime import datetime
import pickle, os
from get_info_from_IDcard import get_info_from_IDcard
import xlrd
import xlutils.copy
from frozen_dir import app_path
from tkinter import CENTER, Tk, Label, StringVar, Button, ttk, messagebox
from simple_province import simple_province2whole
import area2province


def upper_value(df):
    for column in df.columns:
        df[column] = df[column].str.upper().str.strip()
        
    return df


def create_local_raw_df(individual_local_df_name, company_local_df_name):
    '''输入平台发来公户表和个人表 返回有需要字段的合并表'''
    if individual_local_df_name.split('.')[-1] in ['xls', 'xlsx']:
        individual_local_df = pd.read_excel(individual_local_df_name, dtype='str')
        individual_local_df = individual_local_df.loc[:, ['被保人身份证号', '省份', '发动机号', '车险保额（万元）']]
        individual_local_df = individual_local_df.rename(columns={'省份':'地区'})
        individual_local_df = upper_value(individual_local_df)
        individual_local_df['车险保额（万元）'] = individual_local_df['车险保额（万元）'].str.replace('万', '').str.replace('元', '')
        individual_local_df['车辆所属性质'] = '个人'
    else:
        individual_local_df = pd.DataFrame(columns=['被保人身份证号', '地区', '发动机号', '车险保额（万元）', '车辆所属性质'])

    if company_local_df_name.split('.')[-1] in ['xls', 'xlsx']:
        company_local_df = pd.read_excel(company_local_df_name, dtype='str')
        for column in company_local_df.columns:
            if '保额' in column:
                company_local_df = company_local_df.rename(columns={column:'车险保额（万元）', '企业地址（10个字以上）':'地区'})

        company_local_df = company_local_df.loc[:, ['被保人身份证号', '地区', '发动机号', '车险保额（万元）']]
        company_local_df = upper_value(company_local_df)
        company_local_df['车险保额（万元）'] = company_local_df['车险保额（万元）'].str.replace('万', '').str.replace('元', '')
        company_local_df['车辆所属性质'] = '企业'
    else:
        company_local_df = pd.DataFrame(columns=['被保人身份证号', '地区', '发动机号', '车险保额（万元）', '车辆所属性质'])

    return pd.concat([individual_local_df, company_local_df], ignore_index=True)


def create_merge_df(local_raw_df, plywrite_file_name):
    '''输入本地合并表（个人+公户）表和车险核心调出表 输出匹配结果'''
    local_raw_df = local_raw_df.fillna('*')
    plywrite_df = pd.read_excel(plywrite_file_name, dtype='str')
    plywrite_df = plywrite_df.fillna('NAN')
    plywrite_df = upper_value(plywrite_df)
    
    plywrite_df = plywrite_df[plywrite_df['批单号'] == 'NAN']
    plywrite_df = plywrite_df.loc[:, ['投保人',
                                      '保单号',
                                      '被保人', 
                                      '证件后4位', 
                                      '手机', 
                                      '投保联系人',
                                      '保险起期', 
                                      '保险止期', 
                                      '缴费日期', 
                                      '保费(变化)',
                                      '承保机构代码',
                                      '代理渠道',
                                      '车牌号', 
                                      '车型名称', 
                                      '车架号',
                                      '发动机号', 
                                      '车辆类型']]
    plywrite_df = plywrite_df.rename(columns={'保单号':'保单号_0366', '缴费日期':'订单时间_0366', '保费(变化)':'保费_0366'})

    df = pd.merge(local_raw_df, plywrite_df, on='发动机号', how='left')
    df['证件后4位_本地'] = [str(x)[-4:] for x in df['被保人身份证号']]
    df['flag'] = (df['证件后4位_本地'] == df['证件后4位'])
    df_erro = df[df['flag'] != True]
    if df_erro.shape[0] > 0:
        erro_moto_lst = list(df_erro['发动机号'])
        df_erro = df_erro.loc[:, ['被保人', '被保人身份证号', '地区', '发动机号', '车险保额（万元）', '车辆所属性质', '投保人', '保单号_0366', '手机', '投保联系人', '保险起期', '保险止期', '订单时间_0366', '保费_0366', '承保机构代码', '代理渠道', '车牌号', '车型名称', '车架号', '车辆类型', '证件后4位', '证件后4位_本地']]
        df_erro.to_excel(app_path()+'/erro_{}.xlsx'.format(datetime.now().strftime('%Y%m%d')), index=None)
        raise ValueError('发动机号 '+str(erro_moto_lst)+' 匹配数据发生错误')
    else:
        df = df.drop(['证件后4位_本地', '证件后4位', 'flag'], axis=1)
        df.index = range(df.shape[0])

    temp = []
    for i in df.index:
        if len(df['车牌号'][i]) == 7:
            temp.append(simple_province2whole(df['车牌号'][i][0]))
        else:
            temp.append(area2province.get_province_from_info(df['地区'][i]))
    df['地区'] = temp
        
    return df


def create_result_df(df_merge, columns_pkl_nme): 
    global three_wheel_alert_flag
    with open(columns_pkl_nme, 'rb') as f:
        need_columns = pickle.load(f)

    genderLst, birthdayLst = get_info_from_IDcard(df_merge['被保人身份证号'])

    df_check_2_or_3 = df_merge.loc[:, ['车架号', '车型名称']]
    df_check_2_or_3['类型'] = ['三轮' if '三轮' in x else '二轮' for x in list(df_check_2_or_3['车型名称'])]
    df_check_2_or_3 = df_check_2_or_3[df_check_2_or_3['类型']=='三轮']
    if df_check_2_or_3.shape[0] > 0 and three_wheel_alert_flag == 0:
        df_check_2_or_3.to_excel(app_path()+'/三轮_{}.xlsx'.format(datetime.now().strftime('%Y%m%d')), index=None)
        info = '车架号 {} 为三轮车型，请核实！'.format(list(df_check_2_or_3['车架号']))
        messagebox.showinfo('提示', info)
        three_wheel_alert_flag = 1

    with open(app_path() + '/bin/data/temp_0366_{}.pkl'.format(datetime.now().strftime('%Y%m%d')), 'wb') as f:
        pickle.dump(df_merge, f)

    df = pd.DataFrame(columns = need_columns)
    df['B']  = df_merge['被保人']  # 投保人姓名
    df['C']  = '居民身份证_个人'  # 证件类型
    df['D']  = df_merge['被保人身份证号']  # 证件号码
    df['E']  = '本人'  # 与被保险人关系
    df['F']  = genderLst  # 性别
    df['G']  = birthdayLst  # 出生日期
    df['H']  = df_merge['保险起期'].apply(pd.to_datetime).map(lambda x: (str(x)[:10]).replace('/', '-'))  # 起保日期
    df['I']  = df_merge['保险止期'].apply(pd.to_datetime).map(lambda x: (str(x)[:10]).replace('/', '-'))   # 终保日期
    df['K'] = df_merge['地区']  # 通讯地址
    df['Q']  = df_merge['被保人']  # 被保险人姓名
    df['R']  = '居民身份证_个人'  # 证件类型
    df['S']  = df_merge['被保人身份证号']  # 证件号码
    df['T']  = '本人'  # 与投保险人关系
    df['U'] = 'CHN'  # 国籍
    df['Y']  = df_merge['车架号']  # 车架号
    df['AE'] = '0101001'  # 职业代码
    df['BW'] = '是' # 投保人对保险标的是否具有保险利益
    df['CF'] = '摩托车'  # 商品类型
    df['CG'] = df_merge['车型名称']  # 商品型号  
    df = df.fillna('NULL_VALUE')
    df['A']  = [str(int(x)) for x in range(1, df.shape[0]+1)]  # 序号
    
    return df


def create_output(individual_local_df_name, company_local_df_name, plywrite_file_name, columns_pkl_nme, save_name, area_list):
    #指定原始excel路径
    filepath = app_path() + '/bin/data/model_EIZ_AIC_01.xls'
    
    local_raw_df = create_local_raw_df(individual_local_df_name, company_local_df_name)
    df_merge = create_merge_df(local_raw_df, plywrite_file_name)
    df = create_result_df(df_merge, columns_pkl_nme)
    df = df[df['K'].isin(area_list)]

    df.columns = list(range(df.shape[1]))
    df.index = list(range(df.shape[0]))
    rb = xlrd.open_workbook(filepath, formatting_info=True)
    #创建一个可写入的副本
    wb = xlutils.copy.copy(rb)

    outSheet = wb.get_sheet(0)

    for row in range(4, df.shape[0]+4):
        for raw_col in range(df.shape[1]):
            value = str(df[raw_col][row-4]).strip()
            if value != 'NULL_VALUE':
                outSheet.write(row, raw_col, value)
            else:
                pass

    wb.save(save_name)


def create_0695update_main():
    try:
        individual_local_df_name = app_path() + '/' + var_individual_local_df_name.get()
        company_local_df_name = app_path() + '/' + var_company_local_df_name.get()
        plywrite_file_name = app_path() + '/' + var_plywrite_file_name.get()
        columns_pkl_nme = app_path() + '/bin/data/columns.pkl'
        with open(app_path()+'/bin/data/tax_info.pkl', 'rb') as f:
            tax_dict = pickle.load(f)
        info = '保存路径：\n'
        for flag in range(1, 10):
            area_list = tax_dict['area_{}'.format(flag)]
            if len(area_list) > 0:
                save_name = app_path() + '/0695批量导入/' + '导入数据{0}_{1}.xls'.format(datetime.now().strftime('%Y%m%d%H%M'), str(flag).zfill(2))
                create_output(individual_local_df_name, company_local_df_name, plywrite_file_name, columns_pkl_nme, save_name, area_list)
                info += save_name + '\n'
        info = info.strip()
        messagebox.showinfo('处理成功!', info)
    except Exception as e:
        info = '错误原因：' + str(e)
        messagebox.showerror('Error', info)


def create_0695update_gui():
    global window_0695update, var_individual_local_df_name, var_company_local_df_name, var_plywrite_file_name, three_wheel_alert_flag

    if not os.path.exists(app_path() + '/0695批量导入'):
        os.makedirs(app_path() + '/0695批量导入')

    three_wheel_alert_flag = 0
    window_0695update = Tk()
    window_0695update.title('摩托车0695批量导入数据处理')
    window_0695update.resizable(0, 0)  # 设置窗口宽高固定
    window_0695update.iconbitmap(app_path() + '/bin/aic_logo.ico')
    screenWidth = window_0695update.winfo_screenwidth()  # 获取显示区域的宽度
    screenHeight = window_0695update.winfo_screenheight()  # 获取显示区域的高度
    width = 460  # 设定窗口宽度
    height = 180  # 设定窗口高度
    left = int((screenWidth - width) / 2)
    top = int((screenHeight - height) / 2)-100
    window_0695update.geometry('{width}x{height}+{left}+{top}'.format(width=width, height=height, left=left, top=top))
    Label(window_0695update, text='个人投保记录文件（平台）:').place(x=30, y=20)
    Label(window_0695update, text='公户投保记录文件（平台）:').place(x=30, y=50)
    Label(window_0695update, text='当日出单台账  （新核心）:').place(x=30, y=80)
    # 个人投保记录文件（平台）
    var_individual_local_df_name = StringVar()
    comboxlist = ttk.Combobox(window_0695update, width=30, textvariable=var_individual_local_df_name, justify=CENTER)
    list_value = [item for item in os.listdir(app_path()) if item.split('.')[-1] in ['xls', 'xlsx']]
    list_value.sort(reverse=True)
    list_value.insert(0, '------------None------------')
    comboxlist["values"] = list_value
    try:
        for i, value in enumerate(list_value):
            if '个人' in value:
                comboxlist.current(i)
                break
    except:
        comboxlist.current(0)

    comboxlist.place(x=190,y=22)

    # 公户投保记录文件（平台）
    var_company_local_df_name = StringVar()
    comboxlist_2 = ttk.Combobox(window_0695update, width=30, textvariable=var_company_local_df_name, justify=CENTER)
    list_value_2 = [item for item in os.listdir(app_path()) if item.split('.')[-1] in ['xls', 'xlsx']]
    list_value_2.sort(reverse=True)
    list_value_2.insert(0, '------------None------------')
    comboxlist_2["values"] = list_value_2
    try:
        for i, value in enumerate(list_value):
            if '企业' in value or '公户' in value:
                comboxlist_2.current(i)
                break
    except:
        comboxlist_2.current(0)

    comboxlist_2.place(x=190,y=52)

    # 车险核心调出表
    var_plywrite_file_name = StringVar()
    comboxlist_3 = ttk.Combobox(window_0695update, width=30, textvariable=var_plywrite_file_name, justify=CENTER)
    list_value_3 = [item for item in os.listdir(app_path()) if item.split('.')[-1] in ['xls', 'xlsx']]
    list_value_3.sort(reverse=True)
    comboxlist_3["values"] = list_value_3
    try:
        for i, value in enumerate(list_value_3):
            if 'plywrite' in value:
                comboxlist_3.current(i)
                break
    except:
        pass

    comboxlist_3.place(x=190,y=82)

    # 开始处理 按钮
    btn_start = Button(window_0695update, text='开始处理', command=create_0695update_main)
    btn_start.place(x=200, y=130)

    # 主窗口循环显示
    window_0695update.mainloop()

if __name__ == '__main__':
    create_0695update_gui()