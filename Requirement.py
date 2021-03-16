
# This class is all about requirements which can be filled according to some criteria
# Those criteria may be other requirements organized in a tree-like structure

class Requirement:
    def __init__(self, **kwargs):
        self.id = kwargs.get("id")
        