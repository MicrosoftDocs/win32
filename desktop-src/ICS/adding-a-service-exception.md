---
title: Adding a Service Rule
description: This example adds a service rule in the local public store using the Windows Firewall with Advanced Security APIs.VB' This VBScript file includes sample code that adds a service rule ' in the local public store using the Microsoft Windows Firewall APIs.
ms.assetid: dc6ffdd3-b583-4d19-a261-847d3b8f72c7
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Adding a Service Rule

This example adds a service rule in the local public store using the Windows Firewall with Advanced Security APIs.


```VB
'  This VBScript file includes sample code that adds a service rule
'  in the local public store using the Microsoft Windows Firewall APIs.


option explicit

Dim CurrentProfiles

' Protocol
Const NET_FW_IP_PROTOCOL_TCP = 6
Const NET_FW_IP_PROTOCOL_UDP = 17

'Action
Const NET_FW_ACTION_ALLOW = 1

' Create the FwPolicy2 object.
Dim fwPolicy2
Set fwPolicy2 = CreateObject("HNetCfg.FwPolicy2")

' Get the Rules object
Dim RulesObject
Set RulesObject = fwPolicy2.Rules

CurrentProfiles = fwPolicy2.CurrentProfileTypes

'Create a Rule Object.
Dim NewRule
Set NewRule = CreateObject("HNetCfg.FWRule")
    
NewRule.Name = "Service_Rule"
NewRule.Description = "Allow incoming network traffic to myservice"
NewRule.Applicationname = "%SystemDrive%\Windows\system32\myservice.exe"
NewRule.Servicename = "myservicename"
NewRule.Protocol = NET_FW_IP_PROTOCOL_TCP
NewRule.LocalPorts = 135
NewRule.Grouping = "@firewallapi.dll,-23255"
NewRule.Profiles = CurrentProfiles
NewRule.Enabled = TRUE
NewRule.Action = NET_FW_ACTION_ALLOW
      
'Add a new rule
RulesObject.Add NewRule
```



 

 




