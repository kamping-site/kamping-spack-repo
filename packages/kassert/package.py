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

    version("0.2.0", sha256="e07db13bd079e5a2e8458046909b4553e2baa2b91f2ca091dd7385eb2405aab6")
    version("develop", branch="main")

    depends_on("cxx", type="build")
    
    def cmake_args(self):
        args = ["-DKASSERT_BUILD_TESTS=OFF", "-DKASSERT_BUILD_DOCS=OFF"]
        return args
