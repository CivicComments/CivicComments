# CivicComments

The mission of CivicComments is to make civic comments public immediately.

## Running CivicComments locally

### Initial prep

* Setup a Ngrok.io account with subdomain
* Setup local dns ``nanobox dns add local civiccomments.local``
* Setup an Auth0 account with two connections: web app and machine to machine
* Add evars for Auth0 and Stripe
``nanobox evar add local AUTH0_OAUTH_KEY= AUTH0_OAUTH_SECRET= AUTH0_MANAGEMENT_KEY= AUTH0_MANAGEMENT_SECRET= STRIPE_TEST_PUBLIC_KEY= STRIPE_TEST_SECRET_KEY=``
* Add authorized urls to Auth0
``https://civiccomments.ngrok.io/complete/auth0, https://civiccomments.org/complete/auth0``

### Commands for running each time

Command for starting Django ``cd ~/civiccomments; nanobox run python manage.py runserver 0.0.0.0:8000``
Command for starting Ngrok.io ``cd; ./ngrok http --subdomain=[YOUR NGROK SUBDOMAIN] civiccomments.local:8000`` e.g. ``cd; ./ngrok http --subdomain=civiccomments civiccomments.local:8000``
