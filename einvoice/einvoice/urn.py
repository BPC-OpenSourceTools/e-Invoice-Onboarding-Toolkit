#!/usr/bin/env python3
#
# File: urn.py
# About: Dataclass definition of a urn.
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-06-20 (June 20, 2021)
#
"""The dataclass object representing a urn for lookup.

The small class encapsulates the necessary information to work
with the urn as an object.

    Usage:
    my_urn = einvoice()

"""
from dataclasses import dataclass


@dataclass
class Urn:
    """Dataclass which represents the base URN for the SML query.

    The base URN to be constructed as a string.

    Args:

    Attributes:
        specification: str
            OASIS urn specification.
        schema_id: str
            OASIS schema identifier.
        party_id: str
            Unique identifier for the party.
        urn: str
            The urn constructed by default values or passed into the
            dataclass when called.

    Returns:
        Urn as str.

    Raises:

    """

    specification: str = ""
    schema_id: str = ""
    party_id: str = ""

    def urn(self) -> str:
        """Construct string for the party's URN"""
        # return str(f"{self.specification}:{self.schema_id}::{self.party_id}")
        return f"{self.specification}:{self.schema_id}::{self.party_id}"
