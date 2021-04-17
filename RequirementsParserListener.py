# Generated from RequirementsParser.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .RequirementsParserParser import RequirementsParserParser
else:
    from RequirementsParserParser import RequirementsParserParser

import sys
from functools import reduce
# This stack is the listener's buffer. When certain 'exit' functions are called,
# elements are popped from the stack and used to construct corresponding objects
stack = []

# This class defines a complete listener for a parse tree produced by RequirementsParserParser.
class RequirementsParserListener(ParseTreeListener):

    # Enter a parse tree produced by RequirementsParserParser#requirement.
    def enterRequirement(self, ctx:RequirementsParserParser.RequirementContext):
        print(sys._getframe().f_code.co_name)

    # Exit a parse tree produced by RequirementsParserParser#requirement.
    def exitRequirement(self, ctx:RequirementsParserParser.RequirementContext):
        print(sys._getframe().f_code.co_name)
        print([c for c in ctx.getChildren()])


    # Enter a parse tree produced by RequirementsParserParser#course.
    def enterCourse(self, ctx:RequirementsParserParser.CourseContext):
        print(sys._getframe().f_code.co_name)

    # Exit a parse tree produced by RequirementsParserParser#course.
    def exitCourse(self, ctx:RequirementsParserParser.CourseContext):
        stack.append(f"{stack.pop(-2)} {stack.pop(-1)}")
        print(stack)


    # Enter a parse tree produced by RequirementsParserParser#subject.
    def enterSubject(self, ctx:RequirementsParserParser.SubjectContext):
        print(sys._getframe().f_code.co_name)

    # Exit a parse tree produced by RequirementsParserParser#subject.
    def exitSubject(self, ctx:RequirementsParserParser.SubjectContext):
        stack.append( reduce(lambda a,b: a+b,
            [ctx.getChild(i).__str__() for i in range(ctx.getChildCount())])
        )
        print(stack)


    # Enter a parse tree produced by RequirementsParserParser#number.
    def enterNumber(self, ctx:RequirementsParserParser.NumberContext):
        print(sys._getframe().f_code.co_name)

    # Exit a parse tree produced by RequirementsParserParser#number.
    def exitNumber(self, ctx:RequirementsParserParser.NumberContext):
        stack.append( reduce(lambda a,b: a+b,
            [ctx.getChild(i).__str__() for i in range(ctx.getChildCount())])
        )
        print(stack)


    # Enter a parse tree produced by RequirementsParserParser#min_grade.
    def enterMin_grade(self, ctx:RequirementsParserParser.Min_gradeContext):
        print(sys._getframe().f_code.co_name)

    # Exit a parse tree produced by RequirementsParserParser#min_grade.
    def exitMin_grade(self, ctx:RequirementsParserParser.Min_gradeContext):
        stack.append( reduce(lambda a,b: a+b,
            [l for l in [ctx.LETTER(i).__str__() for i in range(ctx.getChildCount())] if l != "None"])
        )
        print(stack)



del RequirementsParserParser