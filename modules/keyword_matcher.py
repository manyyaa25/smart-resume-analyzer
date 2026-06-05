from modules.job_roles import JOB_ROLES


SKILL_ALIASES = {

    "machine learning": [
        "ml"
    ],

    "artificial intelligence": [
        "ai"
    ],

    "javascript": [
        "js"
    ],

    "amazon web services": [
        "aws"
    ],

    "natural language processing": [
        "nlp"
    ],

    "computer vision": [
        "cv"
    ],

    "power bi": [
        "powerbi"
    ],

    "structured query language": [
        "sql"
    ],

    "human resources": [
        "hr"
    ],

    "search engine optimization": [
        "seo"
    ],

    "continuous integration": [
        "ci/cd",
        "cicd"
    ]
}


def skill_exists(skill, resume_text):

    skill = skill.lower()

    if skill in resume_text:
        return True

    aliases = SKILL_ALIASES.get(skill, [])

    for alias in aliases:

        if alias.lower() in resume_text:
            return True

    return False


def calculate_ats_match(resume_text, role):

    required_skills = JOB_ROLES.get(role, [])

    resume_text = resume_text.lower()

    matched_skills = []
    missing_skills = []

    for skill in required_skills:

        if skill_exists(skill, resume_text):

            matched_skills.append(skill)

        else:

            missing_skills.append(skill)

    if len(required_skills) == 0:

        ats_score = 0

    else:

        ats_score = round(
            (len(matched_skills) / len(required_skills)) * 100
        )

    return ats_score, matched_skills, missing_skills