def create_province_dict():
    province_dict = dict()
    province_dict['北京'] = ['东城', '西城', '朝阳', '丰台', '石景山', '海淀', '顺义', '通州', '大兴', '房山', '门头沟', '昌平', '平谷', '密云', '怀柔', '延庆']
    province_dict['天津'] = ['和平', '河东', '河西', '南开', '河北', '红桥', '滨海', '东丽', '西青', '津南', '北辰', '武清', '宝坻', '宁河', '静海', '蓟州']
    province_dict['重庆'] = ['渝中', '万州', '涪陵', '大渡口', '江北', '沙坪坝', '九龙坡', '南岸', '北碚', '綦江', '大足', '渝北', '巴南', '黔江', '长寿', '江津', '合川', '永川', '南川', '璧山', '铜梁', '潼南', '荣昌', '开州', '梁平', '武隆', '城口', '丰都', '垫江', '忠县', '云阳', '奉节', '巫山', '巫溪', '石柱', '秀山', '酉阳', '彭水']
    province_dict['上海'] = ['黄浦', '徐汇', '长宁', '静安', '普陀', '虹口', '杨浦', '闵行', '宝山', '嘉定', '浦东', '金山', '松江', '青浦', '奉贤', '崇明']
    province_dict['内蒙古'] = ['呼和浩特', '包头', '乌海', '赤峰', '通辽', '鄂尔多斯', '呼伦贝尔', '巴彦淖尔', '乌兰察布', '兴安', '锡林郭勒', '阿拉善']
    province_dict['广西'] = ['南宁', '柳州', '桂林', '梧州', '北海', '崇左', '来宾', '贺州', '玉林', '百色', '河池', '钦州', '防城港', '贵港']
    province_dict['西藏'] = ['拉萨', '日喀则', '昌都', '林芝', '山南', '那曲', '阿里']
    province_dict['新疆'] = ['乌鲁木齐', '克拉玛依', '吐鲁番', '哈密', '阿克苏', '喀什', '和田', '昌吉', '博尔塔拉', '巴音郭楞', '克孜勒苏柯尔克孜', '伊犁', '塔城', '阿勒泰']
    province_dict['宁夏'] = ['银川', '石嘴山', '吴忠', '固原', '中卫']
    province_dict['河北'] = ['石家庄', '唐山', '秦皇岛', '邯郸', '邢台', '保定', '张家口', '承德', '沧州', '廊坊', '衡水']
    province_dict['山东'] = ['济南', '青岛', '淄博', '枣庄', '东营', '烟台', '潍坊', '济宁', '泰安', '威海', '日照', '滨州', '德州', '聊城', '临沂', '菏泽']
    province_dict['辽宁'] = ['沈阳', '大连', '鞍山', '抚顺', '本溪', '丹东', '锦州', '营口', '阜新', '辽阳', '盘锦', '铁岭', '朝阳', '葫芦岛', '凤城']
    province_dict['黑龙江'] = ['哈尔滨', '齐齐哈尔', '牡丹江', '佳木斯', '大庆', '鸡西', '双鸭山', '伊春', '七台河', '鹤岗', '黑河', '绥化', '大兴安岭', '黑龙']
    province_dict['甘肃'] = ['兰州', '嘉峪关', '金昌', '白银', '天水', '武威', '张掖', '平凉', '酒泉', '庆阳', '定西', '陇南', '临夏', '甘南']
    province_dict['吉林'] = ['长春', '延边', '四平', '通化', '白城', '辽源', '松原', '白山', '净月']
    province_dict['青海'] = ['西宁', '海东', '海北', '黄南', '海南', '果洛', '玉树', '海西']
    province_dict['河南'] = ['郑州', '开封', '洛阳', '平顶山', '安阳', '鹤壁', '新乡', '焦作', '濮阳', '许昌', '漯河', '三门峡', '商丘', '周口', '驻马店', '南阳', '信阳', '济源']
    province_dict['江苏'] = ['南京', '无锡', '徐州', '常州', '苏州', '南通', '连云港', '淮安', '盐城', '扬州', '镇江', '泰州', '宿迁', '东台']
    province_dict['湖北'] = ['武汉', '黄石', '十堰', '宜昌', '襄阳', '鄂州', '荆门', '孝感', '荆州', '黄冈', '咸宁', '随州', '恩施', '仙桃', '潜江', '天门', '神农架']
    province_dict['湖南'] = ['长沙', '株洲', '湘潭', '衡阳', '邵阳', '岳阳', '常德', '张家界', '益阳', '娄底', '郴州', '永州', '怀化', '湘西']
    province_dict['浙江'] = ['杭州', '宁波', '温州', '绍兴', '湖州', '嘉兴', '金华', '衢州', '台州', '丽水', '舟山']
    province_dict['江西'] = ['南昌', '九江', '上饶', '抚州', '宜春', '吉安', '赣州', '景德镇', '萍乡', '新余', '鹰潭']
    province_dict['广东'] = ['广州', '韶关', '深圳', '珠海', '汕头', '佛山', '惠东', '江门', '湛江', '茂名', '肇庆', '惠州', '梅州', '汕尾', '河源', '阳江', '清远', '东莞', '中山', '潮州', '揭阳', '云浮']
    province_dict['云南'] = ['昆明', '曲靖', '玉溪', '昭通', '保山', '丽江', '普洱', '临沧', '德宏', '怒江', '迪庆', '大理', '楚雄', '红河', '文山', '西双版纳']
    province_dict['福建'] = ['福州', '厦门', '漳州', '泉州', '三明', '莆田', '南平', '龙岩', '宁德', '平潭']
    province_dict['海南'] = ['海口', '三亚', '三沙', '儋州', '五指山']
    province_dict['山西'] = ['太原', '大同', '朔州', '忻州', '阳泉', '吕梁', '晋中', '长治', '晋城', '临汾', '运城']
    province_dict['四川'] = ['成都', '绵阳', '自贡', '攀枝花', '泸州', '德阳', '广元', '遂宁', '内江', '乐山', '资阳', '宜宾', '南充', '达州', '雅安', '阿坝', '甘孜', '凉山', '广安', '巴中', '眉山']
    province_dict['陕西'] = ['西安', '宝鸡', '咸阳', '铜川', '渭南', '延安', '榆林', '汉中', '安康', '商洛']
    province_dict['贵州'] = ['贵阳', '遵义', '六盘水', '安顺', '毕节', '铜仁', '黔东南', '黔南', '黔西南']
    province_dict['安徽'] = ['合肥', '芜湖', '蚌埠', '淮南', '马鞍山', '淮北', '铜陵', '安庆', '黄山', '阜阳', '宿州', '滁州', '六安', '宣城', '池州', '亳州']

    return province_dict


def get_province_from_info(area_info):
    province_dict = create_province_dict()
    return_info = None
    for province in province_dict.keys():
        if province in area_info:
            return_info = province
            break
    if return_info is None:
        for province in province_dict.keys():
            for city in province_dict[province]:
                if city in area_info:
                    return_info = province
                    break
            if return_info is not None:
                break
        if return_info is None:
            return area_info
        else:
            return return_info

    else:
        return return_info