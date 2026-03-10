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
          {{ categoryEmoji(cat) }} {{ cat }} ({{ countByCategory(cat) }})
        </button>
      </div>
    </section>

    <!-- Menu section -->
    <section class="menu-section" v-for="block in groupedMenu" :key="block.category">
      <div class="section-head" @click="toggleSection(block.category)" role="button">
        <div>
          <span class="section-icon">🍔</span>
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
          <div class="style-label">CHOOSE YOUR STYLE:</div>

          <div class="style-options">
            <button
              v-for="style in item.styles"
              :key="style.name"
              :class="['style-btn', { selected: selectedStyle[item.name] === style.name } ]"
              @click="selectStyle(item.name, style.name)">
              <span class="style-name">{{ style.name }}</span>
              <span class="style-price">₹{{ style.price }}</span>
              <span class="add" @click.stop="order(item.name, style)">+ Add</span>
            </button>
          </div>
        </div>
      </div>
    </section>
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
      menu: [
        {
          name: 'Veg Tikki Burger',
          category: 'Burgers',
          styles: [
            { name: 'Plain', price: 70 },
            { name: 'With Schezwan', price: 100 },
            { name: 'With Cheese', price: 100 },
            { name: 'Cheese + Schezwan', price: 120 }
          ]
        },
        {
          name: 'Aloo Tikki Burger',
          category: 'Burgers',
          styles: [
            { name: 'Plain', price: 70 },
            { name: 'With Schezwan', price: 100 },
            { name: 'With Cheese', price: 100 },
            { name: 'Cheese + Schezwan', price: 120 }
          ]
        },
        {
          name: 'Schezwan Burger',
          category: 'Burgers',
          styles: [
            { name: 'Plain', price: 80 },
            { name: 'With Cheese', price: 110 }
          ]
        },
        {
          name: 'Crispy Veggie Burger',
          category: 'Burgers',
          styles: [
            { name: 'Plain', price: 80 },
            { name: 'With Schezwan', price: 110 },
            { name: 'With Cheese', price: 110 },
            { name: 'Cheese + Schezwan', price: 130 }
          ]
        },
        {
          name: 'Paneer Butter masala',
          category: 'Main Course',
        //   styles: [
        //     { name: 'Plain', price: 80 },
        //     { name: 'With Schezwan', price: 110 },
        //     { name: 'With Cheese', price: 110 },
        //     { name: 'Cheese + Schezwan', price: 130 }
        //   ]
        },
        {
          name: 'Paneer mutter masala',
          category: 'Main Course',
        //   styles: [
        //     { name: 'Plain', price: 80 },
        //     { name: 'With Schezwan', price: 110 },
        //     { name: 'With Cheese', price: 110 },
        //     { name: 'Cheese + Schezwan', price: 130 }
        //   ]
        },
        {
          name: 'Paneer Butter masala',
          category: 'Main Course',
        //   styles: [
        //     { name: 'Plain', price: 80 },
        //     { name: 'With Schezwan', price: 110 },
        //     { name: 'With Cheese', price: 110 },
        //     { name: 'Cheese + Schezwan', price: 130 }
        //   ]
        },
        {
          name: 'Paneer Butter masala',
          category: 'Main Course',
        //   styles: [
        //     { name: 'Plain', price: 80 },
        //     { name: 'With Schezwan', price: 110 },
        //     { name: 'With Cheese', price: 110 },
        //     { name: 'Cheese + Schezwan', price: 130 }
        //   ]
        }
      ]
    }
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
    }
  },
  methods: {
    categoryEmoji(cat) {
      const map = { Burgers: '🍔', Chaat: '🥗', Snacks: '🍟', Chinese: '🥡', Drinks: '🥤', Juices: '🧃', Milkshakes: '🥛', Mocktails: '🍹' }
      return map[cat] || '🍴'
    },
    countByCategory(cat) {
      return this.menu.filter((item) => item.category === cat).length
    },
    selectStyle(itemName, styleName) {
      this.$set ? this.$set(this.selectedStyle, itemName, styleName) : (this.selectedStyle[itemName] = styleName)
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
    order(itemName, style) {
      const phone = '919999999999'
      const message = `Hello, I want to order ${itemName} (${style.name} ₹${style.price})`
      window.open(`https://wa.me/${phone}?text=${encodeURIComponent(message)}`, '_blank')
    }
  }
}
</script>

<style scoped>
.menu-page {
  font-family: 'Poppins', sans-serif;
  color: #083b2a;
  background: #f4fff7;
  min-height: 100vh;
  padding-bottom: 40px;
}

.top-banner {
  background: linear-gradient(145deg, #00c75f, #00a54f);
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
