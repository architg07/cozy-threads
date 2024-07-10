<template>
  <div class="home-page">
    <header>
      <h1>Cozy Threads</h1>
      <button class="cart-icon" @click="goToCart">
        <svg 
          fill="none" viewBox="0 0 24 24" 
          stroke-width="1.5" 
          stroke="currentColor" 
          class="size-6"
        >
          <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 3h1.386c.51 0 .955.343 1.087.835l.383 1.437M7.5 14.25a3 3 0 0 0-3 3h15.75m-12.75-3h11.218c1.121-2.3 2.1-4.684 2.924-7.138a60.114 60.114 0 0 0-16.536-1.84M7.5 14.25 5.106 5.272M6 20.25a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0Zm12.75 0a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0Z" />
        </svg>
      </button>
    </header>
    <section class="background-story">
      <h2>Our Story</h2>
      <p>
        Cozy Threads blends comfort, quality, and conscience in every piece. We offer high-quality, ethically-sourced apparel and accessories crafted with organic materials and cruelty-free processes. Our collections are limited edition, ensuring exclusivity and sustainability. Join us in making a statement for style and mindful consumption. Discover Cozy Threads, where luxury meets responsibility.
      </p>
    </section>
    <section class="catalog" ref="catalog">
      <h2>Our Products</h2>
      <div v-for="product in products" :key="product.id" class="product-card">
        <img :src="getProductImage(product.id)" :alt="product.name" class="product-image">
        <div class="product-details">
          <h3>{{ product.name }}</h3>
          <p>{{ product.shortDescription }}</p>
          <p class="price">{{ '$' + product.price }}</p>
          <div class="buttons">
            <button class="cart-button" @click="addToCart(product.id)">Add to Cart</button>
            <button class="info-button" @click="expandProduct(product.id)">More Info</button>
          </div>
          <div v-if="expandedProductId === product.id" class="expanded-info">
            <p>{{ product.longDescription }}</p>
          </div>
        </div>
      </div>
    </section>
    <div v-if="showMessage" class="message">{{ message }}</div>
    <div v-if="showMessageFail" class="messageFail">{{ message }}</div>
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
      products: [],
      expandedProductId: null,
      productsToBuy: [],
      showMessage: false,
      showMessageFail: false,
      message: '',
    };
  },
  methods: {
    getItems() {
      const apiUrl = "https://archit-stripe-server.0jff1935f759s.us-east-1.cs.amazonlightsail.com";
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
    expandProduct(productId) {
      this.expandedProductId = this.expandedProductId === productId ? null : productId;
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
    addToCart(productId) {
      
      let cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];
      if (!cartItems.includes(productId)) {
        cartItems.push(productId);
        localStorage.setItem('cartItems', JSON.stringify(cartItems));
        this.message = 'Item added to cart';
        this.showMessage = true;
        setTimeout(() => {
          this.showMessage = false;
        }, 2000);
      } 
      else {
        this.message = 'Item Already Added to cart';
        this.showMessageFail = true;
        setTimeout(() => {
          this.showMessageFail = false;
        }, 2000);
      }
    },
    goToCart() {
      this.$router.push({ path: '/cart' });
    }
  },
  created() {
    this.getItems();
    this.getStripePublishableKey();
  },
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

* {
  font-family: 'Roboto', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

html, body {
  font-family: 'Roboto', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.home-page {
  color: #e5e2e2;
  background: #1f1e1e;
  padding: 20px;
}

header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
  background: linear-gradient(135deg, #462b00, #f1e6c8);
  color: #333;
  border-radius: 10px;
  margin-bottom: 20px;
}

header h1 {
  margin: 0;
  font-size: 2.5em;
  letter-spacing: 1px;
  text-align: center;
  width: 100%;
}

.cart-icon {
  background: none;
  border: none;
  cursor: pointer;
}

.cart-icon img {
  width: 30px;
  height: 30px;
}

.background-story {
  padding: 40px;
  background: #462b00;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  margin-bottom: 20px;
}

.background-story h2 {
  text-align: center;
  color: #e5e2e2;
}

.background-story p {
  color: #e5e2e2;
}

.catalog {
  padding: 40px;
  background: rgb(70, 43, 0); 
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.catalog h2 {
  text-align: center;
  color: #e5e2e2;
}

.product-card {
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
  width: 250px;
  height: auto;
  border-radius: 10px;
  object-fit: cover;
}

.product-details {
  flex-grow: 1;
}

.product-card h3 {
  margin: 10px 0;
  color: #e52e71;
}

.product-card p {
  margin: 5px 0;
  text-align: left;
  color: #e5e2e2;
}

.product-card .price {
  font-size: 1.2em;
  color: #e5e2e2;
  margin-top: 5px;
}

.buttons {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  margin-top: 10px;
}

.product-card button {
  margin: 5px;
  padding: 10px;
  border: #ddd;
  background: #462b00;
  color: #e5e2e2;
  cursor: pointer;
  border-radius: 5px;
  transition: background 0.3s;
}

.product-card button:hover {
  background: #7d4d00;
}

.expanded-info {
  margin-top: 10px;
  padding: 10px;
  background: #462b00;
  border-radius: 5px;
  box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.1);
  color: #e5e2e2;
}

.size-6 {
  width: 24px;
  height: 24px;
}

.message {
  position: fixed;
  bottom: 20px;
  right: 20px;
  background: #a8e8b0; 
  color: #333;
  padding: 10px 20px;
  border-radius: 5px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: opacity 0.3s ease;
}

.messageFail {
  position: fixed;
  bottom: 20px;
  right: 20px;
  background: #dd5a76; 
  color: #333;
  padding: 10px 20px;
  border-radius: 5px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: opacity 0.3s ease;
}
</style>
