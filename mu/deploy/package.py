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

import zipfile
import re
import os

try:
    import zlib
    compression = zipfile.ZIP_DEFLATED
except:
    compression = zipfile.ZIP_STORED

ENTRY_FILENAME = '_generated.py'
BUILD_PATH = './build'

TEMPLATE = """
from {module} import {object}
from mu import Request, Response

def handler(event, context):
    request = Request()
    response = Response()
    api.routes['{uri_template}'].{method}(request, response)
    return response.body

"""
class Package(object):
    """
    each API Endpoint will be turned into a package for upload to Lambda.
    all requirements get included with local code and some generated code
    into a single .zip file
    """

    def __init__(self, uri_template, resource, method):
        self.uri_template = uri_template
        self.resource = resource
        self.method = method

    def filename(self):
        return re.sub('[/{}]', '_', self.uri_template) + '_' + self.method + '.zip'

    def make_entry_function(self, module, obj):
        with open(ENTRY_FILENAME, 'w') as entry:
            entry.write(TEMPLATE.format(**{'module':module, 'object':obj, 'uri_template':self.uri_template, 'method':self.method}))

    def make_zip(self):
        with zipfile.ZipFile(os.path.join(BUILD_PATH, self.filename()), mode='w') as archive:
            for dirpath, dirnames, filenames in os.walk('.'):
                if dirpath.startswith(BUILD_PATH):
                    continue
                for file in filenames:
                    print(os.path.join(dirpath, file))
                    archive.write(os.path.join(dirpath, file), compress_type=compression)
