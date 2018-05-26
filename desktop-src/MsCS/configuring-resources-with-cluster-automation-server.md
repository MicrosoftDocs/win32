---
title: Configuring Resources With the Failover Cluster Automation Server
description: The following example creates resources of different types, satisfying required private properties and required dependencies as necessary. The example consists of two separate files, CreateResource.vbs and CreateResource.wsf.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 91780f2d-6a7a-4c65-a8ff-7d0c507a185f
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Configuring Resources With the Failover Cluster Automation Server

\[The [Failover Cluster Automation Server](https://msdn.microsoft.com/library/aa372940) is available for use in Windows Server 2008. It may be altered or unavailable in subsequent versions.\]

The following example creates resources of different types, satisfying required private properties and required dependencies as necessary. The example consists of two separate files, CreateResource.vbs and CreateResource.wsf.


```VB
'---------------------------------------------------------------------
' CreateResource.vbs
' Global data and functions supporting CreateResource.wsf.
'---------------------------------------------------------------------
Option Explicit

' In CreateResource.wsf, each resource type assigns appropriate 
' values to these global variables. The CreateResource function 
' uses these values to parse the command-line arguments and assign 
' values to the required private properties for a given resource type.
Public strResType, strSyntax
Public intBasicArgs, intMinArgs, intMaxArgs, intReqDeps
Public varPropNames, varPropValues, varReqDeps

Public Function CreateResource()
    Dim objGroup, objNewRes, objResource, objProperties, objReqDeps, objCluster, objArgs
    Dim strClusterName, strGroupName, strResName
    Dim intCounter
    Set objArgs = WScript.Arguments
    If objArgs.Count < intMinArgs Or objArgs.Count > intMaxArgs Then 
        Wscript.Echo strSyntax
        WScript.Quit
    End If
    strClusterName = objArgs(0)
    strGroupName = objArgs(1)
    strResName = objArgs(2)    

'   Load property values for required private properties
'   into an array.  The size of the array and the
'   expected arguments are defined by the calling script.
    For intCounter = 0 To objArgs.Count - intBasicArgs - 1
    If IsNumeric( objArgs( intCounter + intBasicArgs )) Then
            varPropValues(intCounter) = CLng(objArgs(intCounter + intBasicArgs))
    Else
            varPropValues(intCounter) = objArgs(intCounter + intBasicArgs)
        End If
    Next

    Set objCluster = CreateObject("MSCluster.Cluster")
    objCluster.Open strClusterName
    Set objGroup = objCluster.ResourceGroups.Item(strGroupName)
    Set objNewRes = objGroup.Resources.CreateItem(strResName, strResType, 0)
    Set objReqDeps = objNewRes.Dependencies

'   Look for resources already in the group that will satisfy the
'   required dependencies specified in CreateResource.wsf.  
'   If a resource of the required type does not exist it
'   will have to be created and added as a dependency by some
'   other means. 
    For intCounter = 0 To intReqDeps - 1
        For Each objResource In objGroup.Resources
            If objResource.Type.Name = varReqDeps(intCounter) Then
                objNewRes.Dependencies.AddItem objResource
                Exit For
            End If
        Next
    Next
    Set objProperties = objNewRes.PrivateProperties
    For intCounter = 0 To intMaxArgs - intBasicArgs - 1
        objProperties.Item(varPropNames(intCounter)).Value = varPropValues(intCounter)
    Next
    objProperties.SaveChanges
    Set objGroup = Nothing
    Set objNewRes = Nothing
    Set objProperties = Nothing
    Set objReqDeps = Nothing
    Set objCluster = Nothing
End Function
```



``` syntax
<?xml version="1.0" encoding="US-ASCII"?>
<!--==================================================================
;  CreateResource.wsf  (requires CreateResource.vbs to run!)
;
;  Creates resources of different types.  To create a resource of
;  a given type, use the resource type name as a job ID.  Each
;  resource type will have a different syntax depending
;  on its required private properties.
;
;  Basic syntax:
;     cscript //job:[object type] CreateResource.wsf cluster group resource prop1, prop2, ... , propN
;
;  Refer to the syntax string in each job for specific commands.
===================================================================-->
<package>
  <job id="File Share">
    <!-- The following line references the MSCLUS type library. -->
    <reference guid="{F2E606E0-2631-11D1-89F1-00A0C90D061E}" version="1.0"/>
    <script language="VBScript" src="createresource.vbs"/>
    <script language="VBScript">
      <![CDATA[
        Option Explicit
        strResType = "File Share"
        strSyntax = "cscript //job:" & Chr(39) & strResType & Chr(39) & _
                    " CreateResource.wsf cluster group resource " & _
                    "Path Sharename <Remarks> <ShareSubDirs>"
        intBasicArgs = 3
        intMinArgs = 5
        intMaxArgs = 7
        varPropNames = Array( "Path", "ShareName", "Remark", "ShareSubDirs" )
        varPropValues = Array( "", "", "", 1 )
        intReqDeps = 3
        varReqDeps = Array( "Physical Disk", "IP Address", "Network Name" )
        CreateResource
      ]]>
    </script>
  </job>
  <job id="Generic Application">
    <!-- The following line references the MSCLUS type library. -->
    <reference guid="{F2E606E0-2631-11D1-89F1-00A0C90D061E}" version="1.0"/>
    <script language="VBScript" src="createresource.vbs"/>
    <script language="VBScript">
      <![CDATA[
        Option Explicit
        strResType = "Generic Application"
        strSyntax = "cscript //job:" & Chr(39) & strResType & Chr(39) & _
                    " CreateResource.wsf cluster group resource " & _
                    "CommandLine CurrentDirectory <InteractWithDesktop> <UseNetworkName>"
        intBasicArgs = 3
        intMinArgs = 5
        intMaxArgs = 7
        varPropNames = Array( "CommandLine", "CurrentDirectory", "InteractWithDesktop", "UseNetworkName" ) 
        varPropValues = Array( "", "", 1, 0 )
        intReqDeps = 1
        varReqDeps = Array( "Network Name" )
        CreateResource
      ]]>
    </script>
  </job>
  <job id="Generic Service">
    <!-- The following line references the MSCLUS type library. -->
    <reference guid="{F2E606E0-2631-11D1-89F1-00A0C90D061E}" version="1.0"/>
    <script language="VBScript" src="createresource.vbs"/>
    <script language="VBScript">
      <![CDATA[
        Option Explicit
        strResType = "Generic Service"
        strSyntax = "cscript //job:" & Chr(39) & strResType & Chr(39) & _
                    " CreateResource.wsf cluster group resource " & _
                    "ServiceName <StartupParameters> <UseNetworkName>"
        intBasicArgs = 3
        intMinArgs = 4
        intMaxArgs = 6
        varPropNames = Array( "ServiceName", "StartupParameters", "UseNetworkName" ) 
        varPropValues = Array( "", "", 0 )
        intReqDeps = 1
        varReqDeps = Array( "Network Name" )
        CreateResource
      ]]>
    </script>
  </job>
  <job id="IP Address">
    <!-- The following line references the MSCLUS type library. -->
    <reference guid="{F2E606E0-2631-11D1-89F1-00A0C90D061E}" version="1.0"/>
    <script language="VBScript" src="createresource.vbs"/>
    <script language="VBScript">
      <![CDATA[
        Option Explicit
        strResType = "IP Address"
        strSyntax = "cscript //job:" & Chr(39) & strResType & Chr(39) & _
                    " CreateResource.wsf cluster group resource " & _
                    "Address SubnetMask Network <EnableNetBIOS>"
        intBasicArgs = 3
        intMinArgs = 6
        intMaxArgs = 7
        varPropNames = Array( "Address", "SubnetMask", "Network", "EnableNetBIOS" )
        varPropValues = Array( "", "", "", 1 )
        intReqDeps = 0
        varReqDeps = 0
        CreateResource 
      ]]>
    </script>
  </job>
  <job id="Network Name">
    <!-- The following line references the MSCLUS type library. -->
    <reference guid="{F2E606E0-2631-11D1-89F1-00A0C90D061E}" version="1.0"/>
    <script language="VBScript" src="createresource.vbs"/>
    <script language="VBScript">
      <![CDATA[
        Option Explicit
        strResType = "Network Name"
        strSyntax = "cscript //job:" & Chr(39) & strResType & Chr(39) & _
                    " CreateResource.wsf cluster group resource " & _
                    "Name <RemapPipeNames>"
        intBasicArgs = 3
        intMinArgs = 4
        intMaxArgs = 5
        varPropNames = Array( "Name", "RemapPipeNames" ) 
        varPropValues = Array( "", 0 )
        intReqDeps = 1
        varReqDeps = Array( "IP Address" )
        CreateResource
      ]]>
    </script>
  </job>
  <job id="Physical Disk">
    <!-- The following line references the MSCLUS type library. -->
    <reference guid="{F2E606E0-2631-11D1-89F1-00A0C90D061E}" version="1.0"/>
    <script language="VBScript" src="createresource.vbs"/>
    <script language="VBScript">
      <![CDATA[
        Option Explicit
        strResType = "Physical Disk"
        strSyntax = "cscript //job:" & Chr(39) & strResType & Chr(39) & _
                    " CreateResource.wsf cluster group resource " & _
                    "Signature(in decimal) <SkipChkdsk> <ConditionalMount>"
        intBasicArgs = 3
        intMinArgs = 4
        intMaxArgs = 6
        varPropNames = Array( "Signature", "SkipChkdsk", "ConditionalMount" ) 
        varPropValues = Array( -1, 0, 1 )
        intReqDeps = 0
        varReqDeps = 0
        CreateResource
      ]]>
    </script>
  </job>
  <job id="Print Spooler">
    <!-- The following line references the MSCLUS type library. -->
    <reference guid="{F2E606E0-2631-11D1-89F1-00A0C90D061E}" version="1.0"/>
    <script language="VBScript" src="createresource.vbs"/>
    <script language="VBScript">
      <![CDATA[
        Option Explicit
        strResType = "Print Spooler"
        strSyntax = "cscript //job:" & Chr(39) & strResType & Chr(39) & _
                    " CreateResource.wsf cluster group resource " & _
                    "Path <Timeout>"
        intBasicArgs = 3
        intMinArgs = 4
        intMaxArgs = 5
        varPropNames = Array( "DefaultSpoolDirectory", "JobCompletionTimeout" )
        varPropValues = Array( "", 160000 )
        intReqDeps = 2
        varReqDeps = Array( "Physical Disk", "Network Name" )
        CreateResource
      ]]>
    </script>
  </job>
</package>
```

 

 




