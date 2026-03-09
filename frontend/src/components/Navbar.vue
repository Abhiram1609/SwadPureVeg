<template>
  <nav class="navbar">
    <div class="logo">
      <img src="../components/img/swad_logo.svg" alt="Swad Pure Veg Logo" class="logo-image">
      Swad Pure Veg
    </div>

    <ul class="nav-links">
      <li><router-link to="/">Home</router-link></li>
      <li><router-link to="/menu">Menu</router-link></li>
      <li><router-link to="/about">About</router-link></li>
      <li><router-link to="/contact">Contact</router-link></li>
      <li><router-link to="/location">Location</router-link></li>
    </ul>
  </nav>
</template>

<script setup>

</script>

<style scoped>

/* .navbar{
  display:flex;
  justify-content:space-between;
  align-items:center;
  padding:15px 100px;
  background: #ffffff;
  color: #e45604;
  width: 100%;
  height: 6rem;
  position: fixed;
} */

.navbar{
  display:flex;
  justify-content:space-between;
  align-items:center;

  padding:15px 100px;
  background:#ffffff;
  color:#e45604;

  width:100%;
  height:6rem;

  position:fixed;
  top:0;
  left:0;

  z-index:1000;
  box-sizing:border-box;
}

.logo{
  font-size:22px;
  font-weight:bold;
  display: flex;
  align-items: center;
  gap: 0;
}

.logo-image{
  height: 200px;
  width: 200px;
}

.nav-links{
  display:flex;
  list-style:none;
  gap:25px;
}

.nav-links a{
  text-decoration:none;
  color:#000000;
  font-weight: 500;
  font-size: large;
  position: relative;
  transition: color 0.3s ease;
}

.nav-links a::after{
  content: '';
  position: absolute;
  bottom: -5px;
  left: 0;
  width: 0;
  height: 2px;
  background-color: #e45604;
  transition: width 0.3s ease;
}

.nav-links a:hover::after{
  width: 100%;
}


/* active page underline */
.nav-links a.router-link-active{
  border-bottom:none;
}

.nav-links a.router-link-active::after{
  width: 100%;
}


</style>