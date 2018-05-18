---
title: Configure FSRM Debugging
description: This PowerShell script, FSRMDebug.ps1, can be used to configure FSRM debugging.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '912c55b6-746b-4af8-85c8-d28163d38f8d'
ms.prod: 'windows-server-dev'
ms.technology: 'file-server-resource-manager'
ms.tgt_platform: multiple
---

# Configure FSRM Debugging

This PowerShell script, FSRMDebug.ps1, can be used to configure FSRM debugging.


```PowerShell
<#
.SYNOPSIS
Configures FSRM module debugging.

.DESCRIPTION
This script creates the registry entries required to enable FSRM module debugging for the specified module.
Module is identified by name and can be either a storage or a classification module.

.PARAMETER moduleName
Specifies the name of the module to debug.

.PARAMETER clear
The script clears all module debug settings.

.PARAMETER debugCommand
Specifies the command used to start the debugger process. The command string must contain the string literal '[pid]' 
(in lowercase), which is replaced by the process ID of the process that hosts the module being debugged. The debugger 
used must thus support attaching to a process by process ID upon startup. 
Environment variables can be used in the command. They are resolved in the context of the user that is logged on when 
the debugger process starts.

.PARAMETER breakPoints
Specifies one or more breakpoints to enable. Valid breakpoint are:

    LoadProperties
    SaveProperties
    UseRulesAndDefinitions
    OnBeginFile
    OnEndFile
    DoesPropertyValueApply 
    GetPropertyValueToApply

Breakoint names are not case-sensitive. If not specified, all above breakpoints will be enabled.

.EXAMPLE
FSRMDebug.ps1 'My Classifier'

This command enables debugging for the module named 'My Classifier' using windbg.exe as debugger and enables
all breakpoints.

.EXAMPLE
FSRMDebug.ps1 'My Classifier' -debugCommand 'vsjitdebugger.exe -p [pid]' -breakPoints UseRulesAndDefinitions,OnBeginFile

This command enables debugging for the module named 'My Classifier' using Visual Studio debugger and enables
two breakpoints: UseRulesAndDefinitions and OnBeginFile.

.EXAMPLE
FSRMDebug.ps1 -clear

This command clears all module debug settings.

.INPUTS

None

.OUTPUTS

None

#>


param(
    [Parameter(Mandatory=$true, Position=0, ParameterSetName="set")]
    [string] $moduleName,

    [Parameter(ParameterSetName="set")]
    [string] $debugCommand = 'windbg.exe -p [pid] -g -G -QY -QSY',

    [Parameter(ParameterSetName="set")]
    [string[]] $breakPoints,

    [Parameter(Mandatory=$true, ParameterSetName="clear")]
    [switch] $clear
    )

$key = 'HKLM\System\CurrentControlSet\Services\SrmSvc\Settings\ModuleDebug'

if($clear)
{
    $dummy = reg delete $key /f
}
else
{
    $definedBps = @(
        'LoadProperties', 
        'SaveProperties', 
        'UseRulesAndDefinitions', 
        'OnBeginFile', 
        'OnEndFile', 
        'DoesPropertyValueApply', 
        'GetPropertyValueToApply'
        )

    $comparer = [Collections.CaseInsensitiveComparer]::DefaultInvariant
    [Array]::Sort($definedBps, $comparer)

    if($breakPoints.Length -eq 0)
    {
        $breakPoints = $definedBps
    }

    if($debugCommand.IndexOf('[pid]', [StringComparison]::InvariantCulture) -lt 0)
    {
        throw New-Object ArgumentException('Command does not contain "[pid]"')
    }

    $dummy = reg add $key /v Command /t REG_EXPAND_SZ /d $debugCommand /f
    $dummy = reg add $key /v ModuleName /t REG_SZ /d $moduleName /f

    foreach($bp in $breakPoints)
    {
        if([Array]::BinarySearch($definedBps, $bp, $comparer) -lt 0)
        {
            throw New-Object ArgumentException 'Invalid breakpoint name'
        }

        $dummy = reg add $key /v $bp /t REG_DWORD /d 1 /f
    }
}
```



 

 




