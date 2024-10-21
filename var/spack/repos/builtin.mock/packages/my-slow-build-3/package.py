# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import time

from llnl.util.filesystem import touch

from spack.package import *


class MySlowBuild3(Package):
    """This is a fake vtk-m package used to demonstrate virtual package providers
    with dependencies."""

    homepage = "http://www.example.com"
    has_code = False

   # depends_on("my-slow-build-2")
   # depends_on("my-slow-build-3")

    version("1.0")

    def install(self, spec, prefix):
        print("There's no reason we can't share")
        time.sleep(4)
        print("See? Sharing is caring.")

        touch(prefix.dummy_file)
