from behave import *
from Pages import RegistrationPage
from Base import startBrowser
import time


@given(u'User is on registration page')
def step_impl(context):
    context.driver = startBrowser.start_browser()
    context.register = RegistrationPage.RegistrationClass(context.driver)

@when(u'User enters username')
def step_impl(context):
    context.register.enter_username("John", "Doe")


@when(u'User enters email id')
def step_impl(context):
    context.register.enter_email("teste@email.com")


@when(u'User select Male')
def step_impl(context):
    context.register.enter_button_male()


@when(u'User enters phoneNumber')
def step_impl(context):
    context.register.enter_phoneNumber("61991567089")


@when(u'User upload file')
def step_impl(context):
    context.register.enter_uploadPicture("D:\\BDDautomationPOM\\configFiles\\Elements.cfg")


@when(u'User Click on signup button')
def step_impl(context):
    context.register.click_submmit()


@then(u'User should be registered successfully')
def step_impl(context):
    time.sleep(5)
    print("User registered successfully")

