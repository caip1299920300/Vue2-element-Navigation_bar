import axios from "./axios"

//getMenu
export const getMenu = (param) => {
  return axios.request({
    url: 'http://127.0.0.1:5000/api/permission/getMenu',
    method: 'post',
    data: param                          
  })
}

export const getData = () => {
  return axios.request({
    url: 'http://127.0.0.1:5000/api/home/getData'
  })
}

export const getUser = (params) => {
  return axios.request({
    url: 'http://127.0.0.1:5000/api/user/getUser',
    method: 'get',
    params
  })
}
