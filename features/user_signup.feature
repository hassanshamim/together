Scenario:
  As an interested party
  In order to explore the site and create an event
  I want to create a Together account


Given that I am on the root page
And I click the 'Sign Up' link
Then I should see the 'Sign Up' button
And the current path should be '/signup'

Given I am on the Sign Up page
And I enter 'hassan.has.you@gmail.com' in the email field
And I enter 'a_password' in the password field
And I click the 'Sign Up' button
Then I should see 'Congratulations' on the page
