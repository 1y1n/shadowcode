<template>
<div class="baseEnc">
    <h1>base64/32/16</h1>
    <RadioGroup v-model="code">
        <Radio label="decode">
            <Icon type="ios-nutrition" />
            <span>decode</span>
        </Radio>
        <Radio label="encode">
            <Icon type="ios-nutrition" />
            <span>encode</span>
        </Radio>
        <p id='down'>{{code}}</p>
    </RadioGroup>
    <br>
    <RadioGroup v-model="type">
        <Radio label="base64">
            <Icon type="ios-nutrition" />
            <span>base64</span>
        </Radio>
        <Radio label="base32">
            <Icon type="ios-nutrition" />
            <span>base32</span>
        </Radio>
        <Radio label="base16">
            <Icon type="ios-nutrition" />
            <span>base16</span>
        </Radio>
        <p id='down'>{{type}}</p>
    </RadioGroup>
    <div class='largeInput'>
        <Input id="code" v-model="valueSub" type="textarea" :autosize="{minRows: 10,maxRows: 25}" placeholder="Enter something..." />
        <p>| |</p>
        <p>| |</p>
        <p> V </p>
        <Input v-model="valueRec" type="textarea" :autosize="{minRows: 10,maxRows: 25}" placeholder="something..." />
    </div>
    <br><br>
    <Button type="success" @click="submitVal()">SUBMIT</Button>
    <br><br>
    <Button type="error" @click="reset()">Reset</Button>
</div>
</template>

<script>
import * as api from '@/utils/api.js'

export default {
    name: 'baseEnc',
    data () {
        return {
            valueSub: '',
            valueRec: '',
            code: 'decode',
            type: 'base64'
        }
    },
    methods: {
        reset: function reset () {
            this.valueSub= ''
        },
        submitVal: async function submitVal () {
            if (this.valueSub == '') {
                alert("submit is null")
            } else {
                let rec = await api.baseSubmit(this.code, this.type, this.valueSub)
                if (rec != '') {
                    if (rec.code == 0) {
                        this.valueRec = rec.data
                    } else {
                        alert('input error.')
                    }
                } else {
                    alert('error')
                }
            }
        }
    }
}
</script>

<style scoped>
#down {
    color: gray
}
</style>
