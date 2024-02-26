import os 
import traceback

from dotenv import load_dotenv

def get_openai_api_key():
    load_dotenv()
    key = os.getenv("OPENAI_API_KEY")
    return key

def get_table_data(quiz_dict):
    quiz_table_data = []
    for key, value in quiz_dict.items():
        mcq = value['mcq']
        option_a = value['options']['a']
        option_b = value['options']['b']
        option_c = value['options']['c']
        option_d = value['options']['d']
        correct = value['Correct']
        quiz_table_data.append({'Question': mcq, "Options A": option_a, "Options B": option_b, "Options C": option_c, "Options D": option_d, "Correct Answer": correct})

    return quiz_table_data
