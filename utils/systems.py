"""This module contains functions to access the system library.
If you want to use this module in your jupyter notebook, you need to
install the pyyaml package. You can do this by running the following
command in your terminal: %pip install pyyaml."""

import yaml
import control as ct
from pathlib import Path

system_library = Path(__file__).parent / "systems" / "systems.yaml"


def library_tf_SISO(system: int) -> tuple[ct.TransferFunction, str]:
    """Returns the a tuple containing the transfer function and the
    name of the system."""
    with open(system_library, "r") as f:
        try:
            systems = yaml.safe_load(f)["Num/Den SISO"]
            if system > len(systems):
                raise ValueError(f"System {system} not found in systems.yaml")
            tf = ct.TransferFunction(systems[system]["num"], systems[system]["den"])
            return tf, systems[system]["name"]

        except yaml.YAMLError as exc:
            raise Exception(exc)

def library_ss_SISO(system: int) -> tuple[ct.StateSpace, str]:
    """Returns the a tuple containing the state space representation and the
    name of the system."""
    with open(system_library, "r") as f:
        try:
            systems = yaml.safe_load(f)["State Space SISO"]
            if system > len(systems):
                raise ValueError(f"System {system} not found in systems.yaml")
            ss = ct.StateSpace(systems[system]["A"], systems[system]["B"],
                               systems[system]["C"], systems[system]["D"])
            return ss, systems[system]["name"]

        except yaml.YAMLError as exc:
            raise Exception(exc)
        
def library_ss_MIMO(system: int) -> tuple[ct.StateSpace, str]:
    """Returns the a tuple containing the state space representation and the
    name of the system."""
    with open(system_library, "r") as f:
        try:
            systems = yaml.safe_load(f)["State Space MIMO"]
            if system > len(systems):
                raise ValueError(f"System {system} not found in systems.yaml")
            ss = ct.StateSpace(systems[system]["A"], systems[system]["B"],
                               systems[system]["C"], systems[system]["D"])
            return ss, systems[system]["name"]

        except yaml.YAMLError as exc:
            raise Exception(exc)       
