from pybuilder.core import use_plugin, init, Author

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")

name = "av-agent-utils"
url = "https://github.com/AlienVault-Engineering/agent-utils"
summary = "Some debugging tools for AV engineers to use"
description = ""
authors = [Author("Rusty Brooks", "rbrooks@alienvault.com")]
license = "AlienVault Commercial"
home_page = "https://github.com/AlienVault-Engineering/agent-utils"
default_task = "publish"
requires_python = ">=3.6.0"


@init
def set_properties(project):
    # build_number = project.get_property("bamboo_build")
    # if build_number:
    #     project.version = build_number
    # else:
    #     project.version = "0.0.999"
    project.version("0.0.1")
    project.depends_on_requirements("requirements.txt")

    # Build and test settings
    project.set_property("flake8_break_build", True)
    project.set_property("flake8_verbose_output", True)
    project.set_property("flake8_include_test_sources", True)
    project.set_property("flake8_max_line_length", 150)
    project.set_property("run_unit_tests_propagate_stdout", True)
    project.set_property("run_unit_tests_propagate_stderr", True)
    project.set_property("coverage_branch_threshold_warn", 75)
    project.set_property("coverage_branch_partial_threshold_warn", 50)

    # Deploy settings
#    project.set_property("distutils_upload_repository_key", "av-agent-utils")
    project.set_property("distutils_upload_repository", "pypi")
