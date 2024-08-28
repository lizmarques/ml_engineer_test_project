# HR Agent Platform
## Overview
The HR Agent Platform is an AI-powered system designed to streamline the hiring process by automating candidate research, review, and interview question generation. This platform leverages a multi-agent system to perform complex tasks, such as searching for potential candidates, reviewing their profiles, and crafting tailored interview questions. Each agent is specialized in a particular aspect of the recruitment process, ensuring efficiency and accuracy.

## System Architecture
<p align="center"> <img width="800px" heigth="500px" src="imagens/MFCC.png">

    
### Components
- Agents

    - **Recruiter Agent:** Acts as a Senior Tech Recruiter with expertise in LinkedIn searches to find candidates that meet specific job requirements.
    - **Review Agent:** Reviews and refines the candidate list, ensuring all necessary information is available and accurate.
    - **Interview Agent:** Creates customized job interview questions based on the candidates' profiles and the job requirements.
  
- Tasks

    - **Research Potential Candidates Task:** Conducts research on LinkedIn to find candidates based on the provided job title, required skills, differential skills, and location.
    - **Review Potential Candidates Task:** Reviews the draft list of candidates and filters them down to the top three, ensuring all key information is summarized.
    - **Generate Job Interview Question Task:** Generates tailored interview questions for each candidate based on their professional information and the job requirements.

- Tools

    - **WebsiteSearchTool:** Performs a Retrieval-Augmented Generation (RAG) search over websites.
    - **SerperDevTool:** Executes Google searches to gather information.
    - **FileReadTool:** Reads the draft and final candidate files (potencial_candidates_draft.md and potencial_candidates.md).

- Workflow
  
    - **Recruiter Agent:** Uses the WebsiteSearchTool and SerperDevTool to search LinkedIn and generate a draft list of potential candidates.
    - **Review Agent:** Reads the draft list, checks for completeness, and refines it to the top three candidates.
    - **Interview Agent:** Reads the final candidate file and generates a set of customized interview questions based on the candidates' profiles and job requirements.

## File Structure
- agents.py: Contains the definitions of the AI agents (Recruiter Agent, Review Agent, and Interview Agent).
- tasks.py: Contains the definitions of the tasks each agent will perform.
- main.py: The entry point of the application, where the Streamlit interface is set up, and the task execution begins.
- potencial_candidates_draft.md: The draft file where the initial list of candidates is stored.
- potencial_candidates.md: The final refined list of candidates after the review process.
- interview_questions.doc: The file where the generated interview questions are saved.

## Logging and Debugging
- Verbose Mode: The agents are set to verbose mode (verbose=True), which will output detailed logs of the process to the console.
- Output Files: The results of each task are saved in the specified markdown and document files (potencial_candidates_draft.md, potencial_candidates.md, and interview_questions.doc).


## Running the Prototype
### Installation

1. Clone the repository:
    ```plaintext
    git clone git clone https://github.com/lizmarques/ml_engineer_test_project.git
    ```

2.  Create a virtual environment:
    
    ```plaintext
    python -m venv venv
    ```
    
3.  Install the dependencies:
    
    ```plaintext
    pip install -r requirements.txt
    ```
    
4.  Adjust all file paths in the scripts to match your personal directory structure. For example:
   
    ```plaintext
    load_dotenv(r"C:\Users\YourUsername\YourProject\.env")
    ```
    
5.  Update the .env file with your own credentials and configuration settings.
    ```plaintext
    SERPER_API_KEY=your_serper_api_key
    OPENAI_API_KEY=your_openai_api_key
    AGENTOPS_API_KEY=your_agentops_api_key
    ```
    
7.  Launch the Streamlit application by running the following command in your terminal:
    ```plaintext
    streamlit run main.py
    ```
### Streamlit
- Usage:
    - About: Provides an overview of the platform.
    - HR Agent Platform: Allows you to input job details and run the agents to find and evaluate candidates.
    - 
- Use the Interface:
    - Navigate to the "HR Agent Platform" tab.
    - Fill in the form with the job title, brief description, required skills, differential skills, and location.
    - Submit the form to initiate the process.
  
- Process Flow:
    - After submission, the agents will execute their respective tasks, with the Recruiter Agent first identifying potential candidates, followed by the Review Agent refining the list, and finally, the Interview Agent generating tailored interview questions.
    - The results will be saved in the respective files and displayed in the console
      
- Outputs
    - potencial_candidates_draft.md: The initial list of potential candidates.
    - potencial_candidates.md: The reviewed and refined list of top 3 candidates.
    - interview_questions.doc: The tailored job interview questions for each candidate.

  
