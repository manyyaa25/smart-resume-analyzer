def generate_feedback(
    resume_text,
    resume_score,
    ats_score,
    missing_skills,
    job_role
):

    feedback = {

        "resume": [],
        "skills": [],
        "experience": [],
        "certifications": []

    }

    resume_text = resume_text.lower()

    # =====================
    # Resume Improvements
    # =====================

    if resume_score < 60:

        feedback["resume"].append(
            "Improve resume structure and overall completeness."
        )

    elif resume_score < 80:

        feedback["resume"].append(
            "Add more detailed projects and achievements."
        )

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

        feedback["resume"].append(
            "Add measurable achievements using numbers and percentages."
        )

    if "linkedin" not in resume_text:

        feedback["resume"].append(
            "Add your LinkedIn profile."
        )

    # =====================
    # Skills Development
    # =====================

    if ats_score < 80:

        feedback["skills"].append(
            f"Improve ATS compatibility for {job_role}."
        )

    if len(missing_skills) > 0:

        top_skills = ", ".join(
            missing_skills[:5]
        )

        feedback["skills"].append(
            f"Learn and add: {top_skills}"
        )

    # =====================
    # Experience Building
    # =====================

    if (

        "internship" not in resume_text
        and "intern" not in resume_text
        and "trainee" not in resume_text

    ):

        feedback["experience"].append(
            "Add internship or practical experience."
        )

    if "project" not in resume_text:

        feedback["experience"].append(
            "Add more practical projects."
        )

    # =====================
    # Certifications
    # =====================

    if (

        "certification" not in resume_text
        and "certificate" not in resume_text
        and "certified" not in resume_text

    ):

        feedback["certifications"].append(
            "Add relevant certifications."
        )

    return feedback