---
title: Adding a LAN Rule
description: This example adds a LAN rule using the Windows Firewall with Advanced Security APIs.VB' This VBScript file includes sample code that adds a ' LAN rule using the Microsoft Windows Firewall APIs.
ms.assetid: 1a17e974-0b13-4c9c-acb0-99afa04ae86b
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Adding a LAN Rule

This example adds a LAN rule using the Windows Firewall with Advanced Security APIs.


```VB
'  This VBScript file includes sample code that adds a 
'  LAN rule using the Microsoft Windows Firewall APIs.


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
    
NewRule.Name = "Per_InterfaceType_Rule"
NewRule.Description = "Allow incoming network traffic over port 2400 coming from LAN interfcace type"
NewRule.Protocol = NET_FW_IP_PROTOCOL_TCP
NewRule.LocalPorts = 2300
NewRule.Interfacetypes = "LAN"
NewRule.Enabled = TRUE
NewRule.Grouping = "@firewallapi.dll,-23255"
NewRule.Profiles = CurrentProfiles
NewRule.Action = NET_FW_ACTION_ALLOW   
    
'Add a new rule
RulesObject.Add NewRule
```



 

 




