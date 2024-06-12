# Ensure the script is running from the 'src' directory
$currentDir = Split-Path -Path $MyInvocation.MyCommand.Definition -Parent
$srcDir = $currentDir
$pdfDir = Join-Path -Path $currentDir -ChildPath "..\pdfs"

# Ensure the destination directory exists
if (-not (Test-Path $pdfDir)) {
    New-Item -ItemType Directory -Path $pdfDir -Force
}

# Get all .md files in the source directory
$mdFiles = Get-ChildItem -Path $srcDir -Filter *.md

# Convert each .md file to .pdf using Pandoc
foreach ($mdFile in $mdFiles) {
    $mdFilePath = $mdFile.Name
    $pdfFilePath = Join-Path -Path "..\pdfs" -ChildPath ($mdFile.BaseName + ".pdf")
    
    Write-Host "Converting $mdFilePath to $pdfFilePath"
    
    # Execute the pandoc command
    & pandoc $mdFilePath -o $pdfFilePath
}
