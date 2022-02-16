Feature: Right formatting of currency

  Scenario: 1000 RUB
    Given Number is 1000, currency is RUB 
    Then Result must be _1 000,00 ₽_

  Scenario: 1000 USD
    Given Number is 1000, currency is USD 
    Then Result must be _1 000,00 $_
