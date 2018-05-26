---
title: Adding a Rule with Edge Traversal
description: This example adds an application rule with Edge Traversal using the Windows Firewall with Advanced Security APIs.VB This VBScript file includes sample code that adds an application  rule with Edge Traversal using the Microsoft Windows Firewall APIs.
ms.assetid: 60f27c2e-0117-496e-b3e3-d0adee194a4c
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Adding a Rule with Edge Traversal

This example adds an application rule with Edge Traversal using the Windows Firewall with Advanced Security APIs.


```VB
'  This VBScript file includes sample code that adds an application  
'  rule with Edge Traversal using the Microsoft Windows Firewall APIs.


option explicit

Dim CurrentProfiles

' Protocol
Const NET_FW_IP_PROTOCOL_TCP = 6

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
    
NewRule.Name = "My Application Name with Edge Traversal"
NewRule.Description = "Allow my application network traffic with Edge Traversal"
NewRule.Applicationname = "%systemDrive%\Program Files\MyApplication.exe"
NewRule.Protocol = NET_FW_IP_PROTOCOL_TCP
NewRule.LocalPorts = 5000
NewRule.Enabled = TRUE
NewRule.Grouping = "@firewallapi.dll,-23255"
NewRule.Profiles = CurrentProfiles
NewRule.Action = NET_FW_ACTION_ALLOW
NewRule.EdgeTraversal = TRUE
    
'Add a new rule
RulesObject.Add NewRule
```



 

 




