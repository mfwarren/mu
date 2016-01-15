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

HTTP_METHODS = (
    'CONNECT',
    'DELETE',
    'GET',
    'HEAD',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'TRACE',
)

DEFAULT_MEDIA_TYPE = 'application/json; charset=utf-8'


from mu.version import __version__  # NOQA
# from mu.status_codes import *  # NOQA
from mu.errors import *  # NOQA
# from mu.redirects import *  # NOQA
# from mu.http_error import HTTPError  # NOQA
# from mu.http_status import HTTPStatus  # NOQA
from mu.util import *  # NOQA
# from mu.hooks import before, after  # NOQA
from mu.request import Request#, RequestOptions  # NOQA
from mu.response import Response  # NOQA
from mu.api import API#, DEFAULT_MEDIA_TYPE  # NOQA
