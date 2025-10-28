#!/bin/bash

# Ensure the script is running from the 'src' directory
currentDir=$(dirname "$0")
srcDir="$currentDir"
pdfDir="$currentDir/../pdfs"

# Ensure the destination directory exists
mkdir -p "$pdfDir"

# Get all .md files in the source directory
mdFiles=("$srcDir"/*.md)

# Convert each .md file to .pdf using Pandoc
for mdFile in "${mdFiles[@]}"; do
    mdFilePath=$(basename "$mdFile")
    pdfFilePath="$pdfDir/${mdFilePath%.md}.pdf"
    
    echo "Converting $mdFilePath to $pdfFilePath"
    
    # Execute the pandoc command
    pandoc --pdf-engine=xelatex "$mdFile" -o "$pdfFilePath"
done
