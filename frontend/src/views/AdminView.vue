<template>
    <div class="admin-page">
        <section class="top-banner">
            <h1 class="brand">Swad Pure Veg Menu Admin Portal</h1>
            <p class="subtitle">Menu Management Portal</p>
        </section>

        <section class="card">
            <h2>Add Menu Item</h2>

            <div class="form">
                <input v-model="this.newItem.name" placeholder="Item Name" />
                <select v-model="newItem.category" >
                    <option value="" disabled>Select Category</option>
                    <option v-for="cat in categories" :key="cat" :value="cat">{{ cat }}</option>
                </select>
                <input v-model="this.newItem.price" placeholder="Price" type="number" />
                <button @click="this.addMenuItem">Add Item</button>
            </div>
        </section>

        <section class="card">
            <h2>Current Menu</h2>

            <div class="search-bar">
                <input v-model="search" placeholder="Search menu items" />
            </div>

            <div class="menu-list">
                <div v-for="item in filteredMenu" :key="item._id" class="menu-row">
                    <div>
                        <div class="item-name">{{ item.name }}</div>
                        <div class="item-meta">{{ item.category }} - ₹{{ item.price }}</div>
                    </div>
                    <div>
                        <button class="delete-btn" @click="deleteItem(item._id)">Delete</button>
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>

<script>
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';

export default {
    data() {
        return {
            categories: [
                "Indian Starters",
                "Chinese Starters",
                "Main Course",
                "Breads",
                "Rice",
                "Soup",
                "Beverages"
            ],
            menu: [],
            search: "",
            newItem: {
                name: "",
                category: "",
                price: ""
            }
        }
    },

    computed: {
        filteredMenu() {
            const term = this.search.trim().toLowerCase();
            if (!term) return this.menu;
            return this.menu.filter(item => {
                const name = item.name?.toLowerCase() || "";
                const category = item.category?.toLowerCase() || "";
                return name.includes(term) || category.includes(term);
            });
        }
    },

    mounted() {
        this.fetchMenu();
    },

     methods: {

        async fetchMenu() {
            const response = await fetch("http://127.0.0.1:5000/menu");
            this.menu = await response.json();
        },

        async addMenuItem() {

            if(!this.newItem.name || !this.newItem.category || !this.newItem.price) {
                alert("Please fill all fields");
                return;
            }

            await fetch("http://127.0.0.1:5000/menu", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(this.newItem)
            });

            toast(`${this.newItem.name} added successfully!`, {
                autoClose: 1000,
                type: "success"
            });

            this.newItem = { name: "", category: "", price: "" };
            this.fetchMenu();

        },

        async deleteItem(id) {
            await fetch(`http://127.0.0.1:5000/menu/${id}`, {
                method: "DELETE"
            });

            toast("Item deleted successfully!", {
                autoClose: 1000,
                type: "success"
            });

            this.fetchMenu();

        }
    }
}
</script>

<style scoped>

select {
  padding: 10px;
  border-radius: 8px;
  border: 1px solid #ddd;
  width: 200px;
}

.admin-page{
background:#f4fff7;
min-height:100vh;
padding-bottom:40px;
}

.top-banner{
background: #e05819;
color:white;
text-align:center;
padding:40px 20px;
margin:30px 0;
}

.brand{
font-size:2.2rem;
margin-top: 5%;
}

.subtitle{
opacity:.9;
}

.card{
background:white;
max-width:700px;
margin:auto;
margin-bottom:20px;
padding:20px;
border-radius:12px;
box-shadow:0 10px 25px rgba(0,0,0,0.08);
}

.card h2{
color: black;}

.form{
display:flex;
flex-direction:row;
gap:10px;
}

.form input{
padding:10px;
border:1px solid #ddd;
border-radius:8px;
font-size:0.95rem;
}

.form button{
background:#00c75f;
border:none;
color:white;
padding:10px;
border-radius:8px;
font-weight:700;
cursor:pointer;
}

.search-bar {
  margin: 15px 0;
}

.search-bar input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 8px;
  font-size: 0.95rem;
}

.menu-list{
display:flex;
flex-direction:column;
gap:10px;
}

.menu-row{
display:flex;
justify-content:space-between;
align-items:center;
padding:10px;
border:1px solid #e8f5ea;
border-radius:8px;
background:#f9fffb;
}

.item-name{
font-weight:700;
color: black;
}

.item-meta{
font-size:.85rem;
color:#5a6f5d;
}

.delete-btn{
background:#ff5252;
border:none;
color:white;
padding:6px 10px;
border-radius:6px;
cursor:pointer;
}

</style>
