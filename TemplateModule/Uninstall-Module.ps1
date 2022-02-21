# Loop to check each module path in the configured module paths
ForEach ($ModulePath in ($Env:PSModulePath -split ";")){
	# Check if the module exists in the path, and remove it if it does
	if (Test-Path -Path $ModulePath\{{ module_name }}) {
		Remove-Item -Path $ModulePath\{{ module_name }} -Recurse -Force
	}
}