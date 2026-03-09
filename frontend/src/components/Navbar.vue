<template>
  <nav class="navbar">
    <div class="logo">
      Swad Pure Veg
    </div>

    <ul class="nav-links">
      <li><router-link to="/">Home</router-link></li>
      <li><router-link to="/menu">Menu</router-link></li>
      <li><router-link to="/about">About</router-link></li>
      <li><router-link to="/contact">Contact</router-link></li>
    </ul>
  </nav>
</template>

<script setup>

</script>

<style scoped>

.navbar{
  display:flex;
  justify-content:space-between;
  align-items:center;
  padding:15px 40px;
  background:#e45604;
  color:white;
  width: 100%;
  height: 6rem;
}

.logo{
  font-size:22px;
  font-weight:bold;
}

.nav-links{
  display:flex;
  list-style:none;
  gap:25px;
}

.nav-links a{
  text-decoration:none;
  color:white;
  font-weight: 500;
  font-size: large;

}


/* active page underline */
.nav-links a.router-link-active{
  border-bottom:2px solid #ffffff;
}


</style>