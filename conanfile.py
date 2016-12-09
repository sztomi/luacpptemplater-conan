from conans import ConanFile, CMake

class LuaCppTemplater(ConanFile):
    name = "LuaCppTemplater"
    version = "1.0.0"
    settings = "os", "compiler", "build_type", "arch"
    exports = "*.h", "*.cpp", "cog-batteries/*.py", "*.txt"
    requires = 'lua/5.3.3@dwerner/testing'
    src_dir = 'luacpptemplater'

    def build(self):
        cmake = CMake(self.settings)
        self.run('conan install {} --build'.format(self.src_dir))
        self.run('cmake %s %s' % (self.src_dir, cmake.command_line))
        self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy(pattern="*.h", src='{}/include'.format(self.src_dir), dst="include")
        self.copy("*.lib", dst="lib", src="lib")
        self.copy("*.a", dst="lib", src="lib")

    def package_info(self):
        self.cpp_info.libs = ["luacpptemplater", "lua"]
