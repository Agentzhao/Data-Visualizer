from fetch_result import *            #import relevant coded Python files
import domain
from parse_results import parse_results
from frequency import *
search = input("What would you like to search?")
def overallProcess(search_term, number_results):
    keyword, html = fetch_results(search_term, number_results)
    return parse_results(html,'')

if __name__ == "__main__":
    print(most_Common(commonise(overallProcess(search,50)),10))
