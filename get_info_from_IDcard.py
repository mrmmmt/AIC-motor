def is_leap_year(year):
    """
    能被4整除且不能被100整除；能被400整除
    """
    if year % 400 == 0:
        return True
    if year % 4 == 0 and year % 100 != 0:
        return True

    return False


def month_day(year):
    if is_leap_year(year):
        month_lst = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        month_lst = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    return month_lst


def check_IDcard(IDCardNumber):
    IDCardNumber = str(IDCardNumber).upper()
    if len(IDCardNumber) == 18:

        # 18位身份证需要验证最后一位校验位
        factor = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        parity = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
        sum_value = 0
        for i in range(17):
            ai = int(IDCardNumber[i])
            wi = factor[i]
            sum_value += ai * wi

        if IDCardNumber[17] != parity[sum_value % 11]:
            raise ValueError('身份证号：{} 不合法'.format(IDCardNumber))

        # 地址和出生日期验证
        if IDCardNumber[:2] not in ['11', '12', '13', '14', '15', '21', '22', '23', '31', '32', '33', '34', '35', '36', '37', '41', '42', '43', '44', '45', '46', '50', '51', '52', '53', '54', '61', '62', '63', '64', '65', '71']:
            raise ValueError('身份证号：{} 不合法（地址）'.format(IDCardNumber))
        
        flag = IDCardNumber[6:14]  # 得到代表出生日期7-14位数字
        if int(flag[0:4]) > 2020 or int(flag[0:4]) < 1950:
            raise ValueError('身份证号：{} 不合法（年份）'.format(IDCardNumber))
        if int(flag[4:6]) > 12 or int(flag[4:6]) == 0:
            raise ValueError('身份证号：{} 不合法（月份）'.format(IDCardNumber))
        if int(flag[6:]) > month_day(int(flag[0:4]))[int(flag[4:6])-1] or int(flag[6:]) == 0:
            raise ValueError('身份证号：{} 不合法（日期）'.format(IDCardNumber))

    else:
        raise ValueError('身份证号：{} 不是18位'.format(IDCardNumber))


def get_info_from_IDcard(IDCardNumberLst):
    genderLst = []
    birthdayLst = []
    for IDCardNumber in IDCardNumberLst:
        check_IDcard(IDCardNumber)
        flag = IDCardNumber[16]  # 身份证第17位数字，奇数为男性，偶数为女性
        flag2 = IDCardNumber[6:14]  # 得到代表出生日期7-14位数字
        birthday = flag2[0:4] + '-' + flag2[4:6] + '-' + flag2[6:]
        birthdayLst.append(birthday)
        
        if flag in ['1', '3', '5', '7', '9']:
            genderLst.append('男')
        else:
            genderLst.append('女')

    return genderLst, birthdayLst
    