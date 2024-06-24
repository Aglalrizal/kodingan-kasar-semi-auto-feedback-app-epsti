import os
from flask import Flask, render_template, request
#from openai import OpenAI
import google.generativeai as genai

app = Flask(__name__)

genai.configure(api_key="AIzaSyCvcW0AqSTrendSRWa71faiO0Tc8-LqyS4")
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/', methods=['GET', 'POST'])
def index():
    feedback_options = None
    if request.method == 'POST':
        student_name = request.form['student_name']
        pb = request.form['pb']
        ps = request.form['ps']
        
        feedback_options = generate_feedback(student_name, pb, ps)
        
    return render_template('index.html', feedback_options=feedback_options)

def generate_feedback(student_name, pb, ps):
    response = model.generate_content(f"Generate three feedback for student and explanation for a question \'{student_name}\' with right answer {pb} and why the {ps} is wrong")
    #print(response)
    print(response.text)
    options = response.text.split("\n\n**Option")
    #print(options)
    #feedback_options = []
    feedback_options = response.text

    # for option in options[1:]:
    #     option_parts = option.split("\n\n> ")
    #     feedback_options.append({
    #         "option": option_parts[0].strip(),
    #         "feedback": option_parts[1].strip()
    # })
    
    # for option in options[1:]:
    #     option_parts = option.split("\n\n> ", 1)  # Limit split to only 1 occurrence to avoid IndexError
    #     if len(option_parts) == 2:
    #         feedback_options.append({
    #             "option": option_parts[0].strip(),
    #             "feedback": option_parts[1].strip()
    #         })
    #     else:
    #         print("Error: Unable to parse option:", option)
            
    # print(feedback_options)
    return feedback_options

if __name__ == '__main__':
    app.run(debug=True)
