import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Updated KPI Data
kpi_data = {
    "Month": ["Jan 2025", "Feb 2025", "Mar 2025", "Apr 2025", "May 2025"],
    "Revenue ($)": [21961.21, 16009.24, 18934.77, 17395.22, 18515.85],
    "Net Income ($)": [6270.98, -209.55, 2993.88, 4338.07, -97.74],
    "Revenue vs Goal (%)": [9.81, -19.96, -5.33, -13.02, -7.42],
    "Net Income vs Goal (%)": [56.77, -105.24, -25.15, 8.45, -102.44],
    "Revenue MoM Change (%)": [None, -27.11, 18.26, -8.13, 6.44],
    "Net Income MoM Change (%)": [None, -103.34, 1528.64, 44.80, -102.25]
}

kpi_df = pd.DataFrame(kpi_data)

# Header
st.title("📊 CrossFit Surf City – Monthly KPI Dashboard")
st.markdown("---")

# Visuals per month
for i, row in kpi_df.iterrows():
    st.subheader(f"📅 {row['Month']}")

    rev_color = "green" if row['Revenue vs Goal (%)'] >= 0 else "red"
    ni_color = "green" if row['Net Income vs Goal (%)'] >= 0 else "red"

    st.markdown(f"**Revenue:** <span style='color:{rev_color}'>${row['Revenue ($)']:.2f} ({row['Revenue vs Goal (%)']:+.2f}%)</span>", unsafe_allow_html=True)
    st.markdown(f"**Net Income:** <span style='color:{ni_color}'>${row['Net Income ($)']:.2f} ({row['Net Income vs Goal (%)']:+.2f}%)</span>", unsafe_allow_html=True)

    st.markdown(f"**Revenue MoM Change:** {row['Revenue MoM Change (%)']:+.2f}%" if pd.notnull(row['Revenue MoM Change (%)']) else "")
    st.markdown(f"**Net Income MoM Change:** {row['Net Income MoM Change (%)']:+.2f}%" if pd.notnull(row['Net Income MoM Change (%)']) else "")

    # CFO Insight
    rev_goal = row['Revenue vs Goal (%)']
    ni_goal = row['Net Income vs Goal (%)']
    if rev_goal > 0 and ni_goal > 0:
        commentary = "✔ Strong month: both top-line and bottom-line exceeded expectations."
    elif rev_goal > 0 and ni_goal < 0:
        commentary = "⚠ Revenue hit goal, but margins may need attention — check costs."
    elif rev_goal < 0 and ni_goal > 0:
        commentary = "⚠ Solid profitability despite revenue miss — efficient ops or cost control."
    else:
        commentary = "❌ Underperformance — revisit pricing, expense control, or membership churn."

    st.markdown(f"**🧠 CFO Insight:** {commentary}")
    st.markdown("---")
