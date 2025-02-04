"""
Other utils in this proj
"""

import subprocess
from os import path
from re import sub

from py_apps.utils.app_manage import install_app


def to_snakecase(string: str) -> str:
    """
    Change the given string to the from of a_b_c (Snake Case)

    Params:
        str string: the input string
    """

    return "_".join(
        sub(
            "([A-Z][a-z]+)", r" \1", sub("([A-Z]+)", r" \1", string.replace("-", " "))
        ).split()
    ).lower()


def fix_electron_libxssl(distro: str) -> None:
    """Fix electron libxssl problem"""
    match distro:
        case "debian":
            if (
                not subprocess.run(
                    ["whereis", "libnss3.so"], stdout=subprocess.PIPE
                ).stdout.decode("utf-8")
                == "libnss3.so:"
            ):
                install_app(distro, ["libnss3"])
        case "redhat":
            install_app(distro, ["libXScrnSaver"])
        case "arch":
            if not path.exists("/usr/lib/libnss3.so"):
                install_app(distro, ["nss"])
        case "suse":
            install_app(distro, ["mozilla-nss"])
        case _:
            install_app(distro, ["nss"])
