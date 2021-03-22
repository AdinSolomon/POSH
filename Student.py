
import Requirement

# This class is used to represent a student's status
# - what courses have been completed
# - currently enrolled courses

class Student:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.enrollment_year = kwargs.get("enrollment_year")
        self.completed_courses:dict = kwargs.get("completed_courses")
        self.current_courses:dict = kwargs.get("current_courses")
    # Requirement methods
    def meets_prerequisite(self, prereq:Requirement.Requirement) -> bool:
        return prereq.satisfied(self.completed_courses)
    def meets_corequisite(self, coreq:Requirement.Requirement) -> bool:
        return coreq.satisfied(self.current_courses)
        
        
