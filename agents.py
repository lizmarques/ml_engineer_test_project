# Import
from crewai import Agent
from crewai_tools.tools import WebsiteSearchTool, SerperDevTool, FileReadTool
from langchain_openai import ChatOpenAI

# Tool that does a RAG search over a website
web_search_tool = WebsiteSearchTool()

# Tool that does Google search 
search_tool = SerperDevTool()

# Tool that reads the potencial candidates draft file
draft_file_read_tool = FileReadTool(
     file_path='potencial_candidates_draft.md',
     description='A tool to read the potencial cadidates draft file.')

# Tool that reads the potencial candidates file
file_read_tool = FileReadTool(
     file_path='potencial_candidates.md',
     description='A tool to read the potencial cadidates file.')

# Instantiate the ChatOpenAI model
gpt = ChatOpenAI(model_name="gpt-4o-mini")

# Create Agents class
class Agents():
    def recruiter_agent(self):
        return Agent(
                role='Senior Tech Recruiter',
                goal='Find the best candidates based on the job requirements',
                tools=[web_search_tool, search_tool],
                llm=gpt,
                backstory='You are a specialist at finding the right candidates by exploring Linkedin. Your 10 years of experience and skill in identifying suitable candidates ensures the best match for job positions.',
                allow_delegation=False,
                verbose=True
        )

    def review_agent(self):
         return Agent(
                 role='Review and Editing Specialist',
                 goal='Review the selected potencial cadidates to make sure that each one of them have the following summarized basic information: Brief Profile (highlighting their suitability), Current Position, Skills, Linkedin profile link and GitHub profile link (if it is found). If any information (other then the GitHub) of a candidate is missing, remove the candidate from the final list.',
                 tools=[web_search_tool, search_tool, draft_file_read_tool],
                 llm=gpt,
                 backstory='A meticulous editor with an eye for detail, ensuring every piece of content is clear and all the basic information is provided.',
                 allow_delegation=False,
                 verbose=True
         )

    def interview_agent(self):
        return Agent(
                 role='Job Interview Question Writer',
                 goal='Use the potencial_candidates file generated from the Review and Editing Specialist to create tailored job interview questions for each candidate based on their professional information and the job_title, required_skills, differential_skills required for the position.',
                 tools=[web_search_tool, search_tool, file_read_tool],
                 llm=gpt,
                 backstory='Skilled in crafting accurate job interview questions that extracts the best from each candidate and that helps to select the right candidate for the job.',
                 allow_delegation=False,
                 verbose=True
         )

