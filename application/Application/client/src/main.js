import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import VueRouter from 'vue-router'
import router from './router'
import navigationbar from './components/navigationbar'
import home from './components/home'
import steamcard from './components/steamcard'
import VueApexCharts from 'vue-apexcharts'
import echarts from 'echarts'
import axios from 'axios'
import * as am4core from "@amcharts/amcharts4/core";
import * as am4charts from "@amcharts/amcharts4/charts";
import am4themes_animated from "@amcharts/amcharts4/themes/animated";
am4core.useTheme(am4themes_animated);
Vue.prototype.$axios = axios
Vue.prototype.$echarts = echarts
Vue.use(VueApexCharts)
Vue.component('apexchart', VueApexCharts)
Vue.use(VueRouter)
Vue.config.productionTip = false
new Vue({
  vuetify,
  router,
  navigationbar,
  home,
  steamcard,
  render: h => h(App)
}).$mount('#app')
