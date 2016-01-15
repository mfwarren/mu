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

from mu import Request, Response
from mu import util

HTTP_METHODS = {'GET': 'on_get', 'POST': 'on_post'}


class API(object):

    def __init__(self):
        self.routes = {}

    def add_route(self, uri_template, resource):
        """
        Actual routing will happen by the Amazon API Gateway service.
        You can add path parameters using brackets. For example,
        the resource path {username} represents a path parameter called 'username'.
        """
        self.routes[uri_template] = resource

    def __call__(self, event, context):
        request = Request()
        response = Response()
        api = util.import_app(event['_app_module'])
        getattr(api.routes[event['_resource_path']], HTTP_METHODS[event['_http_method']])(request, response)
        return response.body  # TODO: reformat to JSON for HTTP Headers

    # TODO:
    # def add_error_handler(self, exception, handler=None):
    # add middleware concept
