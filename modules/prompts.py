def resume_analysis_prompt(context):

    prompt = f"""
You are an expert ATS Resume Reviewer.

Analyze the resume and provide the response using EXACTLY the following headings:

1. Resume Strength Summary

2. Technical Skills Identified

3. Missing Skills

4. ATS Compatibility Score

5. Resume Improvement Suggestions

6. Recommended Projects

7. Recommended Certifications

Resume:
{context}

Format the answer professionally using clear headings and bullet points.
"""

    return prompt