from openai import OpenAI
import os
import json
from datetime import datetime
# from main.models import *
import time

# this is the function for printing the OPENAI objects i creat(just for testing)
def show_json(obj):
    return (json.loads(obj.model_dump_json()))

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# this is the class that powers the chatbot

class ChatAI():
    
    def __init__(self):

    # getting the students information
        # student = User.objects.get(email=email)
        # student_info = User.learnerCustomizer_set.get(id=1)
        # student_bio = User.userProfile_set.get(id=1)
        # self.name =student_bio.username
        # self.grade = student_info.grade
        # self.career = student_info.future_career
        # self.assistant_name = student_info.assistant_name
        self.name = "isaac"
        self.grade = "eight"
        self.career = "physist"
        self.assistant_name = "allen"

    # initiate customization of the AI assistant

        instructions_prompt = f"you are a friendly personal tutor of a student in grade {self.grade} called {self.name} who is aspiring to be {self.career}, answer in a coversational polite way that isnpires the student, sparks creativity and imagination, end the answers asked with the a a simple question that provokes thought"

        assistant = client.beta.assistants.create(
            name = self.assistant_name,
            instructions = instructions_prompt,
            model= "gpt-3.5-turbo",
        )

        self.assistant_id = show_json(assistant)["id"]
        
    # initiating the thread

        thread = client.beta.threads.create()

        self.thread_id = show_json(thread)["id"]

    # initiating the run
    def call_run(self):
        run = client.beta.threads.runs.create(
            thread_id=self.thread_id,
            assistant_id=self.assistant_id,
        )

        return run

    def wait_on_run(self, run):
        while run.status == "queued" or run.status == "in_progress":
            run = client.beta.threads.runs.retrieve(
                thread_id=self.thread_id,
                run_id=show_json(run)["id"],
            )
            time.sleep(0.5)
        return run


    def submit_message(self, user_message):
        client.beta.threads.messages.create(
            thread_id= self.thread_id, role="user", content=user_message
        )
        run = self.call_run()
        self.wait_on_run(run)
        return client.beta.threads.messages.list(thread_id=self.thread_id, order="asc")


    def get_response(self, message):
        messages = self.submit_message(message)
        for m in messages:
            print(f"{m.role}: {m.content[0].text.value}")


isaac = ChatAI()

isaac.get_response("hello, can you teach me about the solar system")