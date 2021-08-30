#!/usr/bin/env python3
#
# File: test_urn.py
# About: e-Invoice testing suite; urn.
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-08-15 (August 15th, 2021)
#
"""This is a test file to be run using pytest.

"""
from einvoice.app_logging import create_logger
from einvoice.urn import Urn


def create_urn():
    """Test helper to create an instace of an object to test."""
    some_urn = Urn("urn:oasis:names:tc:ebcore:partyid-type",
                   "iso6523", "0123456789")
    return some_urn


def test_urn():
    """Test case for party_address."""
    log = create_logger("test_urn")
    log.info("Begin testing urn creation.")
    another_urn = create_urn()
    log.info(f"specification: {another_urn.specification}")
    assert another_urn.specification == "urn:oasis:names:tc:ebcore:"\
        "partyid-type"
    log.info(f"schema: {another_urn.schema}")
    assert another_urn.schema == "iso6523"
    log.info(f"party_id {another_urn.party_id}")
    assert another_urn.party_id == "0123456789"
    log.info(f"urn: {another_urn.urn()}")
    assert (
        another_urn.urn()
        == "urn:oasis:names:tc:ebcore:partyid-type:iso6523:0123456789"
    )
    log.info("Completed testing urn creation.")
