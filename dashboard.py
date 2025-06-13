import streamlit as st

months = [
    {"month": "Jan 2025", "revenue": 21961.21, "net_income": 6270.38, "rev_mom": 38.91, "ni_mom": 56.77, "rev_goal_pct": 9.81, "ni_goal_pct": 56.77, "cfo_note": "✅ Strong top and bottom line."},
    {"month": "Feb 2025", "revenue": 16009.24, "net_income": -209.55, "rev_mom": -27.11, "ni_mom": -103.34, "rev_goal_pct": -19.95, "ni_goal_pct": -105.24, "cfo_note": "❌ Underperformance—check pricing or costs."},
    {"month": "Mar 2025", "revenue": 18934.77, "net_income": 2993.88, "rev_mom": 18.26, "ni_mom": 1528.64, "rev_goal_pct": -5.33, "ni_goal_pct": -25.15, "cfo_note": "⚠️ Revenue down, but margins recovering."},
    {"month": "Apr 2025", "revenue": 17395.22, "net_income": 4338.07, "rev_mom": -8.13, "ni_mom": 44.80, "rev_goal_pct": -13.02, "ni_goal_pct": 8.45, "cfo_note": "⚖️ Profit strong, revenue a bit low."},
    {"month": "May 2025", "revenue": 18515.85, "net_income": -97.74, "rev_mom": 6.44, "ni_mom": -102.25, "rev_goal_pct": -7.42, "ni_goal_pct": -102.44, "cfo_note": "❌ Underperformance—restrict expenses."}
]

st.set_page_config(layout="wide")
st.title("📊 CrossFit Surf City – Monthly KPI Dashboard")

for i in range(0, len(months), 2):
    col1, col2 = st.columns(2)
    for col, idx in zip([col1, col2], [i, i+1]):
        if idx < len(months):
            m = months[idx]
            with col:
                st.markdown(f"### 📅 {m['month']}")
                st.markdown(f"**Revenue:** ${m['revenue']:,.2f} ({'🔺' if m['rev_goal_pct']>=0 else '🔻'} {abs(m['rev_goal_pct']):.2f}%)")
                st.markdown(f"**Net Income:** ${m['net_income']:,.2f} ({'🔺' if m['ni_goal_pct']>=0 else '🔻'} {abs(m['ni_goal_pct']):.2f}%)")
                st.markdown(f"**Revenue MoM Change:** {m['rev_mom']:+.2f}%")
                st.markdown(f"**Net Income MoM Change:** {m['ni_mom']:+.2f}%")
                st.markdown(f"**🧠 CFO Insight:** {m['cfo_note']}")
                st.markdown("---")
