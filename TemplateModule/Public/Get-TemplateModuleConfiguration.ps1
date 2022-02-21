function Get-{{ friendly_name }}Configuration {
    <#
    .SYNOPSIS
        Retrieves the current configuration values for the {{ module_name }} Module
    
    #>
    
    #Param(
     
    #)
    # Log the command executed by the user
    $InitializationLog = $MyInvocation.MyCommand.Name
    $MyInvocation.BoundParameters.GetEnumerator() | ForEach-Object { $InitializationLog = $InitializationLog + " -$($_.Key) $($_.Value)"}
    Write-Log -Message $InitializationLog -Level Verbose

    $Configuration = Read-{{ friendly_name }}Configuration -Path $Script:{{ module_name }}.ConfPath

    return $Configuration
}