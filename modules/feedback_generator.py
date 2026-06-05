def generate_feedback(
    resume_text,
    resume_score,
    ats_score,
    missing_skills,
    job_role
):

    suggestions = []

    resume_text = resume_text.lower()

    # =====================
    # Resume Score Analysis
    # =====================

    if resume_score < 60:

        suggestions.append(
            "Improve resume structure and overall completeness."
        )

    elif resume_score < 80:

        suggestions.append(
            "Resume is good but can be strengthened with more detailed projects and achievements."
        )

    # =====================
    # ATS Analysis
    # =====================

    if ats_score < 50:

        suggestions.append(
            f"Your resume has low ATS compatibility for the role of {job_role}. Add more role-specific keywords."
        )

    elif ats_score < 80:

        suggestions.append(
            f"Your ATS compatibility is moderate. Consider adding more relevant skills for {job_role}."
        )

    # =====================
    # Missing Skills
    # =====================

    if len(missing_skills) > 0:

        top_skills = ", ".join(
            missing_skills[:5]
        )

        suggestions.append(
            f"Consider learning and adding these important skills: {top_skills}."
        )

    # =====================
    # Projects
    # =====================

    if "project" not in resume_text:

        suggestions.append(
            "Add technical or domain-specific projects to showcase practical skills."
        )

    # =====================
    # Certifications
    # =====================

    if (
        "certification" not in resume_text
        and "certificate" not in resume_text
        and "certified" not in resume_text
    ):

        suggestions.append(
            "Include relevant certifications to strengthen your profile."
        )

    # =====================
    # Internship Experience
    # =====================

    if (
        "internship" not in resume_text
        and "intern" not in resume_text
        and "trainee" not in resume_text
    ):

        suggestions.append(
            "Add internship or practical industry experience."
        )

    # =====================
    # LinkedIn
    # =====================

    if "linkedin" not in resume_text:

        suggestions.append(
            "Add your LinkedIn profile link for professional visibility."
        )

    # =====================
    # GitHub
    # =====================

    tech_roles = [

        "Software Engineer",
        "Frontend Developer",
        "Backend Developer",
        "Full Stack Developer",
        "Data Analyst",
        "Data Scientist",
        "AI Engineer",
        "Cloud Engineer",
        "DevOps Engineer",
        "Cyber Security Analyst",
        "Mobile App Developer"
    ]

    if (
        job_role in tech_roles
        and "github" not in resume_text
    ):

        suggestions.append(
            "Add your GitHub profile to showcase projects and technical skills."
        )

    # =====================
    # Quantified Achievements
    # =====================

    achievement_words = [

        "%",
        "improved",
        "increased",
        "reduced",
        "saved",
        "optimized"
    ]

    found = False

    for word in achievement_words:

        if word in resume_text:

            found = True

            break

    if not found:

        suggestions.append(
            "Add measurable achievements using numbers and percentages."
        )

    # =====================
    # Role-Specific Suggestions
    # =====================

    role_suggestions = {

        "Data Analyst":
            "Create Power BI or Tableau dashboard projects.",

        "Data Scientist":
            "Build machine learning projects with real datasets.",

        "AI Engineer":
            "Develop NLP or Generative AI projects.",

        "Cloud Engineer":
            "Earn AWS or Azure cloud certifications.",

        "Financial Analyst":
            "Include valuation and financial modeling projects.",

        "Business Analyst":
            "Add business case studies and dashboard projects.",

        "Digital Marketing Specialist":
            "Showcase marketing campaigns and analytics experience.",

        "HR Executive":
            "Highlight recruitment, onboarding, and employee engagement experience."
    }

    if job_role in role_suggestions:

        suggestions.append(
            role_suggestions[job_role]
        )

    return suggestions