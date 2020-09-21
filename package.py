
name = "PySide"

description = "Python bindings for the Qt cross-platform application " \
              "and UI framework"

version = "1.2.4"

requires = [
    "shiboken==1.2.2"
]

variants = [
    ["os-*", "python-2.7"],
]


private_build_requires = ["rezutil-1", "pipz"]
build_command = "python -m rezutil build {root} --use-pipz"


def commands():
    env = globals()["env"]

    env.PATH.prepend("{root}/bin")
    env.PYTHONPATH.prepend("{root}/python")
