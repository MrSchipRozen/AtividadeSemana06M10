from behave import given, when, then
from src.conversao import celsius_para_fahrenheit

@given('que a temperatura é {celsius:d} graus Celsius')
def step_impl(context, celsius):
    context.celsius = celsius

@when('eu converto para Fahrenheit')
def step_impl(context):
    context.resultado = celsius_para_fahrenheit(context.celsius)

@then('o resultado deve ser {fahrenheit:d} graus Fahrenheit')
def step_impl(context, fahrenheit):
    assert context.resultado == fahrenheit
