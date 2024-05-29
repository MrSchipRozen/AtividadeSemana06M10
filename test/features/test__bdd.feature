Feature: Conversão de Temperatura

  Scenario: Converter Celsius para Fahrenheit
    Given que a temperatura é 0 graus Celsius
    When eu converto para Fahrenheit
    Then o resultado deve ser 32 graus Fahrenheit