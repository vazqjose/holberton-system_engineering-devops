#!/bin/bash
# Script that takes in a URL, returns size of body
curl -sI "$1" | grep -i Content-Length
