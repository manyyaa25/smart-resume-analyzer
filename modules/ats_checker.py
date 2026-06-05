import re


def calculate_resume_score(text):

    score = 0

    # Contact Information (15)

    email_pattern = r'\S+@\S+'

    phone_pattern = r'\d{10}'

    if re.search(email_pattern, text):
        score += 8

    if re.search(phone_pattern, text):
        score += 7

    # Skills Section (20)

    if "skills" in text.lower():
        score += 20

    # Education Section (15)

    if "education" in text.lower():
        score += 15

    # Projects Section (20)

    if "project" in text.lower():
        score += 20

    # Resume Structure (15)

    if len(text) > 1000:
        score += 15

    # Resume Completeness (15)

    if len(text) > 1500:
        score += 15

    return score