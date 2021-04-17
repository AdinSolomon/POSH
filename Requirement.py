
import abc
from functools import reduce

# This class is all about requirements which can be filled according to some criteria
# Those criteria may be other requirements organized in a tree structure

class Requirement(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __str__(self):
        pass
    @abc.abstractmethod
    def is_satisfied(self, **kwargs) -> bool:
        pass

class CourseRequirement(Requirement):
    def __init__(self, subject:str, number:str, can_be_taken_concurrently:bool = False):
        self.subject = subject
        self.number = number
        self.can_be_taken_concurrently = can_be_taken_concurrently
    def __str__(self):
        return f"{self.subject} {self.number}"
    def is_satisfied(self, **kwargs) -> bool:
        return self.__str__() in kwargs["courses"]

class MinGradeRequirement(CourseRequirement):
    def __init__(self, subject:str, number:str, grade:str, can_be_taken_concurrently:bool = False):
        self.subject = subject
        self.number = number
        self.can_be_taken_concurrently = can_be_taken_concurrently
        self.grade = grade
    def __str__(self):
        return f"{self.subject} {self.number} [Min Grade: {self.grade}]"
    def is_satisfied(self, **kwargs) -> bool:
        c = super().__str__()
        courses = kwargs["courses"]
        return (c in courses) and (courses[c].upper() <= self.grade.upper())

class AndRequirement(Requirement):
    def __init__(self, *args):
        self.components = []
        for arg in args:
            if not isinstance(arg, Requirement):
                raise TypeError(f"AndRequirement can only depend on Requirements - {repr(arg)}")
            self.components.append(arg)
    def __str__(self):
        return '(' + ") and (".join([str(c) for c in self.components]) + ')'
    def is_satisfied(self, **kwargs):
        return reduce(lambda p,q: p and q, [c.is_satisfied(courses = kwargs["courses"]) for c in self.components])

class OrRequirement(Requirement):
    def __init__(self, *args):
        self.components = []
        for arg in args:
            if not isinstance(arg, Requirement):
                raise TypeError(f"OrRequirement can only depend on Requirements - {repr(arg)}")
            self.components.append(arg)
    def __str__(self):
        return '(' + ") or (".join([str(c) for c in self.components]) + ')'
    def is_satisfied(self, **kwargs):
        return reduce(lambda p,q: p or q, [c.is_satisfied(courses = kwargs["courses"]) for c in self.components])

