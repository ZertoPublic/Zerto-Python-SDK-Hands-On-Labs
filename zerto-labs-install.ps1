# Fixed Zerto Labs Installation Script
param([string]$InstallPath = "C:\zerto-labs")

Write-Host "=== Zerto Labs Installation Script ===" -ForegroundColor Cyan
Write-Host "Installation path: $InstallPath" -ForegroundColor White

# Create installation directory
if (!(Test-Path $InstallPath)) {
    Write-Host "Creating installation directory..." -ForegroundColor Yellow
    New-Item -ItemType Directory -Path $InstallPath -Force | Out-Null
    Write-Host "Directory created successfully!" -ForegroundColor Green
} else {
    Write-Host "Directory already exists!" -ForegroundColor Yellow
}

# Create temp directory
$TempDir = Join-Path $InstallPath "temp"
New-Item -ItemType Directory -Path $TempDir -Force | Out-Null

# Download repositories - Simple step by step
# First repository: zvml-python-sdk
$repoName = "zvml-python-sdk"
$repoUrl = "https://github.com/ZertoPublic/zvml-python-sdk/archive/refs/heads/main.zip"
$zipFile = Join-Path $TempDir "$repoName.zip"

Write-Host "`nProcessing: $repoName" -ForegroundColor Cyan
Write-Host "URL: $repoUrl" -ForegroundColor White

try {
    # Download
    Write-Host "Downloading..." -ForegroundColor Yellow
    $webClient = New-Object System.Net.WebClient
    $webClient.DownloadFile($repoUrl, $zipFile)
    $webClient.Dispose()
    Write-Host "Download completed!" -ForegroundColor Green
    
    # Extract
    Write-Host "Extracting..." -ForegroundColor Yellow
    $extractPath = Join-Path $InstallPath $repoName
    Expand-Archive -Path $zipFile -DestinationPath $extractPath -Force
    Write-Host "Extraction completed!" -ForegroundColor Green
    
    # Copy contents from -main folder to parent directory
    Write-Host "Copying contents from -main folder..." -ForegroundColor Yellow
    $mainFolders = Get-ChildItem -Path $extractPath -Directory | Where-Object { $_.Name -like "*-main" }
    
    if ($mainFolders.Count -gt 0) {
        $mainFolder = $mainFolders[0]
        Write-Host "Found main folder: $($mainFolder.Name)" -ForegroundColor White
        
        # Copy all contents from the main folder to the extract path
        $sourcePath = $mainFolder.FullName
        Write-Host "Copying from: $sourcePath" -ForegroundColor White
        Write-Host "Copying to: $extractPath" -ForegroundColor White
        
        Copy-Item -Path "$sourcePath\*" -Destination $extractPath -Recurse -Force
        Write-Host "Contents copied successfully!" -ForegroundColor Green
        
        # Delete the -main folder
        Write-Host "Removing -main folder..." -ForegroundColor Yellow
        Remove-Item -Path $sourcePath -Recurse -Force
        Write-Host "-main folder removed!" -ForegroundColor Green
    } else {
        Write-Host "No -main folder found in extracted content!" -ForegroundColor Red
    }
    
    Write-Host "$repoName installed successfully!" -ForegroundColor Green
}
catch {
    Write-Host "Failed to install $repoName`: $($_.Exception.Message)" -ForegroundColor Red
}

# Second repository: Zerto-Python-SDK-Hands-On-Labs
$repoName = "Zerto-Python-SDK-Hands-On-Labs"
$repoUrl = "https://github.com/ZertoPublic/Zerto-Python-SDK-Hands-On-Labs/archive/refs/heads/main.zip"
$zipFile = Join-Path $TempDir "$repoName.zip"

Write-Host "`nProcessing: $repoName" -ForegroundColor Cyan
Write-Host "URL: $repoUrl" -ForegroundColor White

try {
    # Download
    Write-Host "Downloading..." -ForegroundColor Yellow
    $webClient = New-Object System.Net.WebClient
    $webClient.DownloadFile($repoUrl, $zipFile)
    $webClient.Dispose()
    Write-Host "Download completed!" -ForegroundColor Green
    
    # Extract
    Write-Host "Extracting..." -ForegroundColor Yellow
    $extractPath = Join-Path $InstallPath $repoName
    Expand-Archive -Path $zipFile -DestinationPath $extractPath -Force
    Write-Host "Extraction completed!" -ForegroundColor Green
    
    # Copy contents from -main folder to parent directory
    Write-Host "Copying contents from -main folder..." -ForegroundColor Yellow
    $mainFolders = Get-ChildItem -Path $extractPath -Directory | Where-Object { $_.Name -like "*-main" }
    
    if ($mainFolders.Count -gt 0) {
        $mainFolder = $mainFolders[0]
        Write-Host "Found main folder: $($mainFolder.Name)" -ForegroundColor White
        
        # Copy all contents from the main folder to the extract path
        $sourcePath = $mainFolder.FullName
        Write-Host "Copying from: $sourcePath" -ForegroundColor White
        Write-Host "Copying to: $extractPath" -ForegroundColor White
        
        Copy-Item -Path "$sourcePath\*" -Destination $extractPath -Recurse -Force
        Write-Host "Contents copied successfully!" -ForegroundColor Green
        
        # Delete the -main folder
        Write-Host "Removing -main folder..." -ForegroundColor Yellow
        Remove-Item -Path $sourcePath -Recurse -Force
        Write-Host "-main folder removed!" -ForegroundColor Green
    } else {
        Write-Host "No -main folder found in extracted content!" -ForegroundColor Red
    }
    
    Write-Host "$repoName installed successfully!" -ForegroundColor Green
}
catch {
    Write-Host "Failed to install $repoName`: $($_.Exception.Message)" -ForegroundColor Red
}

# Clean up
Write-Host "`nCleaning up..." -ForegroundColor Yellow
Remove-Item -Path $TempDir -Recurse -Force

# Create README
$readmeContent = "# Zerto Labs Installation`n`n"
$readmeContent += "This directory contains the Zerto Python SDK and Hands-On Labs.`n`n"
$readmeContent += "## Directory Structure`n"
$readmeContent += "- `zvml-python-sdk/` - Zerto Virtual Manager Linux Python SDK`n"
$readmeContent += "- `Zerto-Python-SDK-Hands-On-Labs/` - Hands-on labs and exercises`n`n"
$readmeContent += "## Setup Instructions`n`n"
$readmeContent += "### 1. Install Python`n"
$readmeContent += "Make sure you have Python 3.8 or higher installed.`n`n"
$readmeContent += "### 2. Create Virtual Environment`n"
$readmeContent += "```powershell`n"
$readmeContent += "cd Zerto-Python-SDK-Hands-On-Labs`n"
$readmeContent += "python -m venv venv`n"
$readmeContent += ".\venv\Scripts\Activate.ps1`n"
$readmeContent += "pip install -r prerequisites\requirements.txt`n"
$readmeContent += "pip install -e ..\zvml-python-sdk`n"
$readmeContent += "````n`n"
$readmeContent += "## Next Steps`n"
$readmeContent += "1. Configure your ZVM connection details in `prerequisites\config.py``n"
$readmeContent += "2. Start with Exercise 1 in the Hands-On Labs`n"
$readmeContent += "3. Follow the step-by-step instructions in each exercise`n`n"
$readmeContent += "Installation completed on: $(Get-Date)"

$readmePath = Join-Path $InstallPath "README.md"
$readmeContent | Out-File -FilePath $readmePath -Encoding UTF8

Write-Host "`n=== Installation Complete ===" -ForegroundColor Green
Write-Host "Installation directory: $InstallPath" -ForegroundColor White

# Show what was installed
Write-Host "`nInstalled repositories:" -ForegroundColor Cyan
Write-Host "  + zvml-python-sdk" -ForegroundColor Green
Write-Host "  + Zerto-Python-SDK-Hands-On-Labs" -ForegroundColor Green

Write-Host "`nNext steps:" -ForegroundColor Cyan
Write-Host "1. Navigate to: $InstallPath" -ForegroundColor White
Write-Host "2. Read the README.md file for setup instructions" -ForegroundColor White
Write-Host "3. Configure your ZVM connection details" -ForegroundColor White
Write-Host "4. Start with the Hands-On Labs exercises" -ForegroundColor White
Write-Host "Installation completed successfully!" -ForegroundColor Green

# Open VS Code with the installation directory
Start-Process "C:\Users\$env:USERNAME\AppData\Local\Programs\Microsoft VS Code\Code.exe" -ArgumentList "C:\zerto-labs"

# Pause at the end to show results
Write-Host "`nPress any key to exit..." -ForegroundColor Cyan
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown") 
