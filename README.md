# django-webdriver
[![pypi version](http://img.shields.io/pypi/v/django-webdriver.svg)](https://pypi.python.org/pypi/django-webdriver) [![pypi download week](http://img.shields.io/pypi/dw/django-webdriver.svg)](https://pypi.python.org/pypi/django-webdriver)

Django app to run selenium tests with webdriver

## Features

Extends the feature of [django-nose](https://github.com/django-nose/django-nose) to manage the selenium tests.

## Installation

You can get django-webdriver from PyPi:
```bash
pip install django-webdriver
```
  
To use it you should add it to your `INSTALLED_APPS` in `settings.py`.  
Django-webdriver uses django-nose to run the tests, so you should also configure django-nose in your project:

```python
INSTALLED_APPS = (
    ...  
    'django_webdriver',
    'django_nose',
    ...
)
  
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
```
  
## Usage

With django-webdriver you may run just unit tests or just selenium tests or the both.

### Launch tests

* `--selenium-only`: only run selenium tests
* `--with-selenium`: run all tests (unit and selenium)
* ` `: will only run unit test.

### Configure

#### Local

Add `--webdriver=` to specify webdriver you want to use locally.

It can be one of these for example (be careful to case):
* Firefox
* PhantomJS
* Chrome
* ...
* [More here](http://selenium-python.readthedocs.org/en/latest/api.html#webdriver-api)

##### Example

```bash
./manage.py test --with-selenium --webdriver=PhantomJS
```

#### Remote

* Add `--remote_selenium_provider=` to specify which remote grid you want to use.
* Add configuration for each grid in your `settings.py`:
```python
DJANGO_WEBDRIVER_SETTINGS = {
    'remote_providers': {
        'grid': {
            'url': 'http://192.168.0.18:4444/wd/hub',
            # will use 'default' capabilities
        },
        'sauce-lab': {
            'url': 'http://my_url',
            'capabilities': 'ie',
        },
    },
    'remote_capabilities': {
        'default': [
            {
                'browser': 'firefox',
                'platform': 'WINDOWS'
            },
        ],
        'ie': [
            {
                'browser: 'internet explorer',
                'version': 6,
            }
        ]
    }
}
```

### Write selenium tests

To write selenium tests you have to name the files `tests_selenium.py`. You may also use a python module name `tests_selenium` but you have to define your test files in the `__init__.py`.  

Your selenium test classes have to inherit of `django_webdriver.base.DjangoWebdriverTestCase`.
You have not to manage the life cycle of the webdriver in the setUp or in the tearDown methods. The webdriver is instanciated before the setUp and it is stoped after the tearDown, so you may use it in these methods.

```python
from django_webdriver.base import DjangoWebdriverTestCase

class TestSelenium(DjangoWebdriverTestCase):

    def setUp(self):
        self.webdriver.get('http://wwww.github.com') #it's ok
        self.webdriver = '...' #it's forbiden because you break the life cycle.
    
    def tearDown(self):
        self.webdriver... #it's ok
        self.webdriver.quit() #it's forbiden because you break the life cycle too.
    
    def test_google(self):
        url = 'https://www.google.fr/'
        self.webdriver.get(url)
        self.assertEqual(url, self.webdriver.current_url)

```

