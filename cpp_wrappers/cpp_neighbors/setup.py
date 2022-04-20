from distutils.core import setup
import numpy.distutils.misc_util
from torch.utils.cpp_extension import BuildExtension, CppExtension

# Adding OpenCV to project
# ************************

# Adding sources of the project
# *****************************

SOURCES = ["../cpp_utils/cloud/cloud.cpp",
             "neighbors/neighbors.cpp",
             "wrapper.cpp"]

module = CppExtension(name="KPConv_radius_neighbors",
                    sources=SOURCES,
                    extra_compile_args=['-std=c++11',
                                        '-D_GLIBCXX_USE_CXX11_ABI=0'])

setup(
    name="KPConv_radius_neighbors",
    ext_modules=[module],
    include_dirs=numpy.distutils.misc_util.get_numpy_include_dirs(),
    cmdclass={
        'build_ext': BuildExtension
    }
)
