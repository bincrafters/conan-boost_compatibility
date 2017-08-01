from conans import ConanFile, tools, os

class BoostCompatibilityConan(ConanFile):
    name = "Boost.Compatibility"
    version = "1.64.0"
    generators = "txt"
    url = "https://github.com/boostorg/compatibility"
    description = "For a description of this library, please visit http://boost.org/compatibility "
    license = "www.boost.org/users/license.html"
    lib_short_name = "compatibility"

    def source(self):
        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, self.url))

    def package(self):
        include_dir = src=os.path.join(os.getcwd(), self.lib_short_name, "include")
        self.copy(pattern="*.h", dst="", src=include_dir)
        self.copy(pattern="*.hpp", dst="", src=include_dir)
        self.copy(pattern="*.ipp", dst="", src=include_dir)
        
    def package_info(self):
        self.cpp_info.libs = [self.lib_short_name]

