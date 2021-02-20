from sumarpi.api import create_app
import unittest
import sys

USAGE_STRING = """\nUsage:                               
            sumarpi <command>\n               
            Commands:                                   
                start: \t Launches the flask API server at localhost:5000   
            
            e.g sumarpi start
                """


def client():

    args = sys.argv
    sys.argv = [sys.argv[0]]  # Clear args, not to be passed in tests

    if len(args[1:]) < 1:
        print(USAGE_STRING)
    elif args[1] == 'start':
        app = create_app()
        app.run()
    else:
        print(USAGE_STRING)
