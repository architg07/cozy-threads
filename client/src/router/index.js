import { createRouter, createWebHistory } from 'vue-router'
import Items from '../components/Items.vue'
import Cart from '../components/Cart.vue'
import Checkout from '../components/Checkout.vue'
import OrderSuccess from '../components/OrderSuccess.vue'
import OrderFail from '../components/OrderFail.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Items',
      component: Items,
    },
    {
      path: '/cart',
      name: 'Cart',
      component: Cart
    },
    {
      path: '/checkout',
      name: 'Checkout',
      component: Checkout
    },
    {
      path: '/success',
      name: 'OrderSuccess',
      component: OrderSuccess
    },
    {
      path: '/cancelled',
      name: 'OrderFail',
      component: OrderFail
    }

  ]
})

export default router