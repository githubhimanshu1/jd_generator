# main.py
import sys
import os
print("System Path:", sys.path)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
print("System Path:", sys.path)
try:
    from agents.jd.jd_generator  import JDGenerator
    from agents.seo.seo_optimizer import SEOOptimizer
    from agents.tone_analyzer.tone_analyzer import ToneAnalyzer
except Exception as ex:
    print("error is")
    print(ex)

def main():
    # Input job data
    job_title = "Software Engineer"
    description = "developing software, debugging, and collaborating with teams"
    skills = ["Python", "Django", "REST APIs"]
    location = "Remote"

    # Agent 1: Generate initial JD using AI
    jd_agent = JDGenerator(job_title, description, skills, location)
    initial_jd = jd_agent.generate()
    print("Initial Job Description:")
    print(initial_jd)

    # # Agent 2: Optimize JD for SEO using AI
    # seo_agent = SEOOptimizer(initial_jd, job_title)
    # seo_jd = seo_agent.optimize_for_seo()
    # print("\nSEO-Optimized Job Description:")
    # print(seo_jd)

    # # Agent 3: Analyze tone and technicality using AI
    # tone_agent = ToneAnalyzer(seo_jd)
    # analysis_result = tone_agent.analyze()
    # print("\nTone and Technicality Analysis:")
    # print(f"Tone: {analysis_result['tone']}")
    # print(f"Technicality: {analysis_result['technicality']}")

if __name__ == "__main__":
    main()
