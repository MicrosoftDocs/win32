---
title: Adding an Outbound Rule
description: This example adds an outbound rule using the Windows Firewall with Advanced Security APIs.VB' This VBScript file includes sample code that adds an ' outbound rule using the Microsoft Windows Firewall APIs.
ms.assetid: 38b0f4d3-4a06-4c5a-99d6-ec0135826f92
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Adding an Outbound Rule

This example adds an outbound rule using the Windows Firewall with Advanced Security APIs.


```VB
'  This VBScript file includes sample code that adds an  
'  outbound rule using the Microsoft Windows Firewall APIs.


option explicit

Dim CurrentProfiles

' Protocol
Const NET_FW_IP_PROTOCOL_TCP = 6
Const NET_FW_IP_PROTOCOL_UDP = 17

'Direction
Const NET_FW_RULE_DIR_IN = 1
Const NET_FW_RULE_DIR_OUT = 2

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
    
NewRule.Name = "Outbound_Rule"
NewRule.Description = "Allow outbound network traffic from my Application over TCP port 4000"
NewRule.Applicationname = "%systemDrive%\Program Files\MyApplication.exe"
NewRule.Protocol = NET_FW_IP_PROTOCOL_TCP
NewRule.LocalPorts = 4000
NewRule.Direction = NET_FW_RULE_DIR_OUT
NewRule.Enabled = TRUE  
NewRule.Grouping = "@firewallapi.dll,-23255"
NewRule.Profiles = CurrentProfiles
NewRule.Action = NET_FW_ACTION_ALLOW
        
'Add a new rule
RulesObject.Add NewRule

```



 

 




