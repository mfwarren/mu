# Copyright 2015 by Halotis, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import shutil

from mu import util
from .package import Package, BUILD_PATH

class Deployment(object):
    """
    A Deployment is the collection of Packages along with the meta data required
    to deploy it to Lambda.
    """

    def __init__(self, app_uri):
        """
        api_import is the importable module:object that is a Mu API object
        """
        self.app_uri = app_uri

    def load(self):
        # load the app
        return util.import_app(self.app_uri)

    def clean(self):
        try:
            shutil.rmtree(BUILD_PATH)
        except:
            pass
        os.mkdir(BUILD_PATH)

    def create(self):
        app = self.load()
        self.clean()
        for endpoint in app.routes:
            for handler in [h for h in dir(app.routes[endpoint]) if h.startswith('on_')]:
                package = Package(endpoint, app.routes[endpoint], handler)
                package.make_entry_function(self.app_uri.split(":")[0], self.app_uri.split(":")[1])
                package.make_zip()

if __name__ == '__main__':
    deployment = Deployment('sample:api')
    deployment.create()
