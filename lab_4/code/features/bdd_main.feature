Feature: Test Biquadratic equation Functionality

Scenario: Test my biquadratic equation
    Given Biquadratic equation app is run
    When I have the odds "1", "-5", and "6"
    Then I get result "-1.732, 1.732, -1.414, 1.414"

Scenario: Test my biquadratic equation
    Given Biquadratic equation app is run
    When I have the odds "1", "-4", and "4"
    Then I get result "-1.414, 1.414"

Scenario: Test my biquadratic equation
    Given Biquadratic equation app is run
    When I have the odds "1", "0", and "-16"
    Then I get result "-2.0, 2.0"