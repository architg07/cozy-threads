<template>
  <div class="cart-page">
    <header>
      <h1>Your Cart</h1>
      <button class="home-button" @click="goToHome">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
          class="size-6">
          <path stroke-linecap="round" stroke-linejoin="round"
            d="m2.25 12 8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
        </svg>
      </button>
    </header>
    <div v-if="cartItems.length === 0">
      <p>Your cart is empty.</p>
    </div>
    <div v-else>
      <div class="cart-content">
        <div class="cart-items">
          <div v-for="product in cartItemsDisplay" :key="product.id" class="cart-item">
            <img :src="getProductImage(product.id)" :alt="product.name" class="product-image">
            <div class="product-details">
              <h3>{{ product.name }}</h3>
              <p class="price">{{ '$' + product.price }}</p>
              <button class="remove-button" @click="removeFromCart(product.id)">Remove</button>
            </div>
          </div>
        </div>
        <div class="cart-summary">
          <p>Total: ${{ totalCost }}</p>
          <p>Tax (@7.00%): ${{ tax }}</p>
          <p>Total with Tax: ${{ totalCostWithTax }}</p>
          <button class="checkout-button" @click="proceedToCheckout">Proceed to Checkout</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import shirt from '../../products/cozy-shirt.jpeg';
import pants from '../../products/cozy-pants.jpeg';
import jacket from '../../products/cozy-jacket.jpeg';
import shoes from '../../products/cozy-shoes.jpeg';
import sweater from '../../products/cozy-sweater.jpeg';


export default {
  data() {
    return {
      cartItems: [],
      products: [],
      taxRate: 0.07,
      stripe: null,
      totCost: 0,
    };
  },
  computed: {
    cartItemsDisplay() {
      return this.cartItems.map(item => {
        const product = this.products.find(p => p.id === item);
        if (!product) {
          console.error(`Product with id ${item} not found in products list.`);
          return {
            id: item,
            name: 'Unknown Product',
            price: 0
          };
        }
        return {
          ...product,
          price: product.price
        };
      });
    },
    totalCost() {
      return this.cartItemsDisplay.reduce((acc, item) => acc + item.price, 0).toFixed(2);
    },
    tax() {
      return (this.totalCost * this.taxRate).toFixed(2);
    },
    totalCostWithTax() {
      const self = this;
      self.totCost = parseFloat(self.totalCost) + parseFloat(self.tax);
      return (parseFloat(this.totalCost) + parseFloat(this.tax)).toFixed(2);
    }
  },
  methods: {
    getItems() {
      const apiUrl = "https://archit-stripe-server.0jff1935f759s.us-east-1.cs.amazonlightsail.com"
      axios.get(`${apiUrl}/items`)
        .then(response => {
          this.products = response.data.items;
        })
        .catch(error => {
          console.error('There was an error!', error);
        });
    },
    getProductImage(pid) {
      switch (pid) {
        case 1:
          return shirt;
        case 2:
          return sweater;
        case 3:
          return jacket;
        case 4:
          return pants;
        case 5:
          return shoes;
        default:
          return '';
      }
    },
    removeFromCart(productId) {
      this.cartItems = this.cartItems.filter(item => item !== productId);
      localStorage.setItem('cartItems', JSON.stringify(this.cartItems));
    },

    proceedToCheckout() {
      const apiUrl = "https://archit-stripe-server.0jff1935f759s.us-east-1.cs.amazonlightsail.com";
      
      axios.post(`${apiUrl}/create-checkout-session`, {
        cartItems: this.cartItems
      }, {
        headers: {
          'Content-Type': 'application/json',
        }
      })
      .then((response) => {
        const data = response.data;
        return this.stripe.redirectToCheckout({ sessionId: data.sessionId });
      })
      .catch((error) => {
        console.error('Error creating checkout session:', error);
      });
    },
    goToHome() {
      this.$router.push({ path: '/' });
    },
    getStripePublishableKey() {
      const apiUrl = "https://archit-stripe-server.0jff1935f759s.us-east-1.cs.amazonlightsail.com";
      
      axios.get(`${apiUrl}/config`)
        .then((response) => {
          const data = response.data;
          this.stripe = Stripe(data.publicKey);
        })
        .catch((error) => {
          console.error('Error fetching Stripe publishable key:', error);
        });
    },

  },
  created() {
    this.getItems();
    this.getStripePublishableKey();
    this.cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

* {
  font-family: 'Roboto', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

html,
body {
  font-family: 'Roboto', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.cart-page {
  font-family: 'Arial, sans-serif';
  color: #333;
  background: #2f2e2e;
  padding: 20px;
}

header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
  background: linear-gradient(135deg, #462b00, #f1e6c8);
  color: #e5e2e2;
  border-radius: 10px;
  margin-bottom: 20px;
}

header h1 {
  margin: 0;
  font-size: 2.5em;
  letter-spacing: 1px;
}

.cart-content {
  display: flex;
  justify-content: space-between;
}

.cart-items {
  flex: 2;
  margin-right: 20px;
}

.cart-item {
  display: flex;
  align-items: flex-start;
  gap: 20px;
  max-width: 800px;
  margin: 20px auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 10px;
  background: #1f1e1e;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.product-image {
  width: 100px;
  height: auto;
  border-radius: 10px;
  object-fit: cover;
}

.product-details {
  flex-grow: 1;
}

.cart-item h3 {
  margin: 10px 0;
  color: #e52e71;
}

.cart-item p {
  margin: 5px 0;
  text-align: left;
  color: #777;
}

.cart-item .price {
  font-size: 1.2em;
  color: #e5e2e2;
  margin-top: 5px;
}

.remove-button {
  margin: 5px;
  padding: 10px;
  border: none;
  background: #462b00;
  color: #e5e2e2;
  cursor: pointer;
  border-radius: 5px;
  transition: background 0.3s;
}

.remove-button:hover {
  background: #7d4d00;
}

.cart-summary {
  flex: 1;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 10px;
  background: #1f1e1e;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
}

.cart-summary p {
  margin: 10px 0;
  font-size: 1.2em;
  color: #e5e2e2;
}

.checkout-button {
  margin-top: auto;
  padding: 10px;
  border: none;
  background: #462b00;
  color: #e5e2e2;
  cursor: pointer;
  border-radius: 5px;
  width: 100%;
  transition: background 0.3s;
}

.checkout-button:hover {
  background: #7d4d00;
}

.home-button {
  color: #f1e6c8;
  border: none;
  padding: 10px;
  border-radius: 5px;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 8px;
  transition: background-color 0.3s;
}

.home-button svg {
  stroke: rgb(9, 9, 9);
}

.size-6 {
  width: 24px;
  height: 24px;
}
</style>