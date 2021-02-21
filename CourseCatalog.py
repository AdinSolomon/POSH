
from util.web import make_url2

HomePage = "http://catalog.drexel.edu/coursedescriptions/"

TermLengths = ["quarter", "semester"]
Degrees = ["undergrad", "grad"]
URLs = sum([[make_url2([HomePage, term_length, degree]) for degree in Degrees] for term_length in TermLengths],[])

