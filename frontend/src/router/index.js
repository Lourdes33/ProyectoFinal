import { createRouter, createWebHistory } from 'vue-router'
import inicio from '../views/inicio.vue'
import usuario from '../views/usuario.vue' 
import cuestionario from '../views/cuestionario.vue' 
import CuestionarioInicio from '../views/cuestionarioInicio.vue'
import resultado from '../views/resultado.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'cuestionarioInicio',
      component: CuestionarioInicio
    },
    {
      path: '/login',
      name: 'login',
      component: inicio
    },
    {
      path: '/panel',
      name: 'panel',
      component: usuario 
    },
    {
      path: '/cuestionario',
      name: 'cuestionario',
      component: cuestionario
    },
    {
      path: '/resultado',
      name: 'resultado',
      component: resultado
    }
  ]
})

export default router