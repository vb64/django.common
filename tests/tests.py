import sys
import unittest

if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise Exception(
          "Usage: tests.py project_path [fully.qualified.names.of.the.tests] [verbose]\n"
          "Example:\n"
          "tests.py ..\\source google.appengine.tools.api_server_test"
        )

    sys.path.insert(1, sys.argv[1])
    verbose = 1
    suite = None
    loader = unittest.TestLoader()
    buf = True

    if "verbose" in sys.argv:
        verbose = 2

    if (len(sys.argv) > 2) and (sys.argv[2] not in ["verbose"]):
        suite = loader.loadTestsFromNames([sys.argv[2]])
        buf = False
    else:
        suite = loader.discover('.')

    unittest.TextTestRunner(verbosity=verbose, buffer=buf).run(suite)
