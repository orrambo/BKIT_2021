Feature: Test summary
    Scenario: test summary for making check with 1 2 3
        Given ordering albums with answers in bot queen album - 1 rhcp album - 2 green day album - 3
        When we form summary of check
        Then check should be with correct price 13600
    Scenario: test summary for making check with 2 1 3
        Given ordering albums with answers in bot queen album - 2 rhcp album - 1 green day album - 3
        When we form summary of check
        Then check should be with correct price 13700