import Vue from 'vue'
import Router from 'vue-router'
import Index from '~/pages/index.vue'
import Jogos from '~/pages/jogos.vue'
import Quemsomos from '~/pages/quemsomos.vue'
import Busca from '~/pages/busca.vue'
import Login from '~/pages/login.vue'
import Basquete from '~/pages/basquete.vue'
import Futebol from '~/pages/futebol.vue'
import Volei from '~/pages/volei.vue'
import Username from '~/pages/user/_username/index.vue'

Vue.use(Router)

export const routerOptions = {
  mode: 'history',
  routes: [
    {path: '/', component: Index, name: 'index'},
    {path: '/jogos', component: Jogos, name: 'jogos'},
    {path: '/quemsomos', component: Quemsomos, name: 'quemsomos'},
    {path: '/busca', component: Busca, name: 'busca'},
    {path: '/login', component: Login, name: 'login'},
    {path: '/basquete', component: Basquete, name: 'basquete'},
    {path: '/futebol', component: Futebol, name: 'futebol'},
    {path: '/volei', component: Volei, name: 'volei'},
    {path: '/user/:username?', component: Username, name: 'username'}
  ]
}

export function createRouter (ctx) {
  return new Router(routerOptions)
}
