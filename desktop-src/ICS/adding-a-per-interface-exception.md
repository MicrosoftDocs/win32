---
title: Adding a per Interface Rule
description: The following example adds a per interface rule using the Windows Firewall with Advanced Security APIs.VB This VBScript file includes sample code that adds a  per interface rule using the Microsoft Windows Firewall APIs.
ms.assetid: 433656b1-9aff-4d5c-b8bd-d7cce7e03d13
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Adding a per Interface Rule

The following example adds a per interface rule using the Windows Firewall with Advanced Security APIs.


```VB
'  This VBScript file includes sample code that adds a   
'  per interface rule using the Microsoft Windows Firewall APIs.


option explicit

Dim CurrentProfiles
Dim InterfaceArray
Dim LowerBound
Dim UpperBound
Dim iterate

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
    
InterfaceArray = Array("Local Area Connection")

LowerBound = LBound(InterfaceArray)
UpperBound = UBound(InterfaceArray)
        
NewRule.Name = "Per_Interface_Rule"
NewRule.Description = "Add a Per Interface Rule"
NewRule.Protocol = NET_FW_IP_PROTOCOL_TCP
NewRule.LocalPorts = 2300
NewRule.Enabled = TRUE
NewRule.Grouping = "@firewallapi.dll,-23255"
NewRule.Profiles = CurrentProfiles    
NewRule.Interfaces = InterfaceArray
NewRule.Action = NET_FW_ACTION_ALLOW
    
'Add a new rule
RulesObject.Add NewRule
```



 

 




