<template>
    <div id="app">
        <Menu mode="horizontal" :theme="theme1" active-name="1">
            <MenuItem name="1" to="/">
                <Icon type="ios-paper" />
                首页
            </MenuItem>
            <MenuItem name="2" to="/tools">
                <Icon type="ios-people" />
                工具
            </MenuItem>
            <MenuItem name="3" to="/about">
                <Icon type="ios-construct" />
                关于
            </MenuItem>
            <MenuItem id="theme">
                <RadioGroup v-model="theme1">
                    <Radio label="light"></Radio>
                    <Radio label="dark"></Radio>
                    <Radio label="primary"></Radio>
                </RadioGroup>
            </MenuItem>
        </Menu>
        <br>

      <router-view/>
    </div>
</template>

<style>
#app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
}
#theme {
    float: right;
}
</style>

<script>
export default {
    data() {
        return {
            theme1: 'light'
        }
    }
}
</script>
