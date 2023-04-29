import Cookie from 'js-cookie'
// import router from '@/router';
export default {
  state: {
    isCollapse: false,
    tabsList: [
      {
        path: '/home',
        name: 'home',
        label: '首页',
        icon: 'home'
      }
    ],
    currentMenu: null,
    menu: []
  },
  mutations: {
    collapseMenu(state) {
      state.isCollapse  = !state.isCollapse
    },
    selectMenu(state, val) {
      if(val.name !== 'home') {
        state.currentMenu = val
        const result = state.tabsList.findIndex(item => item.name === val.name)
        if(result === -1) {
          state.tabsList.push(val)
        }
      }else {
        state.currentMenu = null
      }
    },
    closeTag(state, val) {
      const result = state.tabsList.findIndex(item => item.name === val.name)
      state.tabsList.splice(result, 1)
    },
    setMenu(state, val) {
      state.menu = val
      // 将menu缓存到浏览器的存储当中
      Cookie.set('menu', JSON.stringify(val))
    },
    clearMenu(state) {
      state.menu = []
      Cookie.remove('menu')
    },
    // 做路由的动态添加
    addMenu(state, router) {
      if( !Cookie.get('menu')) {
        return 
      }
      const menu = JSON.parse(Cookie.get('menu'))
      state.menu = menu
      // 对数据进行相关处理
      const menuArray = []
      menu.forEach(item => {
        // 有二级菜单
        if(item.children) {
          item.children = item.children.map(item => {
            item.component = () => import(`../views/${item.url}`)
            return item
          })
          // 二维数组扁平化
          menuArray.push(...item.children)
        }else {
          item.component = () => import(`../views/${item.url}`)
          menuArray.push(item)
        }
      })
      // 路由的动态添加
      menuArray.forEach(item => {
        router.addRoute('Main', item)
      })
    }
  }
}