#    Copyright 2022 name of copyright ivmavi

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

import random

"""Test suite functions

This module contains functions that are used to test the test suite.
"""

def run_success() -> bool:
    """ Simulate a successful test """
    print("Success")
    return True

def run_failure() -> bool:
    """ Simulate a failed test """
    print("Failure")
    return False

def run_error() -> bool:
    """ Simulate an error """
    print("Error")
    raise Exception("Error")

def run_skip() -> None:
    """ Simulate a skipped test """
    print("Skip")
    return None

def run_random() -> bool:
    """ Simulate a random test """
    print("Random")
    return random.choice([True, False])

def run_percent_error(percent: int) -> bool:
    """ Simulate a random test with a % chance of error """
    print("Percent Error")
    if random.randint(1, 100) < percent:
        return run_failure()
    return run_success()
