# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: MIT

from spack.package import *


class Kassert(CMakePackage):
    """
    Powerful assertions made easy: Define assertion levels, get
    insights with expression decomposition, and switch between
    exceptions and assertions.
    """

    homepage = "https://kamping-site.github.io/kassert/"
    url = "https://github.com/kamping-site/kassert/archive/refs/tags/v0.1.0.tar.gz"
    git = "https://github.com/kamping-site/kassert.git"

    maintainers("niklas-uhl")

    license("MIT", checked_by="niklas-uhl")

    #version("0.1.0", sha256="cc666f3bb434c47074b6eee8c12984cc9b06030910ddce437ad188571642fb5c")
    version("develop", branch="feature/cmake-dependencies")

    depends_on("cxx", type="build")
    
    def cmake_args(self):
        args = []
        return args
