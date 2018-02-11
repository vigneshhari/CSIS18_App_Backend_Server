# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.conf.urls import include, url
from django.contrib import admin

from csis.views import index
from csis.views import checkUpdates
from csis.views import getTypes
from csis.views import getLevels
from csis.views import getTracks
from csis.views import getSpeakers
from csis.views import getLocations
from csis.views import getSessions
from csis.views import getBofs
from csis.views import getSocialEvents
from csis.views import getPOI
from csis.views import getInfo
from csis.views import getFloorPlans
from csis.views import getSettings

urlpatterns = [
    url(r'^$', index),
    url(r'^checkUpdates$', checkUpdates),
    url(r'^getTypes$', getTypes),
    url(r'^getLevels$', getLevels),
    url(r'^getTracks$', getTracks),
    url(r'^getSpeakers$', getSpeakers),
    url(r'^getLocations$', getLocations),
    url(r'^getSessions$', getSessions),
    url(r'^getBofs$', getBofs),
    url(r'^getSocialEvents$', getSocialEvents),
    url(r'^getPOI$', getPOI),
    url(r'^getInfo$', getInfo),
    url(r'^getFloorPlans$', getFloorPlans),
    url(r'^getSettings$', getSettings),
    url(r'^admin/', include(admin.site.urls)),
]