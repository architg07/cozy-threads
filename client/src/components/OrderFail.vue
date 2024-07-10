<template>
    <div class="order-fail">
      <h1>Order Canceled</h1>
      <p>Your order has been canceled. Please try again.</p>
      <button @click="goToCart">Return to Cart</button>
    </div>
  </template>
  
  <script>
  export default {
    methods: {
      goToCart() {
        this.$router.push({ path: '/cart' });
      }
    }
  }
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
  
  .order-fail {
    text-align: center;
    padding: 50px;
  }
  
  .order-fail h1 {
    font-size: 2em;
    margin-bottom: 20px;
  }
  
  .order-fail p {
    font-size: 1.2em;
    margin-bottom: 30px;
  }
  
  .order-fail button {
    padding: 10px 20px;
    font-size: 1em;
    background-color: #f44336;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  .order-fail button:hover {
    background-color: #d32f2f;
  }
  </style>
  