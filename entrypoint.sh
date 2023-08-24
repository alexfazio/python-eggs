#!/bin/bash

# Check if python is installed
if command -v python > /dev/null 2>&1; then
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    pip install -r requirements.txt
else
      pip install -r requirements.txt
fi
