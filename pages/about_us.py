import streamlit as st

def render_about():

    # ----- Page Title -----
    st.markdown(
        """
        <h1 style='text-align: center; font-size: 36px;
                   background: linear-gradient(90deg, #4f46e5, #6366f1);
                   -webkit-background-clip: text;
                   -webkit-text-fill-color: transparent;
                   font-weight: bold; margin-bottom: 10px;'>
            ℹ️ About Grocery Saving Solution
        </h1>
        <p style='text-align: center; font-size: 18px; color: #d1d5db;'>
            Turning Grocery Data Into Smart Savings
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    # ----- Our Vision -----
    st.header("💡 Our Vision")
    st.write("""
    Grocery Saving Solution is a data-driven platform designed to help customers 
    optimize their grocery spending through intelligent insights and analytics.

    Our goal is to transform raw grocery data into meaningful recommendations 
    that support smarter purchasing decisions.
    """)

    # ----- What We Do -----
    st.header("📊 What We Do")
    st.write("""
    Using machine learning techniques and clustering analysis, we:
    - Analyze customer purchasing behavior
    - Identify spending patterns
    - Provide strategic insights for cost-saving opportunities
    - Support data-driven decision making
    """)

    st.markdown("---")

    # ----- Meet Our Team -----
    st.markdown(
        """
        <h2 style='text-align: center; font-size: 30px;
                   background: linear-gradient(90deg, #4f46e5, #6366f1);
                   -webkit-background-clip: text;
                   -webkit-text-fill-color: transparent;
                   font-weight: bold; margin-bottom: 20px;'>
            👩‍💻 Meet Our Team
        </h2>
        <p style='text-align: center; color: #d1d5db; font-size: 16px; margin-bottom: 40px;'>
            We are a multidisciplinary team Master Students from Data ScienceTech Institute (DSTI).
        </p>
        """,
        unsafe_allow_html=True
    )

    # ----- Team Members -----
    team = [
        {"name": "Nona Shamila SALLAY", "role": "Data Science", "img": "images/shamila.png"},
        {"name": "Dinh Duy TRAN", "role": "Software Engineering", "img": "images/duy.png"},
        {"name": "Viet Linh VU", "role": "Software Engineering", "img": "images/linh.png"},
        {"name": "Kim Yen LE", "role": "Data Analytics", "img": "images/kim.png"}, 
        {"name": "Myat Noe WAI", "role": "Data Analytics", "img": "images/nora.png"},
        {"name": "Doreen Chepkoech KOSKE", "role": "Data Analytics", "img": "images/doren.png"},
        {"name": "Leonardo Mariano HERNANDEZ ECHENIQUE", "role": "Data Analytics", "img": "images/leo.png"},
    ]

    # ----- Display Team (3 per row) -----
    for i in range(0, len(team), 3):
        cols = st.columns(3)

        for idx, col in enumerate(cols):
            if i + idx < len(team):
                member = team[i + idx]

                with col:
                    st.markdown(
                        """
                        <div style='background-color: #1f2937; padding: 25px; 
                                    border-radius: 20px;
                                    text-align: center; 
                                    box-shadow: 0 10px 25px rgba(0,0,0,0.2); 
                                    margin-bottom: 20px;'>
                        """,
                        unsafe_allow_html=True
                    )

                    st.image(member["img"], width=90)

                    st.markdown(
                        f"<h3 style='color:white; margin-top: 15px; font-size:16px; text-align:center;'>{member['name']}</h3>",
                        unsafe_allow_html=True
                    )

                    st.markdown(
                        f"<p style='color:#9ca3af; font-size:14px; text-align:center;'>{member['role']}</p>",
                        unsafe_allow_html=True
                    )

                    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.success("Thank you for visiting Grocery Saving Solution 🚀")