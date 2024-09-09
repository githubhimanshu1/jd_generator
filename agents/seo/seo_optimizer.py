# agents/seo_optimizer.py
import openai
import os
from dotenv import load_dotenv
from utils.seo_keywords import get_seo_keywords

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

class SEOOptimizer:
    def __init__(self, jd_text, job_title):
        self.jd_text = jd_text
        self.job_title = job_title

    def optimize_for_seo(self):
        # Fetch SEO keywords based on job title
        keywords = get_seo_keywords(self.job_title)
        keyword_str = ", ".join(keywords)

        prompt = (
            f"Refine the following job description with SEO keywords to improve its ranking. "
            f"Make sure to naturally integrate these SEO keywords: {keyword_str}. "
            f"Job Description: {self.jd_text}"
        )

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=250
        )
        
        seo_optimized_jd = response.choices[0].text.strip()
        return seo_optimized_jd
