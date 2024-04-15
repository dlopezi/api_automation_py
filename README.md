# automation_py
Task for automation course

Comamnds to run:

1. To run the test cases, run the following command:
```python -m pytest odoo_module/ -v -s```

2. To run the test cases with html report, run the following command:
```python -m pytest odoo_module/ -v -s --html=pytest_html_report.html```

3. To run behave for all the features:
```behave```

4. To run allure:
```python -m pytest odoo_module --alluredir=allure```

5. To run Dockerfile:
```docker build -t pytest-auto-framework .```