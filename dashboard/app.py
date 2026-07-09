from pathlib import Path
import streamlit as st

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Retail Sales Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# LOAD CSS
# ==========================================================

css_path = Path(__file__).parent / "assets" / "style.css"

if css_path.exists():
    with open(css_path) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# ==========================================================
# HERO
# ==========================================================

st.markdown(
"""
<div class="hero">

<h1>📊 Retail Sales Analytics Platform</h1>

<p>
Modern Business Intelligence Dashboard built using
Python, MySQL, SQL, Streamlit & Plotly.
</p>

</div>
""",
unsafe_allow_html=True
)

# ==========================================================
# TECH STACK
# ==========================================================

st.markdown("## 🚀 Technology Stack")

c1,c2,c3,c4,c5=st.columns(5)

c1.metric("🐍 Python","ETL")
c2.metric("🗄 MySQL","Warehouse")
c3.metric("📈 SQL","Analytics")
c4.metric("📊 Streamlit","Dashboard")
c5.metric("📉 Plotly","Visualization")

st.divider()

# ==========================================================
# PROJECT OVERVIEW
# ==========================================================

left,right=st.columns([2,1])

with left:

    st.markdown("""
## 📌 About the Project

This project demonstrates a complete **Retail Data Warehouse**
implemented using a modern analytics stack.

### Key Features

- Automated ETL Pipeline
- Star Schema Data Warehouse
- SQL Analytics
- Business Intelligence Dashboard
- Interactive Charts
- KPI Monitoring
- Customer Insights
- Product Analytics
- Time-based Analysis
- Store Performance
""")

with right:

    st.markdown("""
### 🛠 Tools

- Python

- MySQL

- SQLAlchemy

- Pandas

- Plotly

- Streamlit

- Git

- GitHub
""")

st.divider()

# ==========================================================
# DASHBOARD MODULES
# ==========================================================

st.markdown("## 📚 Dashboard Modules")

r1,r2,r3=st.columns(3)

with r1:

    st.success("📈 Executive Dashboard")

    st.success("👥 Customer Analytics")

with r2:

    st.success("📦 Product Analytics")

    st.success("🏬 Store Analytics")

with r3:

    st.success("📅 Time Analytics")

    st.success("💳 Payment Analytics")

st.divider()

# ==========================================================
# WORKFLOW
# ==========================================================

st.markdown("## ⚙️ Architecture")

st.code(
"""
Raw CSV Data
        │
        ▼
Python ETL
        │
        ▼
MySQL Data Warehouse
        │
        ▼
SQL Views
        │
        ▼
Business Analytics
        │
        ▼
Interactive Streamlit Dashboard
""",
language="text"
)

st.divider()

# ==========================================================
# PROJECT HIGHLIGHTS
# ==========================================================

st.markdown("## ⭐ Highlights")

col1,col2,col3,col4=st.columns(4)

with col1:
    st.metric("Customers","10,000+")

with col2:
    st.metric("Products","1,000+")

with col3:
    st.metric("Sales","500,000+")

with col4:
    st.metric("Reports","6 Dashboards")

st.divider()

# ==========================================================
# FEATURES
# ==========================================================

st.markdown("## 💡 Features")

f1,f2=st.columns(2)

with f1:

    st.info("""
✅ Modern Dashboard

✅ Interactive Filters

✅ KPI Monitoring

✅ Responsive Charts

✅ Download CSV

✅ Search
""")

with f2:

    st.info("""
✅ Customer Insights

✅ Product Analysis

✅ Time Intelligence

✅ Store Analytics

✅ Payment Analytics

✅ Executive Reporting
""")

st.divider()

# ==========================================================
# QUICK START
# ==========================================================

st.success(
"""
👈 Open the sidebar and explore the dashboard modules.

Recommended order:

1. Executive Dashboard

2. Customer Analytics

3. Product Analytics

4. Store Analytics

5. Time Analysis

6. Payment Analysis
"""
)

st.divider()

# ==========================================================
# FOOTER
# ==========================================================

st.markdown(
"""
<div class="footer">

Built with ❤️ using Python • MySQL • Streamlit • Plotly

</div>
""",
unsafe_allow_html=True
)