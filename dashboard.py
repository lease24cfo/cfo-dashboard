import streamlit as st

# Monthly data based on uploaded financials
months = [
    {"month": "Jan 2025", "revenue": 21961.21, "net_income": 6270.38, "rev_goal": 20000, "ni_goal": 4000, "prev_revenue": None, "prev_income": None},
    {"month": "Feb 2025", "revenue": 16009.24, "net_income": -210.93, "rev_goal": 20000, "ni_goal": 4000, "prev_revenue": 21961.21, "prev_income": 6270.38},
    {"month": "Mar 2025", "revenue": 18934.77, "net_income": 2994.77, "rev_goal": 20000, "ni_goal": 4000, "prev_revenue": 16009.24, "prev_income": -210.93},
    {"month": "Apr 2025", "revenue": 17395.22, "net_income": 4338.85, "rev_goal": 20000, "ni_goal": 4000, "prev_revenue": 18934.77, "prev_income": 2994.77},
    {"month": "May 2025", "revenue": 18515.85, "net_income": -98.85, "rev_goal": 20000, "ni_goal": 4000, "prev_revenue": 17395.22, "prev_income": 4338.85},
]

st.set_page_config(layout="wide")
st.title("📊 CrossFit Surf City – Monthly KPI Dashboard")

def format_pct(value):
    color = "green" if value >= 0 else "red"
    sign = "+" if value >= 0 else ""
    return f":{color}[{sign}{value:.2f}%]"

def generate_summary(income, goal):
    if income >= goal:
        return "✅ Strong performance"
    elif income >= 0:
        return "⚠️ Positive but below target"
    else:
        return "❌ Negative income – review urgently"

# Layout: 2 months per row
for i in range(0, len(months), 2):
    col1, col2 = st.columns(2)

    for col, idx in zip([col1, col2], [i, i+1]):
        if idx >= len(months): continue
        m = months[idx]

        # Goal %s
        rev_goal_pct = ((m["revenue"] - m["rev_goal"]) / m["rev_goal"]) * 100
        ni_goal_pct = ((m["net_income"] - m["ni_goal"]) / m["ni_goal"]) * 100

        # MoM %
        rev_mom = None if m["prev_revenue"] is None else ((m["revenue"] - m["prev_revenue"]) / m["prev_revenue"]) * 100
        ni_mom = None if m["prev_income"] is None else ((m["net_income"] - m["prev_income"]) / abs(m["prev_income"] or 1)) * 100

        with col:
            st.markdown(f"### 📅 {m['month']}")
            st.metric("Revenue", f"${m['revenue']:,.2f}")
            st.markdown(f"**% to Monthly Goal:** {format_pct(rev_goal_pct)}")
            if rev_mom is not None:
                st.markdown(f"**Revenue MoM Change:** {format_pct(rev_mom)}")

            st.metric("Net Income", f"${m['net_income']:,.2f}")
            st.markdown(f"**% to Monthly Goal:** {format_pct(ni_goal_pct)}")
            if ni_mom is not None:
                st.markdown(f"**Net Income MoM Change:** {format_pct(ni_mom)}")

            st.markdown(f"**🧠 CFO Summary:** {generate_summary(m['net_income'], m['ni_goal'])}")
            st.markdown("---")
