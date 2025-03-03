#!/bin/bash

# Define the directory to search
SEARCH_DIR=${1:-.}

# Define the target and replacement
TARGET='\${jenkins_env.fp_image_hash}'
REPLACEMENT="pipeline"

# Find and replace all the files
find "$SEARCH_DIR" -type f -exec sed -i "s|$TARGET|$REPLACEMENT|g" {} +

echo "Replacement complete. FROM '${TARGET}' to '${REPLACEMENT}' in all the files under '$SEARCH_DIR'."
