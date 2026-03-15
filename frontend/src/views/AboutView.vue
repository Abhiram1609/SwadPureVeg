<template>
    <div class="about-page">
        <section class="top-banner">
            <h1 class="brand">About Us</h1>
            <h3 class="subtitle">Your Trusted 100% Vegetarian Food restaurant</h3>
        </section>

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

        <section class="features">

            <div class="feature-card">
                <img src="../components/icons/mission.svg" alt="">
                <h3>Our Mission</h3>
                <p>To serve delicious, hygienic, and affordable 100% vegetarian fast food that brings joy to every customer while maintaining the highest standards of quality and service.</p>
            </div>

            <div class="feature-card">
                <img src="../components/icons/vision.svg" alt="">
                <h3>Our Vision</h3>
                <p>To become the most trusted and loved vegetarian fast food restaurant in Navi Mumbai, known for our commitment to quality, innovation, and customer satisfaction.</p>
            </div>

            <div class="feature-card">
                <img src="../components/icons/values.svg" alt="">
                <h3>Our Values</h3>
                <p>Quality, Hygiene, Customer Satisfaction, Affordability, and Integrity — these core values drive everything we do at The Fast Food Co.</p>
            </div>

        </section>

        <section class="different">
            <h1>What Makes Us Different</h1>
            <div class="quality-container">

                <div class="feature-card">
                    <img src="../components/icons/veg.svg" alt="">
                    <h3>100% Vegetarian</h3>
                    <p>To serve delicious, hygienic, and affordable 100% vegetarian fast food that brings joy to every customer while maintaining the highest standards of quality and service.</p>
                </div>
                <div class="feature-card">
                    <img src="../components/icons/fresh.svg" alt="">
                    <h3>Fresh Ingredients</h3>
                    <p>To serve delicious, hygienic, and affordable 100% vegetarian fast food that brings joy to every customer while maintaining the highest standards of quality and service.</p>
                </div>
                <div class="feature-card">
                    <img src="../components/icons/hygiene.svg" alt="">
                    <h3>Hygienic Preparations</h3>
                    <p>To serve delicious, hygienic, and affordable 100% vegetarian fast food that brings joy to every customer while maintaining the highest standards of quality and service.</p>
                </div>
                <div class="feature-card">
                    <img src="../components/icons/service.svg" alt="">
                    <h3>Friendly Service</h3>
                    <p>To serve delicious, hygienic, and affordable 100% vegetarian fast food that brings joy to every customer while maintaining the highest standards of quality and service.</p>
                </div>
                <div class="feature-card">
                    <img src="../components/icons/price.svg" alt="">
                    <h3>Affordable Pricing</h3>
                    <p>To serve delicious, hygienic, and affordable 100% vegetarian fast food that brings joy to every customer while maintaining the highest standards of quality and service.</p>
                </div>
                <div class="feature-card">
                    <img src="../components/icons/conv_location.svg" alt="">
                    <h3>Convenient Location</h3>
                    <p>To serve delicious, hygienic, and affordable 100% vegetarian fast food that brings joy to every customer while maintaining the highest standards of quality and service.</p>
                </div>
            </div>
        </section>

        <section class="sitemap">

        <div class="sitemap-container">

            <!-- Restaurant Info -->
            <div class="sitemap-col">
            <h2>Swad Pure Veg</h2>
            <p>Serving fresh and delicious vegetarian fast food in Navi Mumbai.</p>
            </div>

            <!-- Quick Links -->
            <div class="sitemap-col">
            <h2>Quick Links</h2>
            <ul>
                <li><RouterLink to="/">Home</RouterLink></li>
                <li><RouterLink to="/menu">Menu</RouterLink></li>
                <li><RouterLink to="/about">About</RouterLink></li>
                <li><RouterLink to="/contact">Contact</RouterLink></li>
            </ul>
            </div>

            <!-- Contact -->
            <div class="sitemap-col">
                <h2>Contact</h2>

                <div class="contact-item">
                    <span>📍</span>
                    <p>Silver height, Shop no 6,7,8, Plot no A5, Sector 19B, Ulwe, Navi Mumbai</p>
                </div>

                <div class="contact-item">
                    <span>📞</span>
                    <p>+91 XXXXX XXXXX</p>
                </div>

                <div class="contact-item">
                    <span>🟢</span>
                    <p>WhatsApp Orders Available</p>
                </div>
            </div>

        </div>

    </section>

    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const years = ref(0);
const customers = ref(0);
const items = ref(0);

function animateCount(target, duration, final) {
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
        animateCount(years, 1000, 5);
        animateCount(customers, 1000, 1000);
        animateCount(items, 1000, 50);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.5 });

  const aboutSection = document.querySelector('.about-us');
  if (aboutSection) observer.observe(aboutSection);
});
</script>

<style scoped>

.about-page{
  text-align:center;
  background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
}

.top-banner{
    background: #e05819;
    color: white;
    text-align: center;
    padding: 40px 20px;
    margin: 30px 0;
}

.brand{
font-size:2.2rem;
margin-top: 5%;
}

/* About us */

.about-us{
  display:flex;
  justify-content:center;
  gap:30px;
  padding: 40px 40px;
  flex-wrap:wrap;
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

/* Features */
.features {
  display:flex;
  justify-content:center;
  gap:30px;
  padding:80px 40px;
  background:#eef1f3;
  flex-wrap:wrap;
}

.feature-card{
  width:25%;
  background:rgb(255, 255, 255);
  border-radius:12px;
  padding:30px 20px;
  text-align:center;
  box-shadow:0 2px 15px rgba(0, 0, 0, 0.1);;
  transition:transform 0.2s;
}

.feature-card img{
    width: 60px;
    height: 60px;
    object-fit: contain;
    margin-bottom: 15px;
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
  font-size: 1.5rem;
  font-weight: 500;
}

.feature-card p{
  color:#666;
}

/* Different */
.different{
  padding:80px 40px;
  background:#fff;
  color: black;
}

.different h1{
  font-size:2.5rem;
  margin-bottom:40px;
  font-weight:700;
}
.quality-container{
  display:flex;
  justify-content:center;
  gap:30px;
  flex-wrap:wrap;
}

/* Sitemap  */
.sitemap{
  background: linear-gradient(135deg, #0f172a 0%, #1a2540 100%);
  color:white;
  padding: 20px 40px;
}

.sitemap-container{
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 60px;
}

.sitemap-col{
  padding: 20px;
}

.sitemap-col h2{
  margin-bottom: 20px;
  font-weight: 700;
  font-size: 1.2rem;
  color: #f5f7fa;
  position: relative;
  padding-bottom: 12px;
}

.sitemap-col h2::after{
  content: '';
  position: absolute;
  bottom: 0;
  left: 25%;
  width: 50%;
  height: 3px;
  border-bottom: #e45604 2px solid;
}

.sitemap-col p{
  color: #cbd5e1;
  line-height: 1.6;
  font-size: 0.95rem;
}

.sitemap-col ul{
  list-style:none;
  padding:0;
  margin: 0;
}

.sitemap-col ul li{
  margin-bottom: 12px;
}

.sitemap-col a{
  color: #cbd5e1;
  text-decoration: none;
  transition: all 0.3s ease;
  display: inline-block;
  padding: 4px 0;
  position: relative;
}

.sitemap-col a::after{
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 2px;
  background: #ff7600;
  transition: width 0.3s ease;
}

.sitemap-col a:hover{
  color: #f97316;
}

.sitemap-col a:hover::after{
  width: 100%;
}

.contact-item{
  display: flex;
  align-items: flex-start;
  gap: 12px;
  margin-bottom: 15px;
  padding: 12px 0;
  border-bottom: 1px solid rgba(203, 213, 225, 0.1);
}

.contact-item:last-child{
  border-bottom: none;
}

.contact-item span{
  font-size: 20px;
  flex-shrink: 0;
}

.contact-item p{
  margin: 0;
  line-height: 1.5;
  color: #cbd5e1;
  font-size: 0.95rem;
}

</style>