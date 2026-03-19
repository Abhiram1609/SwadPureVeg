<template>
  <nav :class="['navbar', { 'navbar-scrolled': scrolled }]">
    <div class="logo">
      <img src="../components/img/swad_logo.svg" alt="Swad Pure Veg Logo">
      <span>Swad Pure Veg</span>
    </div>

    <div :class="['hamburger', { 'hamburger-scrolled': scrolled }]" @click="toggleMenu" aria-label="Toggle menu" aria-expanded="isMenuOpen">
      <span></span>
      <span></span>
      <span></span>
    </div>

    <div class="cross" @click="closeMenu" :class="{ open: isMenuOpen }"></div>

    <ul :class="['nav-links', {'nav-links-scrolled': scrolled, 'nav-open': isMenuOpen}]">
      <li><router-link to="/" @click="closeMenu">Home</router-link></li>
      <li><router-link to="/menu" @click="closeMenu">Menu</router-link></li>
      <li><router-link to="/about" @click="closeMenu">About</router-link></li>
      <li><router-link to="/contact" @click="closeMenu">Contact</router-link></li>
      <li><router-link to="/admin" @click="closeMenu">Admin</router-link></li>
    </ul>
  </nav>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const scrolled = ref(false)
const isMenuOpen = ref(false)

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value
}

const closeMenu = () => {
  isMenuOpen.value = false
}

const handleScroll = () => {
  const hero = document.querySelector('.hero')
  const heroHeight = hero?.offsetHeight || 500
  scrolled.value = window.scrollY > heroHeight
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>


<style scoped>
.navbar-scrolled{
  background:#e45604 !important;
  transition: 0.3s ease;
  color: #ffffff !important;
}

.navbar{
  display:flex;
  justify-content:space-between;
  align-items:center;

  padding:15px 60px;
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

.logo span{
  margin-left: 50px;
  font-size:22px;
  font-weight:bold;
}

.logo img{
  width: 150px;
  height: 220px;
}

.cross{
  display:none;
  font-size:18px;
  cursor:pointer;
  user-select: none;
}

.hamburger{
  display:none;
  flex-direction:column;
  justify-content:space-between;
  width:28px;
  height:22px;
  cursor:pointer;
}

.hamburger span{
  display:block;
  height:3px;
  width:100%;
  background:#e45604;
  border-radius:2px;
}

.hamburger-scrolled span{
  background:#ffffff;
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

.nav-links-scrolled a{
    color: #ffffff;
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

.nav-links-scrolled a::after{
  background-color: #ffffff;
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

@media (max-width: 480px) {
    .logo img {
        height: 150px;
        width: 100px;
    } 

    .logo span {
        font-size: 18px;
        margin-left: 20px;
    }
    .navbar {
        padding: 10px 16px;
        height: 5rem;
    }
    .nav-links {
        display: none;
        gap: 15px;
        position: absolute;
        top: 100%;
        left: 0;
        width: 100%;
        flex-direction: column;
        background: #ffffff;
        padding: 1rem 0;
        border-top: 1px solid #f0f0f0;
        box-shadow: 0 8px 16px rgba(0,0,0,.1);
        z-index: 999;
    }

    .nav-links.nav-open {
        display: flex;
    }

    .nav-links li {
        padding: 0.6rem 1rem;
    }

    .nav-links a {
        font-size: 1rem;
        font-weight: 600;
        color: #333;
    }

    .cross {
        display: none;
    }

    .cross.open {
        display: block;
        position: absolute;
        right: 16px;
        top: 15px;
        color: #e45604;
        font-weight: 700;
    }

    .hamburger {
        display: flex;
    }
}


</style>