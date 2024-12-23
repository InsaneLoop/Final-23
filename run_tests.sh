#!/bin/bash

# Run all tests and generate Allure report
pytest --alluredir=allure-results
allure serve allure-results