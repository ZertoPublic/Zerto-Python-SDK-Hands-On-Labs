# Fixed Zerto Labs Installation Script
param([string]$InstallPath = "C:\zerto-labs")

Write-Host "=== Zerto Labs Installation Script ===" -ForegroundColor Cyan
Write-Host "Installation path: $InstallPath" -ForegroundColor White

# Install Python 3.13.5
Write-Host "`nInstalling Python 3.13.5..." -ForegroundColor Yellow

# Create temp directory for Python installer
$TempDir = Join-Path $InstallPath "temp"
New-Item -ItemType Directory -Path $TempDir -Force | Out-Null

# Download Python installer
$pythonUrl = "https://www.python.org/ftp/python/3.13.5/python-3.13.5-amd64.exe"
$pythonInstaller = Join-Path $TempDir "python-3.13.5-amd64.exe"

Write-Host "Downloading Python 3.13.5..." -ForegroundColor Yellow
try {
    $webClient = New-Object System.Net.WebClient
    $webClient.DownloadFile($pythonUrl, $pythonInstaller)
    $webClient.Dispose()
    Write-Host "Python installer downloaded successfully!" -ForegroundColor Green
}
catch {
    Write-Host "Failed to download Python installer: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}

# Install Python with "add to path" option
Write-Host "Installing Python 3.13.5..." -ForegroundColor Yellow
Write-Host "This may take a few minutes. Please wait..." -ForegroundColor White

try {
    $process = Start-Process -FilePath $pythonInstaller -ArgumentList "/quiet", "InstallAllUsers=1", "PrependPath=1", "Include_test=0" -Wait -PassThru
    if ($process.ExitCode -eq 0) {
        Write-Host "Python installed successfully!" -ForegroundColor Green
    } else {
        Write-Host "Python installation failed with exit code: $($process.ExitCode)" -ForegroundColor Red
        exit 1
    }
}
catch {
    Write-Host "Failed to install Python: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}

# Refresh environment variables
Write-Host "Refreshing environment variables..." -ForegroundColor Yellow
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

# Verify Python installation
Write-Host "Verifying Python installation..." -ForegroundColor Yellow
$pythonVersion = python --version 2>$null
if ($pythonVersion) {
    Write-Host "Python installation verified: $pythonVersion" -ForegroundColor Green
} else {
    Write-Host "Python installation verification failed. Please restart your terminal and run the script again." -ForegroundColor Red
    exit 1
}

# Clean up Python installer
Remove-Item -Path $pythonInstaller -Force

# Install VS Code Python Extension
Write-Host "`nInstalling VS Code Python Extension..." -ForegroundColor Yellow
$vscodePath = "C:\Program Files\Microsoft VS Code\Code.exe"
if (Test-Path $vscodePath) {
    & $vscodePath --install-extension ms-python.python
    Write-Host "VS Code Python extension installed!" -ForegroundColor Green
} else {
    Write-Host "VS Code not found. Please install VS Code first." -ForegroundColor Red
}

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
$readmeContent += "### 1. Python Installation`n"
$readmeContent += "Python 3.13.5 has been automatically installed with 'Add to PATH' option.`n`n"
$readmeContent += "### 2. VS Code Extension`n"
$readmeContent += "VS Code Python extension (ms-python.python) has been automatically installed.`n`n"
$readmeContent += "### 3. Create Virtual Environment`n"
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
Write-Host "`n1. Navigate to: $InstallPath" -ForegroundColor White
Write-Host "`n2. Read the README.md file for setup instructions" -ForegroundColor White
Write-Host "`n3. Configure your ZVM connection details" -ForegroundColor White
Write-Host "`n4. Start with the Hands-On Labs exercises" -ForegroundColor White
Write-Host "`nInstallation completed successfully!" -ForegroundColor Green

# Open VS Code with the installation directory
Start-Process "C:\Program Files\Microsoft VS Code\Code.exe" -ArgumentList "C:\zerto-labs"
