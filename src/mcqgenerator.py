from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain_community.callbacks import get_openai_callback
from src.utils import OPENAI_API_KEY
import pandas as pd
import json

#Initialise the LLM Model
llm_OpenAI = ChatOpenAI(model = 'gpt-3.5-turbo', temperature = 0)

# Read the Json file
with open("i:\8_end_to_end_projects\Project_2\MCQ_Generator\Response.json", 'r') as f:
    Response_JSON = json.load(f)

# Creating a template and defining the input variables that helps to generate the MCQ For the desired topic
main_template="""

    Text:{topic}
    You are an expert MCQ generator. Given the above Topic, it is your job to \
    create a quiz  of {number} multiple choice questions for students in {tone} tone. 
    Make sure the questions are not repeated and check all the questions to be conforming the topic as well.
    Make sure to format your response like  RESPONSE_JSON below  and use it as a guide. \
    Ensure to make {number} MCQs

    ### RESPONSE_JSON
    {response_json}

"""

# Creating the Prompt Template for MCQ Generator
quiz_generation_prompt = PromptTemplate(
    input_variables = ['topic', 'number', 'tone', 'response_json'],
    template = main_template
)


# Creating the chain for MCQ Generator
quiz_generation_chain = LLMChain(llm=llm_OpenAI, prompt= quiz_generation_prompt, output_key = 'quiz')

# Creating a template that helps in verifing the MCQ generated are as per the expectation or not
verification_template="""
You are an expert english grammarian and evaluator. Given a Multiple Choice Quiz for students who are studying {topic} topic.\
You need to evaluate the complexity of the question and give a complete analysis of the quiz. Only use at max 50 words for complexity analysis. 
if the quiz is not at per with the cognitive and analytical abilities of the students,\
update the quiz questions which needs to be changed and change the {tone} such that it perfectly fits the student abilities
Quiz_MCQs:
{quiz}

Check from an expert English Writer of the above quiz:
"""
# Creating the Prompt Template for MCQ Generator reviewer
quiz_verification_prompt = PromptTemplate(
    input_variables=["subject", "quiz", "tone"],
    template=verification_template
    )

# Creating the chain for MCQ Generator reviewer
quiz_verification_chain = LLMChain(llm=llm_OpenAI, prompt = quiz_verification_prompt, output_key= "review")

# Creating the Sequential chain to automate the process of MCQ generation and Reviewer feedback
overall_chain = SequentialChain(chains = [quiz_generation_chain, quiz_verification_chain], input_variables=["topic", "number", "tone", "response_json"], output_variables= ['quiz', 'review'])

# Intialising the overall chain to get the output
with get_openai_callback() as cb:
    Final_output=overall_chain(
        {'topic':'Supervised Machine Learning', 
        'number': 5, 
        'subject' : 'Machine learning', 
        'tone' :'academic',
        'response_json' : json.dumps(Response_JSON)}
        )
    
print(f"Total Tokens:{cb.total_tokens}")
print(f"Prompt Tokens:{cb.prompt_tokens}")
print(f"Completion Tokens:{cb.completion_tokens}")
print(f"Total Cost:{cb.total_cost}")
print('\n******************************************\n')
print(Final_output)