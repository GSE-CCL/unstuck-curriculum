#!/usr/bin/env bash

# This script is called by package.json after intstalling any node modules. 

# Copy BootStrap Javascript output from node node plugin folder to appropriate site content folder.  
cp node_modules/bootstrap/dist/js/bootstrap.min.* app/static/js/

