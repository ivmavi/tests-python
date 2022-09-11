# tests-python

Test suite written in Python.
This suite cover the baisc test success and failures.
* Test Always success
* Test Always fail
* Test Always throw and error
* Test fails ramdomly
* Test fails 1% of the executions
* Test fails 5% of the executions
* Test fails 10% of the executions
* Test fails 20% of the executions
* Test fails 30% of the executions
* Test fails 50% of the executions
* Test fails 75% of the executions
* Test fails 90% of the executions
* Test fails 95% of the executions
* Test fails 99% of the executions

# Usage 

To run the test you can use the `make test` target this will generate the file `junit-test_suite.xml` file,
the file contains the test suite result in JUnit format.

# Contributing

If you want to add your own use case you must follow these steps:
* Create your own fork
* Add your code and your tests
* Check your code is correct `make lint` and `make test`
* Submit a pull request to the main repository
* Be patient, we will review your PR for sure.

