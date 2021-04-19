def simple_province2whole(first_chr):
    simple_province_dict = {
        '京': '北京',
        '津': '天津',
        '沪': '上海',
        '渝': '重庆',
        '蒙': '内蒙古',
        '新': '新疆',
        '藏': '西藏',
        '宁': '宁夏',
        '桂': '广西',
        '港': '香港',
        '澳': '澳门',
        '黑': '黑龙江',
        '吉': '吉林',
        '辽': '辽宁',
        '晋': '山西',
        '冀': '河北',
        '青': '青海',
        '鲁': '山东',
        '豫': '河南',
        '苏': '江苏',
        '皖': '安徽',
        '浙': '浙江',
        '闽': '福建',
        '赣': '江西',
        '湘': '湖南',
        '鄂': '湖北',
        '粤': '广东',
        '琼': '海南',
        '甘': '甘肃',
        '陕': '陕西',
        '黔': '贵州',
        '贵': '贵州',
        '滇': '云南',
        '云': '云南',
        '川': '四川'
    }
    
    try:
        return simple_province_dict[first_chr]
    except:
        raise ValueError('%s车牌号不合法' % first_chr)