#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/testing")

class BoostCompatibilityConan(base.BoostBaseConan):
    name = "boost_compatibility"
    url = "https://github.com/bincrafters/conan-boost_compatibility"
    lib_short_names = ["compatibility"]
    header_only_libs = ["compatibility"]
