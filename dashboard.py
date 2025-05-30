import streamlit as st
import pandas as pd

# 🚀 LIVE TEST HEADER
st.markdown("# 🚀 Dashboard Live Test Successful")
st.markdown("_If you're seeing this, the live connection is working!_")

# Title & Date
st.title("CrossFit Surf City – Financial KPI Dashboard")
st.markdown("### Period: Jan–Apr 2025")
st.divider()

# Example KPI data
months = ["Jan 2025", "Feb 2025", "Mar 2025", "Apr 2025"]
kpis = {
    "Revenue ($)": ["$83,716.83", "$84,296.96", "$81,535.59", "$17,395.00"],
    "Goal: Revenue ($)": ["$90,000.00"] * 4,
    "Revenue Variance (%)": ["-6.98%", "-6.34%", "-9.40%", "-80.67%"],
    "Revenue Growth (%)": ["-1.51%", "0.69%", "-3.27%", "-78.66%"],
    "Revenue YOY (%)": ["22.11%", "-5.94%", "5.01%", "-10.76%"],

    "Expenses ($)": ["$61,723.34", "$69,135.39", "$63,933.43", "$13,056.00"],
    "Goal: Expenses ($)": ["$75,000.00"] * 4,
    "Expenses Variance (%)": ["-17.70%", "-7.82%", "-14.75%", "-82.59%"],
    "Expenses YOY (%)": ["34.84%", "5.87%", "-10.61%", "-23.96%"],

    "Net Income ($)": ["$21,993.49", "$15,161.57", "$17,602.16", "$4,339.00"],
    "Goal: Net Income ($)": ["$15,000.00"] * 4,
    "Net Income Variance (%)": ["46.62%", "1.08%", "17.35%", "-71.07%"],
    "Net Income Margin (%)": ["26.27%", "17.98%", "21.59%", "24.94%"],
    "Net Income YOY (%)": ["-1.19%", "-112.48%", "1292.31%", "85.70%"]
}

# Dashboard
for i, month in enumerate(months):
    st.markdown(f"## 📅 {month}")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Revenue", kpis["Revenue ($)"][i], kpis["Revenue Growth (%)"][i])
        st.caption(f"🎯 Goal: {kpis['Goal: Revenue ($)'][i]} | Variance: {kpis['Revenue Variance (%)'][i]}")
        st.caption(f"📉 YOY: {kpis['Revenue YOY (%)'][i]}")
        st.markdown("_Revenue is trending below goal despite YOY growth._")

    with col2:
        st.metric("Expenses", kpis["Expenses ($)"][i])
        st.caption(f"🎯 Goal: {kpis['Goal: Expenses ($)'][i]} | Variance: {kpis['Expenses Variance (%)'][i]}")
        st.caption(f"📉 YOY: {kpis['Expenses YOY (%)'][i]}")
        st.markdown("_Expenses remain controlled, significantly under budget._")

    with col3:
        st.metric("Net Income", kpis["Net Income ($)"][i], kpis["Net Income Margin (%)"][i])
        st.caption(f"🎯 Goal: {kpis['Goal: Net Income ($)'][i]} | Variance: {kpis['Net Income Variance (%)'][i]}")
        st.caption(f"📉 YOY: {kpis['Net Income YOY (%)'][i]}")
        st.markdown("_Profitability improved year-over-year, margin is strong._")

    st.divider()
