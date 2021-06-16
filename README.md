# python_slack
python_slack_notification
Code sample to test if url is valid and update slack channels with the information.

**Python version - 3.9.5 **

## Repo includes the following
1. Main script
2. f.py function file that includes functions to test and dechipher url status codes.
3. slack.py that shows the basic of how to send slack message to a channel from slack documentation (https://slack.dev/python-slackclient/basic_usage.html)
4. URL to clone repo https://github.com/Talg39/python_slack.git
### Task
1. Validate that the code is running as expected as given, if not fix the mistakes.
2. Complete the slack function to send slack messages to a channel.
    a. message template should include the following
      * url address that the user has given.
      * status code
3. There are three scenarios when the code will send the message. (see comments in code where to call the function)
    * When status code is 200 (OK)
    * When the status code isn't 200 (OK)
    * When given url by the user input is not valid 
    
4. Before committing and pushing the code remove the token variable for slack (security reassons :) )

#### Bonus
1. Include in the slack message the current logged in user to the computer
2. Include the date and time in slack message
