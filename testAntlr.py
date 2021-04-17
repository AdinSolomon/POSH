import sys
from antlr4 import *
from RequirementsParserLexer import RequirementsParserLexer
from RequirementsParserParser import RequirementsParserParser
from RequirementsParserListener import RequirementsParserListener

def main(argv):
    
    data = "CS 345 [Min Grade: D] (Can be taken Concurrently) and CS T164"
    print(data)
    data_in = InputStream(data)

    lexer = RequirementsParserLexer(data_in)
    tokens = CommonTokenStream(lexer)
    parser = RequirementsParserParser(tokens)
    tree = parser.requirement()
    #print(tree.toStringTree(recog=parser))
    printer = RequirementsParserListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    



    #print(f"{tree.getChildCount()}")
    #print(f"  {tree.getChild(0).getChildCount()}")
    #print(f"    {tree.getChild(0).getChild(0).getChildCount()}")
    #print(f"       {tree.getChild(0).getChild(0).getChild(0).getChildCount()}")
    #print(f"         {tree.getChild(0).getChild(0).getChild(0).getChild(0)}")
    #print(f"         {tree.getChild(0).getChild(0).getChild(0).getChild(1)}")
    #print(f"       {tree.getChild(0).getChild(0).getChild(1).getChildCount()}")
    #print(f"         {tree.getChild(0).getChild(0).getChild(1).getChild(0)}")
    #print(f"         {tree.getChild(0).getChild(0).getChild(1).getChild(1)}")
    #print(f"         {tree.getChild(0).getChild(0).getChild(1).getChild(2)}")
        

if __name__ == '__main__':
    main(sys.argv)