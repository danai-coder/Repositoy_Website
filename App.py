import streamlit as st
st.markdown("""
    <style>
        .main {background-color: #f5f5f5;}
    </style>
""", unsafe_allow_html=True)

# Page config
st.set_page_config(page_title="Danai Portfolio", layout="wide")

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects", "Skills", "Contact"])

# Home Page
if page == "Home":
    st.title("Danai Asefaw")
    st.subheader("Data Analyst | Aspiring Data Scientist")

    st.write("""
    Welcome to my portfolio! I specialize in:
    - Data Analysis
    - Machine Learning
    - Web Apps with Streamlit
    """)

# Projects Page
elif page == "Projects":
    st.title("Projects")

    project = st.selectbox(
        "Select a project",
        ["Customer Churn Model", "Health Risk Dashboard"]
    )

    if project == "Customer Churn Model":
        st.subheader("Customer Churn Prediction")
        st.write("""
        - Built using Python & Scikit-learn
        - Deployed with Streamlit
        - Includes prediction dashboard
        """)
        st.link_button("View App", "https://customer-churn-predic.streamlit.app/")

    elif project == "Annual Medical Cost Prediction":
        st.subheader("Annual Medical Cost Prediction")
        st.write("""
        - Built using Python & Scikit-learn
        - Includes prediction dashboard
        """)

# Skills Page
elif page == "Skills":
    st.title("Skills")

    st.write("""
    - Python (Pandas, NumPy, Scikit-learn)
    - Power BI & Data Visualization
    - SQL
    - Streamlit
    """)

# Contact Page
elif page == "Contact":
    st.title("Contact Me")

    st.markdown("📧 Email: [danaiasefaw@gmail.com](mailto:danaiasefaw@gmail.com)")
    st.markdown("🔗 LinkedIn: [linkedin.com/in/danaiasefaw](https://www.linkedin.com/in/danaiasefaw)")
    st.markdown("💻 GitHub: [github.com/danaiasefaw](https://github.com/danaiasefaw)")