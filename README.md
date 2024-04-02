# MCQ Generator Project

This project utilizes the OpenAI API with the LLM model GPT4 and Langchain to generate multiple-choice questions (MCQs) based on a specified topic, number of questions, and complexity level. The generated MCQs are presented within a Streamlit web application and can also be downloaded in CSV format.

## Cloning the Repository

To clone the repository, use the following command:

```git clone https://github.com/Vipul111196/MCQ_Generator_chatbot.git```

## Usage

1. Navigate to the project directory:

```cd MCQ_Generator_chatbot```

2. Set up a new environment (optional but recommended):

```conda create -p venv python -y```

3. Install dependencies using pip:

```pip install -r requirements.txt```

4. Activate the environment (if created):

```conda activate venv\```   # for Windows

5. Run the Streamlit app:

```streamlit run streamlit_app.py```

6. Access the Streamlit app in your web browser at ```[http://localhost:8501](http://localhost:8501).```

7. Enter the desired topic, number of questions, and complexity level.

8. Click the "Generate MCQs" button to generate MCQs based on your input.

9. View and interact with the generated MCQs within the Streamlit app.

10. Optionally, download the generated MCQs in CSV format by clicking the "Download CSV" button.

## Dependencies

Ensure you have Python, Anaconda package and pip installed on your system. The project dependencies are listed in the `requirements.txt` file and can be installed using the command mentioned in step 2 above.

## Notes

- You may need to sign up for an OpenAI API key and configure it within the `streamlit_app.py` file.
- This project is for educational and informational purposes only.
- If you want to collaborate and want to modify the project, please create a pull request. 

### Thank you for visiting the profile.
