$CurrentPath = Split-Path $MyInvocation.MyCommand.Path -Parent

# Retrieve the configured paths for PowerShell Modules, and select the 1st entry.
# The first entry is typically a path specific to the user's profile e.g. C:\users\windowsuser\Documents\WindowsPowershell\Modules\
$ModulePath = ($Env:PSModulePath -split ";")[0]

# Copy the Module to the Module Path
Copy-Item -Path "$CurrentPath\{{ module_name }}" -Destination $ModulePath -Recurse -Force -ErrorAction SilentlyContinue