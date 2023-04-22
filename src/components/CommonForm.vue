<template>
  <el-form ref="form" label-width="100px" :model="form" :inline="inline">
    <el-form-item v-for="item in formLabel" :key="item.label" :label="item.label">
      <el-input
      v-if="item.type === 'input'"
      :placeholder="`请输入${item.label}`"
      v-model="form[item.model]"
      >
      </el-input>

      <e-switch v-if="item.type === 'switch' " v-model="form[item.label]"></e-switch>
      <el-date-picker
        v-if="item.type === 'data'"
        value-format="yyyy-mm-dd"
        placeholder="选择日期"
        v-model="form[item.model]"
      >
      </el-date-picker>

      <el-select
        v-if="item.type === 'select'"
        placeholder="请选择"
        v-model="form[item.model]"
      >
        <el-option
          v-for="item in item.opts"
          :key="item.value"
          :label="item.label"
          :value="item.value"
        >
        </el-option>
      </el-select>
    </el-form-item>

    <el-form-item>
      <slot></slot>
    </el-form-item>
  </el-form>
</template>

<script>
export default {
  name: 'CommonFrom',
  // commonForm在user/index.vue中被el-dialog组件 包裹着 所以数据是从user/index.vue中传过来的
  // 用来接收数据
  props: {
    // 配置的数据
    formLabel: Array,
    // form的数据
    form: Object,
    // 布局的显示
    inline: Boolean
  },
  data() {
    return {

    }
  }
}
</script>

<style>

</style>