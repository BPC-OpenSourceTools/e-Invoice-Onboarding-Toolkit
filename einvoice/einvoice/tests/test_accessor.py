#!/usr/bin/env python3
# pylint: disable=W1203
# Not using lazy logging.
# File: test_line_item.py
# About: e-Invoice testing suite; line_item.
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-08-15 (August 15th, 2021)
#
"""This is a test file to be run using pytest.

"""
import os
from os.path import join, dirname
from dotenv import load_dotenv
from einvoice.app_logging import create_logger
from einvoice.accessor import Accessor


def test_accessor():
    """Pytest case for test_accesspr."""
    log = create_logger("test_accessor")
    log.info("Start accessor test")
    dotenv_path = join(dirname(__file__), '../../certificates/.env')
    load_dotenv(dotenv_path)
    specification = str(os.getenv("TEST_SPECIFICATION"))
    log.info("Specification: %s", specification)
    schema_id = str(os.getenv("TEST_SCHEMA_ID"))
    log.info("schema_id: %s", schema_id)
    party_id = str(os.getenv("TEST_PARTY_ID"))
    log.info("party_id: %s", party_id)

    accessor_test = Accessor()

    test_urn = accessor_test.call_hash(specification, schema_id,
                                       party_id)
    log.info(f"returned urn dict: {test_urn}")
    test_specification = test_urn["specification"]
    test_schema_type_id = test_urn["schema_type_id"]
    test_party_id = test_urn["party_id"]
    example_urn = (f"{test_specification}:{test_schema_type_id}::"
                   f"{test_party_id}")

    log.info("Urn is: %s", example_urn)
    test_final_urn = test_urn["final_urn"]
    assert test_final_urn == example_urn.lower()

    hashed_urn = accessor_test.call_hash(test_specification,
                                         test_schema_type_id, test_party_id)
    log.info("Hashed urn: %s", hashed_urn)
    assert hashed_urn["urn_hash"] == (
        "yn5tj7bteln4c5o4mtul7yv"
        "nq3pwu6dpmipcof4pwcbsd3avvn7a"
    )