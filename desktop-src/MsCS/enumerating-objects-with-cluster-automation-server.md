---
title: Enumerating Objects with the Failover Cluster Automation Server
description: The following example demonstrates a simple use of the job tag to separate functionality in a Windows Script Host script. The example consists of two separate files, MyClusterScriptLibrary.vbs and ClusEnum.wsf.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b68a2c6c-095d-4cad-bf68-9cf9b773dfaa
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Failover Cluster Automation Server Failover Cluster ,enumerating objects
- Cluster Automation Server Failover Cluster ,enumerating objects
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Enumerating Objects with the Failover Cluster Automation Server

\[The [Failover Cluster Automation Server](https://msdn.microsoft.com/library/aa372940) is available for use in Windows Server 2008. It may be altered or unavailable in subsequent versions.\]

The following example demonstrates a simple use of the &lt;job&gt; tag to separate functionality in a Windows Script Host script. The example consists of two separate files, MyClusterScriptLibrary.vbs and ClusEnum.wsf.


```VB
'''''''''''''''''''''''''''''''
'
'  MyClusterScriptLibrary.vbs
'
'  Contains global data and common functions.
'
'''''''''''''''''''''''''''''''
Option Explicit
Public objArgs, objCluster

Public Function Connect()
'
' Opens a global cluster object. Using Windows Script Host syntax,
' the cluster name or "" must be passed as the first argument.
'
        Set objArgs = WScript.Arguments
        Set objCluster = CreateObject("MSCluster.Cluster")
        objCluster.Open objArgs(0)
End Function

Public Function Disconnect()
'
' Dereferences global objects.  Used with Connect.
'
        Set objCluster = Nothing
        Set objArgs = Nothing
End Function

Public Function GetEnumString(objCollection, strDelimiter)
'
'  Returns a delimited string of names from a collection.
'  Objects in the collection must support the Name property.
'
        Dim objEnum
        For Each objEnum in objCollection
          GetEnumString = GetEnumString & objEnum.Name & strDelimiter
        Next
        Set objEnum = Nothing
End Function
```



``` syntax
<?xml version="1.0" encoding="US-ASCII"?>
<!--==================================================================
;  clusenum.wsf  (requires MyClusterScriptLibrary.vbs to run!)
;
;  Enumerates cluster objects.  Each type of object is contained
;  within a job identified by the object type.  Usage syntax:
;
;     cscript //job:[object type] clusenum.wsf [cluster name]
;
;  Use "" for the cluster name to specify the local cluster.
;
;  Legal object types:   group
;                        network
;                        network interface
;                        node
;                        resource
;                        resource type
;
;  Example:  to enumerate the groups in the local cluster, enter
;
;           cscript //job:"groups" clusenum.wsf ""
;
===================================================================-->
<package id="clusenum">
 <job id="groups">
  <!-- The following line references the MSCLUS type library. -->
  <reference guid="{F2E606E0-2631-11D1-89F1-00A0C90D061E}" version="1.0"/>
  <script language="VBScript" src="MyClusterScriptLibrary.vbs"/>
  <script language="VBScript">
   <![CDATA[
    Option Explicit
    Connect
    WScript.Echo GetEnumString(objCluster.ResourceGroups, vbCrLf)
    Disconnect
   ]]>
  </script>
 </job>
 <job id="networks">
  <!-- The following line references the MSCLUS type library. -->
  <reference guid="{F2E606E0-2631-11D1-89F1-00A0C90D061E}" version="1.0"/>
  <script language="VBScript" src="MyClusterScriptLibrary.vbs"/>
  <script language="VBScript">
   <![CDATA[
    Option Explicit
    Connect
    WScript.Echo GetEnumString(objCluster.Networks, vbCrLf)
    Disconnect
   ]]>
  </script>
 </job>
 <job id="network interfaces">
  <!-- The following line references the MSCLUS type library. -->
  <reference guid="{F2E606E0-2631-11D1-89F1-00A0C90D061E}" version="1.0"/>
  <script language="VBScript" src="MyClusterScriptLibrary.vbs"/>
  <script language="VBScript">
   <![CDATA[
    Option Explicit
    Connect
    WScript.Echo GetEnumString(objCluster.NetInterfaces, vbCrLf)
    Disconnect
   ]]>
  </script>
 </job>
 <job id="nodes">
  <!-- The following line references the MSCLUS type library. -->
  <reference guid="{F2E606E0-2631-11D1-89F1-00A0C90D061E}" version="1.0"/>
  <script language="VBScript" src="MyClusterScriptLibrary.vbs"/>
  <script language="VBScript">
   <![CDATA[
    Option Explicit
    Connect
    WScript.Echo GetEnumString(objCluster.Nodes, vbCrLf)
    Disconnect
   ]]>
  </script>
 </job>
 <job id="resources">
  <!-- The following line references the MSCLUS type library. -->
  <reference guid="{F2E606E0-2631-11D1-89F1-00A0C90D061E}" version="1.0"/>
  <script language="VBScript" src="MyClusterScriptLibrary.vbs"/>
  <script language="VBScript">
   <![CDATA[
    Option Explicit
    Connect
    WScript.Echo GetEnumString(objCluster.Resources, vbCrLf)
    Disconnect
   ]]>
  </script>
 </job>
 <job id="resource types">
  <!-- The following line references the MSCLUS type library. -->
  <reference guid="{F2E606E0-2631-11D1-89F1-00A0C90D061E}" version="1.0"/>
  <script language="VBScript" src="MyClusterScriptLibrary.vbs"/>
  <script language="VBScript">
   <![CDATA[
    Option Explicit
    Connect
    WScript.Echo GetEnumString(objCluster.ResourceTypes, vbCrLf)
    Disconnect
   ]]>
  </script>
 </job>
</package>
```

 

 




