import streamlit as st
from src.mcqgenerator import overall_chain
from langchain_community.callbacks import get_openai_callback
import pandas as pd
from src.utils import get_openai_api_key, get_table_data
from src.logger import logging
import os
import json
import traceback

with open('Response.json', 'r') as f:
    Response_json = json.load(f)

st.title('MCQ Generator WebApp using OpenAI and Langchain')

with st.form('User Input'):
    topic = st.text_input('Enter the topic for which you want to generate MCQs')
    mcq_count = st.number_input('No. of MCQs', min_value = 3, max_value = 20)
    tone = st.selectbox('Select the complexity level of the Questions', ['Simple', 'Medium', 'Difficult'])
    submit_button = st.form_submit_button("Generate MCQs")

    if submit_button and mcq_count and topic and tone:
        with st.spinner('Loading...'):
            try:
                with get_openai_callback() as cb:
                    Final_output=overall_chain(
                        {
                        'topic': topic, 
                        'number': mcq_count, 
                        'tone' : tone,
                        'response_json' : json.dumps(Response_json)
                            }
                        )
            except Exception as e:
                traceback.print_exception(type(e), e, e.__traceback__)
                st.error('Error')

            else:
                print(f"Total Tokens:{cb.total_tokens}")
                print(f"Prompt Tokens:{cb.prompt_tokens}")
                print(f"Completion Tokens:{cb.completion_tokens}")
                print(f"Total Cost:{cb.total_cost}")
            
                if isinstance(Final_output, dict):
                            #Extract the quiz data from the response
                            quiz=Final_output.get("quiz", None)
                            quiz_dict=json.loads(quiz)

                            if quiz_dict is not None:
                                table_data=get_table_data(quiz_dict)
                                if table_data is not None:
                                    df=pd.DataFrame(table_data)
                                    df.index=df.index+1
                                    st.table(df)
                                    #Display the review in atext box as well
                                    st.text_area(label="Review", value=Final_output["review"])
                                else:
                                    st.error("Error in the table data")

                            else:
                                st.write(Final_output)

