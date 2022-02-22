# PSModuleTemplate
Template for building and generating robust powershell modules. A powershell module generator for effiency and those new to writing PS modules to provide a jumping off point for all types of powershell use cases. 


## Installation 
```powershell
git clone https://github.com/0day-bot/PSModuleTemplate.git
cd PSModuleTemplate
pip install -r requirements.txt 
```
or simply `pip install jinja2` as that and it's dependencies are all that's needed. 

## Usage

```bash
./generateModule.py --mName WidgetCorporation --fName WC
```
The above command will generate a module named WidgetCorporation and provide a skeleton for the module with functions named using the fName (friendly name) provided. The command will overwrite file names in the TemplateModule directory so if multiple modules are needed you will need to clone the repo multiple times. 

[[/Images/resultingFoldersAfterTemplate.PNG|ALT TEXT]]

You can then navigate to the TemplateModule directory and run the `Install-Module.ps1` script provided. You can use this in conjunction with `Uninstall-Module.ps1` to make changes to the files in the directory and add your own functionality to the module. 

```powershell
Import-Module WidgetCorporation
./Uninstall-Module.ps1
# Make necessary changes
./Install-Module.ps1

# In a new powershell session
Import-Module WidgetCorporation 
```

## File Descriptions

| File                                | Description                                                                                                                                                                                                                                       |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| generateModule.py                   | Jinja2 template generator to render powershell files with variable and other key names replaced.                                                                                                                                                  |
| Install-Module.ps1                  | Load module files into the first directory listed in `$env:PSModulePath`                                                                                                                                                                          |
| Uninstall-Module.ps1                | Unload module files into the first directory listed in `$env:PSModulePath`                                                                                                                                                                        |
| module_name.psm1                    | Template `.psm1` file that will have values replaced with new module name and load Public and Private functions from those respective directories.                                                                                                |
| Get-friendly_nameConfiguration      | Function that retrieves module config from localappdata location, config can be customized to store any needed values like apikeys or passwords.                                                                                                  |
| Set-friendly_nameConfiguration      | Function that sets customizable values into json file in localappdata location, by default accepts -Username and -Token parameters, where the token value will be encrypted before being stored in config.json under `%LOCALAPPDATA%\module_name` |
| Write-Log.ps1                       | Logging function that can be used to provide more insight to functions when running them with -Verbose                                                                                                                                            |
| Save-friendly_nameConfiguration.ps1 | function that serializes config to json used by Set-friendly_nameConfiguration                                                                                                                                                                    |
| Read-friendly_nameConfiguration.ps1 | function that unserializes config from json to use in other functions                                                                                                                                                                             |
| Protect-friendly_nameToken.ps1      | takes a string value and converts it to a securestring then encrypts it before writing it to stdout, used by Set-friendly_nameConfiguration to encrypt value for -Token                                                                           |
| Unprotect-friendly_nameToken.ps1    | This function should be used in other functions that would need to unencrypt the token value from memory for usage in things like API calls or username/password logins                                                                           |


## Contributing 
Please submit a pull request with any ideas. :)