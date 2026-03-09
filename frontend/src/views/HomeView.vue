<script setup>
</script>

<template>
  <div class="home">

    <!-- HERO SECTION -->
    <section class="hero">
      <h1>Welcome to Swad Pure Veg</h1>
      <p>One stop destination for Delicious Pure <span>Vegetarian</span> Food</p>
      <h2>Delicious, Fresh & Hygienic Veg Food in the Heart of Navi Mumbai</h2>

      <RouterLink to="/menu">
        <button class="menu-btn">View Menu</button>
      </RouterLink>
      <RouterLink to="/location">
        <button class="menu-btn">Get directions</button>
      </RouterLink>

      <div class="hero-timing">
        🕛 Open Daily 8:00 AM - 12:00 PM
      </div>
    </section>

    <!-- CATEGORIES -->
    <section class="features">

        <div class="feature-card">
            <div class="icon">🌿</div>
            <h3>100% Vegetarian</h3>
            <p>Pure veg goodness</p>
        </div>

        <div class="feature-card">
            <div class="icon">⭐</div>
            <h3>Fresh Ingredients</h3>
            <p>Quality guaranteed</p>
        </div>

        <div class="feature-card">
            <div class="icon">⚡</div>
            <h3>Quick Service</h3>
            <p>Fast & efficient</p>
        </div>

        <div class="feature-card">
            <div class="icon">₹</div>
            <h3>Budget Friendly</h3>
            <p>Great value</p>
        </div>

    </section>

    <!-- Customer reviews -->
    <section class="reviews">

        <h2 class="review-title">What Our Customers Say</h2>

        <div class="review-container">

            <div class="review-card">
            <div class="stars">★★★★★</div>

            <p>
                "Best vegetarian fast food in Ulwe! The sandwiches are amazing and
                the prices are very reasonable."
            </p>

            <h4>Priya S.</h4>
            <span>Local Guide</span>
            </div>

            <div class="review-card">
            <div class="stars">★★★★★</div>

            <p>
                "Finally, a pure veg fast food place in Navi Mumbai that delivers
                on taste and quality. Highly recommend!"
            </p>

            <h4>Rahul M.</h4>
            <span>Regular Customer</span>
            </div>

            <div class="review-card">
            <div class="stars">★★★★★</div>

            <p>
                "Great food, great service! Perfect spot for a quick lunch.
                The staff is friendly and the place is always clean."
            </p>

            <h4>Anjali P.</h4>
            <span>Office Worker</span>
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
  margin-top: 6%;
  padding-top: 5%;
  background: linear-gradient(135deg, #dc2f02 0%, #e85d04 100%);
  height: 30rem;
}


.hero h1{
  font-size: 5rem;
  font-weight: bold;
  margin-bottom:10px;
  color: white;
}

.hero h2{
  color: white;
  margin-bottom: 1%;
}

.hero p{
  font-size: 2rem;
  margin-bottom:20px;
  color: white;
}

.hero-timing{
    margin-top: 30px;
    font-size: 1.1rem;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    animation: fadeInUp 1.8s;
    color: #ffffff;
    font-weight: 600;
    text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.3);
}

.hero span{
    color: rgb(66, 231, 0);
}

.menu-btn{
  padding:12px 25px;
  font-size:16px;
  border:none;
  background:#ff7600;
  color:white;
  cursor:pointer;
  border-radius: 25px;
}

.menu-btn:hover{
  background:#ea580c;
  border-radius: 25px;

}

/* FEATURES */

.features{
  display:flex;
  justify-content:center;
  gap:30px;
  padding:80px 40px;
  background:#eef1f3;
  flex-wrap:wrap;
}

.feature-card{
  width:240px;
  background:white;
  border-radius:12px;
  padding:30px 20px;
  text-align:center;
  box-shadow:0 2px 15px rgba(0, 0, 0, 0.1);;
  transition:transform 0.2s;
}

.feature-card:hover{
  transform:translateY(-5px);
}

.icon{
  font-size:40px;
  color:#e45604;
  margin-bottom:10px;
}

.feature-card h3{
  margin-bottom:8px;
  color: black;
  font-size: x-large;
}

.feature-card p{
  color:#666;
}

/* REVIEWS SECTION */

.reviews{
  background:#eef1f3;
  padding:80px 40px;
  text-align:center;
}

.review-title{
  font-size:50px;
  margin-bottom:50px;
  position:relative;
  color: black;
  font-weight: 600;
}

.review-title::after{
  content:'';
  width:60px;
  height:3px;
  background:#e45604;
  display:block;
  margin:10px auto 0;
}

.review-container{
  display:flex;
  justify-content:center;
  gap:30px;
  flex-wrap:wrap;
}

.review-card{
  background:white;
  width:320px;
  padding:30px;
  border-radius:12px;

  box-shadow:0 6px 15px rgba(0,0,0,0.08);
  text-align:left;
}

.stars{
  color:#f59e0b;
  font-size:20px;
  margin-bottom:15px;
}

.review-card p{
  font-style:italic;
  color:#444;
  margin-bottom:20px;
}

.review-card h4{
  margin:0;
  color: #444;
  font-weight: bold;
}

.review-card span{
  font-size:14px;
  color:#777;
}

</style>