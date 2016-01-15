# Copyright 2015 by Matt Warren <matt.warren@gmail>
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

import zipfile
import re
import os
import mu.handler
import inspect

# from jinja2 import Template

try:
    import zlib
    compression = zipfile.ZIP_DEFLATED
except:
    compression = zipfile.ZIP_STORED

ENTRY_FILENAME = '_generated.py'
BUILD_PATH = './build'


class Handler(object):
    """
    Information about each endpoint hander function
    """
    def __init__(self, resource, method, module, uri_template):
        self.resource = resource
        self.method = method
        self.module = module
        self.uri_template = uri_template


class Package(object):
    """
    Take all the code, add a handler function for each endpoint, zip everything up
    for uploading to Lambda.
    """

    def __init__(self, app_uri):
        pass

    def filename(self):
        return 'mu_handler.zip'

    def make_zip(self):
        # TODO: zip in dependancies
        with zipfile.ZipFile(os.path.join(BUILD_PATH, self.filename()), mode='w') as archive:
            for dirpath, dirnames, filenames in os.walk('.'):
                if dirpath.startswith(BUILD_PATH):
                    continue
                for file in filenames:
                    print(os.path.join(dirpath, file))
                    archive.write(os.path.join(dirpath, file), compress_type=compression)
