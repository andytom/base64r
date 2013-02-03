# base64r

A simple tool for dealing with base64 encoded files.

## About

base64r is a simple tool for decoding base64 strings into binary documents.

## Usage

A list of requirements can be found in the requirements.pip file.

You should change the SECRET_KEY in the main.cfg file to be something more secure.
You can set up a development server by running "python run_dev_server.py".

If used in a production environment the static and the OUTPUT_FOLDER (set in main.cfg) need to be served by a Web Server (eg. Apache or Nginx) since they will perform a lot better than flask.

