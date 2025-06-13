import streamlit as st

# Monthly KPI data
months = [
    {
        "Month": "January",
        "Revenue": 21961.43,
        "Expenses": 13364.44,
        "Net Income": 6271.16,
        "Revenue Goal": 20000,
        "Expense Goal": 14000,
        "Net Income Goal": 4000,
        "YTD Revenue": 21961.43,
        "YTD Expenses": 13364.44,
        "YTD Net Income": 6271.16
    },
    {
        "Month": "February",
        "Revenue": 16009.24,
        "Expenses": 16055.92,
        "Net Income": -210.93,
        "Revenue Goal": 20000,
        "Expense Goal": 14000,
        "Net Income Goal": 4000,
        "YTD Revenue": 37970.67,
        "YTD Expenses": 29420.36,
        "YTD Net Income": 6060.23
    },
    {
        "Month": "March",
        "Revenue": 18935.33,
        "Expenses": 15940.56,
        "Net Income": 2994.77,
        "Revenue Goal": 20000,
        "Expense Goal": 14000,
        "Net Income Goal": 4000,
        "YTD Revenue": 56906.00,
        "YTD Expenses": 45360.92,
        "YTD Net Income": 9055.00
    },
    {
        "Month": "April",
        "Revenue": 17395.27,
        "Expenses": 13056.42,
        "Net Income": 4338.85,
        "Revenue Goal": 20000,
        "Expense Goal": 14000,
        "Net Income Goal": 4000,
        "YTD Revenue": 74301.27,
        "YTD Expenses": 58417.34,
        "YTD Net Income": 13393.85
    },
    {
        "Month": "May",
        "Revenue": 18516.35,
        "Expenses": 18615.20,
        "Net Income": -98.85,
        "Revenue Goal": 20000,
        "Expense Goal": 14000,
        "Net Income Goal": 4000,
        "YTD Revenue": 92817.62,
        "YTD Expenses": 77032.54,
        "YTD Net Income": 13295.00
    }
]

st.title("📅 Monthly KPI Dashboard – Final Visual Layout")

def colored_label(value):
    color = "green" if value >= 0 else "red"
    sign = "+" if value >= 0 else ""
    return f":{color}[{sign}{value:.2f}%]"

def percent_delta(current, previous):
    if previous == 0:
        return 0.0
    return ((current - previous) / previous) * 100

for i, m in enumerate(months):
    st.subheader(f"📌 {m['Month']}")

    col1, col2, col3 = st.columns(3)

    with col1:
        revenue_delta = ((m['Revenue'] - m['Revenue Goal']) / m['Revenue Goal']) * 100
        ytd_revenue_goal = m["Revenue Goal"] * (i + 1)
        ytd_revenue_delta = ((m['YTD Revenue'] - ytd_revenue_goal) / ytd_revenue_goal) * 100
        revenue_mom = percent_delta(m["Revenue"], months[i - 1]["Revenue"]) if i > 0 else 0

        st.metric("Revenue", f"${m['Revenue']:,.2f}")
        st.markdown(f"**Monthly Goal %:** {colored_label(revenue_delta)}")
        st.markdown(f"**MoM % Change:** {colored_label(revenue_mom)}")
        st.metric("YTD Revenue", f"${m['YTD Revenue']:,.2f}")
        st.markdown(f"**YTD Goal %:** {colored_label(ytd_revenue_delta)}")

    with col2:
        expense_delta = ((m['Expenses'] - m['Expense Goal']) / m['Expense Goal']) * 100
        ytd_expense_goal = m["Expense Goal"] * (i + 1)
        ytd_expense_delta = ((m['YTD Expenses'] - ytd_expense_goal) / ytd_expense_goal) * 100
        expense_mom = percent_delta(m["Expenses"], months[i - 1]["Expenses"]) if i > 0 else 0

        st.metric("Expenses", f"${m['Expenses']:,.2f}")
        st.markdown(f"**Monthly Goal %:** {colored_label(expense_delta)}")
        st.markdown(f"**MoM % Change:** {colored_label(expense_mom)}")
        st.metric("YTD Expenses", f"${m['YTD Expenses']:,.2f}")
        st.markdown(f"**YTD Goal %:** {colored_label(ytd_expense_delta)}")

    with col3:
        income_delta = ((m['Net Income'] - m['Net Income Goal']) / m['Net Income Goal']) * 100
        ytd_income_goal = m["Net Income Goal"] * (i + 1)
        ytd_income_delta = ((m['YTD Net Income'] - ytd_income_goal) / ytd_income_goal) * 100
        income_mom = percent_delta(m["Net Income"], months[i - 1]["Net Income"]) if i > 0 else 0

        st.metric("Net Income", f"${m['Net Income']:,.2f}")
        st.markdown(f"**Monthly Goal %:** {colored_label(income_delta)}")
        st.markdown(f"**MoM % Change:** {colored_label(income_mom)}")
        st.metric("YTD Net Income", f"${m['YTD Net Income']:,.2f}")
        st.markdown(f"**YTD Goal %:** {colored_label(ytd_income_delta)}")

    comment = "📈 Strong performance." if m["Net Income"] >= m["Net Income Goal"] else "⚠️ Below target, review margins or revenue gaps."
    st.markdown(f"**CFO Summary:** {comment}")
    st.markdown("---")
