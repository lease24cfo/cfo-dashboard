import streamlit as st

# Monthly KPI data
months = [
    {"Month": "January", "Revenue": 21961.43, "Expenses": 13364.44, "Net Income": 6271.16, "Revenue Goal": 20000, "Expense Goal": 14000, "Net Income Goal": 4000},
    {"Month": "February", "Revenue": 16009.24, "Expenses": 16055.92, "Net Income": -210.93, "Revenue Goal": 20000, "Expense Goal": 14000, "Net Income Goal": 4000},
    {"Month": "March", "Revenue": 18935.33, "Expenses": 15940.56, "Net Income": 2994.77, "Revenue Goal": 20000, "Expense Goal": 14000, "Net Income Goal": 4000},
    {"Month": "April", "Revenue": 17395.27, "Expenses": 13056.42, "Net Income": 4338.85, "Revenue Goal": 20000, "Expense Goal": 14000, "Net Income Goal": 4000},
    {"Month": "May", "Revenue": 18516.35, "Expenses": 18615.20, "Net Income": -98.85, "Revenue Goal": 20000, "Expense Goal": 14000, "Net Income Goal": 4000}
]

st.set_page_config(layout="wide")
st.title("📊 Monthly KPI Dashboard")

def percent_delta(current, previous):
    return ((current - previous) / previous * 100) if previous != 0 else 0

def goal_percent(actual, goal):
    return ((actual - goal) / goal * 100) if goal != 0 else 0

def colorized_pct(value):
    return f":{'green' if value>=0 else 'red'}[{value:+.2f}%]"

# Initialize YTD accumulators
ytd_rev = ytd_exp = ytd_ni = 0
ytd_rev_goal = ytd_exp_goal = ytd_ni_goal = 0

for i, m in enumerate(months):
    st.subheader(f"📌 {m['Month']}")
    col1, col2, col3 = st.columns(3)

    prev = months[i-1] if i > 0 else m
    rev_mom = percent_delta(m['Revenue'], prev['Revenue'])
    exp_mom = percent_delta(m['Expenses'], prev['Expenses'])
    ni_mom = percent_delta(m['Net Income'], prev['Net Income'])

    ytd_rev += m['Revenue']
    ytd_exp += m['Expenses']
    ytd_ni += m['Net Income']

    ytd_rev_goal += m['Revenue Goal']
    ytd_exp_goal += m['Expense Goal']
    ytd_ni_goal += m['Net Income Goal']

    rev_goal_pct = goal_percent(m['Revenue'], m['Revenue Goal'])
    exp_goal_pct = goal_percent(m['Expenses'], m['Expense Goal'])
    ni_goal_pct = goal_percent(m['Net Income'], m['Net Income Goal'])

    ytd_rev_goal_pct = goal_percent(ytd_rev, ytd_rev_goal)
    ytd_exp_goal_pct = goal_percent(ytd_exp, ytd_exp_goal)
    ytd_ni_goal_pct = goal_percent(ytd_ni, ytd_ni_goal)

    with col1:
        st.metric("Revenue", f"${m['Revenue']:,.2f}")
        st.markdown(f"Monthly Goal %: {colorized_pct(rev_goal_pct)}")
        st.markdown(f"MoM Change: {colorized_pct(rev_mom)}")
        st.metric("YTD Revenue", f"${ytd_rev:,.2f}")
        st.markdown(f"YTD Goal %: {colorized_pct(ytd_rev_goal_pct)}")

    with col2:
        st.metric("Expenses", f"${m['Expenses']:,.2f}")
        st.markdown(f"Monthly Goal %: {colorized_pct(exp_goal_pct)}")
        st.markdown(f"MoM Change: {colorized_pct(exp_mom)}")
        st.metric("YTD Expenses", f"${ytd_exp:,.2f}")
        st.markdown(f"YTD Goal %: {colorized_pct(ytd_exp_goal_pct)}")

    with col3:
        st.metric("Net Income", f"${m['Net Income']:,.2f}")
        st.markdown(f"Monthly Goal %: {colorized_pct(ni_goal_pct)}")
        st.markdown(f"MoM Change: {colorized_pct(ni_mom)}")
        st.metric("YTD Net Income", f"${ytd_ni:,.2f}")
        st.markdown(f"YTD Goal %: {colorized_pct(ytd_ni_goal_pct)}")

    rev_text = "📈 On track." if ytd_rev_goal_pct >= 0 else "⚠️ Behind pace."
    exp_text = "✅ Under budget." if ytd_exp_goal_pct <= 0 else "⚠️ Over budget."
    ni_text = "✅ Profit strong." if ytd_ni_goal_pct >= 0 else "⚠️ Profit behind."

    st.markdown(f"**CFO Summary – Revenue:** {rev_text}  ")
    st.markdown(f"**CFO Summary – Expenses:** {exp_text}  ")
    st.markdown(f"**CFO Summary – Net Income:** {ni_text}")

    st.markdown("---")
