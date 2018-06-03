---
title: Displaying and Changing DFSR Local Computer Settings
description: VBScript example shows how to use an instance of the DfsrMachineConfig class to display and change DFSR local computer settings.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2f9dea5a-105b-4f9c-b5da-fbc7520687b3
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-replication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Distributed File System Replication examples Files , displaying and changing DFSR local computer settings
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Displaying and Changing DFSR Local Computer Settings

The following VBScript example shows how to use an instance of the [**DfsrMachineConfig**](dfsrmachineconfig.md) class to display and change DFSR local computer settings.

To run the script, which is in Windows Script Host (WSH) 2.0 XML file format, save the text in a file with a .wsf extension.


```XML
<?XML version="1.0" standalone="yes" ?>

<job id="TweakMachineConfig">
 <runtime>
  <description>
   This script displays/changes DFSR local computer settings through the DFSR WMI Provider.
  </description>
  <named 
        name="Server"
        helpstring="The server to change local computer settings on"
        type="string"
        required="true"
/>
  <named
        name="DebugLogFilePath"
        helpstring="Path where debug log files will be stored"
        type="string"
        required="false"
/>
  <named
        name="MaxDebugLogFiles"
        helpstring="Maximum number of debug log files"
        type="string"
        required="false"
/>
  <named
        name="DebugLogSeverity"
        helpstring="Verbosity level of Debug log"
        type="string"
        required="false"
/>
  <named
        name="MaxDebugLogMessages"
        helpstring="Max. no. of lines per debug log file"
        type="string"
        required="false"
/>
  <named
        name="DsPollingIntervalInMin"
        helpstring="Interval in minutes for polling configuration changes from DC"
        type="string"
        required="false"
/>
  <named
        name="EnableLightDsPolling"
        helpstring="Enable/Disable lightweight polling for configuration changes from DC"
        type="boolean"
        required="false"
/>
  <named
        name="RpcPortAssignment"
        helpstring="Static RPC Server Port for DFSR"
        type="string"
        required="false"
/>
  <named
        name="StagingHighWatermarkPercent"
        helpstring="Staging High Watermark Percent"
        type="string"
        required="false"
/>
  <named
        name="StagingLowWatermarkPercent"
        helpstring="Staging Low Watermark Percent"
        type="string"
        required="false"
/>
  <named
        name="EnableDebugLog"
        helpstring="Enable/Disable Debug Log"
        type="boolean"
        required="false"
/>
  <named
        name="ConflictHighWatermarkPercent"
        helpstring="Conflict And Deleted High Watermark Percent"
        type="string"
        required="false"
/>
  <named
        name="ConflictLowWatermarkPercent"
        helpstring="Conflict And Deleted Low Watermark Percent"
        type="string"
        required="false"
/>
  <named
        name="CurrentSettings"
        helpstring="Display current local computer settings"
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
 <resource id="DfsrMachineConfig">DfsrMachineConfig</resource>
 <resource id="DfsrNamespace">\root\microsoftdfs</resource>

 <reference object="Scripting.FileSystemObject"/>
 <reference object="WbemScripting.SWbemLocator"/>

 <script language="VBScript">
  <![CDATA[
    Option Explicit
    
    Dim objWbemDateTime
    Set objWbemDateTime = CreateObject("WbemScripting.SWbemDateTime")
    
    Call Main()
    
    Function WmiDateStringToDate(dtmDate)
        objWbemDateTime.Value = dtmDate
        WmiDateStringToDate = objWbemDateTime.GetVarDate
    End Function

    Sub DisplayWmiObject(objObjectToDisplay)
        Dim objPropValue, objProperty
        Dim strObjectClassName

        strObjectClassName = objObjectToDisplay.Path_.[Class]
        WScript.Echo objObjectToDisplay.Path_.Server & " " & strObjectClassName
        WScript.Echo _
            String(Len(objObjectToDisplay.Path_.Server) + _
                   Len(strObjectClassName) + 1, _
                   "-")
        For Each objProperty In objObjectToDisplay.Properties_
            objPropValue = objProperty.Value
            If ( objProperty.CIMType = wbemCimtypeDatetime ) Then
                objPropValue = WmiDateStringToDate(objPropValue)
            End If
            WScript.Echo objProperty.Name & _
                         Space(40-Len(objProperty.Name)) & _
                         " : " & _
                         objPropValue
        Next
    End Sub
    
    Sub Main
        Dim objNamedArgs
        Dim strComputer
        Dim objWmiService, objDfsrMachineConfig
        Dim objProperty
        Dim blnObjectChanged
    
        Set objNamedArgs   = WScript.Arguments.Named
    
        ' Display help if there are any unnamed arguments in the command line
        If ( WScript.Arguments.Unnamed.Length <> 0 ) Then
            WScript.Arguments.ShowUsage()
            WScript.Quit(1)
        End If
        
        ' Display help if there are not enough arguments, help is requested or
        ' required server argument is not specified
        If ( objNamedArgs.Length < 2 Or _
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
    
        ' Get the DfsrMachineConfig singleton instance
        ' from target server
        Set objDfsrMachineConfig = _
            objWmiService.Get(getResource("DfsrMachineConfig") & "=@")
        
        ' Display current settings and quit if requested
        If ( objNamedArgs.Exists("currentsettings") ) Then
            Call DisplayWmiObject(objDfsrMachineConfig)
            WScript.Quit(0)
        End If
        
        ' Change properties as specified in command line
        blnObjectChanged = False
        For Each objProperty In objDfsrMachineConfig.Properties_
            If ( objNamedArgs.Exists(objProperty.Name) ) Then
                ' Here's where you should validate the value specified
                ' in the command line
                WScript.Echo "Setting " & _
                             objProperty.Name & _
                             " to " & _
                             objNamedArgs.Item(objProperty.Name)
                objDfsrMachineConfig.Properties_(objProperty.Name) = _
                    objNamedArgs.Item(objProperty.Name)
                blnObjectChanged = True
            End If
        Next
        
        WScript.Echo vbCrLf
        
        ' Save the changed instance to update DFSR local computer
        ' properties via WMI provider on the target server
        If ( blnObjectChanged ) Then
            Call objDfsrMachineConfig.Put_()
        End If
        
        ' Refresh the instance back from the server
        Set objDfsrMachineConfig = _
            objWmiService.Get(getResource("DfsrMachineConfig") & "=@")
    
        ' Display the new instance
        Call DisplayWmiObject(objDfsrMachineConfig)
        WScript.Quit(0)
    End Sub
  ]]>
 </script>

</job>
```



 

 




