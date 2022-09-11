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

from src.test_python import run_error, run_failure, run_random, run_skip, run_success, run_percent_error


def test_success():
    assert run_success()

def test_failure():
    assert run_failure()

def test_error():
    assert run_error()

def test_random():
    assert run_random()

def test_percent_error_1():
    assert run_percent_error(1)

def test_percent_error_5():
    assert run_percent_error(5)

def test_percent_error_10():
    assert run_percent_error(10)

def test_percent_error_20():
    assert run_percent_error(20)

def test_percent_error_30():
    assert run_percent_error(30)

def test_percent_error_50():
    assert run_percent_error(50)

def test_percent_error_75():
    assert run_percent_error(75)

def test_percent_error_90():
    assert run_percent_error(90)

def test_percent_error_95():
    assert run_percent_error(95)

def test_percent_error_99():
    assert run_percent_error(99)
