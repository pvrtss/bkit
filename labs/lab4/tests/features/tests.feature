Feature: Modern or Vintage

  In order to extend the list of produced chairs
  As a chair factory manager
  I want my workers to decide in which factory 
  they will create chairs, based on customer's style choice 



  Scenario: Cheap vintage chair
    Given The chair style is vintage, weight is 3 lbs, cost is 50 dollars
    When We choosing factory we must choose appropriate one 
    Then Produced chair should be vintage with given parameters: weight is 3 lbs, cost is 50 dollars

  Scenario: Expensive vintage chair
    Given The chair style is vintage, weight is 6 lbs, cost is 350 dollars
    When We choosing factory we must choose appropriate one 
    Then Produced chair should be vintage with given parameters: weight is 6 lbs, cost is 350 dollars

  Scenario: Cheap modern chair
    Given The chair style is modern, weight is 2 lbs, cost is 55 dollars
    When We choosing factory we must choose appropriate one 
    Then Produced chair should be modern with given parameters: weight is 2 lbs, cost is 55 dollars

  Scenario: Expensive modern chair
    Given The chair style is modern, weight is 7 lbs, cost is 150 dollars
    When We choosing factory we must choose appropriate one 
    Then Produced chair should be modern with given parameters: weight is 7 lbs, cost is 150 dollars
