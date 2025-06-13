import streamlit as st

st.set_page_config(layout="wide")
st.title("📊 Monthly KPI Dashboard – Jan to May 2025")

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

# Utility to return colored label for goal variance
def colored_label(value):
    color = "green" if value >= 0 else "red"
    sign = "+" if value >= 0 else ""
    return f":{color}[{sign}{value:.2f}%]"

# Render each pair of months side-by-side
for i in range(0, len(months), 2):
    cols = st.columns(2)
    for j in range(2):
        if i + j < len(months):
            m = months[i + j]
            with cols[j]:
                st.subheader(f"📌 {m['Month']}")
                # Revenue Section
                revenue_delta = ((m['Revenue'] - m['Revenue Goal']) / m['Revenue Goal']) * 100
                ytd_revenue_goal = 20000 * (i + j + 1)
                ytd_revenue_delta = ((m['YTD Revenue'] - ytd_revenue_goal) / ytd_revenue_goal) * 100

                st.metric("Revenue", f"${m['Revenue']:,.2f}")
                st.markdown(f"**Monthly Goal %:** {colored_label(revenue_delta)}")
                st.metric("YTD Revenue", f"${m['YTD Revenue']:,.2f}")
                st.markdown(f"**YTD Goal %:** {colored_label(ytd_revenue_delta)}")

                # Expense placeholder (if needed in future)
                # st.metric("Expenses", f"$XX,XXX.XX")

                # Net Income Section
                income_delta = ((m['Net Income'] - m['Net Income Goal']) / m['Net Income Goal']) * 100
                ytd_income_goal = 4000 * (i + j + 1)
                ytd_income_delta = ((m['YTD Net Income'] - ytd_income_goal) / ytd_income_goal) * 100

                st.metric("Net Income", f"${m['Net Income']:,.2f}")
                st.markdown(f"**Monthly Goal %:** {colored_label(income_delta)}")
                st.metric("YTD Net Income", f"${m['YTD Net Income']:,.2f}")
                st.markdown(f"**YTD Goal %:** {colored_label(ytd_income_delta)}")

                # Commentary
                if m['Net Income'] >= m['Net Income Goal']:
                    comment = "📈 Strong performance. On track or better."
                elif m['Net Income'] > 0:
                    comment = "⚠️ Positive income, but below target."
                else:
                    comment = "🔻 Negative income – assess cost controls and revenue strategy."

                st.markdown(f"**CFO Insight:** {comment}")
