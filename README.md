# Job Description Generator Multi-Agent AI Application

This project is a modular AI-based multi-agent system that automates the generation, refinement, and analysis of job descriptions (JD). It uses OpenAI's GPT models for generating content, embedding SEO keywords, and analyzing tone and technicality.

## Features
- **AI-Generated Job Descriptions**: Generate professional job descriptions based on inputs like job title, responsibilities, required skills, and location.
- **SEO Optimization**: Refine the job description by embedding relevant SEO keywords to increase visibility and ranking on job search engines.
- **Tone and Technicality Analysis**: Analyze the tone (masculine, feminine, or neutral) of the job description and provide a score for its technical complexity.
- **Modular Design**: The project is modular, allowing easy integration of additional agents for future tasks such as diversity checks, grammar analysis, and more.

## Prerequisites

Before you set up this project, ensure you have the following:
- **Python** 3.8 or higher
- **pip** (Python package installer)
- **OpenAI API key** (to access GPT models for job description generation)

## Installation and Setup

### 1. Clone the Repository
First, clone this repository to your local machine:
```bash
git clone https://github.com/yourusername/job_description_generator.git
cd job_description_generator

### 2. Install dependencies
pip install -r requirements.txt

### 3. SEO Keywords (Optional)

SEO keywords for different job titles can be modified or added to the data/sample_keywords.json file. For example: json
{
    "software engineer": ["python developer", "remote software engineer", "backend engineer"],
    "data scientist": ["machine learning", "AI expert", "data mining"]
}


### 4. How to Run
python main.py


Example Workflow
Here’s what happens when you run the program:

JD Generation: The system will first generate an initial job description using OpenAI’s GPT-3 based on your input (e.g., job title, description, required skills, and location).

SEO Optimization: The generated job description will be refined to include relevant SEO keywords to improve search engine visibility.

Tone and Technicality Analysis: The refined job description will be analyzed for tone (masculine, feminine, or neutral) and technical complexity.


###5 . Output
Initial Job Description:
We are seeking a Software Engineer with experience in Python, Django, and REST APIs. Responsibilities include developing software, debugging, and collaborating with teams. This position is based in Remote.

SEO-Optimized Job Description:
We are seeking a Software Engineer, Python Developer, Backend Engineer with experience in Python, Django, and REST APIs. Responsibilities include developing software, debugging, and collaborating with teams. This position is based in Remote.

Tone and Technicality Analysis:
Tone: Neutral
Technicality: 7/10 (Moderately Technical)