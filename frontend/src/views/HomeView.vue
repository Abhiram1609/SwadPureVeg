<script setup>
</script>

<template>
  <div class="home">

    <!-- HERO SECTION -->
    <section class="hero">
      <h1>Swad Pure Veg</h1>
      <p>Delicious Pure Vegetarian Food</p>

      <RouterLink to="/menu">
        <button class="menu-btn">View Menu</button>
      </RouterLink>
    </section>

    <!-- CATEGORIES -->
    <section class="categories">
      <h2>Our Categories</h2>

      <div class="category-container">

        <div class="category-card">
          🍔
          <h3>Burgers</h3>
        </div>

        <div class="category-card">
          🌮
          <h3>Chaat</h3>
        </div>

        <div class="category-card">
          🍜
          <h3>Chinese</h3>
        </div>

      </div>
    </section>

  </div>
</template>

<style scoped>

.home{
  text-align:center;
}

/* HERO */

.hero{
  padding:80px 20px;
  background:#f8fafc;
}

.hero h1{
  font-size:48px;
  margin-bottom:10px;
}

.hero p{
  font-size:18px;
  margin-bottom:20px;
}

.menu-btn{
  padding:12px 25px;
  font-size:16px;
  border:none;
  background:#f97316;
  color:white;
  cursor:pointer;
  border-radius:6px;
}

.menu-btn:hover{
  background:#ea580c;
}

/* CATEGORIES */

.categories{
  padding:60px 20px;
}

.category-container{
  display:flex;
  justify-content:center;
  gap:30px;
  margin-top:30px;
}

.category-card{
  width:150px;
  height:120px;
  background:white;
  border-radius:10px;
  box-shadow:0 3px 10px rgba(0,0,0,0.1);
  display:flex;
  flex-direction:column;
  justify-content:center;
  align-items:center;
  font-size:30px;
}

.category-card h3{
  margin-top:10px;
  font-size:16px;
}

</style>