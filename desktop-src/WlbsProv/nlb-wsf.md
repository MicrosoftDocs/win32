---
title: Nlb.wsf
description: Nlb.wsf is an XML-compliant Windows Script Host (WSH) script that can perform a number of different jobs.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 13f582e4-8024-4535-aa44-d61eb06af65b
ms.prod: windows-server-dev
ms.technology:
- network-load-balancing
- windows-management-instrumentation
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Nlb.wsf

Nlb.wsf is an XML-compliant Windows Script Host (WSH) script that can perform a number of different jobs. Configuration data is supplied by Nlb.xml, and NlbScriptLib.vbs provides a common library of functions. The script is designed to run on the command line and requires two command-line arguments in addition to a job identifier.

The command syntax is:

**cscript //job:***JobId* **nlb.wsf** *ArgList*

For *JobId* use the name of the job you want to run.

For *ArgList*, specify the following command-line arguments:

-   Your network user name.
-   Your network password.

``` syntax
<?xml version="1.0" encoding="US-ASCII"?>
<!--=================================================================
Nlb.wsf

Example script used to demonstrate the NLB provider. Must be used in
conjunction with NlbScriptLib.vbs and Nlb.xml. To extend the 
functionality of this script simply add more jobs.
=================================================================-->
<package>
 <job id="Test">
  <script language="VBScript" src="NLBScriptLib.vbs"/>
  <script language="VBScript">
   <![CDATA[
    ConnectNLB
    WScript.Echo g_objNode.Name
    DisconnectNLB
   ]]>
  </script>
 </job>
 <job id="Disable">
  <script language="VBScript" src="NLBScriptLib.vbs"/>
  <script language="VBScript">
   <![CDATA[
    ConnectNLB
    g_objNode.Disable(CLng(g_strPort))
    DisconnectNLB
   ]]>
  </script>
 </job>
 <job id="Drain">
  <script language="VBScript" src="NLBScriptLib.vbs"/>
  <script language="VBScript">
   <![CDATA[
    ConnectNLB
    g_objNode.Drain(CLng(g_strPort))
    DisconnectNLB
   ]]>
  </script>
 </job>
 <job id="DrainStop">
  <script language="VBScript" src="NLBScriptLib.vbs"/>
  <script language="VBScript">
   <![CDATA[
    ConnectNLB
    g_objNode.DrainStop
    DisconnectNLB
   ]]>
  </script>
 </job>
 <job id="Enable">
  <script language="VBScript" src="NLBScriptLib.vbs"/>
  <script language="VBScript">
   <![CDATA[
    ConnectNLB
    g_objNode.Enable(CLng(g_strPort))
    DisconnectNLB
   ]]>
  </script>
 </job>
 <job id="Resume">
  <script language="VBScript" src="NLBScriptLib.vbs"/>
  <script language="VBScript">
   <![CDATA[
    ConnectNLB
    g_objNode.Resume
    DisconnectNLB
   ]]>
  </script>
 </job>
 <job id="Start">
  <script language="VBScript" src="NLBScriptLib.vbs"/>
  <script language="VBScript">
   <![CDATA[
    ConnectNLB
    g_objNode.Start
    DisconnectNLB
   ]]>
  </script>
 </job>
 <job id="Stop">
  <script language="VBScript" src="NLBScriptLib.vbs"/>
  <script language="VBScript">
   <![CDATA[
    ConnectNLB
    g_objNode.Stop
    DisconnectNLB
   ]]>
  </script>
 </job>
 <job id="Suspend">
  <script language="VBScript" src="NLBScriptLib.vbs"/>
  <script language="VBScript">
   <![CDATA[
    ConnectNLB
    g_objNode.Suspend
    DisconnectNLB
   ]]>
  </script>
 </job>
 <job id="ShowNodeSettings">
  <script language="VBScript" src="NLBScriptLib.vbs"/>
  <script language="VBScript">
   <![CDATA[
    Dim objNodeSettings, objNodeSetting
    ConnectNLB
    Set objNodeSettings = g_objService.InstancesOf ("MicrosoftNLB_NodeSetting")
    For Each objNodeSetting in objNodeSettings
      EnumProperties objNodeSetting
    Next
    Set objNodeSetting = Nothing
    Set objNodeSettings = Nothing
    DisconnectNLB
   ]]>
  </script>
 </job>
 <job id="SetDefaults">
  <script language="VBScript" src="NLBScriptLib.vbs"/>
  <script language="VBScript">
   <![CDATA[
    Dim objNodeSettings, objNodeSetting, objPortRules, objPortRule
    ConnectNLB
    Set objNodeSettings = g_objService.InstancesOf ("MicrosoftNLB_NodeSetting")
    On Error Resume Next
    For Each objNodeSetting in objNodeSettings
      Exit For
    Next
    objNodeSetting.SetDefaults
    objNodeSetting.LoadAllSettings
    Set objNodeSetting = Nothing
    Set objNodeSettings = Nothing
    DisconnectNLB
   ]]>
  </script>
 </job>
 <job id="ShowPortRule">
  <script language="VBScript" src="NLBScriptLib.vbs"/>
  <script language="VBScript">
   <![CDATA[
    Dim objNodeSettings, objNodeSetting, objPortRule
    ConnectNLB
    Set objNodeSettings = g_objService.InstancesOf ("MicrosoftNLB_NodeSetting")
    For Each objNodeSetting in objNodeSettings
      Exit For
    Next
    objNodeSetting.GetPortRule CLng(g_strPort), objPortRule
    EnumProperties objPortRule
    Set objPortRule = Nothing
    Set objNodeSetting = Nothing
    Set objNodeSettings = Nothing
    DisconnectNLB
   ]]>
  </script>
 </job>
</package>
```

 

 




