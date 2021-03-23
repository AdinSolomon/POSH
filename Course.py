
# Experimental class for courses

class Course:
    def __init__(self, subject:str, number:str):
        self.subject = subject
        self.number = number
    def __str__(self):
        return f"{self.subject} {self.number}"
    
