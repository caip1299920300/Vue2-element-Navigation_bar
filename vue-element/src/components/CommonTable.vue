<template>
  <div class="common-table">
    <el-table :data="tableData" height="90%" stripe   style="width: 100%">
      <el-table-column
        show-overflow-tooltip
        v-for="item in tableLabel" 
        :key="item.prop"
        :label="item.label"
        :width="item.width ? item.width : 180"
      >
        <template slot-scope="scope">
          <span style="margin-left: 10px">{{scope.row[item.prop] }}</span>
        </template>
      </el-table-column>
      
      <el-table-column label="操作" min-width="180">
        <!-- 点击编辑之后，内容自动填充在文本框中 修改想修改的即可 -->
        <template slot-scope="scope">
          <el-button size="mini" @click="handleEdit(scope.row)">编辑</el-button>
          <!-- 删除部分有bug 点击删除提示删除成功  但是数据还是在页面中显示了 -->
          <el-button size="mini" type="danger" @click="handleDelete(scope.row)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>

    <el-pagination class="pager"
      layout="prev, pager, next"
      :total="config.total"
      :current-page.sync="config.page"
      @current-change="changePage"
      :page-size="20"
    ></el-pagination>
  </div>
</template>

<script>
export default {
  name: 'CommonTable',
  props: {
    tableData: Array,
    tableLabel: Array,
    config: Object
  },
  data() {
    return {

    }
  },
  methods: {
    handleEdit(row) {
      this.$emit('edit',row)
    },
    handleDelete(row) {
      this.$emit('del',row)

    },
    changePage(page) {
      this.$emit('changePage', page)

    }
  }
}
</script>

<style lang="less" scoped>
.common-table {
  height: calc(100% - 62px);
  background: #fff;
  position: relative;

  .pager {
    position: absolute;
    bottom: 0;
    right: 20px;
  }
}

</style>