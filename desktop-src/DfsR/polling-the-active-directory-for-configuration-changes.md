---
title: Polling the Active Directory for Configuration Changes
description: VBScript example shows how to use the PollDsNow method of the DfsrConfig class to poll the Active Directory for configuration changes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: bd9eea21-f005-40af-8429-d586ae2a69f4
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-replication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Distributed File System Replication examples Files , polling Active Directory for configuration changes
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Polling the Active Directory for Configuration Changes

The following VBScript example shows how to use the [**PollDsNow**](polldsnow-dfsrconfig.md) method of the [**DfsrConfig**](dfsrconfig.md) class to poll the Active Directory for configuration changes.

To run the script, which is in Windows Script Host (WSH) 2.0 XML file format, save the text in a file with a .wsf extension.


```XML
<?XML version="1.0" standalone="yes" ?>

<job id="PollDs">
 <runtime>
  <description>
   This script uses the DFSR WMI provider to trigger AD poll for configuration changes.
  </description>
  <named 
        name="server"
        helpstring="The server to change machine configuration settings on"
        type="string"
        required="true"
/>
  <named
        name="help"
        helpstring="Display help for this script"
        type="simple"
        required="false"
/>
  <named
        name="?"
        helpstring="Display help for this script"
        type="simple"
        required="false"
/>
 </runtime>

 <resource id="DfsrConfig">DfsrConfig</resource>
 <resource id="DfsrNamespace">\root\microsoftdfs</resource>

 <resource id="ConfigError0">Success.</resource>
 <resource id="ConfigError1">Registry key is not found.</resource>
 <resource id="ConfigError2">Registry key is not accessible.</resource>
 <resource id="ConfigError3">Registry value is not found.</resource>
 <resource id="ConfigError4">Registry value is not valid.</resource>
 <resource id="ConfigError5">Generic registry error.</resource>
 <resource id="ConfigError6">MSXML.dll Not installed.</resource>
 <resource id="ConfigError7">Missing XML DOM.</resource>
 <resource id="ConfigError8">XML DOM is not valid.</resource>
 <resource id="ConfigError9">XML file not found.</resource>
 <resource id="ConfigError10">XML file not accessible</resource>
 <resource id="ConfigError11">Generic XML error.</resource>
 <resource id="ConfigError12">Cannot connect to AD.</resource>
 <resource id="ConfigError14">Generic AD error.</resource>
 <resource id="ConfigError15">Bad XML\AD parameter.</resource>
 <resource id="ConfigError16">Bad XML\AD parameter.</resource>
 <resource id="ConfigError17">File path is not valid.</resource>
 <resource id="ConfigError18">Volume not found.</resource>
 <resource id="ConfigError19">Out of memory.</resource>
 <resource id="ConfigError20">Configuration source mismatch.</resource>
 <resource id="ConfigError21">Access denied.</resource>
 <resource id="ConfigError22">Generic error.</resource>

 <reference object="Scripting.FileSystemObject"/>
 <reference object="WbemScripting.SWbemLocator"/>

 <script language="VBScript">
  <![CDATA[
    Option Explicit
    
    Call Main()
    
    Sub Main
        Dim objNamedArgs
        Dim strComputer
        Dim objWmiService, objDfsrConfig
        Dim uintPollRc
    
        Set objNamedArgs   = WScript.Arguments.Named
    
        ' Display help if there are any unnamed arguments in the command line
        If ( WScript.Arguments.Unnamed.Length <> 0 ) Then
            WScript.Arguments.ShowUsage()
            WScript.Quit(1)
        End If
        
        ' Display help if there are not enough arguments, 
        ' help is requested or
        ' required server argument is not specified
        If ( objNamedArgs.Length < 1 Or _
             objNamedArgs.Exists("help") Or _
             objNamedArgs.Exists("?") Or _
             NOT objNamedArgs.Exists("server") ) Then
            WScript.Arguments.ShowUsage()
            WScript.Quit(1)
        End If
        
        strComputer = objNamedArgs("server")
        
        ' Connect to the target server's DFSR WMI namespace
        ' \\server\root\microsoftdfs
        Set objWmiService = _
            GetObject("winmgmts:\\" & strComputer & getResource("DfsrNamespace"))
    
        ' Get the DfsrConfig singleton instance
        ' from target server
        Set objDfsrConfig = _
            objWmiService.Get(getResource("DfsrConfig") & "=@")
        
        ' Invoke the PollDsNow method on target server
        uintPollRc = objDfsrConfig.PollDsNow()
        
        If uintPollRc <> 0 Then
            WScript.Echo "DFSR AD Poll on " & strComputer & " failed"
            WScript.Echo "Error returned from DFSR Provider: " & _
                         getResource("ConfigError" & CStr(uintPollRc))
        Else
            WScript.Echo "Successfully initiated DFSR AD Poll on " & _
                         strComputer
        End If
    End Sub
   ]]>
 </script>

</job>
```



 

 




