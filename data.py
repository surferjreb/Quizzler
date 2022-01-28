import requests
from tkinter import messagebox
from ui import QuizInterface

q_params = {
    "amount": 10,
    "type": 'boolean',
}
question_data = []

response = requests.get(url="https://opentdb.com/api.php?",
                        params=q_params)
response.raise_for_status()
response_code = response.json()["response_code"]

match response_code:
    case int(0):
        question_data = response.json()["results"]
    case int(1):
        messagebox.showinfo(title="Error...",
                            message="You have requested to many questions."
                            "Please correct and try again"
                            )
        QuizInterface.window.destroy()
    case _:
        messagebox.showinfo(title="Ahoy..",
                            message="Check your question paramaters"
                            )
        QuizInterface.window.destroy()
