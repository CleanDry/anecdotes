# Anecdotes

An app to keep track of anecdotes and find other people who have found anecdotes you might be interested.

Built for HY Cyber Security Base course. Has several intentional security flaws for showcasing. Main exploits are:
- SQL-injection
- Broken authentication
- Sensitive data exposure
- Broken access control
- Security misconfiguration

Built with Python and Django.

### Instructions

You need to have Python and Django installed and set up.

To use app, you must start the Django server by:
- Going to anecdotes directory with your CLI (the one that has manage.py)
- run commands: 
``` python3 manage.py migrate ```
``` python3 manage.py runserver ```
- open the link provided in server startup prompt. Default: http://127.0.0.1:8000

Built in test users (Username: Password):

mikke: mikkepw

jakke: jakkepw
