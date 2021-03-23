
valid_grades = {'A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'F', 'P', 'NP'}

grade_points = {
    'A+' : 4.00,
    'A'  : 4.00,
    'A-' : 3.67,
    'B+' : 3.33,
    'B'  : 3.00,
    'B-' : 2.67,
    'C+' : 2.33,
    'C'  : 2.00,
    'C-' : 1.67,
    'D+' : 1.33,
    'D'  : 1.00,
    'F'  : 0.00
}
P_NP_POINTS_NOT_FOR_GPA = 4.00 # TODO - get the actual value for this

class Grade:
    # Base Functions
    def __init__(self, grade:str):
        if grade not in valid_grades:
            raise Exception(f"Invalid grade {grade}")
        self.grade = grade
    def __str__(self):
        return self.grade
    # Comparison Functions
    def points(self, forGPA:bool = False) -> float:
        return grade_points.get(self.grade, default = None if forGPA else P_NP_POINTS_NOT_FOR_GPA)
    def __eq__(self, other):
        return self.points() == other.points()
    def __ne__(self, other):
        return self.points() != other.points()
    def __lt__(self, other):
        return self.points() <  other.points()
    def __le__(self, other):
        return self.points() <= other.points()
    def __ge__(self, other):
        return self.points() >= other.points()
    def __gt__(self, other):
        return self.points() >  other.points()
