import google.generativeai as genai


def analyze_resume(resume_text):

    models = [
        m.name
        for m in genai.list_models()
        if "generateContent" in m.supported_generation_methods
    ]

    if not models:
        return "No Gemini model available."

    model = genai.GenerativeModel(models[0])

    prompt = f"""
    You are an ATS Resume Analyzer.

    Analyze the following resume and provide:

    1. Resume Summary
    2. Technical Skills
    3. Strengths
    4. Weaknesses
    5. ATS Score out of 100
    6. Suggestions for Improvement

    Resume:

    {resume_text[:15000]}
    """

    response = model.generate_content(prompt)

    return response.text