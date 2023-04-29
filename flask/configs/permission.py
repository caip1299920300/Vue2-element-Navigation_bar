import json
admin_data = {
    "code": 20000,
    "data": {
        "menu": [
            {
                "path": '/home',
                "name": 'home',
                "label": '首页',
                "icon": 's-home',
                "url": 'home/index'
            },
            {
                "path": '/mall',
                "name": 'mall',
                "label": '商品管理',
                "icon": 'video-play',
                "url": 'mall/index'
            },
            {
                "path": '/user',
                "name": 'user',
                "label": '用户管理',
                "icon": 'user',
                "url": 'user/index'
            },
            {
                "label": '其他',
                "icon": 'location',
                "children": [
                    {
                        "path": '/page1',
                        "name": 'page1',
                        "label": '页面1',
                        "icon": 'setting',
                        "url": 'other/pageOne.vue'
                    },
                    {
                        "path": '/page2',
                        "name": 'page2',
                        "label": '页面2',
                        "icon": 'setting',
                        "url": 'other/pageTwo.vue'
                    }
                ]
            }
        ],
        "token": "Mock.Random.guid()",
        "message": '获取成功'
    }
}
# 将字符串转换成JSON格式
admin_ata_json = json.dumps(admin_data)


user_data = {
    "code": 20000,
    "data": {
        "menu": [
            {
                "path": '/home',
                "name": 'home',
                "label": '首页',
                "icon": 's-home',
                "url": 'home/index'
            },
            {
                "path": '/mall',
                "name": 'mall',
                "label": '商品管理',
                "icon": 'video-play',
                "url": 'mall/index'
            },
            {
                "label": '其他',
                "icon": 'location',
                "children": [
                    {
                        "path": '/page1',
                        "name": 'page1',
                        "label": '页面1',
                        "icon": 'setting',
                        "url": 'other/pageOne.vue'
                    },
                    {
                        "path": '/page2',
                        "name": 'page2',
                        "label": '页面2',
                        "icon": 'setting',
                        "url": 'other/pageTwo.vue'
                    }
                ]
            }
        ],
        "token": "Mock.Random.guid()",
        "message": '获取成功'
    }
}
# 将字符串转换成JSON格式
user_data_json = json.dumps(user_data)