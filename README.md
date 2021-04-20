# AIC-motor 摩托车承保数据处理

AIC-motor 是一个用于完成 AIC 和某互联网摩托车保险销售平台合作销售摩托车第三者责任保险和驾乘人员意外伤害保险，AIC 端承保所需工作的程序。



![AIC-承保操作流程](/env/承保操作流程.png)

## 依赖

- pandas
- pickle
- openyxl
- xlrd
- xlutils

## frozen_dir

Python 程序中使用相对路径在打包后会出现错误，只可以使用绝对路径。使用绝对路径在移动到其他设备会造成一定的麻烦，因此出现了冻结路径的方法 `frozen_dir.py`

```python
import sys
import os


def app_path():
    if hasattr(sys, 'frozen'):
        root_dir = os.path.dirname(os.path.dirname(sys.executable))
    else:
        root_dir = os.path.dirname(__file__)

    return root_dir.replace('\\','/')
```

## 版本

### v 1.61 (Build 20210419) 

- 自动生成驾乘人员意外伤害保险的批量导入模板 [`create_update0695.py`](https://github.com/mrmmmt/AIC-motor/blob/main/create_update0695.py)
  - 验证身份证的准确性 [`get_info_from_IDcard.py`](https://github.com/mrmmmt/AIC-motor/blob/main/get_info_from_IDcard.py)
  - 提示承保清单中的疑似正三轮车型 `create_result_df`
  - 将地区均归类至省份 [`area2province.py`](https://github.com/mrmmmt/AIC-motor/blob/main/area2province.py)
  - 得到车牌中省份简写所对应省份 [`simple_province.py`](https://github.com/mrmmmt/AIC-motor/blob/main/simple_province.py)
- 自动生成截至每日承保信息的汇总表 [`create_total_sheet_super.py`](https://github.com/mrmmmt/AIC-motor/blob/main/create_total_sheet_super.py)
  - 检查意健险系统调出表和平台发来表的信息是否对应 `create_total_sheet_raw_df`
  - 检查生成汇总表之后汇总表中车架号的重复值 `find_duplicated`
- 电子保单自动多线程下载并压缩为 .zip 压缩包 [`download_super.py`](https://github.com/mrmmmt/AIC-motor/blob/main/download_super.py)
- 修改驾乘人员意外伤害保险的保费、不含税保费及税额 [`change_tax.py`](https://github.com/mrmmmt/AIC-motor/blob/main/change_tax.py)
- 修改驾乘人员意外伤害保险的投保单号 [`change_policy_number.py`](https://github.com/mrmmmt/AIC-motor/blob/main/change_policy_number.py)
- 计算满期保费，分年度计算 [`calc_earned_premiun.py`](https://github.com/mrmmmt/AIC-motor/blob/main/calc_earned_premiun.py)


