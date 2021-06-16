# pyhon_slack
python_slack_notification
Code sample to test if url is valid and update slack channels with the information.

## Repo includes the following
1. Main script
2. f.py functions file that include function to test and dechipher url status code.
3. slack.py that show the basic to send slack message to channel from slack documentation (https://slack.dev/python-slackclient/basic_usage.html)
4. URL to clone repo https://github.com/Talg39/python_slack.git
### Task
1. Validate that the code is running as expected as given, if not fix the mistakes.
2. Complete the slack function to send slack messages to a channel.
    a. message template should include the following
      * url address that the user has given.
      * status code
3. There are three scenarios when the code will send the message. (see comments in code where to call the function)
    a. When status code is 200 (OK)
    b. When the status code isn't 200 (OK)
    c. When given url by the user input is not valid 
    
4. When finish before commit and push the code remove the token variable for slack (security reassons :) )

#### Bonus
1. Include in the slack message the current logged in user to the computer
2. Include the date and time in slack message
