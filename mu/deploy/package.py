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

import distutils.dir_util
import zipfile
import re
import os
import sys
import shutil
import inspect

# from jinja2 import Template
import mu

try:
    import zlib
    compression = zipfile.ZIP_DEFLATED
except:
    compression = zipfile.ZIP_STORED

ENTRY_FILENAME = '_generated.py'
BUILD_PATH = './build'
DIST_PATH = './dist'


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

    def build(self):
        print("BUILDING ---->")
        # TODO: copy all requirements into build directory
        distutils.dir_util.copy_tree(os.path.dirname(mu.__file__), os.path.join(BUILD_PATH, 'mu'))

        # copy project into build directory
        for dirpath, dirnames, filenames in os.walk('.'):
            if dirpath.startswith(BUILD_PATH) or dirpath.startswith(DIST_PATH):
                continue
            for file in filenames:
                print(os.path.join(dirpath, file))
                shutil.copy(os.path.join(dirpath, file), BUILD_PATH)
                # distutils.dir_util.copy_tree(os.path.dirname(mu.__file__), BUILD_PATH)

        print("BUILD FINISHED")

    def make_zip(self):
        "zip up the build directory, place zip file in DIST directory"

        print("CREATE ZIP")

        # print(sys.path)
        # print
        # for p in sys.path:
        #     print(p)
        #     shutil.copytree(p, BUILD_PATH+'/', symlinks=False)

        with zipfile.ZipFile(os.path.join(DIST_PATH, self.filename()), mode='w') as archive:
            for dirpath, dirnames, filenames in os.walk(BUILD_PATH):
                for file in filenames:
                    print(os.path.join(dirpath, file))
                    archive.write(os.path.join(dirpath, file), os.path.join(dirpath, file).replace(BUILD_PATH, ''), compress_type=compression)

        print("ZIP CREATED: %s" % os.path.join(DIST_PATH, self.filename()))
