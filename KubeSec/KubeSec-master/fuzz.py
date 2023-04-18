import scanner
import graphtaint
import parser
import main

def fuzzFunctions() :

    ListOfExceptions = []

    # all of these are just unexpected inputs that cause errors in different methods

    try : scanner.getYAMLFiles(12)
    except Exception as e: ListOfExceptions.append("Method Name: scanner.getYAMLFiles\nError: " + str(e))

    try : graphtaint.mineNetPolGraph(None, None, None, None)
    except Exception as e: ListOfExceptions.append("Method Name: graphtaint.mineNetPolGraph\nError: " + str(e))

    try : scanner.scanForUnconfinedSeccomp('')
    except Exception as e: ListOfExceptions.append("Method Name: scanner.scanForUnconfinedSeccomp\nError: " + str(e))

    try : main.getCountFromAnalysis('nothing')
    except Exception as e: ListOfExceptions.append("Method Name: main.getCountFromAnalysis\nError: " + str(e))

    try : parser.getValuesRecursively({})
    except Exception as e: ListOfExceptions.append("Method Name: parser.getValuesRecursively\nError: " + str(e))

    return ListOfExceptions

if __name__ == '__main__': 

    results = fuzzFunctions()

    for i in results :
        print('\n' + i)
