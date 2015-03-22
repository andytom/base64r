# base64r

A simple tool for dealing with base64 encoded files.

**Deprecated in favour of [toolkit](https://github.com/andytom/toolkit)**

## About

base64r is a simple tool for decoding base64 strings into binary documents.

## Usage

A list of requirements can be found in the requirements.txt file.

You should change the ```SECRET_KEY``` in the main.cfg file to be something more secure.

A development server can be started by running ```python run_dev_server.py```

## TODO
* Limit the filesize
* Test for valid base64
* Use cStringIOs when available
* Better Test
 * Test for unknow file types ('.dat')
