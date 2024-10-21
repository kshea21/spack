# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import time

from llnl.util.filesystem import touch

from spack.package import *


class MySlowBuild2(Package):
    """This is a fake vtk-m package used to demonstrate virtual package providers
    with dependencies."""

    homepage = "http://www.example.com"
    has_code = False

    version("1.0")

    def install(self, spec, prefix):
        print("I am also trying to build!")
        time.sleep(3)
        print("Oh would you look at that, we can share <3")

        touch(prefix.dummy_file)
