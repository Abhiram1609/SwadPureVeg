<template>
    <div class="contact-page">
        <section class="top-banner">
            <h1 class="brand">Find Us</h1>
            <h3 class="subtitle">Visit Swad Pure Veg, Ulwe</h3>
        </section>

        <section class="location-container">
            <div class="location-info">
                <h2>Visit Our Restaurant</h2>
                <h3>We're conveniently located near Bamandongri Railway Station, Ulwe. Come experience the best 100% vegetarian fast food in the area.</h3>

                <div class="info-item">
                    <div class="info-title">
                        <span class="info-icon" aria-hidden="true">
                            <img src="../components/icons/location.svg" alt="Location">
                        </span>
                        <h3>Address</h3>
                    </div>
                    <p>
                        Shop No 102,<br />
                        Ananta Towers, Plot No 2, Sector 6,<br />
                        Opposite Bamandongri Railway Station,<br />
                        Ulwe - 410206
                    </p>
                </div>

                <div class="info-item">
                    <div class="info-title">
                        <span class="info-icon" aria-hidden="true">
                            <img src="../components/icons/clock.svg" alt="Clock">
                        </span>
                        <h3>Business Hours</h3>
                    </div>
                    <p>Monday - Sunday: 8:00 AM - 12:00 PM<br /><span class="open">Open Every Day</span></p>
                </div>

                <div class="info-item">
                    <div class="info-title">
                        <span class="info-icon" aria-hidden="true">
                            <img src="../components/icons/call.svg" alt="Call">
                        </span>
                        <h3>Phone</h3>
                    </div>
                    <p><a class="phone-link" href="tel:+919833744979">+91 7709946197</a></p>
                </div>

                <div class="info-item">
                    <div class="info-title">
                        <span class="info-icon" aria-hidden="true">
                            <img src="../components/icons/directions.svg" alt="Get Directions">
                        </span>
                        <h3>Get Directions</h3>
                    </div>
                    <p><a class="directions-link" href="https://www.google.com/maps/dir/?api=1&destination=Swad+Pure+Veg+Restaurant+Ulwe" target="_blank" rel="noopener">Open in Google Maps</a></p>
                </div>

                <div class="buttons">
                    <a class="call-btn" href="tel:+919833744979">Call Us</a>
                    <a class="map-btn" href="https://www.google.com/maps/dir/?api=1&destination=Swad+Pure+Veg+Restaurant+Ulwe" target="_blank" rel="noopener">Open Map</a>
                </div>
            </div>

            <div class="map">
                <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d60369.10580280438!2d72.9496217486328!3d18.972554899999995!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3be7c3739649ba4d%3A0x158bf92448adb109!2sSwad%20Pure%20Veg%20Restaurant!5e0!3m2!1sen!2sus!4v1773425583469!5m2!1sen!2sus" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
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

<script>

</script>

<style scoped>
.contact-page{
    background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
}

.top-banner{
background: #e05819;
color:white;
text-align:center;
padding:40px 20px;
margin-bottom:30px;
}

.brand{
font-size:2.2rem;
margin-top: 5%;
}

/* MAIN SECTION */

.location-container{
  max-width: 1100px;
  margin: auto;
  padding: 60px 20px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 40px;
}

@media (max-width: 900px) {
  .location-container {
    grid-template-columns: 1fr;
  }

  .map iframe {
    height: 360px;
  }
}


/* INFO SECTION */

.location-info h2{
    font-size: 2.5rem;
    color: #2c3e50;
    margin-bottom: 20px;
    font-weight: 700;
}

.location-info p{
  color: #555;
  margin-left: 7%;
}

.location-info h3{
  color: #333;
  margin-bottom: 10px;
}

.info-item{
  margin-top: 25px;
}

.info-item h3{
  margin-bottom: 6px;
  color: #222;
  font-size: 1.5rem;
  font-weight: 700;
}

.info-title{
  display: flex;
  align-items: center;
  gap: 12px;
}

.info-icon svg{
  width: 24px;
  height: 24px;
}

.info-icon img{
  width: 24px;
  height: 24px;

}

.open{
  color: green;
  font-weight: bold;
}

.phone-link,
.directions-link {
  color: #222;
  text-decoration: none;
  font-weight: 600;
}

.phone-link:hover,
.directions-link:hover {
  text-decoration: underline;
}


/* BUTTONS */

.buttons{
  margin-top: 30px;
  display: flex;
  gap: 15px;
}

.call-btn{
  background: #e53900;
  color: white;
  padding: 12px 22px;
  border-radius: 25px;
  text-decoration: none;
}

.map-btn{
  border: 2px solid #e53900;
  color: #e53900;
  padding: 12px 22px;
  border-radius: 25px;
  text-decoration: none;
}

.call-btn:hover{
  background: #c62f00;
}

.map-btn:hover{
  background: #e53900;
  color: white;
}


/* MAP */

.map iframe{
  width: 100%;
  height: 420px;
  border: none;
  border-radius: 12px;
  box-shadow: 0 5px 20px rgba(0,0,0,0.1);
}


/* sitemap  */
.sitemap{
    text-align: center;
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