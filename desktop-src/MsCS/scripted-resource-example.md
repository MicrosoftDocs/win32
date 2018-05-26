---
title: Scripted Resource Example
description: The following examples show simple control scripts.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 42d414ab-4162-4101-a029-63c817766cb0
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- scripted resource example Failover Cluster
- resources Failover Cluster , scripted example
- scripts Failover Cluster , scripted resource example
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Scripted Resource Example

The following examples show simple control scripts.



| Example                              | Purpose                                                                                         |
|--------------------------------------|-------------------------------------------------------------------------------------------------|
| Using Private Properties<br/>  | Illustrates how private properties are used.<br/>                                         |
| Revealing Node Properties<br/> | Demonstrates how to reveal node properties, in this case the node's local time zone.<br/> |



 

## VBScript Example - Using Private Properties

This example illustrates the use of private properties. When brought online (see the [**Online**](/windows/previous-versions/ResApi/nc-resapi-ponline_routine?branch=master) function), the script logs a prompt if the private properties [**ShareName**](file-shares-sharename.md) or [**SharePath**](sharepath.md) do not exist. A console operator can set values for these properties using the /priv command line switch.

This is an example of cluster log output when the private properties are set successfully:

``` syntax
00000934.00000b14::...   [API] Creating resource Generic Script <FileShareGenScript>(... ...)
... ...
00000604.00000448::... : Loaded script engine 'VBScript' successfully.
00000604.00000448::... : Script-wide code begins execution
00000604.00000448::... : Loaded script 'e:\truesample.vbs' successfully.
... ...
00000934.00000844::...   Setting value of ShareName for key Resources\... ...\Parameters to
... ...
00000934.00000844::...   Setting value of SharePath for key Resources\... ...\Parameters to
... ...
00000604.00000448::... : Unloaded script engine 'VBScript' successfully.
```

The following is the sample script.


```VB
'Script-Level Global Variables
Resource.LogInformation("Script-wide code begins execution")
Dim WshShell, oExec, oLooksAlive, oIsAlive, oWait
Set WshShell = CreateObject("WScript.Shell")
Dim fso
Set fso = CreateObject("Scripting.FileSystemObject")

Function Online( )
'   ... Create a network share...
    Resource.LogInformation "Entering Online"
'   ... Prompt console operator for a sharename if none provided...
    If Resource.Sharename = "" Then
      Resource.LogInformation "You need to set the sharename private property before attempting to go online"
'   ... No-zero return code will appear in console log...
      Online = 1
      Exit Function
    End If
'   ... Prompt console operator for a sharepath if none provided...
    If Resource.SharePath = "" Then
      Resource.LogInformation "You need to set the SharePath private property before attempting to go online"
      Online = 1
      Exit Function
    End If

    Set oExec = WshShell.Exec("net share """ & Resource.ShareName & """=""" & Resource.SharePath & """")
'   ... Allow time for operation to complete...  
    Do While oExec.Status = 0
      Set oWait = WshShell.Exec("sleep 1")
    Loop
    
    If oExec.ExitCode <> 0 Then
     Resource.LogInformation "net share """ & Resource.ShareName & """=""" & Resource.SharePath & """ command failed"
     Resource.LogInformation oExec.StdErr.ReadAll
    End If
    
    Online = oExec.ExitCode
End Function

Function Offline( )
    Resource.LogInformation "Entering Offline"
    Set oExec = WshShell.Exec("net share """ & Resource.ShareName & """ /delete")
    Do While oExec.Status = 0
      Set oWait = WshShell.Exec("sleep 1")
    Loop
    If oExec.ExitCode <> 0 Then
     Resource.LogInformation "Failed to disconnect the resource to an offline status gracefully"
     Resource.LogInformation oExec.StdErr.ReadAll
    End If
    Offline = oExec.ExitCode
End Function

Function LooksAlive( )
    Resource.LogInformation "Entering LooksAlive" 
    Set oLooksAlive = WshShell.Exec("net share """ & Resource.ShareName & """")
    Do While oLooksAlive.Status = 0
      Set oWait = WshShell.Exec("sleep 1")
    Loop
    If oLooksAlive.ExitCode <> 0 Then
     Resource.LogInformation "net share """ & Resource.ShareName & """ command is failing with"
     Resource.LogInformation oLooksAlive.StdErr.ReadAll
    End If
    LooksAlive = oLooksAlive.ExitCode
End Function

Function IsAlive( )
    Resource.LogInformation "Entering IsAlive" 
    Set oIsAlive = WshShell.Exec("net share """ & Resource.ShareName & """")
    Do While oIsAlive.Status = 0
      Set oWait = WshShell.Exec("sleep 1")
    Loop 
    If oIsAlive.ExitCode <> 0 Then
     Resource.LogInformation "net share """ & Resource.ShareName & """ command is failing with"
     Resource.LogInformation oIsAlive.StdErr.ReadAll
    End If  
    If (fso.FolderExists(Resource.SharePath) = False) Then
      Resource.LogInformation "folder " & Resource.SharePath & " no longer exists"
      IsAlive = 1
      Exit Function
    End If
    IsAlive = oIsAlive.ExitCode
End Function

Function Open( )
    If Resource.PropertyExists("ShareName") = False Then
     Resource.AddProperty("ShareName")
    End If
    If Resource.PropertyExists("SharePath") = False Then
     Resource.AddProperty("SharePath")
    End If
    Open = 0
End Function

Function Close( )
    Close = 0
End Function

Function Terminate( )
    Resource.LogInformation "Entering Terminate"
    Set oExec = WshShell.Exec("net share """ & Resource.ShareName & """ /delete")
    Do While oExec.Status = 0
      Set oWait = WshShell.Exec("sleep 1")
    Loop
    If oExec.ExitCode <> 0 Then
     Resource.LogInformation oExec.StdErr.ReadAll
    End If
    Terminate = oExec.ExitCode

End Function
```



## VBScript Example - Revealing Node Properties

This VBScript example illustrates the use of WMI to reveal a node property, in this case the node's local time zone. The code, in the [**Online**](/windows/previous-versions/ResApi/nc-resapi-ponline_routine?branch=master) function, is executed once when the script resource is brought online. The required script entry points [**LooksAlive**](/windows/previous-versions/ResApi/nc-resapi-plooks_alive_routine?branch=master) and [**IsAlive**](/windows/previous-versions/ResApi/nc-resapi-pis_alive_routine?branch=master) are empty functions in this example.

Note that the scripted resource does not reveal desktop objects, so attempts to write to the console using WMI will fail. The [**Resource**](resource-object.md) object must be used instead.

This is an example of console log output when the script executes:

``` syntax
00000604.000006dc::...   Loaded script engine 'VBScript' successfully.
00000604.000006dc::...   Loaded script 'e:\wmitime.vbs' successfully.
00000604.000006dc::...   Local Time Zone is: (GMT-08:00) Pacific Time (US & Canada): Tijuana
... ...
```

The following is the sample script.


```VB
Function Online( )
'
'   Application VBScript uses WMI to reveal the node's local time zone description
'
On Error Resume Next
'
'   For the local computer only...
'
strComputer = "."
'
'   ... query the property...
'
Set objWMIService = GetObject("winmgmts:\\" & strComputer & "\root\cimv2")
Set colItems = objWMIService.ExecQuery("Select * from Win32_TimeZone",,48)
'
'   ... and output the local time zone to the log
'
For Each objItem in colItems
Resource.LogInformation "Local Time Zone is: " & objItem.Description
Next
'   ... Return success
Online =  true
End Function
 
Function LooksAlive( )
LooksAlive = true
End Function
 
Function IsAlive( )
IsAlive = true
End Function

```



 

 





