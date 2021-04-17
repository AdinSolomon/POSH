# Generated from RequirementsParser.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("C\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\5\2\24\n\2\3\2\5\2\27\n\2\5\2\31\n\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\7\2&\n\2")
        buf.write("\f\2\16\2)\13\2\3\3\3\3\3\3\3\4\3\4\6\4\60\n\4\r\4\16")
        buf.write("\4\61\3\5\5\5\65\n\5\3\5\3\5\3\5\3\5\3\6\3\6\6\6=\n\6")
        buf.write("\r\6\16\6>\3\6\3\6\3\6\2\3\2\7\2\4\6\b\n\2\2\2G\2\30\3")
        buf.write("\2\2\2\4*\3\2\2\2\6-\3\2\2\2\b\64\3\2\2\2\n:\3\2\2\2\f")
        buf.write("\r\b\2\1\2\r\16\7\3\2\2\16\17\5\2\2\2\17\20\7\4\2\2\20")
        buf.write("\31\3\2\2\2\21\23\5\4\3\2\22\24\5\n\6\2\23\22\3\2\2\2")
        buf.write("\23\24\3\2\2\2\24\26\3\2\2\2\25\27\7\r\2\2\26\25\3\2\2")
        buf.write("\2\26\27\3\2\2\2\27\31\3\2\2\2\30\f\3\2\2\2\30\21\3\2")
        buf.write("\2\2\31\'\3\2\2\2\32\33\f\7\2\2\33\34\7\5\2\2\34&\5\2")
        buf.write("\2\b\35\36\f\6\2\2\36\37\7\6\2\2\37&\5\2\2\7 !\f\5\2\2")
        buf.write("!\"\7\7\2\2\"&\5\2\2\6#$\f\4\2\2$&\5\2\2\5%\32\3\2\2\2")
        buf.write("%\35\3\2\2\2% \3\2\2\2%#\3\2\2\2&)\3\2\2\2\'%\3\2\2\2")
        buf.write("\'(\3\2\2\2(\3\3\2\2\2)\'\3\2\2\2*+\5\6\4\2+,\5\b\5\2")
        buf.write(",\5\3\2\2\2-/\7\n\2\2.\60\7\n\2\2/.\3\2\2\2\60\61\3\2")
        buf.write("\2\2\61/\3\2\2\2\61\62\3\2\2\2\62\7\3\2\2\2\63\65\7\f")
        buf.write("\2\2\64\63\3\2\2\2\64\65\3\2\2\2\65\66\3\2\2\2\66\67\7")
        buf.write("\13\2\2\678\7\13\2\289\7\13\2\29\t\3\2\2\2:<\7\b\2\2;")
        buf.write("=\7\n\2\2<;\3\2\2\2=>\3\2\2\2><\3\2\2\2>?\3\2\2\2?@\3")
        buf.write("\2\2\2@A\7\t\2\2A\13\3\2\2\2\n\23\26\30%\'\61\64>")
        return buf.getvalue()


class RequirementsParserParser ( Parser ):

    grammarFileName = "RequirementsParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'and'", "','", "'or'", 
                     "'[Min Grade:'", "']'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'(Can be taken Concurrently)'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "LETTER", "DIGIT", "SPECIAL_DIGIT", "CONCURRENCY", 
                      "WHITESPACE", "END_OF_FILE" ]

    RULE_requirement = 0
    RULE_course = 1
    RULE_subject = 2
    RULE_number = 3
    RULE_min_grade = 4

    ruleNames =  [ "requirement", "course", "subject", "number", "min_grade" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    LETTER=8
    DIGIT=9
    SPECIAL_DIGIT=10
    CONCURRENCY=11
    WHITESPACE=12
    END_OF_FILE=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RequirementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def requirement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RequirementsParserParser.RequirementContext)
            else:
                return self.getTypedRuleContext(RequirementsParserParser.RequirementContext,i)


        def course(self):
            return self.getTypedRuleContext(RequirementsParserParser.CourseContext,0)


        def min_grade(self):
            return self.getTypedRuleContext(RequirementsParserParser.Min_gradeContext,0)


        def CONCURRENCY(self):
            return self.getToken(RequirementsParserParser.CONCURRENCY, 0)

        def getRuleIndex(self):
            return RequirementsParserParser.RULE_requirement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRequirement" ):
                listener.enterRequirement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRequirement" ):
                listener.exitRequirement(self)



    def requirement(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RequirementsParserParser.RequirementContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_requirement, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RequirementsParserParser.T__0]:
                self.state = 11
                self.match(RequirementsParserParser.T__0)
                self.state = 12
                self.requirement(0)
                self.state = 13
                self.match(RequirementsParserParser.T__1)
                pass
            elif token in [RequirementsParserParser.LETTER]:
                self.state = 15
                self.course()
                self.state = 17
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 16
                    self.min_grade()


                self.state = 20
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 19
                    self.match(RequirementsParserParser.CONCURRENCY)


                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 37
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 35
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = RequirementsParserParser.RequirementContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_requirement)
                        self.state = 24
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 25
                        self.match(RequirementsParserParser.T__2)
                        self.state = 26
                        self.requirement(6)
                        pass

                    elif la_ == 2:
                        localctx = RequirementsParserParser.RequirementContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_requirement)
                        self.state = 27
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 28
                        self.match(RequirementsParserParser.T__3)
                        self.state = 29
                        self.requirement(5)
                        pass

                    elif la_ == 3:
                        localctx = RequirementsParserParser.RequirementContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_requirement)
                        self.state = 30
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 31
                        self.match(RequirementsParserParser.T__4)
                        self.state = 32
                        self.requirement(4)
                        pass

                    elif la_ == 4:
                        localctx = RequirementsParserParser.RequirementContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_requirement)
                        self.state = 33
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 34
                        self.requirement(3)
                        pass

             
                self.state = 39
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class CourseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subject(self):
            return self.getTypedRuleContext(RequirementsParserParser.SubjectContext,0)


        def number(self):
            return self.getTypedRuleContext(RequirementsParserParser.NumberContext,0)


        def getRuleIndex(self):
            return RequirementsParserParser.RULE_course

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCourse" ):
                listener.enterCourse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCourse" ):
                listener.exitCourse(self)




    def course(self):

        localctx = RequirementsParserParser.CourseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_course)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.subject()
            self.state = 41
            self.number()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubjectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LETTER(self, i:int=None):
            if i is None:
                return self.getTokens(RequirementsParserParser.LETTER)
            else:
                return self.getToken(RequirementsParserParser.LETTER, i)

        def getRuleIndex(self):
            return RequirementsParserParser.RULE_subject

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubject" ):
                listener.enterSubject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubject" ):
                listener.exitSubject(self)




    def subject(self):

        localctx = RequirementsParserParser.SubjectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_subject)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(RequirementsParserParser.LETTER)
            self.state = 45 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 44
                self.match(RequirementsParserParser.LETTER)
                self.state = 47 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==RequirementsParserParser.LETTER):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGIT(self, i:int=None):
            if i is None:
                return self.getTokens(RequirementsParserParser.DIGIT)
            else:
                return self.getToken(RequirementsParserParser.DIGIT, i)

        def SPECIAL_DIGIT(self):
            return self.getToken(RequirementsParserParser.SPECIAL_DIGIT, 0)

        def getRuleIndex(self):
            return RequirementsParserParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = RequirementsParserParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RequirementsParserParser.SPECIAL_DIGIT:
                self.state = 49
                self.match(RequirementsParserParser.SPECIAL_DIGIT)


            self.state = 52
            self.match(RequirementsParserParser.DIGIT)
            self.state = 53
            self.match(RequirementsParserParser.DIGIT)
            self.state = 54
            self.match(RequirementsParserParser.DIGIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Min_gradeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LETTER(self, i:int=None):
            if i is None:
                return self.getTokens(RequirementsParserParser.LETTER)
            else:
                return self.getToken(RequirementsParserParser.LETTER, i)

        def getRuleIndex(self):
            return RequirementsParserParser.RULE_min_grade

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMin_grade" ):
                listener.enterMin_grade(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMin_grade" ):
                listener.exitMin_grade(self)




    def min_grade(self):

        localctx = RequirementsParserParser.Min_gradeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_min_grade)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(RequirementsParserParser.T__5)
            self.state = 58 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 57
                self.match(RequirementsParserParser.LETTER)
                self.state = 60 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==RequirementsParserParser.LETTER):
                    break

            self.state = 62
            self.match(RequirementsParserParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.requirement_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def requirement_sempred(self, localctx:RequirementContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




