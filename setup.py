import sys

import numpy
from setuptools import Extension, setup
from setuptools.command.build_ext import build_ext


class build_ext_cxx17(build_ext):
    def build_extensions(self):
        std_flag = (
            "-std:c++17" if self.compiler.compiler_type == "msvc" else "-std=c++17"
        )
        for e in self.extensions:
            e.extra_compile_args.append(std_flag)
        super().build_extensions()


macros = [("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")]
profiling = False
linetrace = False
if "--profile" in sys.argv:
    profiling = True
    linetrace = True
    macros += [("CYTHON_TRACE_NOGIL", "1")]
    sys.argv.remove("--profile")

stats_cpp = Extension(
    "pyrecombatseq.utils.stats_cpp",
    [
        "pyrecombatseq/utils/_stats.pyx",
    ],
    include_dirs=[numpy.get_include()],
    define_macros=macros,
)

edgepy_cpp = Extension(
    "pyrecombatseq.edgepy.edgepy_cpp",
    [
        "pyrecombatseq/edgepy/edgepy_cpp/edgepy_cpp.pyx",
    ],
    include_dirs=[numpy.get_include()],
    define_macros=macros,
)


setup(
    cmdclass={"build_ext": build_ext_cxx17},
    packages=[
        "pyrecombatseq",
        "pyrecombatseq/pycombat",
        "pyrecombatseq/edgepy",
        "pyrecombatseq/edgepy/edgepy_cpp",
        "pyrecombatseq/utils",
        "pyrecombatseq/diffexp",
        "pyrecombatseq/limma"
    ],
    package_data={
        "pyrecombatseq/edgepy/edgepy_cpp": [
            "edgepy_cpp.pyx",
            "__init__.pxd",
            "edgepy_cpp.h",
        ],
    },
    ext_modules=[edgepy_cpp, stats_cpp],
)
