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

    version("0.2.2", sha256="72e0ada22b03af5a4dcde542e4987ae2c1acfe506dc1f4c62318725bf2a6cad5")
    version("0.2.1", sha256="319d0a55868cb0081cbc8b811857f2ef7c19a449fa77af16147a1ab69ba3d9c9")
    version("0.2.0", sha256="e07db13bd079e5a2e8458046909b4553e2baa2b91f2ca091dd7385eb2405aab6")
    version("develop", branch="main")

    depends_on("cxx", type="build")
    depends_on("cmake@3.14:", type="build")
    
    def cmake_args(self):
        args = ["-DKASSERT_BUILD_TESTS=OFF", "-DKASSERT_BUILD_DOCS=OFF"]
        return args
