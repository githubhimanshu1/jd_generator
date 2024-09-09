from transformers import AutoTokenizer, AutoModelForCausalLM

class JDGenerator:
    def __init__(self, job_title, description, skills, location):
        self.job_title = job_title
        self.description = description
        self.skills = skills
        self.location = location
        
        # Load BLOOM model and tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained("bigscience/bloom-1b7")  # You can choose other sizes like bloom-7b1
        self.model = AutoModelForCausalLM.from_pretrained("bigscience/bloom-1b7")

    def generate(self):
        # Create the prompt for BLOOM
        prompt = (
            f"Write a detailed professional job description for the role of {self.job_title}. "
            f"The responsibilities include {self.description}. "
            f"Required skills are: {', '.join(self.skills)}. "
            f"The job is located in {self.location}."
            f"The generated content should have job description details , skills required , location ,company culture , benifits and other required parameters"
        )
        
        # Tokenize the input
        input_ids = self.tokenizer(prompt, return_tensors="pt").input_ids
        
        # Generate the job description using BLOOM
        output = self.model.generate(input_ids, max_length=650)
        
        # Decode the generated output
        jd_text = self.tokenizer.decode(output[0], skip_special_tokens=True)
        
        return jd_text