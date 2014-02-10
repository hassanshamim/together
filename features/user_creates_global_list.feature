Scenario:
   As an organizer for the event
   In order to make sure all attendees are on the same page and prepared
   I want to create a To-Do list for every person or pod

Given I am logged in
And I am on my account page
And I click 'To-Do Lists'
Then I am on the 'list' page
And I see the 'Create List' link
And I click 'Create List'
Then I should be on the 'new_list' page

Given I am logged in
And I am an Organizer
And I go to the 'new_list' page
And I click 'Create Item'
And I enter the title 'Bring Grab Bag Gift'
And I enter the description 'Wrapped gift <$5 for exchange after dinner, before dessert'
And I click 'Create'
Then I should be on the 'list' page
And I should see the 'Bring Grab Bag Gift' link
