import streamlit as st
from inventory_data import Product
from inventory_utils import InventoryManager
import pandas as pd

st.set_page_config(page_title="Inventory System", layout="wide")

st.title("📦 Inventory Management System")

inv = InventoryManager()

# Sidebar Navigation
page = st.sidebar.radio("📁 Menu", ["➕ Add Product", "📄 View Inventory", "🔍 Search", "⚠️ Low Stock", "📊 Report"])

if page == "➕ Add Product":
    st.subheader("Add a New Product")
    with st.form("add_form"):
        pid = st.text_input("Product ID")
        name = st.text_input("Product Name")
        price = st.number_input("Price", min_value=0.0)
        qty = st.number_input("Quantity", min_value=0, step=1)
        cat = st.text_input("Category")
        submit = st.form_submit_button("Add Product")

    if submit:
        if pid and name:
            inv.add_product(Product(pid, name, price, qty, cat))
            st.success("✅ Product added!")
        else:
            st.error("❌ ID and Name are required")

elif page == "📄 View Inventory":
    st.subheader("All Products")
    df = inv.to_dataframe()
    if not df.empty:
        st.dataframe(df)
        st.download_button("📥 Download CSV", df.to_csv(index=False), "inventory.csv", "text/csv")
    else:
        st.info("No products found.")

elif page == "🔍 Search":
    st.subheader("Search Products")
    q = st.text_input("Enter keyword")
    if q:
        results = inv.search(q)
        if results:
            st.dataframe(pd.DataFrame(results))
        else:
            st.warning("No matches found.")

elif page == "⚠️ Low Stock":
    st.subheader("Low Stock Products")
    t = st.slider("Threshold", 1, 20, 5)
    low = inv.low_stock(t)
    if low:
        st.dataframe(pd.DataFrame(low))
    else:
        st.success("No low stock alerts!")

elif page == "📊 Report":
    st.subheader("Inventory Report")
    df = inv.to_dataframe()
    if not df.empty:
        total_value = inv.get_total_value()
        st.metric("📦 Total Products", len(df))
        st.metric("💰 Inventory Value", f"₹{total_value}")
        st.bar_chart(df['Quantity'])
    else:
        st.warning("No data to show.")
