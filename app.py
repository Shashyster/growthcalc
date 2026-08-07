import streamlit as st

st.title("GrowthCalc")

initial = st.slider("Starting Amount", 0, 200000, 5000)

monthly = st.slider("Monthly Contribution", 0, 5000, 300)

rate = st.slider("Annual Return (%)", 0.0, 15.0, 7.0)

years = st.slider("Years Invested", 1, 50, 25)

months = years * 12
monthly_rate = rate / 100 / 12


history = []
balance = initial
for i in range(months):
    balance = balance * (1 + monthly_rate) + monthly
    history.append(balance)

st.metric("Ending Balance", f"${balance:,.2f}")
st.line_chart(history)