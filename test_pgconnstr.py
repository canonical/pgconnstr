# This file is part of the pgconnstr library.
# Copyright 2016-2020 Canonical Ltd.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the Lesser GNU General Public License version 3,
# as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranties of
# MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR
# PURPOSE.  See the Lesser GNU General Public License for more details.
#
# You should have received a copy of the Lesser GNU General Public
# License along with this program.  If not, see
# <http://www.gnu.org/licenses/>.

import doctest

import pgconnstr


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(pgconnstr))
    tests.addTests(doctest.DocFileSuite("README.md"))
    return tests
