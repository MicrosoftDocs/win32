---
title: Adding an ICMP Rule
description: This example adds an ICMP rule using the Windows Firewall with Advanced Security APIs.VB' This VBScript file includes sample code that adds an ' ICMP rule using the Microsoft Windows Firewall APIs.
ms.assetid: dfc99536-4d9b-43d9-825b-4c1752911298
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Adding an ICMP Rule

This example adds an ICMP rule using the Windows Firewall with Advanced Security APIs.


```VB
'  This VBScript file includes sample code that adds an   
'  ICMP rule using the Microsoft Windows Firewall APIs.


option explicit

Dim CurrentProfiles

Const NET_FW_IP_PROTOCOL_ICMPv4 = 1
Const NET_FW_IP_PROTOCOL_ICMPv6 = 58

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
    
NewRule.Name = "ICMP_Rule"
NewRule.Description = "Allow ICMP network traffic"    
NewRule.Protocol = NET_FW_IP_PROTOCOL_ICMPv4
NewRule.IcmpTypesAndCodes = "1:1"
NewRule.Enabled = TRUE
NewRule.Grouping = "@firewallapi.dll,-23255"
NewRule.Profiles = CurrentProfiles
NewRule.Action = NET_FW_ACTION_ALLOW
    
 'Add a new rule
RulesObject.Add NewRule
```



 

 




