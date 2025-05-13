import streamlit as st
import matplotlib.pyplot as plt
from collections import defaultdict

# ---------- Custom CSS ----------
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
        padding: 2rem;
    }
    h1 {
        color: #3366cc;
        font-family: 'Segoe UI', sans-serif;
    }
    .css-1aumxhk, .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        font-weight: bold;
    }
    .stNumberInput>div>input {
        background-color: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- Session State Init ----------
if "expenses" not in st.session_state:
    st.session_state.expenses = []

if "income" not in st.session_state:
    st.session_state.income = 0.0

if "savings_goal" not in st.session_state:
    st.session_state.savings_goal = 0.0

# ---------- Title ----------
st.markdown("<h1 style='text-align: center;'>💰 Personal Budget Planner App</h1>", unsafe_allow_html=True)

# ---------- Sidebar Inputs ----------
with st.sidebar:
    st.header("🔒 Savings & Income")
    goal = st.number_input("Set monthly savings goal ($)", min_value=0.0, value=st.session_state.savings_goal)
    income = st.number_input("Enter your monthly income ($)", min_value=0.0, value=st.session_state.income)
    st.session_state.savings_goal = goal
    st.session_state.income = income
    st.markdown("---")
    st.write("✨ Plan your expenses wisely!")

# ---------- Add Expense ----------
st.subheader("➕ Add Expense")
with st.form("expense_form"):
    col1, col2 = st.columns(2)
    with col1:
        category = st.selectbox("Category", ["Food", "Housing", "Transport", "Entertainment", "Others"])
    with col2:
        amount = st.number_input("Amount ($)", min_value=0.0, step=1.0)

    submitted = st.form_submit_button("➕ Add")
    if submitted and amount > 0:
        st.session_state.expenses.append({"category": category, "amount": amount})
        st.success(f"✅ Added ${amount:.2f} under **{category}**")

# ---------- Expense Overview ----------
st.subheader("📊 Expense Overview")
category_totals = defaultdict(float)
for expense in st.session_state.expenses:
    category_totals[expense["category"]] += expense["amount"]

if category_totals:
    with st.expander("💼 View breakdown"):
        for cat, total in category_totals.items():
            st.markdown(f"- **{cat}**: `${total:.2f}`")

# ---------- Budget Summary ----------
st.subheader("💡 Budget Summary")
total_expenses = sum(exp["amount"] for exp in st.session_state.expenses)
remaining = st.session_state.income - total_expenses

col1, col2 = st.columns(2)
col1.metric("📉 Total Expenses", f"${total_expenses:.2f}")
col2.metric("💵 Remaining Budget", f"${remaining:.2f}")

# ---------- Savings Goal ----------
st.subheader("🎯 Savings Goal")
if remaining >= goal:
    st.success(f"🎉 You met your goal with **${remaining - goal:.2f}** left!")
else:
    st.warning(f"⚠️ Still need **${goal - remaining:.2f}** to hit your goal.")

# ---------- Pie Chart ----------
st.subheader("📈 Expense Distribution")
if category_totals:
    fig, ax = plt.subplots()
    ax.pie(category_totals.values(), labels=category_totals.keys(), autopct="%1.1f%%", startangle=90)
    ax.set_title("💸 Your Spending by Category")
    st.pyplot(fig)
else:
    st.info("No expenses to show yet. Add one above!")

st.markdown("---")
st.caption("🚀 Phát triển bởi Nguyễn Công Phát - Contact for work: congphatnguyen.work@gmail.com")