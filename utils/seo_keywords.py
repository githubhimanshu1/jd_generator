# utils/seo_keywords.py
import json

def get_seo_keywords(job_title):
    with open('data/sample_keywords.json', 'r') as f:
        keywords_data = json.load(f)

    return keywords_data.get(job_title.lower(), ["general keyword"])