<template>
  <div class="menu-page">
    <!-- Page Header -->
    <section class="top-banner">
      <h1 class="brand">Swad Pure Veg Menu</h1>
      <div class="meta-pills">
        <span class="pill rating">⭐ 5.0 Google Rating</span>
        <span class="pill closed">🔴 Closed • Opens 4 PM</span>
        <span class="pill location">📍 Ulwe, Navi Mumbai</span>
        <span class="pill options">🟠 Jain Options Available</span>
        <span class="pill cart" @click="showCart = true" style="cursor:pointer;">🛒 {{ cartTotalQuantity }} items in cart</span>
      </div>
    </section>

    <!-- Search + Categories -->
    <section class="search-bar-section">
      <input
        type="text"
        v-model="searchQuery"
        placeholder="🔎 Search food..."
        class="search-input"
      />

      <div class="category-scroll">
        <button
          class="category-pill"
          :class="{ active: selectedCategory === '' }"
          @click="selectedCategory = ''"
        >
          🍽 All
        </button>
        <button
          v-for="cat in categories"
          :key="cat"
          class="category-pill"
          :class="{ active: selectedCategory === cat }"
          @click="selectedCategory = cat"
        >
          {{ cat }} ({{ countByCategory(cat) }})
        </button>
      </div>
    </section>

    <div v-if="showCart" class="cart-overlay" @click.self="showCart = false">
      <div class="cart-modal">
        <div class="cart-header">
          <h3>Your Cart ({{ cartTotalQuantity }} items)</h3>
          <button @click="showCart = false" class="close-cart">✕</button>
        </div>

        <div v-if="cartItems.length" class="cart-items">
          <div v-for="entry in cartItems" :key="entry.name" class="cart-item-row">
            <div>
              <div class="cart-item-name">{{ entry.name }}</div>
              <div class="cart-item-meta">₹{{ entry.price }} × {{ entry.quantity }} = ₹{{ entry.subtotal }}</div>
            </div>
            <div class="cart-item-buttons">
              <button @click="changeQuantity(entry, -1)" class="qty-btn">-</button>
              <span>{{ entry.quantity }}</span>
              <button @click="changeQuantity(entry, 1)" class="qty-btn">+</button>
            </div>
          </div>
          <div class="cart-total">Total: ₹{{ cartItems.reduce((acc, item) => acc + item.subtotal, 0) }}</div>
          <button class="checkout-btn" @click="placeOrder">Proceed to Checkout</button>
        </div>
        <div v-else class="cart-empty">Your cart is empty.</div>
      </div>
    </div>

    <!-- Menu section -->
    <section class="menu-section" v-for="block in groupedMenu" :key="block.category">
      <div class="section-head" @click="toggleSection(block.category)" role="button">
        <div>
          <h2>{{ block.category.toUpperCase() }}</h2>
        </div>
        <span class="expand">{{ isCollapsed(block.category) ? '▼' : '▲' }}</span>
      </div>

      <div class="cards-grid" v-show="!isCollapsed(block.category)">
        <div class="menu-card" v-for="item in block.items" :key="item.name">
          <div class="card-header">
            <h3>{{ item.name }}</h3>
            <span class="price">₹{{ item.price }}</span>
          </div>

          <div class="qty-price-section">

              <div class="quantity-control">
                  
                  <!-- SHOW ADD BUTTON -->
                <button
                    v-if="!(itemQuantities[item.name] > 0)"
                    class="add-btn"
                    @click="changeQuantity(item, 1)"
                >
                    + Add
                </button>
            
            <!-- SHOW COUNTER -->
                <div v-else class="qty-box">
                    <button class="qty-btn" @click="changeQuantity(item, -1)">-</button>
                    <span class="qty-label">{{ itemQuantities[item.name] }}</span>
                    <button class="qty-btn" @click="changeQuantity(item, 1)">+</button>
                </div>
            
              </div>
        <!-- <div class="cart-line">Subtotal: ₹{{ (itemQuantities[item.name] || 0) * item.price }}</div> -->
                <div v-if="itemQuantities[item.name]" class="cart-line">
                    {{ itemQuantities[item.name] * item.price }}
                </div>
           </div>
        </div>
      </div>
    </section>

    <!-- Floating Cart Bar -->
    <div v-if="cartTotalQuantity > 0" class="floating-cart" @click="showCart = true">
        <div class="cart-price">
            ₹{{ cartItems.reduce((acc, item) => acc + item.subtotal, 0) }}
        </div>
        <div class="cart-count">{{ cartTotalQuantity }}</div>
        </div>
    </div>
</template>

<script>
export default {
  data() {
    return {
      searchQuery: '',
      selectedCategory: '',
      selectedStyle: {},
      collapsedSections: {},
      itemQuantities: {},
      showCart: false,
      menu: [
      ]
    }
  },
  mounted() {
    this.fetchMenu()
  },
  computed: {
    categories() {
      const unique = new Set(this.menu.map((i) => i.category))
      return [...unique]
    },
    filteredMenu() {
      let items = this.menu
      if (this.searchQuery) {
        const q = this.searchQuery.toLowerCase().trim()
        items = items.filter((i) => i.name.toLowerCase().includes(q) || i.category.toLowerCase().includes(q))
      }
      if (this.selectedCategory) {
        items = items.filter((i) => i.category === this.selectedCategory)
      }
      return items
    },
    groupedMenu() {
      const groups = {}
      this.filteredMenu.forEach((item) => {
        if (!groups[item.category]) groups[item.category] = []
        groups[item.category].push(item)
      })
      return Object.keys(groups).map((category) => ({ category, items: groups[category] }))
    },
    cartTotalQuantity() {
      return Object.values(this.itemQuantities).reduce((sum, qty) => sum + qty, 0)
    },
    cartItems() {
      return Object.entries(this.itemQuantities).map(([name, qty]) => {
        const item = this.menu.find((m) => m.name === name)
        if (!item) return null
        return {
          ...item,
          quantity: qty,
          subtotal: qty * item.price
        }
      }).filter(Boolean)
    }
  },
  methods: {
    countByCategory(cat) {
      return this.menu.filter((item) => item.category === cat).length
    },
    selectStyle(itemName, styleName) {
      this.$set ? this.$set(this.selectedStyle, itemName, styleName) : (this.selectedStyle[itemName] = styleName)
    },
    changeQuantity(item, delta) {
      const key = item.name
      const current = this.itemQuantities[key] || 0
      const next = Math.max(0, current + delta)

      if (next === 0) {
        if (this.$delete) {
          this.$delete(this.itemQuantities, key)
        } else {
          delete this.itemQuantities[key]
        }
      } else {
        this.itemQuantities[key] = next
      }
    },
    isCollapsed(category) {
      return this.collapsedSections[category] || false
    },
    toggleSection(category) {
      const newVal = !this.isCollapsed(category)
      if (this.$set) {
        this.$set(this.collapsedSections, category, newVal)
      } else {
        this.collapsedSections[category] = newVal
      }
    },
    generateOrderMessage() {
      const lines = ['I would like to place the following order:']
      this.cartItems.forEach((item) => {
        lines.push(`${item.name} x ${item.quantity} = ₹${item.subtotal}`)
      })
      const total = this.cartItems.reduce((acc, item) => acc + item.subtotal, 0)
      lines.push(`Total: ₹${total}`)
      return encodeURIComponent(lines.join('\n'))
    },

    placeOrder() {
      const phoneNumber = '917709946197' // Replace with actual phone number
      const message = this.generateOrderMessage()
      const url = `https://wa.me/${phoneNumber}?text=${message}`
      window.open(url, '_blank')
    },
    async fetchMenu() {
    try {

            const response = await fetch("http://localhost:5000/menu")

            const data = await response.json()

            this.menu = data

        } catch (error) {

            console.error("Error loading menu:", error)

        }
    }
  }
}
</script>

<style scoped>

.floating-cart {
  position: fixed;
  bottom: 16px;
  left: 95%;
  transform: translateX(-50%);
  width: fit-content;
  background: #00c75f;
  color: white;
  border-radius: 30px;
  padding: 14px 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-weight: 700;
  box-shadow: 0 10px 25px rgba(0,0,0,0.25);
  cursor: pointer;
  z-index: 2000;
  animation: slideUp 0.25s ease;
}

.cart-summary {
  font-size: 0.95rem;
}

.cart-price {
  font-size: 1.25rem;
  font-weight: bold;
}

.cart-count{
    position: absolute;
    top: -5px;
    right: -5px;
    background: #ef4444;
    color: white;
    border-radius: 50%;
    width: 24px;
    height: 24px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.75rem;
    font-weight: 900;
    border: 2px solid white;
}

.view-cart {
  font-size: 0.9rem;
}

@keyframes slideUp {
  from {
    transform: translate(-50%, 40px);
    opacity: 0;
  }
  to {
    transform: translate(-50%, 0);
    opacity: 1;
  }
}

.menu-page {
  font-family: 'Poppins', sans-serif;
  color: #083b2a;
  background: #f4fff7;
  min-height: 100vh;
  padding-bottom: 40px;
}

.top-banner {
  background: #e05819;
  text-align: center;
  color: #fff;
  padding: 30px 20px 28px;
  margin-top: 70px;
  border-bottom-left-radius: 20px;
  border-bottom-right-radius: 20px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
}

.tag {
  display: inline-flex;
  background: rgba(255, 255, 255, 0.3);
  color: #fff;
  font-weight: 700;
  border-radius: 999px;
  padding: 8px 18px;
  letter-spacing: 0.6px;
  margin-bottom: 10px;
}

.brand {
  font-size: 3rem;
  margin: 6px 0 4px;
  letter-spacing: 1.6px;
}

.subtitle {
  margin-bottom: 12px;
  font-size: 1.1rem;
  font-weight: 500;
  opacity: 0.95;
}

.meta-pills {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 10px;
}

.pill {
  background: #ffffff33;
  border-radius: 999px;
  color: #fff;
  font-weight: 600;
  padding: 7px 14px;
  font-size: .88rem;
}

.closed { background: rgba(255, 69, 69, 0.22); }

.location { background: rgba(255, 255, 255, 0.3); }

.options { background: rgba(255, 163, 61, 0.25); }

.search-bar-section {
  max-width: 1120px;
  margin: 22px auto 12px;
  padding: 0 16px;
}

.search-input {
  width: 100%;
  max-width: 1000px;
  border: 2px solid #00c75f;
  border-radius: 12px;
  padding: 13px 16px;
  font-size: 1rem;
  outline: none;
  box-shadow: 0 5px 16px rgba(0, 0, 0, 0.06);
}

.category-scroll {
  margin-top: 14px;
  display: flex;
  gap: 10px;
  overflow-x: auto;
  padding-bottom: 4px;
}

.category-pill {
  white-space: nowrap;
  border: 1px solid #00af4b;
  border-radius: 999px;
  min-width: 120px;
  padding: 8px 14px;
  font-weight: 600;
  background: #f7fff9;
  color: #064022;
  cursor: pointer;
}

.category-pill.active {
  background: #00c75f;
  color: #fff;
  border-color: #00c75f;
}

.menu-section {
  max-width: 1120px;
  margin: 18px auto 0;
  padding: 0 16px 8px;
}

.section-head {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #ff9f0f;
  border-radius: 14px;
  color: #fff;
  padding: 12px 18px;
  margin-bottom: 10px;
  box-shadow: 0 5px 10px rgba(0,0,0,0.12);
  cursor: pointer;
}

.section-head:hover { background: #ff8a06; }

.section-head h2 {
  margin: 0;
  font-size: 1.5rem;
  letter-spacing: 0.8px;
}

.section-icon { margin-right: 8px; }

.expand { font-size: 0.9rem; }

.cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(238px, 1fr));
  gap: 14px;
}

.menu-card {
  background: #ffffff;
  border: 1px solid #e7f9e9;
  border-radius: 14px;
  box-shadow: 0 8px 18px rgba(0, 0, 0, 0.08);
  padding: 14px;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.card-header h3 {
  font-size: 1.1rem;
  margin: 0;
}

.price {
  font-weight: 800;
  color: #0f9e4a;
}

.qty-price-section {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-top: 2px dashed #e3e3e3;
}

.quantity-control {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  gap: 0.5rem;
  margin: 8px 0;
  border-radius: 8px;
  padding: 0.25rem;
  width: fit-content;
}

.qty-btn {
  width: 25px;
  height: 25px;
  border: 1px solid #00a13e;
  border-radius: 6px;
  background: #00c75f;
  color: #fff;
  font-weight: bold;
  cursor: pointer;
  border: none;
}

.qty-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.qty-label {
  min-width: 22px;
  text-align: center;
  font-weight: 700;
  color: #0f9e4a;
}

.cart-line {
  font-size: 0.85rem;
  color: #1f5f3b;
  font-size: large;
  font-weight: 700;
}

.add-btn{
  background:#00c75f;
  border:none;
  color:white;
  font-weight:700;
  padding:10px 20px;
  border-radius:20px;
  cursor:pointer;
  border: none;
}

.qty-box{
  display:flex;
  align-items:center;
  gap:10px;
  border:2px solid #00c75f;
  border-radius:12px;
  padding:4px 0px;
  border: none;
}

.style-label {
  font-size: 0.8rem;
  font-weight: 700;
  color: #009047;
  margin-bottom: 8px;
}

.style-options {
  display: grid;
  gap: 8px;
}

.style-btn {
  display: grid;
  grid-template-columns: 1fr auto auto;
  align-items: center;
  gap: 10px;
  border: 2px solid #d8f6dd;
  border-radius: 10px;
  padding: 8px 10px;
  background: #f8fff8;
  color: #0a5131;
  font-weight: 600;
  cursor: pointer;
}

.style-btn.selected {
  border-color: #00a13e;
  background: #ebfff0;
}

.style-name { font-size: 0.92rem; }

.style-price { color: #038a30; }

.cart-overlay {
  position: fixed;
  inset: 0;
  background: rgba(7, 14, 12, 0.45);
  z-index: 1500;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 12px;
}

.cart-modal {
  width: min(600px, 100%);
  background: white;
  border-radius: 12px;
  box-shadow: 0 20px 45px rgba(0,0,0,0.25);
  padding: 16px;
  max-height: 80vh;
  overflow-y: auto;
}

.cart-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
}

.close-cart {
  border: 0;
  background: #f0f0f0;
  color: #555;
  border-radius: 999px;
  width: 30px;
  height: 30px;
  font-size: 1rem;
  cursor: pointer;
}

.cart-items {
  display: grid;
  gap: 10px;
}

.cart-item-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border: 1px solid #e7f9e9;
  border-radius: 10px;
  padding: 10px;
  background: #f7fffb;
}

.cart-item-name {
  font-weight: 600;
}

.cart-item-meta {
  color: #6e7c6c;
  font-size: 0.85rem;
}

.cart-item-buttons {
  display: flex;
  align-items: center;
  gap: 8px;
}

.cart-total {
  font-size: 1.1rem;
  font-weight: 700;
  text-align: right;
  margin-top: 8px;
}

.checkout-btn {
  width: 100%;
  margin-top: 12px;
  border: none;
  background: #00c75f;
  color: white;
  border-radius: 8px;
  padding: 10px;
  font-weight: 700;
  cursor: pointer;
}

.cart-empty {
  color: #5f6d60;
  text-align: center;
  padding: 20px;
  font-weight: 600;
}

.add {
  background: #00c75f;
  color: #fff;
  border-radius: 999px;
  padding: 4px 10px;
  font-size: 0.8rem;
  font-weight: 700;
  cursor: pointer;
}

@media (max-width: 780px) {
  .top-banner { margin-top: 80px; }
  .brand { font-size: 2.2rem; }
  .section-head h2 { font-size: 1.2rem; }
}
</style>
