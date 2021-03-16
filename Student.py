
# This class is used to represent a student's status
# - what courses have been completed
# - currently enrolled courses

class Student:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.enrollment_year = kwargs.get("enrollment_year")
        self.completed_courses = kwargs.get("completed_courses")
        self.current_courses = kwargs.get("current_courses")
        
        
