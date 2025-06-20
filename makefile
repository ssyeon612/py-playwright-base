.PHONY: test report open clean

test:
	pytest

report:
	allure generate allure-results -o allure-report --clean

open:
	allure open allure-report

clean:
ifeq ($(OS),Windows_NT)
	del /s /q allure-results allure-report screenshots 2>nul || exit 0
	rmdir /s /q allure-results allure-report screenshots 2>nul || exit 0
else
	rm -rf allure-results allure-report screenshots
endif

codegen:
	playwright codegen https://www.google.com --output sample.py