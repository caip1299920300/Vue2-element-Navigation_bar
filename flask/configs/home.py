import random
import json
List = []
for i in range(7):
    List.append({"苹果": random.randint(100, 8000),
                "vivo": random.randint(100, 8000),
                "oppo": random.randint(100, 8000),
                "魅族": random.randint(100, 8000),
                "三星": random.randint(100, 8000),
                "小米": random.randint(100, 8000)})


home_data = {"code": 20000,
             "data": {
                 # 饼图
                 "videoData": [
                     {
                         "name": '小米',
                         "value": 2999
                     },
                     {
                         "name": '苹果',
                         "value": 5999
                     },
                     {
                         "name": 'vivo',
                         "value": 1500
                     },
                     {
                         "name": 'oppo',
                         "value": 1999
                     },
                     {
                         "name": '魅族',
                         "value": 2200
                     },
                     {
                         "name": '三星',
                         "value": 4500
                     }
                 ],
                 # 柱状图
                 "userData": [
                     {
                         "date": '周一',
                         "new": 5,
                         "active": 200
                     },
                     {
                         "date": '周二',
                         "new": 10,
                         "active": 500
                     },
                     {
                         "date": '周三',
                         "new": 12,
                         "active": 550
                     },
                     {
                         "date": '周四',
                         "new": 60,
                         "active": 800
                     },
                     {
                         "date": '周五',
                         "new": 65,
                         "active": 550
                     },
                     {
                         "date": '周六',
                         "new": 53,
                         "active": 770
                     },
                     {
                         "date": '周日',
                         "new": 33,
                         "active": 170
                     }
                 ],
                 # 折线图
                 "orderData": {
                     "date": ['20191001', '20191002', '20191003', '20191004', '20191005', '20191006', '20191007'],
                     "data": List
                 },
                 "tableData": [
                     {
                         "name": 'oppo',
                         "todayBuy": 500,
                         "monthBuy": 3500,
                         "totalBuy": 22000
                     },
                     {
                         "name": 'vivo',
                         "todayBuy": 300,
                         "monthBuy": 2200,
                         "totalBuy": 24000
                     },
                     {
                         "name": '苹果',
                         "todayBuy": 800,
                         "monthBuy": 4500,
                         "totalBuy": 65000
                     },
                     {
                         "name": '小米',
                         "todayBuy": 1200,
                         "monthBuy": 6500,
                         "totalBuy": 45000
                     },
                     {
                         "name": '三星',
                         "todayBuy": 300,
                         "monthBuy": 2000,
                         "totalBuy": 34000
                     },
                     {
                         "name": '魅族',
                         "todayBuy": 350,
                         "monthBuy": 3000,
                         "totalBuy": 22000
                     }
                 ]
             }
             }

# 将字符串转换成JSON格式
home_data_json = json.dumps(home_data)

if __name__ == '__main__':
    # print(home_data_json)
    print(List)
