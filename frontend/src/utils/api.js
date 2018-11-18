import axios from 'axios'
import qs from 'qs'

axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=UTF-8';

// axios demo 
// axios.get(url, {
//      params:{
//          ID:1
//          }
//      })
//      .then(function (response){
//          console.log(response)
//      })
//      .catch(function (error){
//          console.get(error)
//      })
async function asyncTest() {
    try {
        const res = await axios.get('http://127.0.0.1:8888/test')
        return res   // res.data
    } catch (error) {
        return 'error'
    }
}

//  提交的表单需要用  FormData 渲染。或者使用 qs.stringify 。否则post方法会变成 OPTIONS
//  这里错了，经后面测试 FormData 渲染无效。需要这样：
//  let a = new FormData()
//  a.append('key', 'value')
//  才可以。所以这里换成简便的方式，使用 qs.stringify
//  axios.post(url, new FormData({
//      f1: 'x1',
//      f2: 'x2'
//      }))
//      .then(function (response){
//          console.log(response)
//      })
//      .catch(function (error){
//          console.get(error)
//      })
async function testPostData() {
    try {
        const res = await axios.post('http://127.0.0.1:8888/test', qs.stringify({data: 'test'}))
        return res  // res.data
    } catch (error) {
        console.log(error)
    }
}



function testGetData() {
    // 下面这种方式不适合封装。
    // axios
    // .get('http://127.0.0.1:8888/test')
    // .then(response => (this.info = response))
    // axios.get('http://127.0.0.1:8888/test').then(function(response) {
    //     return response
    // })
    return 
}


// async/await 全局封装axios  https://juejin.im/post/5b4049a3f265da0f8524ce12
// Example: let data = await api.get('/ferring/test/list')
// => 箭头函数 类似匿名函数。箭头函数内部的this由上下文确定，而匿名函数内的this作用于在该匿名函数内
// https://zhuanlan.zhihu.com/p/25093389
const api = {
    async get (url, data) {
        try {
            let res = await axios.get(url, {params: data})
            res = res.data
            return new Promise((resolve) => {
                if (res.code === 0) {
                    resolve(res)
                } else {
                    resolve(res) // 都一样有什么意义呢
                }
            })
        } catch (error) {
            console.log(error)
        }
    },
    async post (url, data) {
        try{
            let res = await axios.post(url, qs.stringify(data))
            res = res.data
            return new Promise((resolve, reject) => {
                if (res.code === 0) {
                    resolve(res)
                } else {
                    alert('a')
                    reject(res)
                }
            })
        } catch (error) {
            console.log(error)
        }
    } 
    
}



export { asyncTest, testGetData, testPostData, api}
