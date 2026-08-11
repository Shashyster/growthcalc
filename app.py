import streamlit as st


st.title("GrowthCalc")

tab1, tab2, tab3= st.tabs(["Investment Calculator", "Retirement Checker", "Tax-Advantaged Comparision"])

with tab1:
    st.write("Calculate your investment growth over time.")
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


with tab2:
    st.write("Calculate your retirement savings and income over time.")
    initial_retirement = st.slider("Initial Retirement Amount", 0, 1000000, 100000)
    current_age = st.slider("Current Age", 18, 70, 30)
    retirement_age = st.slider("Retirement Age", 40, 80, 65)
    income = st.slider("Desired Annual Income", 10000, 1000000, 100000)
    r_rate = st.slider("Retirement Annual Return (%)", 0.0, 15.0, 7.0)
    r_monthly = st.slider("Retirement Monthly Contribution", 0, 5000, 300)

    years_to_retirement = retirement_age - current_age
    r_months = years_to_retirement * 12
    r_monthly_rate = r_rate / 100 / 12

    r_balance = initial_retirement
    for i in range(r_months):
        r_balance = r_balance * (1 + r_monthly_rate) + r_monthly

    needed = income / 0.04

    st.metric("Projected Balance at Retirement", f"${r_balance:,.2f}")

    if r_balance >= needed:
        st.success(f"On track! You need about \\${needed:,.2f} to support \\${income:,.2f}/year, and you're projected to have more than that.")
    else:
        gap = needed - r_balance
        st.error(f"Short by \\${gap:,.2f}. You'd need about \\${needed:,.2f} to support \\${income:,.2f}/year.")



with tab3:
    st.write("Compare growth in a taxable vs. tax-advantaged account.")

    t_initial = st.slider("Starting Amount", 0, 200000, 5000, key="t_initial")
    t_monthly = st.slider("Monthly Contribution", 0, 5000, 300, key="t_monthly")
    t_rate = st.slider("Annual Return (%)", 0.0, 15.0, 7.0, key="t_rate")
    t_years = st.slider("Years Invested", 1, 50, 25, key="t_years")
    tax_rate = st.slider("Tax Rate (%)", 0.0, 100.0, 20.0, key="tax_rate")

    t_months = t_years * 12
    t_monthly_rate = t_rate / 100 / 12
    tax_decimal = tax_rate / 100

    adv_balance = t_initial
    adv_history = []

    for i in range(t_months):
        adv_balance = adv_balance * (1 + t_monthly_rate) + t_monthly
        adv_history.append(adv_balance)

    adv_after_tax = adv_balance * (1 - tax_decimal)

    tax_balance = t_initial
    tax_history = []

    for i in range(t_months):
        growth = tax_balance * t_monthly_rate
        after_tax_growth = growth * (1 - tax_decimal)
        tax_balance = tax_balance + after_tax_growth + t_monthly
        tax_history.append(tax_balance)


    col1, col2 = st.columns(2)

    with col1:
        st.metric("Tax_Advantaged Balance", f"\\${adv_after_tax:,.2f}")

    with col2:
        st.metric("Taxable Account Balance", f"\\${tax_balance:,.2f}" )

    st.line_chart({"Tax-Advantaged": adv_history, "Taxable": tax_history})