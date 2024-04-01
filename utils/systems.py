"""This module contains functions to access the system library."""

import yaml
import control as ct
from pathlib import Path

system_library = Path(__file__).parent / "systems" / "systems.yaml"


def library_tf(system: int) -> tuple[ct.TransferFunction, str]:
    """Returns the a tuple containing of the transfer function and the
    name of the system."""
    with open(system_library, "r") as f:
        try:
            systems = yaml.safe_load(f)
            if system > len(systems):
                raise ValueError(f"System {system} not found in systems.yaml")
            tf = ct.TransferFunction(systems[system]["num"], systems[system]["den"])
            return tf, systems[system]["name"]

        except yaml.YAMLError as exc:
            raise Exception(exc)
