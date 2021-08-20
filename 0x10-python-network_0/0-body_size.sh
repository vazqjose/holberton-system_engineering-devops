#!/bin/bash
# Script that takes in a URL, returns size of body
curl -s $1 | grep -i Content-Length | awk '{print $2}'
