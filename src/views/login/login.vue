<template>
  <el-form
    :model="form"
    status-icon
    :rules="rules"
    ref="form"
    label-width="100px"
    class="login-container"
  >
    <h3 class="login_title">系统登录</h3>
    <el-form-item
      label="用户名"
      label-width="80px"
      prop="username"
      class="username"
    >
      <el-input type="input" v-model="form.username" autocomplete="off" placeholder="请输入账号"></el-input>
    </el-form-item>

      <el-form-item
      label="密码"
      label-width="80px"
      prop="password"
    >
      <el-input type="password" v-model="form.password" autocomplete="off" placeholder="请输入密码"></el-input>
    </el-form-item>

    <el-form-item class="login_submit">
      <el-button type="primary" @click="login" class="login_submit">登录</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
// 没有后端 用前端的mock来模拟
import Mock from 'mockjs'
import { getMenu } from '../../api/data'
export default {
  name: 'login',
  data() {
    return {
      form: {

      },
      rules: {
        username: [
          {
            required: true,
            message: '请输入用户名',
            trigger: 'blur'
          },
          {
            min: 3,
            message: '用户名长度不能小于三位',
            trigger: 'blur'
          }
        ],
        password: [
          {
            required: true,
            message: '请输入密码',
            trigger: 'blur'
          }
        ]
      }
    }
  },
  methods: {
    login() {
      getMenu(this.form).then(({data: res}) => {
        if(res.code === 20000) {
          // 清除当前路由
          this.$store.commit('clearMenu')
          // 对menu进行设置
          this.$store.commit('setMenu', res.data.menu)
          // 设置token
          this.$store.commit('setToken', res.data.token)
          // 动态添加路由
          this.$store.commit('addMenu', this.$router)
          // 页面跳转
          this.$router.push({ name: 'home'})
        }else {
          this.$message.warning(res.data.message)
        }
      })
      // const token = Mock.random.guid()
      // this.$store.commit('setToken', token)
      // this.$router.push({ name: 'home'})
    }
  }
}
</script>

<style lang="less" scoped>
  .login-container {
    border-radius: 15px;
    background-clip: padding-box;
    margin: 180px auto;
    width: 350px;
    padding: 35px 35px 15px 15px;
    background-color: #fff;
    border: 1px solid #eaeaea;
    box-shadow: 0 0 25px #cac6c6;
  }

  .login_title {
    margin: 0px auto 40px auto;
    text-align: center;
    color: #505458;
  }

  .login_submit {
    margin: 10px auto 0 auto;
  }
</style>