import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

/* Layout */
import Layout from '@/views/layout/Layout'

/** note: submenu only apppear when children.length>=1
*   detail see  https://panjiachen.github.io/vue-element-admin-site/#/router-and-nav?id=sidebar
**/

/**
* hidden: true                   if `hidden:true` will not show in the sidebar(default is false)
* alwaysShow: true               if set true, will always show the root menu, whatever its child routes length
*                                if not set alwaysShow, only more than one route under the children
*                                it will becomes nested mode, otherwise not show the root menu
* redirect: noredirect           if `redirect:noredirect` will no redirct in the breadcrumb
* name:'router-name'             the name is used by <keep-alive> (must set!!!)
* meta : {
    roles: ['admin','editor']     will control the page roles (you can set multiple roles)
    title: 'title'               the name show in submenu and breadcrumb (recommend set)
    icon: 'svg-name'             the icon show in the sidebar,
    noCache: true                if true ,the page will no be cached(default is false)
  }
**/
export const constantRouterMap = [
  { path: '/login', component: () => import('@/views/login/index'), hidden: true },
  { path: '/authredirect', component: () => import('@/views/login/authredirect'), hidden: true },
  { path: '/404', component: () => import('@/views/errorPage/404'), hidden: true },
  { path: '/401', component: () => import('@/views/errorPage/401'), hidden: true },
  {
    path: '',
    component: Layout,
    redirect: 'dashboard',
    children: [{
      path: 'dashboard',
      component: () => import('@/views/dashboard/index'),
      name: 'dashboard',
      meta: { title: 'dashboard', icon: 'dashboard', noCache: true }
    }]
  }
]

export default new Router({
  // mode: 'history', // require service support
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRouterMap
})

export const asyncRouterMap = [
  {
    path: '/fictionmanage',
    component: Layout,
    redirect: 'noredirect',
    name: 'fictionmanage',
    meta: {
      title: '小说管理',
      icon: 'list'
    },
    children: [
      {
        path: 'fictionsource',
        component: () => import('@/views/fictionmanage/fictionsource'),
        name: 'FictionSource',
        meta: {
          title: '资源',
          noCache: true,
          icon: 'bug'
        }
      },
      {
        path: 'fiction',
        component: () => import('@/views/fictionmanage/fiction'),
        name: 'Fiction',
        meta: {
          title: '小说',
          noCache: true,
          icon: 'list'
        }
      }
    ]
  },
  {
    path: '/homemanage',
    component: Layout,
    redirect: 'noredirect',
    name: 'homemanage',
    meta: {
      title: '家庭管理',
      icon: 'chart'
    },
    children: [
      {
        path: 'bankcard/:version_id',
        component: () => import('@/views/homemanage/bankcard'),
        name: 'Bankcard',
        meta: {
          title: '银行卡管理',
          noCache: true
        }
      },
      { path: 'reading',
        component: () => import('@/views/homemanage/reading'),
        name: 'Reading',
        meta: {
          title: '阅读管理',
          noCache: true
        }
      }
    ]
  },
  { path: '*', redirect: '/404', hidden: true }
]
