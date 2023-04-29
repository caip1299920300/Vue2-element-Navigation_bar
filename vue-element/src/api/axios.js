import axios from 'axios'
import config from '@/config'

// 判断当前的运行环境
const baseUrl = process.env.NODE_ENV === 'development' ? config.baseUrl.dev : config.baseUrl.pro

class HttpRequest {

  constructor(baseUrl) {
    this.baseUrl = baseUrl
  }

  getInsideConfig() {
    const config = {
      baseUrl: this.baseUrl,
      header: {}
    }
    return config
  }

  interceptores(instance) {
    // 添加请求拦截器
    instance.interceptors.request.use(function (config) {
      // 在发送请求之前做些什么
      return config;
    }, function (error) {
      // 对请求错误做些什么
      return Promise.reject(error);
    });

    // 添加响应拦截器
    instance.interceptors.response.use(function (response) {
      // console.log('response',response)
      // 对响应数据做点什么
      return response;
    }, function (error) {
      // console.log('error', error)
      // 对响应错误做点什么
      return Promise.reject(error);
    });
  }

  // 接口请求时使用
  request(options) {
    const instance = axios.create()
    // 把传进来的参数和这里的参数合并
    options = {...this.getInsideConfig(), ...options}
    this.interceptores(instance)
    return instance(options)
  }
}

export default new HttpRequest(baseUrl)