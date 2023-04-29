<template>
  <header>
    <div class="l-content">
      <el-button icon="el-icon-menu" plain size="mini" @click="handleMenu"></el-button>
      <!-- 面包屑 -->
      <!-- <h3 style="color: #fff;">首页</h3> -->
      <el-breadcrumb separator=">">
        <el-breadcrumb-item v-for="item in tags" :key="item.path" :to="{ path: item.path }">{{ item.label }}</el-breadcrumb-item>
      </el-breadcrumb>
    </div>
    <div class="r-content">
      <el-dropdown trigger="click" szie="mini">
        <span>
          <img :src="userImg" class="user">
        </span>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item command="a">个人中心</el-dropdown-item>
          <el-dropdown-item @click.native="logOut" command="b">退出</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
    </div>
  </header>
</template>

<script>
import { mapState } from 'vuex'
export default {
  name: 'CommonHeader',
  data() {
    return {
      userImg: require('../assets/images/user.png')
    }
  },
  methods: {
    handleMenu() {
      this.$store.commit('collapseMenu')
    },
    logOut() {
      // 清除token
      this.$store.commit('clearToken')
      // 重置menu
      this.$store.commit('clearMenu')
      // 跳转到login页面
      this.$router.push('/login')
    }
  },
  computed: {
    ...mapState({
      tags: state => state.tab.tabsList 
    })
  }
}
</script>

<style lang="less" scoped>
.el-breadcrumb ::v-deep .el-breadcrumb__inner {
  color: #fff !important;
}
header {
  display: flex;
  height: 100%;
  justify-content: space-between;
  align-items: center;
  .l-content {
    display: flex;
    align-items: center;
    .el-button {
      margin-right: 20px;
    }
  }

  .r-content {
    .user {
      width: 40px;
      height: 40px;
      border-radius: 50%;
    }
  }
}
</style>