import requests
from frozen_dir import app_path
import os
import pandas as pd
import time
from tkinter import Tk, messagebox, Label, StringVar, Button, ttk, scrolledtext, END
# from create_pretty import create_pretty_result
import shutil
import threading
import queue


class Download_Policy:

    def __init__(self):
        self.download_erro_lst = []
        self.download_finish_count = 0
        self.main()


    def download_by_policyId(self, name, plyNo, date_name):
        url = 'http://www.alltrust.com.cn/person/download/policyId/{}'.format(plyNo)

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Host': 'www.alltrust.com.cn',
            'Referer': 'http://www.alltrust.com.cn/new/policyAndClaim/query/type/policy/index',
            'Upgrade-Insecure-Requests': '1', 
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
        }

        root_dir = app_path()

        if plyNo[5:9] == '0692' or plyNo[5:9] == '0695':
            dirnames = root_dir + '/电子保单/电子保单{}/意外险/'.format(date_name.replace('-', ''))
        else:
            dirnames = root_dir + '/电子保单/电子保单{}/三责险/'.format(date_name.replace('-', ''))

        save_name = dirnames + name + '-' + plyNo + '.pdf'
        start_time = time.time()
        while True:
            if time.time() - start_time > 30:
                self.download_erro_lst.append(name + '-' + plyNo + '.pdf' + '  下载超时')
                os.remove(dirnames + name + '-' + plyNo + '.pdf')
                flag = '失败'
                break
            r = requests.get(url, headers=headers)
            with open(save_name, 'wb') as code:
                code.write(r.content)
            if os.path.getsize(save_name) > 150000:
                flag = '成功'
                break
        
        self.mutex_lock.acquire()
        self.download_finish_count += 1
        self.text.insert(END, '{0}/{1} {2}  {3}-{4}.pdf'.format(self.download_finish_count, self.df_need.shape[0], flag, name, plyNo)+'\n')
        self.text.see(END)
        self.window_download_info.update()
        self.mutex_lock.release()
        if self.download_finish_count == self.df_need.shape[0]:
            self.text.insert(END, '\n下载完成，共下载{}单，{}单下载超时，共耗时{:.2f}秒'.format(self.df_need.shape[0], len(self.download_erro_lst), time.time()-self.start_time)+'\n')
            self.text.see(END)
            self.window_download_info.update()
            if len(self.download_erro_lst) > 0:
                for i, download_erro_info in enumerate(self.download_erro_lst):
                    self.text.insert(END, str(i+1)+'  '+download_erro_info+'\n')
                    self.text.see(END)
                    self.window_download_info.update()

            info = '保存路径: ' + app_path() + '/电子保单'
            date_selected = self.var_date_name.get()
            os.chdir(app_path() + '/电子保单')
            shutil.make_archive('./电子保单{}'.format(date_selected.replace('-', '')), 'zip', base_dir='./电子保单{}'.format(date_selected.replace('-', '')))
            shutil.rmtree('./电子保单{}'.format(date_selected.replace('-', '')))
            messagebox.showinfo('下载完成', info)


    def download_one_time(self):
        while (not self.index_queue.empty()):
            index = self.index_queue.get()
            self.download_by_policyId(name=self.df_need['被保人姓名'][index], plyNo=self.df_need['保单号'][index], date_name=self.df_need['投保日期'][index])


    def choose_file_window(self):
        '''选择汇总表文件'''
        self.window_choose_file = Tk()
        screenWidth = self.window_choose_file.winfo_screenwidth()  # 获取显示区域的宽度
        screenHeight = self.window_choose_file.winfo_screenheight()  # 获取显示区域的高度
        width = 283  # 设定窗口宽度
        height = 80  # 设定窗口高度
        left = int((screenWidth - width) / 2)
        top = int((screenHeight - height) / 2)-100
        self.window_choose_file.title('选择汇总表文件')
        self.window_choose_file.resizable(0, 0)  # 设置窗口宽高固定
        self.window_choose_file.iconbitmap(app_path() + '/bin/aic_logo.ico')
        self.window_choose_file.geometry('{width}x{height}+{left}+{top}'.format(width=width, height=height, left=left, top=top))  # 设定窗口的大小及位置
        self.var_total_sheet_name = StringVar()
        comboxlist = ttk.Combobox(self.window_choose_file, width=30, textvariable=self.var_total_sheet_name, font=('Msyh', 12))
        list_value = [item for item in os.listdir(app_path() + '/汇总表/') if item.split('.')[-1] == 'xlsx']
        list_value.sort(reverse=True)
        comboxlist['values'] = list_value
        try:
            comboxlist.current(0)
        except:
            pass

        comboxlist.place(x=10, y=13)
        Button(self.window_choose_file, text='确定', width=15, command=self.choose_date_window).place(x=80,y=42)
        self.window_choose_file.mainloop()


    def choose_date_window(self):
        '''选择需要的投保日期'''
        self.window_choose_file.destroy()

        total_sheet_name = self.var_total_sheet_name.get()
        df = pd.read_excel(app_path() + '/汇总表/' + total_sheet_name, dtype='str', sheet_name='承保信息汇总')
        df = df[~df['是否退保'].isin(['是', 'T', 'True', 'TRUE', '退保'])]
        self.df = df.loc[:, ['被保人姓名', '三责险-保单号', '驾意险-保单号', '投保日期']]
        unique_date = list(self.df['投保日期'].unique())
        unique_date.sort(reverse=True)
        self.window_choose_date = Tk()
        screenWidth = self.window_choose_date.winfo_screenwidth()  # 获取显示区域的宽度
        screenHeight = self.window_choose_date.winfo_screenheight()  # 获取显示区域的高度
        width = 283  # 设定窗口宽度
        height = 80  # 设定窗口高度
        left = int((screenWidth - width) / 2)
        top = int((screenHeight - height) / 2)-100
        self.window_choose_date.title('选择投保日期')
        self.window_choose_date.resizable(0, 0)  # 设置窗口宽高固定
        self.window_choose_date.iconbitmap(app_path() + '/bin/aic_logo.ico')
        self.window_choose_date.geometry('{width}x{height}+{left}+{top}'.format(width=width, height=height, left=left, top=top))
        self.var_date_name = StringVar()
        comboxlist = ttk.Combobox(self.window_choose_date, width=30, textvariable=self.var_date_name, font=('Msyh', 12))
        comboxlist["values"] = unique_date
        try:
            comboxlist.current(0)
        except:
            pass

        comboxlist.place(x=10,y=13)
        Button(self.window_choose_date, text='确定', width=15, command=self.download_info_window).place(x=80, y=42)
        self.window_choose_date.mainloop()


    def download_multi(self, thread_num=10):
        self.index_queue = queue.Queue(self.df_need.shape[0])
        for index in self.df_need.index:
            self.index_queue.put(index)
        
        self.mutex_lock = threading.Lock()
        for i in range(thread_num):  # 线程数
            t = threading.Thread(target=self.download_one_time, name='LoopThread' + str(i))
            t.setDaemon(True)
            t.start()


    def download_info_window(self):
        
        self.window_choose_date.destroy()

        date_selected = self.var_date_name.get()

        # create_pretty_result(app_path() + '/汇总表/' + self.var_total_sheet_name.get(), date_selected, app_path()+'/{}汇总.xlsx'.format(date_selected))
        df_need = self.df[self.df['投保日期']==date_selected]
        df_need_0366 = df_need.loc[:, ['被保人姓名', '三责险-保单号', '投保日期']]
        df_need_0695 = df_need.loc[:, ['被保人姓名', '驾意险-保单号', '投保日期']]
        df_need_0366 = df_need_0366.rename(columns={'三责险-保单号':'保单号'})
        df_need_0695 = df_need_0695.rename(columns={'驾意险-保单号':'保单号'})

        root_dir = app_path()
        save_dir_0695 = root_dir + '/电子保单/电子保单{}/意外险/'.format(date_selected.replace('-', ''))
        if not os.path.exists(save_dir_0695):
            os.makedirs(save_dir_0695)
        save_dir_0366 = root_dir + '/电子保单/电子保单{}/三责险/'.format(date_selected.replace('-', ''))
        if not os.path.exists(save_dir_0366):
            os.makedirs(save_dir_0366)
        
        self.df_need = pd.concat([df_need_0366, df_need_0695], ignore_index=True)
        self.df_need.index = range(self.df_need.shape[0])

        self.window_download_info = Tk()
        screenWidth = self.window_download_info.winfo_screenwidth()  # 获取显示区域的宽度
        screenHeight = self.window_download_info.winfo_screenheight()  # 获取显示区域的高度
        width = 400  # 设定窗口宽度
        height = 400  # 设定窗口高度
        left = int((screenWidth - width) / 2)
        top = int((screenHeight - height) / 2)-100
        self.window_download_info.title('电子保单下载')
        self.window_download_info.geometry('{width}x{height}+{left}+{top}'.format(width=width, height=height, left=left, top=top))
        self.window_download_info.iconbitmap(app_path() + '/bin/aic_logo.ico')
        self.text = scrolledtext.ScrolledText(self.window_download_info, font=('微软雅黑', 10), fg='blue')
        self.text.pack()
        self.start_time = time.time()
        self.text.insert(END, '共需下载 {} 个电子保单...\n\n'.format(self.df_need.shape[0]))
        self.window_download_info.update()
        self.download_multi(thread_num=25)  # 25线程
        self.window_download_info.mainloop()


    def main(self):
        try:
            self.choose_file_window()
        except Exception as e:
            info = '错误原因：' + str(e)
            messagebox.showerror('Error', info)

    
if __name__ == "__main__":
    download_policy = Download_Policy()