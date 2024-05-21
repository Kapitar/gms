import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import DashboardView from "./views/DashboardView.vue";
import ScheduleView from "./views/ScheduleView.vue";
import "./style.css"

import App from './App.vue'

const app = createApp(App)

const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: "/", component: DashboardView },
        { path: "/schedule", component: ScheduleView }
    ]
})

app.use(router)
app.mount('#app')