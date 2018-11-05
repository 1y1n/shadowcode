<template>
    <div class="home">
        <img alt="Vue logo" src="../assets/logo.png">
        <HomeCop msg="Welcome to Your Vue.js App"/>
    </div>
</template>

<script>
// @ is an alias to /src
import HomeCop from '@/components/HomeCop.vue'

export default {
    name: 'home',
    components: {
        HomeCop
    }
}
</script>
 