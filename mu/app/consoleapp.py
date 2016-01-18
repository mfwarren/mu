# -*- coding: utf-8 -
#
# This file is part of mu released under the MIT license.
# See the NOTICE for more information.

import os
import sys

from mu import util
from mu.deploy import Package


class ConsoleApplication(object):
    def __init__(self, usage=None):
        self.usage = usage
        self.app_uri = None  # module:name format

    def run(self):
        self.app_uri = sys.argv[1]
        p = Package(self.app_uri)
        p.build()
        p.make_zip()



def run():
    """
    The ``mu`` command line runner for launching Mu.
    """
    from mu.app.consoleapp import ConsoleApplication
    ConsoleApplication("%(prog)s [OPTIONS] [APP_MODULE]").run()


if __name__ == '__main__':
    run()
