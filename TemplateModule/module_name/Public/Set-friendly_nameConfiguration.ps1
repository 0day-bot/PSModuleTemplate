function Set-{{ friendly_name }}Configuration {
    <#
    .SYNOPSIS
        Sets the template module configuration values 
    
    .DESCRIPTION
        
    
    .PARAMETER URI
        
    .PARAMETER ApiToken
        
   
        
    #>
    [CmdletBinding()]
    Param(
		[Parameter(Mandatory=$False)]
		[String]
        $Username,

		[Parameter(Mandatory=$False)]
		[String]
        $Token
    )
    # Log the command executed by the user
    $InitializationLog = $MyInvocation.MyCommand.Name
    $MyInvocation.BoundParameters.GetEnumerator() | ForEach-Object { $InitializationLog = $InitializationLog + " -$($_.Key) $($_.Value)"}
    Write-Log -Message $InitializationLog -Level Verbose

   

   
    $Configuration = Read-{{ friendly_name }}Configuration -Path $Script:{{ module_name }}.ConfPath

    if (-not $Configuration) {
        $Configuration = [PSCustomObject]@{}
    }

    if ($Username) {
        if (-not $Configuration.Username) {
            Add-Member -InputObject $Configuration -MemberType NoteProperty -Name Username -Value $Username
        } else {
            $Configuration.Username = $Username
        }
    }

    if ($Token) {
        if (-not $Configuration.Token) {
            Add-Member -InputObject $Configuration -MemberType NoteProperty -Name Token -Value $Token
        } else {
            $Configuration.Token = $Token
        }
    }
        
    Save-{{ friendly_name }}Configuration -Path $Script:{{ module_name }}.ConfPath -InputObject $Configuration
}
