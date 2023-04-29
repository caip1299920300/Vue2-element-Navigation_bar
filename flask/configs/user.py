from datetime import datetime, timedelta
import random
import json
import uuid
List = []
count = 200  # 随机生成图片的个数

# 中文姓氏集合
first_names = [
    '赵', '钱', '孙', '李', '周',
    '吴', '郑', '王', '冯', '陈',
    '褚', '卫', '蒋', '沈', '韩',
    '杨', '朱', '秦', '尤', '许',
    '何', '吕', '施', '张', '孔',
    '曹', '严', '华', '金', '魏',
    '陶', '姜', '戚', '谢', '邹',
    '喻', '柏', '水', '窦', '章'
]

# 中文名字集合
last_names = [
    '峰', '华', '明', '强', '彬',
    '伟', '洋', '勇', '良', '宇',
    '阳', '杰', '辉', '俊', '帅',
    '宁', '栋', '剑', '飞', '翔',
    '超', '浩', '亮', '波', '坤',
    '东', '进', '诚', '震', '轩',
    '宏', '健', '泽', '威', '立',
    '鹏', '坚', '晨', '昊', '琪',
    '振', '涛', '昌', '林', '成'
]


def generate_cname():
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    return first_name + last_name


# 省份集合
provinces = [
    '北京市', '天津市', '上海市', '重庆市', '河北省',
    '山西省', '辽宁省', '吉林省', '黑龙江省', '江苏省',
    '浙江省', '安徽省', '福建省', '江西省', '山东省',
    '河南省', '湖北省', '湖南省', '广东省', '海南省',
    '四川省', '贵州省', '云南省', '陕西省', '甘肃省',
    '青海省', '台湾省', '内蒙古自治区', '广西壮族自治区', '西藏自治区',
    '宁夏回族自治区', '新疆维吾尔自治区', '香港特别行政区', '澳门特别行政区'
]


def generate_random_date(start_date='1990-01-01', end_date='2021-12-31'):
    """
    生成指定范围内的随机日期
    :param start_date: 开始日期，格式为字符串，如 '2020-01-01'
    :param end_date: 结束日期，格式为字符串，如 '2021-12-31'
    :return: 随机日期，格式为字符串，如 '2021-05-12'
    """
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    days = (end_date - start_date).days + 1
    random_days = random.randint(0, days - 1)
    random_date = start_date + timedelta(days=random_days)
    return random_date.strftime('%Y-%m-%d')


for i in range(count):
    List.append(
        {
            "id": str(uuid.uuid4()),
            "name": generate_cname(),
            "addr": random.choice(provinces),
            'age': random.randint(10, 100),
            "birth": generate_random_date(),
            "sex": random.choice([0, 1])
        })

'''
    * 获取列表
    * 要带参数 name, page, limt; name可以不填, page,limit有默认值。
    * @param name, page, limit
    * @return {{code: number, count: number, data: *[]}}
'''
def get_data(page_num, pageSize=20):
   data_list = List[(page_num-1)*pageSize:page_num*pageSize]
   if page_num*pageSize > count:
      data_list = List[(page_num-1)*pageSize:count]
   # print(page_num,pageSize,data_list)
   return json.dumps({
      "code": 20000,
      "count": len(List),
      "list": data_list
    })


'''
   * 增加用户
   * @param name, addr, age, birth, sex
   * @return {{code: number, data: {message: string}}}
'''
def createUser(add_data):
   #  name, addr, age, birth, sex  = add_data.keys()
   add_data['age'] = random.randint(10, 100)
   add_data["id"] = str(uuid.uuid4())
   List.insert(0, add_data)
   return json.dumps({
      "code": 20000,
      "data": {
         "message": '添加成功'
      }
   })


'''
   * 删除用户
   * @param id
   * @return {*}
'''
def deleteUser(del_id):
   if not del_id:
      return json.dumps({
         "code": -999,
         "message": '参数不正确'
      })
   else:
      for index, data in enumerate(List):
         if data["id"] == del_id["id"]:
            List.pop(index)

      return json.dumps({
         "code": 20000,
         "message": '删除成功'
      })


'''
   * 批量删除
   * @param config
   * @return {{code: number, data: {message: string}}}
'''


'''
   * 修改用户
   * @param id, name, addr, age, birth, sex
   * @return {{code: number, data: {message: string}}}
'''
def updateUser(edit_data):
   for index, data in enumerate(List):
      if data["id"] == edit_data["id"]:
         data["name"] = edit_data["name"]
         data["addr"] = edit_data["addr"]
         data["age"] = edit_data["age"]
         data["birth"] = edit_data["birth"]
         data["sex"] = edit_data["sex"]
   return json.dumps({
      "code": 20000,
      "data": {
         "message": '编辑成功'
      }
   })
  

