---
title: Enabling Rule Groups
description: This example enables Windows Firewall rule groups using the Windows Firewall with Advanced Security APIs.VB This VBScript file includes sample code that enables Windows Firewall  rule groups using the Microsoft Windows Firewall APIs.
ms.assetid: a3f1b8f6-5cf3-499d-a530-7fbbbd077c74
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Enabling Rule Groups

This example enables Windows Firewall rule groups using the Windows Firewall with Advanced Security APIs.


```VB
'  This VBScript file includes sample code that enables Windows Firewall
'  rule groups using the Microsoft Windows Firewall APIs.


option explicit

Dim CurrentProfiles

' Create the FwPolicy2 object.
Dim fwPolicy2
Set fwPolicy2 = CreateObject("HNetCfg.FwPolicy2")

' Get the Rules object
Dim RulesObject
Set RulesObject = fwPolicy2.Rules

CurrentProfiles = fwPolicy2.CurrentProfileTypes
fwPolicy2.EnableRuleGroup CurrentProfiles, "File and Printer Sharing", TRUE
```



 

 




