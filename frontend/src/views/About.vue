<template>
    <div class="about">
        <h1>This is an about page</h1>
        <Button type="primary">Primary</Button>
        <Button type="info">Info</Button>
        <div>{{info}}</div>
        <div>{{info2}}</div>
        <div>{{info3}}</div>
        <div>{{info4}}</div>
    </div>
   
</template>


<script>
import * as api from '@/utils/api.js'
// import axios from 'axios'

export default {
    name: 'about',
    data() {
        return {
            info: null,
            info2: null,
            info3: null,
            info4: null,
        }
    },
    mounted() {
        this.asyncTest()
        this.testPostData()
        this.asyncApiTest()
        this.asyncApiPostTest()
    },
    methods: {
        asyncTest: async function asyncTest() {
            let d = await api.asyncTest()  // 直接调用包装好的确定的函数
            this.info = d
        },
        testPostData: async function testPostData() {
            let d = await api.testPostData()  // 直接调用包装好的确定的函数
            this.info2 = d
        },
        asyncApiTest: async function asyncApiTest() {
            let d = await api.api.get('http://127.0.0.1:8888/test')  // 调用 get api
            this.info3 = d
        },
        asyncApiPostTest: async function asyncApiPostTest() {
            let d = await api.api.post('http://127.0.0.1:8888/test', {data: 'test'})  // 调用 post api
            this.info4 = d
        }
    }
}
</script>
