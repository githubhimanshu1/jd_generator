# agents/tone_analyzer.py
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

class ToneAnalyzer:
    def __init__(self, jd_text):
        self.jd_text = jd_text

    def analyze_tone(self):
        prompt = (
            f"Analyze the tone of the following job description and provide feedback on whether "
            f"it has a masculine, feminine, or neutral tone. Job Description: {self.jd_text}"
        )

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100
        )
        
        tone = response.choices[0].text.strip()
        return tone

    def analyze_technicality(self):
        prompt = (
            f"Analyze the technicality of the following job description. "
            f"Give a score from 1 (Non-Technical) to 10 (Highly Technical). "
            f"Job Description: {self.jd_text}"
        )

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=50
        )
        
        technicality_score = response.choices[0].text.strip()
        return technicality_score

    def analyze(self):
        tone_score = self.analyze_tone()
        technicality_score = self.analyze_technicality()

        return {
            'tone': tone_score,
            'technicality': technicality_score
        }
