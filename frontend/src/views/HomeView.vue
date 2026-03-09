<script setup>
import { ref, onMounted } from 'vue';

const years = ref(0);
const customers = ref(0);
const items = ref(0);

function animateCount(target, duration = 2000, final) {
  let start = 0;
  const stepTime = Math.abs(Math.floor(duration / (final || 1)));
  const timer = setInterval(() => {
    start += 1;
    target.value = start;
    if (start >= final) {
      clearInterval(timer);
      target.value = final;
    }
  }, stepTime);
}

onMounted(() => {
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        animateCount(years, 2000, 5);
        animateCount(customers, 2000, 1000);
        animateCount(items, 2000, 50);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.5 });

  const aboutSection = document.querySelector('.about-us');
  if (aboutSection) observer.observe(aboutSection);
});
</script>

<template>
  <div class="home">

    <!-- HERO SECTION -->
    <section class="hero">
      <h1>Welcome to Swad Pure Veg</h1>
      <p>One stop destination for Delicious Pure <span>Vegetarian</span> Food</p>
      <h2>Delicious, Fresh & Hygienic Veg Food in the Heart of Navi Mumbai</h2>

      <div class="button-group">
        <RouterLink to="/menu">
          <button class="menu-btn">View Menu</button>
        </RouterLink>
        <RouterLink to="/location">
          <button class="menu-btn">Get directions</button>
        </RouterLink>
      </div>

      <div class="hero-timing">
        🕛 Open Daily 8:00 AM - 12:00 PM
      </div>
    </section>

    <!-- CATEGORIES -->
    <section class="features">

        <div class="feature-card vegetarian-card">
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

    <!-- ABOUT US -->
    <section class="about-us" id="about">
        <div class="about-container">
            <div class="about-content">
                <h2>About Swad Pure Veg</h2>
                <p>
                    At Swad Pure Veg, we are passionate about serving authentic, delicious vegetarian food
                    that brings people together. Located in the heart of Navi Mumbai, we have been serving
                    our community with fresh, hygienic, and flavorful vegetarian dishes since our establishment.
                </p>
                <p>
                    Our commitment to quality ingredients, traditional cooking methods, and exceptional
                    customer service has made us a beloved destination for food lovers seeking pure
                    vegetarian cuisine. From our signature sandwiches to our daily specials, every dish
                    is prepared with love and care.
                </p>
                <div class="about-stats">
                    <div class="stat">
                        <h3>{{ years }}+</h3>
                        <p>Years of Service</p>
                    </div>
                    <div class="stat">
                        <h3>{{ customers }}+</h3>
                        <p>Happy Customers</p>
                    </div>
                    <div class="stat">
                        <h3>{{ items }}+</h3>
                        <p>Menu Items</p>
                    </div>
                </div>
            </div>
            <div class="about-image">
                <img src="../components/img/swad logo.png" alt="Fresh vegetables at Swad Pure Veg">
            </div>
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
  padding-top: 8%;
  padding-bottom: 5%;
  background: linear-gradient(135deg, rgba(220, 47, 2, 0.75) 0%, rgba(232, 93, 4, 0.75) 100%), url('../components/img/hero-img.jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  min-height: 35rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.hero h1{
  font-size: 3.5rem;
  font-weight: 800;
  margin-bottom: 15px;
  color: white;
  text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.5);
  letter-spacing: -1px;
}

.hero h2{
  color: white;
  margin-bottom: 25px;
  font-size: 1.3rem;
  font-weight: 500;
  text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.4);
  max-width: 800px;
}

.hero p{
  font-size: 1.5rem;
  margin-bottom: 30px;
  color: white;
  font-weight: 500;
  text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.4);
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

.button-group{
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 20px;
  margin-top: 30px;
  flex-wrap: nowrap;
}

.menu-btn{
  padding: 14px 35px;
  font-size: 16px;
  font-weight: 600;
  border: none;
  background: linear-gradient(135deg, #ff7600 0%, #e45604 100%);
  color: white;
  cursor: pointer;
  border-radius: 30px;
  margin: 0 10px;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(255, 118, 0, 0.4);
}

.menu-btn:hover{
  background: linear-gradient(135deg, #ea580c 0%, #d94700 100%);
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(255, 118, 0, 0.6);
}

.menu-btn:active{
  transform: translateY(0);
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

.vegetarian-card{
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.9) 0%, rgba(255, 255, 255, 0.9) 100%), url('../components/img/veg.jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

/* ABOUT US SECTION */

.about-us{
  padding: 80px 40px;
  background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
}


.about-container{
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 60px;
  align-items: center;
}

.about-content h2{
  font-size: 2.5rem;
  color: #2c3e50;
  margin-bottom: 20px;
  font-weight: 700;
}

.about-content h2::after{
  content:'';
  width:60px;
  height:3px;
  background:#e45604;
  display:block;
  margin:10px auto 0;
}

.about-content p{
  font-size: 1.1rem;
  line-height: 1.6;
  color: #555;
  margin-bottom: 15px;
}

.about-stats{
  display: flex;
  gap: 40px;
  margin-top: 30px;
}

.stat{
  text-align: center;
}

.stat h3{
  font-size: 2rem;
  color: #e45604;
  font-weight: 700;
  margin-bottom: 5px;
}

.stat p{
  color: #666;
  font-weight: 500;
}

.about-image img{
  width: 100%;
  height: 300px;
  object-fit: cover;
  border-radius: 12px;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
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