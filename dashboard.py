import streamlit as st

# Set dark theme and wide layout
st.set_page_config(layout="wide")
st.markdown("""
    <style>
    body {
        background-color: #0e1117;
        color: #f0f0f0;
    }
    .metric {
        font-size: 18px;
    }
    .stMarkdown {
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

# Month data
months = [
    {
        "month": "Jan 2025",
        "revenue": 21961.43,
        "cogs": 0.00,
        "gross_profit": 21961.43,
        "expenses": 13690.27,
        "net_income": 6271.16,
        "rev_goal": 20000,
        "ni_goal": 4000,
        "ytd_revenue": 21961.43,
        "ytd_income": 6271.16,
        "prev_revenue": None,
        "prev_income": None,
        "cfo": "✅ Strong month: both top-line and bottom-line exceeded expectations."
    },
    {
        "month": "Feb 2025",
        "revenue": 16009.24,
        "cogs": 0.00,
        "gross_profit": 16009.24,
        "expenses": 16220.17,
        "net_income": -210.93,
        "rev_goal": 20000,
        "ni_goal": 4000,
        "ytd_revenue": 37970.67,
        "ytd_income": 6060.23,
        "prev_revenue": 21961.43,
        "prev_income": 6271.16,
        "cfo": "❌ Underperformance — revisit pricing, expense control, or membership churn."
    },
    {
        "month": "Mar 2025",
        "revenue": 18935.33,
        "cogs": 0.00,
        "gross_profit": 18935.33,
        "expenses": 15940.56,
        "net_income": 2994.77,
        "rev_goal": 20000,
        "ni_goal": 4000,
        "ytd_revenue": 56906.00,
        "ytd_income": 9055.00,
        "prev_revenue": 16009.24,
        "prev_income": -210.93,
        "cfo": "❌ Underperformance — revisit pricing, expense control, or membership churn."
    },
    {
        "month": "Apr 2025",
        "revenue": 17395.27,
        "cogs": 0.00,
        "gross_profit": 17395.27,
        "expenses": 13056.42,
        "net_income": 4338.85,
        "rev_goal": 20000,
        "ni_goal": 4000,
        "ytd_revenue": 74301.27,
        "ytd_income": 13393.85,
        "prev_revenue": 18935.33,
        "prev_income": 2994.77,
        "cfo": "⚠️ Solid profitability despite revenue miss — efficient ops or cost control."
    },
    {
        "month": "May 2025",
        "revenue": 18515.35,
        "cogs": 0.00,
        "gross_profit": 18515.35,
        "expenses": 18614.20,
        "net_income": -98.85,
        "rev_goal": 20000,
        "ni_goal": 4000,
        "ytd_revenue": 92817.62,
        "ytd_income": 13295.00,
        "prev_revenue": 17395.27,
        "prev_income": 4338.85,
        "cfo": "❌ Underperformance — revisit pricing, expense control, or membership churn."
    }
]

# % Helper
def pct(val, goal): return ((val - goal) / goal) * 100 if goal else 0
def format_pct(val): return f"🟢 {val:+.2f}%" if val >= 0 else f"🔴 {val:+.2f}%"

# Layout
st.title("📊 CrossFit Surf City — Monthly KPI Dashboard")

for i in range(0, len(months), 2):
    cols = st.columns(2)
    for j in range(2):
        if i + j >= len(months): break
        m = months[i + j]

        with cols[j]:
            st.markdown(f"### 📅 {m['month']}")
            st.markdown(f"**Revenue:** ${m['revenue']:,.2f} ({format_pct(pct(m['revenue'], m['rev_goal']))})")
            st.markdown(f"**COGS:** ${m['cogs']:,.2f}")
            st.markdown(f"**Gross Profit:** ${m['gross_profit']:,.2f}")
            st.markdown(f"**Expenses:** ${m['expenses']:,.2f}")
            st.markdown(f"**Net Income:** ${m['net_income']:,.2f} ({format_pct(pct(m['net_income'], m['ni_goal']))})")

            # MoM changes
            if m['prev_revenue'] is not None:
                rev_mom = pct(m['revenue'], m['prev_revenue'])
                ni_mom = pct(m['net_income'], m['prev_income'])
                st.markdown(f"**Revenue MoM Change:** {format_pct(rev_mom)}")
                st.markdown(f"**Net Income MoM Change:** {format_pct(ni_mom)}")

            # YTD
            ytd_rev_goal = m['rev_goal'] * (i + j + 1)
            ytd_ni_goal = m['ni_goal'] * (i + j + 1)
            ytd_rev_pct = pct(m['ytd_revenue'], ytd_rev_goal)
            ytd_ni_pct = pct(m['ytd_income'], ytd_ni_goal)
            st.markdown(f"**YTD Revenue:** ${m['ytd_revenue']:,.2f} ({format_pct(ytd_rev_pct)})")
            st.markdown(f"**YTD Net Income:** ${m['ytd_income']:,.2f} ({format_pct(ytd_ni_pct)})")

            st.markdown(f"**CFO Insight:** {m['cfo']}")
            st.markdown("---")
