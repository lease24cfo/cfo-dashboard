
import streamlit as st
import pandas as pd

# Sample structured P&L data (placeholder - replace with real data in production)
data = {
    "Month": ["Jan 2025", "Feb 2025", "Mar 2025", "Apr 2025", "May 2025"],
    "Revenue ($)": [21961.43, 16009.24, 18935.33, 17395.27, 18516.35],
    "COGS ($)": [2861.41, 577.72, 674.78, 240.00, 938.90],
    "Gross Profit ($)": [19100.02, 15431.52, 18260.55, 17155.27, 17577.45],
    "Expenses ($)": [12828.86, 14937.08, 15788.58, 13816.38, 17510.48],
    "Net Operating Income ($)": [5690.93, 494.44, 2471.97, 3338.89, 66.53],
    "Other Expenses ($)": [-580.23, -705.34, -1523.47, -1000.00, -165.38],
    "Net Income ($)": [6271.16, -210.90, 2995.44, 4338.89, -98.85]
}
df = pd.DataFrame(data)

# Set page config
st.set_page_config(page_title="CrossFit Surf City | CFO Dashboard", layout="wide")

# Title
st.title("📊 Monthly P&L Summary - CrossFit Surf City")

# Display the full P&L table
st.dataframe(df.style.format({
    "Revenue ($)": "${:,.2f}",
    "COGS ($)": "${:,.2f}",
    "Gross Profit ($)": "${:,.2f}",
    "Expenses ($)": "${:,.2f}",
    "Net Operating Income ($)": "${:,.2f}",
    "Other Expenses ($)": "${:,.2f}",
    "Net Income ($)": "${:,.2f}"
}), use_container_width=True)

