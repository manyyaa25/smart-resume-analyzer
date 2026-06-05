import streamlit as st
import google.generativeai as genai
import plotly.express as px
import os
from dotenv import load_dotenv

from modules.pdf_parser import extract_text
from modules.prompts import resume_analysis_prompt
from modules.resume_analyzer import analyze_resume
from modules.ats_checker import calculate_resume_score
from modules.keyword_matcher import calculate_ats_match
from modules.job_roles import JOB_ROLES
from modules.feedback_generator import generate_feedback
from modules.report_generator import generate_pdf_report

def get_resume_grade(score):

    if score >= 90:
        return "A+"

    elif score >= 80:
        return "A"

    elif score >= 70:
        return "B"

    elif score >= 60:
        return "C"

    else:
        return "D"


def get_career_roadmap(job_role):

    roadmaps = {

        "Data Analyst": [

            "Build Sales Analytics Dashboard",
            "Build Customer Churn Analysis Project",
            "Build HR Attrition Dashboard",
            "Earn Google Data Analytics Certification"

        ],

        "Data Scientist": [

            "Build House Price Prediction Project",
            "Participate in Kaggle Competitions",
            "Build Recommendation System",
            "Learn Deep Learning"

        ],

        "AI Engineer": [

            "Build NLP Chatbot",
            "Build Resume Analyzer",
            "Develop Generative AI Applications",
            "Learn Vector Databases"

        ],

        "Frontend Developer": [

            "Build Portfolio Website",
            "Build E-Commerce Frontend",
            "Build Task Management App",
            "Master React"

        ],

        "Backend Developer": [

            "Build REST API Project",
            "Build Authentication System",
            "Build Inventory Management Backend",
            "Learn Docker"

        ],

        "Financial Analyst": [

            "Build DCF Valuation Model",
            "Create Financial Dashboard",
            "Perform Ratio Analysis Project",
            "Prepare for CFA Level 1"

        ],

        "Business Analyst": [

            "Create Business KPI Dashboard",
            "Build Power BI Reports",
            "Perform Market Analysis Case Study",
            "Improve SQL Skills"

        ],

        "Cloud Engineer": [

            "Deploy Applications on AWS",
            "Build CI/CD Pipeline",
            "Learn Terraform",
            "Earn AWS Certification"

        ]

    }

    return roadmaps.get(

        job_role,

        [
            "Build Projects",
            "Gain Experience",
            "Earn Certifications",
            "Improve Domain Knowledge"
        ]

    )
# ==========================
# API CONFIGURATION
# ==========================

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="Smart Resume Analyzer",
    layout="wide"
)

st.title("📄 Smart Resume Analyzer")

st.write(
    "Upload your resume and receive ATS analysis, skill gap detection, smart recommendations, and AI-powered feedback."
)

# ==========================
# SIDEBAR
# ==========================

with st.sidebar:

    st.header("Resume Settings")

    uploaded_file = st.file_uploader(
        "Upload Resume (PDF)",
        type="pdf"
    )

    job_role = st.selectbox(
        "Select Target Role",
        sorted(JOB_ROLES.keys())
    )

# ==========================
# MAIN DASHBOARD
# ==========================

if uploaded_file:

    try:

        text = extract_text(uploaded_file)

        st.success("Resume Uploaded Successfully!")

        # ==========================
        # MODULE 2
        # ==========================

        resume_score = calculate_resume_score(text)

        # ==========================
        # MODULE 3
        # ==========================

        ats_score, matched_skills, missing_skills = (
            calculate_ats_match(
                text,
                job_role
            )
        )
        career_readiness = round(
        (resume_score + ats_score) / 2
        )

        resume_grade = get_resume_grade(
            career_readiness
        )

        ai_analysis = ""

        # ==========================
        # DASHBOARD KPI CARDS
        # ==========================

        tab1, tab2, tab3, tab4 = st.tabs([
        "📊 Dashboard",
        "🧠 Skills Analysis",
        "💡 Recommendations",
        "🤖 AI Review"
    ])
        with tab1:
            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric(
                    "Resume Score",
                    f"{resume_score}/100"
                )

            with col2:
                st.metric(
                    "ATS Match",
                    f"{ats_score}%"
                )

            with col3:
                st.metric(
                    "Career Readiness",
                    f"{career_readiness}%"
                )

            with col4:
                st.metric(
                    "Resume Grade",
                    resume_grade
                )

            st.progress(
                career_readiness / 100
            )
            if career_readiness >= 80:

                st.success(
                    "🟢 Excellent Resume Health"
                )

            elif career_readiness >= 60:

                st.warning(
                    "🟡 Good Resume Health"
                )

            else:

                st.error(
                    "🔴 Needs Improvement"
                )

            chart_data = {
                "Category": [
                    "Matched Skills",
                    "Missing Skills"
                ],
                "Count": [
                    len(matched_skills),
                    len(missing_skills)
                ]
            }

            fig = px.pie(
                chart_data,
                names="Category",
                values="Count",
                title="ATS Skill Match Analysis"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )
            st.subheader(
            "Executive Summary"
            )

            st.markdown(f"""

            🎯 **Target Role:** {job_role}

            🏆 **Resume Grade:** {resume_grade}

            📈 **Career Readiness:** {career_readiness}%

            ✅ **Matched Skills:** {len(matched_skills)}

            ❌ **Missing Skills:** {len(missing_skills)}
            """)

        with tab2:

            with st.expander(
                "Matched Skills"
            ):

                for skill in matched_skills:

                    st.success(skill)

            with st.expander(
                "Missing Skills"
            ):

                for skill in missing_skills:

                    st.error(skill)
        with tab3:

            roadmap = get_career_roadmap(
                job_role
            )

            st.subheader(
                "Career Roadmap"
            )

            for step in roadmap:

                st.success(step)

            feedback = generate_feedback(
                        text,
                        resume_score,
                        ats_score,
                        missing_skills,
                        job_role
                    )
            all_suggestions = []
            for category in feedback.values():
                all_suggestions.extend(category)
            # ==========================
            # RECOMMENDATIONS DISPLAY
            # ==========================

            if not any(feedback.values()):

                st.success(
                    "🎉 Excellent! Your resume is already well optimized for this role."
                )

            else:

                if feedback["resume"]:

                    st.subheader(
                        "📄 Resume Improvements"
                    )

                    for item in feedback["resume"]:

                        st.warning(item)

                if feedback["skills"]:

                    st.subheader(
                        "🛠 Skill Development"
                    )

                    for item in feedback["skills"]:

                        st.info(item)

                if feedback["experience"]:

                    st.subheader(
                        "💼 Experience Building"
                    )

                    for item in feedback["experience"]:

                        st.success(item)

                else:

                    st.subheader(
                        "💼 Experience Building"
                    )

                    st.success(
                        "Excellent! Your resume already includes projects and practical experience."
                    )

                if feedback["certifications"]:

                    st.subheader(
                        "🎓 Certifications"
                    )

                    for item in feedback["certifications"]:

                        st.info(item)

                else:

                    st.subheader(
                        "🎓 Certifications"
                    )

                    st.success(
                        "Relevant certifications detected."
                    )

        
        with tab4:

            if st.button(
                "Generate AI Resume Analysis"
            ):

                with st.spinner(
                    "Analyzing Resume..."
                ):

                    prompt = resume_analysis_prompt(
                        text[:15000]
                    )

                    ai_analysis = analyze_resume(
                        prompt
                    )

                    st.write(
                        ai_analysis
                    )
        
            if ai_analysis:
                generate_pdf_report(
                "resume_report.pdf",
                job_role,
                resume_score,
                ats_score,
                matched_skills,
                missing_skills,
                all_suggestions,
                ai_analysis
            )

                with open(
                    "resume_report.pdf",
                    "rb"
                ) as pdf_file:

                    st.download_button(
                        label="📄 Download PDF Report",
                        data=pdf_file,
                        file_name="resume_report.pdf",
                        mime="application/pdf"
                    )
    except Exception as e:
        st.error(
            f"Technical Error: {e}"
        )   