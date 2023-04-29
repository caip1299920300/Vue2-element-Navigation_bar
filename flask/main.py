from flask import Flask,request, jsonify
import json
from flask_cors import CORS
# 数据
from configs import permission,home,user

app = Flask(__name__)
CORS(app)



@app.route('/api/permission/getMenu',methods=["POST"])
# 数据加载路由
def login_data():
    user_data = request.get_json()
    print(user_data)
    if user_data["username"] == "admin" and user_data['password']=='admin':
        return permission.admin_ata_json
    else:
        return permission.user_data_json

@app.route('/api/home/getData',methods=["GET"])
# 数据加载路由
def home_data():
    return home.home_data_json

@app.route('/api/user/getUser',methods=["GET"])
# 数据加载路由
def user_getdata():
    # print(request.args.get("page"))
    page_num = request.args.get("page")
    pageSize = request.args.get("pageSize")
    return user.get_data(int(page_num),int(pageSize))

@app.route('/api/user/edit',methods=["POST"])
# 数据加载路由
def user_edit():
    edit_data = request.get_json()
    print("编辑数据：",edit_data)
    return user.updateUser(edit_data)

@app.route('/api/user/add',methods=["POST"])
# 数据加载路由
def user_add():
    add_data = request.get_json()
    print("添加数据：",add_data)
    return user.createUser(add_data)

@app.route('/api/user/del',methods=["POST"])
# 数据加载路由
def user_del():
    del_id = request.get_json()["params"]
    print(del_id)
    return user.deleteUser(del_id)


if __name__ == '__main__':
    app.run()
