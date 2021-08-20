#!/bin/bash
# Script that takes in a URL, sends a request to that URL
# and displays the size of the body of the response using cURL

curl -sI "$1" | grep -i Content-Length
