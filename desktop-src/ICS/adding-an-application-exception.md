---
title: Adding an Application Rule
description: This example adds an application rule using the Windows Firewall with Advanced Security APIs.
ms.assetid: fff54b6a-dbb2-4ab3-898a-59532e209aa9
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Adding an Application Rule

This example adds an application rule using the Windows Firewall with Advanced Security APIs.


```VB
'    This VBScript file includes sample code that adds an  
'    application rule using the Microsoft Windows Firewall APIs.

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
    
NewRule.Name = "My Application Name"
NewRule.Description = "Allow my application network traffic"
NewRule.Applicationname = "%systemDrive%\Program Files\MyApplication.exe"
NewRule.Protocol = NET_FW_IP_PROTOCOL_TCP
NewRule.LocalPorts = 4000
NewRule.Enabled = TRUE
NewRule.Grouping = "@firewallapi.dll,-23255"
NewRule.Profiles = CurrentProfiles
NewRule.Action = NET_FW_ACTION_ALLOW
    
'Add a new rule
RulesObject.Add NewRule
```



 

 




