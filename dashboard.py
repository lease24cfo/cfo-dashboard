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
st.title("📊 Monthly KPI Dashboard – Visual Layout")

# Utility functions
def pct_change(current, previous):
    return ((current - previous) / previous) * 100 if previous != 0 else 0

def goal_diff(actual, goal):
    return ((actual - goal) / goal) * 100 if goal != 0 else 0

def label_color(pct):
    return f":{'green' if pct >= 0 else 'red'}[{pct:+.2f}%]"

# Initialize YTD totals
ytd_rev = ytd_exp = ytd_ni = 0
ytd_rev_goal = ytd_exp_goal = ytd_ni_goal = 0

for i, m in enumerate(months):
    st.markdown(f"## 📌 {m['Month']}")

    prev = months[i-1] if i > 0 else m
    ytd_rev += m['Revenue']
    ytd_exp += m['Expenses']
    ytd_ni += m['Net Income']
    ytd_rev_goal += m['Revenue Goal']
    ytd_exp_goal += m['Expense Goal']
    ytd_ni_goal += m['Net Income Goal']

    rev_goal_pct = goal_diff(m['Revenue'], m['Revenue Goal'])
    exp_goal_pct = goal_diff(m['Expenses'], m['Expense Goal'])
    ni_goal_pct = goal_diff(m['Net Income'], m['Net Income Goal'])

    rev_mom = pct_change(m['Revenue'], prev['Revenue']) if i > 0 else 0
    exp_mom = pct_change(m['Expenses'], prev['Expenses']) if i > 0 else 0
    ni_mom = pct_change(m['Net Income'], prev['Net Income']) if i > 0 else 0

    ytd_rev_pct = goal_diff(ytd_rev, ytd_rev_goal)
    ytd_exp_pct = goal_diff(ytd_exp, ytd_exp_goal)
    ytd_ni_pct = goal_diff(ytd_ni, ytd_ni_goal)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Revenue", f"${m['Revenue']:,.2f}")
        st.markdown(f"Monthly Goal: {label_color(rev_goal_pct)}")
        st.markdown(f"MoM Change: {label_color(rev_mom)}")
        st.metric("YTD Revenue", f"${ytd_rev:,.2f}")
        st.markdown(f"YTD Goal: {label_color(ytd_rev_pct)}")

    with col2:
        st.metric("Expenses", f"${m['Expenses']:,.2f}")
        st.markdown(f"Monthly Goal: {label_color(exp_goal_pct)}")
        st.markdown(f"MoM Change: {label_color(exp_mom)}")
        st.metric("YTD Expenses", f"${ytd_exp:,.2f}")
        st.markdown(f"YTD Goal: {label_color(ytd_exp_pct)}")

    with col3:
        st.metric("Net Income", f"${m['Net Income']:,.2f}")
        st.markdown(f"Monthly Goal: {label_color(ni_goal_pct)}")
        st.markdown(f"MoM Change: {label_color(ni_mom)}")
        st.metric("YTD Net Income", f"${ytd_ni:,.2f}")
        st.markdown(f"YTD Goal: {label_color(ytd_ni_pct)}")

    rev_text = "📈 Revenue on pace." if ytd_rev_pct >= 0 else "⚠️ Revenue below goal."
    exp_text = "✅_
