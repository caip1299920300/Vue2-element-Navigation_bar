import Vue from 'vue'
import App from './App.vue'
import ElementUI, { MessageBox } from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import router from './router'
import store from './store'
// 引入样式
import './assets/less/index.less'
// 引入axios
import http from 'axios'

// 引入mock
import '@/api/mock.js'
Vue.prototype.$http = http
Vue.prototype.$confirm = MessageBox.confirm
Vue.prototype.$message = MessageBox.message

Vue.use(ElementUI);

Vue.config.productionTip = false

// 导航守卫 实现路由的监听
router.beforeEach((to, from, next) => {
  // 获取token信息  目的：防止页面刷新后vuex丢失token信息
  store.commit('getToken')
  const token = store.state.user.token
  if(!token && to.name !== 'login') {
    next({ name: 'login'})
  }else if(token && to.name === 'login') {
    next({name: 'home'})
  }else {
    next()
  }
})

new Vue({
  store,
  router,
  render: h => h(App),
  created() {
    // 动态设置路由
    store.commit('addMenu', router)
  }
}).$mount('#app')
