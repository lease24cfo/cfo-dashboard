import streamlit as st
import pandas as pd

# Monthly KPI data
months = [
    {
        "Month": "January",
        "Revenue": 21961.43,
        "Net Income": 6271.16,
        "Revenue Goal": 20000,
        "Net Income Goal": 4000,
        "YTD Revenue": 21961.43,
        "YTD Net Income": 6271.16
    },
    {
        "Month": "February",
        "Revenue": 16009.24,
        "Net Income": -210.93,
        "Revenue Goal": 20000,
        "Net Income Goal": 4000,
        "YTD Revenue": 37970.67,
        "YTD Net Income": 6060.23
    },
    {
        "Month": "March",
        "Revenue": 18935.33,
        "Net Income": 2994.77,
        "Revenue Goal": 20000,
        "Net Income Goal": 4000,
        "YTD Revenue": 56906.00,
        "YTD Net Income": 9055.00
    },
    {
        "Month": "April",
        "Revenue": 17395.27,
        "Net Income": 4338.85,
        "Revenue Goal": 20000,
        "Net Income Goal": 4000,
        "YTD Revenue": 74301.27,
        "YTD Net Income": 13393.85
    },
    {
        "Month": "May",
        "Revenue": 18516.35,
        "Net Income": -98.85,
        "Revenue Goal": 20000,
        "Net Income Goal": 4000,
        "YTD Revenue": 92817.62,
        "YTD Net Income": 13295.00
    }
]

st.title("📅 Monthly KPI Dashboard – Individual Layout")

# Utility to return colored label for goal variance
def colored_label(value):
    color = "green" if value >= 0 else "red"
    sign = "+" if value >= 0 else ""
    return f":{color}[{sign}{value:.2f}%]"

# Display each month as its own section
for i, m in enumerate(months):
    st.subheader(f"📌 {m['Month']}")

    col1, col2 = st.columns(2)
    with col1:
        revenue_delta = ((m['Revenue'] - m['Revenue Goal']) / m['Revenue Goal']) * 100
        ytd_revenue_goal = 20000 * (i + 1)
        ytd_revenue_delta = ((m['YTD Revenue'] - ytd_revenue_goal) / ytd_revenue_goal) * 100

        st.metric("Revenue", f"${m['Revenue']:,.2f}")
        st.markdown(f"**Monthly Goal %:** {colored_label(revenue_delta)}")
        st.metric("YTD Revenue", f"${m['YTD Revenue']:,.2f}")
        st.markdown(f"**YTD Goal %:** {colored_label(ytd_revenue_delta)}")

    with col2:
        income_delta = ((m['Net Income'] - m['Net Income Goal']) / m['Net Income Goal']) * 100
        ytd_income_goal = 4000 * (i + 1)
        ytd_income_delta = ((m['YTD Net Income'] - ytd_income_goal) / ytd_income_goal) * 100

        st.metric("Net Income", f"${m['Net Income']:,.2f}")
        st.markdown(f"**Monthly Goal %:** {colored_label(income_delta)}")
        st.metric("YTD Net Income", f"${m['YTD Net Income']:,.2f}")
        st.markdown(f"**YTD Goal %:** {colored_label(ytd_income_delta)}")

    # Add simple financial commentary
    comment = "📈 Strong performance." if m["Net Income"] >= m["Net Income Goal"] else "⚠️ Below target, review expenses or revenue gaps."
    st.markdown(f"**CFO Summary:** {comment}")

    st.markdown("---")
