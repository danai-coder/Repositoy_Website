import streamlit as st
st.markdown("""
<style>
.stApp {
    background-image: url("https://images.unsplash.com/photo-1550751827-4bd374c3f58b");
    background-size: cover;
    background-position: center;
}

.block-container {
    background-color: rgba(255, 255, 255, 0.85);
    padding: 2rem;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# Page config
st.set_page_config(
    page_title="Danai Asefaw | MSc Computer Science | Data Science Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://www.linkedin.com/in/danaiasefaw",
        "Report a bug": "mailto:danaiasefaw@gmail.com",
        "About": "Built using Streamlit for showcasing data science projects"
    }
)
# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Education", "Projects", "Skills", "Contact"])

# Home Page
if page == "Home":
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image("assets/danai.jpg", width=180)

    with col2:
        st.title("Danai Asefaw")
        st.subheader("Data Analyst | Data Scientist")
        st.write("Welcome to my portfolio showcasing data science projects.")

    st.write("""
    Welcome to my portfolio! I specialize in:
    - Data Analysis
    - Machine Learning
    - Web Apps with Streamlit
    """)
elif page == "Education":
    st.title("📚 Education")

    st.subheader("🎓 Master of Science in Computer Science")
    st.write("""
    **American National University — Louisville, KY**  
    *2025 – 2026*  
    """)
    st.write("""
    **Relevant Coursework:**
    """)

    courses = [
        "Computer Networking and Telecommunications",
        "Cloud Computing",
        "Capstone in Computer Science Engineering",
        "Distributed Systems",
        "Practitioner Projects in Computer Science Engineering",
        "Operating Systems",
        "Database Design & Management",
        "Design and Development of Security Architectures",
        "Software Engineering",
        "Big Data Analytics",
        "Web-Based Research Methods",
        "Information Security Project Management"
    ]

    for course in courses:
        st.write(f"• {course}")
    st.subheader("🎓 Professional Certificate in Computer & Data Science")
    st.write("""
    **Massachusetts Institute of Technology (MIT)** — MITx (via edX)  
    *2020 – 2021*  
    Focus Areas:
    - Data Science & Machine Learning  
    - Python Programming  
    - Statistical Analysis  
    """)
    st.subheader("🎓 Bachelor of Medicine")

    st.write("""
    **Orotta School of Medicine and Dental Medicine, Eritrea**  
    *2006 – 2014*
    """)
    
    st.subheader("🏅 Certifications")
    st.markdown("""
    **Data Science & AI**
    - Foundations of Data Science — Coursera  
    - AWS AI Practitioner Challenge  

    **Professional Skills**
    - Na’amal Remote Work Certification  
    - Oyster Remote Ready Certification  

    **Innovation & Leadership**
    - Entrepreneurship, Innovation & Leadership Bootcamp — MIT ReACT  

    **Programming**
    - Learn Java with No Prior Programming Experience — Coursera  
    """)
# Projects Page
elif page == "Projects":
    st.title("Projects")

    project = st.selectbox(
        "Select a project",
        ["Customer Churn Model", "Annual Medical Cost Prediction"]
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
    - Data Analysis & Statistical Modeling
    - SQL
    - Machine Learning & Predictive Modeling
    - Foundational Knowledge in Java and C Programming
    - Streamlit
    """)

# Contact Page
elif page == "Contact":
    st.title("Contact Me")

    st.markdown("📧 Email: [danaiasefaw@gmail.com](mailto:danaiasefaw@gmail.com)")
    st.markdown("🔗 LinkedIn: [linkedin.com/in/danaiasefaw](https://www.linkedin.com/in/danaiasefaw)")
    st.markdown("💻 GitHub: [github.com/danai-coder](https://github.com/danai-coder)")