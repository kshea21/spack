# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import time

from llnl.util.filesystem import touch

from spack.package import *


class MySlowBuild(Package):
    """This is a fake vtk-m package used to demonstrate virtual package providers
    with dependencies."""

    homepage = "http://www.example.com"
    has_code = False

    depends_on("my-slow-build-2")
    depends_on("my-slow-build-3")

    version("1.0")

    def install(self, spec, prefix):
        print("I'm building!")
        time.sleep(5)
        print("I'm done!")

        touch(prefix.dummy_file)
