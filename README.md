
This is an implementation of a simple HTTP webserver which accepts a POST. This currently is written to accept JSON and does a quick load and prints the output to the screen. Please feel free to use this and modify. This source code is licensed under MPL 2.0

## How to run pyWebserv
python pywebserv.py <port number>

## SAMPLE commands to POST using curl
* Send a GET request::    
** curl http://localhost
* Send a HEAD request::   
** curl -I http://localhost
* Send a POST request::   
** curl -d "foo=bar&bin=baz" http://localhost
