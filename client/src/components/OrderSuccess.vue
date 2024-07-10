<template>
    <div class="order-success">
      <h1>Thank You for Your Purchase!</h1>
      <p>Your order has been successfully placed.</p>
      <button @click="goToHome">Return to Home</button>
    </div>
  </template>
  
  <script>
  export default {
    methods: {
      goToHome() {
        this.$router.push({ path: '/' });
      }
    },
    created() {
      localStorage.removeItem('cartItems');
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
  
  .order-success {
    text-align: center;
    padding: 50px;
  }
  
  .order-success h1 {
    font-size: 2em;
    margin-bottom: 20px;
  }
  
  .order-success p {
    font-size: 1.2em;
    margin-bottom: 30px;
  }
  
  .order-success button {
    padding: 10px 20px;
    font-size: 1em;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  .order-success button:hover {
    background-color: #45a049; 
  }
  </style>
  