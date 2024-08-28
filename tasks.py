# Import
from textwrap import dedent
from crewai import Task

# Create Tasks class
class Tasks():
	def research_potencial_candidates_task(self, agent, job_title, brief_description, required_skills, differential_skills, location):
		return Task(
			description=dedent(f"""Conduct thorough research to find potential candidates for the specified job.
    			Utilize various online resources gather a comprehensive list of potential candidates profiles.
                        Ensure that the candidates meet the job requirements provided.

                        Job Requirements:
                        - {job_title}
			- {brief_description}
                        - {required_skills}
                        - {differential_skills}
                        - {location}"""),
			expected_output=dedent("""\
						A list of 5 potential candidates with the following information: 
      						Name, Brief Profile (highlighting their suitability), Current Position, 
	    					Skills (candidate unique skills that are more related to the job description), 
	  					Linkedin profile link, GitHub profile (if it is found) and Location"""),
						output_file="potencial_candidates_draft.md",
						agent=agent
				)
	def review_potencial_candidates_task(self, agent, location):
		return Task(
			description=dedent(f"""\
						Review the potencial candidates draft file and make sure that each candidate 
      						has the following summarized basic information: Name, Brief Profile, 
	    					Current Position, Skills, Linkedin Profile link, GitHub Profile (if it is found) 
	  					and Location: {location}. Reduce only to the top 3 candidates."""),
			expected_output=dedent("""\
						A list of the top 3 potencial job candidates that is clear and has all the 
      						basic information. Formatted in markdown."""),
			agent=agent,
			output_file="potencial_candidates.md"
				)
		
	def generate_job_interview_question_task(self, agent, job_title, brief_description, required_skills, differential_skills):
		return Task(description=dedent(f"""\
						Generate a set of job interview questions tailored for each one of 
						the candidates in the potencial_candidates file based on their 
						professional experience and the position requirements: {job_title},
						{brief_description} {required_skills}, {differential_skills}. 
						If the candidate has a GitHub profile, enrich the questions asking 
						about one of the projects that the candidate developed."""),
			expected_output=dedent("""\
						A detailed set of job interview questions tailored for each one of the 
						candidates that involves: Core Technical Skills, Specialized Knowledge, 
						Problem Solving, Soft Skills and Behavioral Questions. 
						Formatted in doc with headers and bullet points"""),
			agent=agent,
			output_file="interview_questions.doc",
				)
