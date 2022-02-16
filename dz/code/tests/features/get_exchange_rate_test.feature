Feature: Right Currency Choosing

  Scenario: XRP TO RUB 
    Given Crypto currency is XRP, to currency is RUB 
    Then Result must be between 60 and 90

  Scenario: BTC TO USD
    Given Crypto currency is BTC, to currency is USD 
    Then Result must be between 30000 and 60000
