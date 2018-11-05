<template>
<div>
    <h1>tools</h1>
    <Row>
        <i-col span="3">
            <Card class="card">
                <div style="text-align:center">
                    <img src="../assets/logo.png">
                    <h3><a :href="retUrl()">A high quality UI Toolkit based on Vue.js</a></h3>
                </div>
            </Card>
        </i-col>
        <i-col span="3" offset="4">
            <Card class="card">
                <div style="text-align:center">
                    <img src="../assets/logo.png">
                    <h3><a :href="retUrl('t1')">A high quality UI Toolkit based on Vue.js</a></h3>
                </div>
            </Card>
        </i-col>
        <i-col span="3" offset="4">
            <Card class="card">
                <div style="text-align:center">
                    <img src="../assets/logo.png">
                    <h3><a :href="retUrl('t1')">A high quality UI Toolkit based on Vue.js</a></h3>
                </div>
            </Card>
        </i-col>
    </Row>
</div>
</template>
<script>
export default {
    data() {
        return {
            theme1: 'light'
        }
    },
    methods: {
        retUrl(msg) {
            if (msg == 't1') {
                return '/about'
            } else {
                return ''
            }
        }
    }
}
</script>

<style scoped>
.card {
    width: 320px;
    margin-left: 50%;
    margin-top: 100px;
}
</style>
