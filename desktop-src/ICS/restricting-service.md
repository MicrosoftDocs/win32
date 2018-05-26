---
title: Restricting Service
description: This example restricts a service using the Windows Firewall with Advanced Security APIs.VB This VBScript file includes sample code that restricts  a service using the Microsoft Windows Firewall APIs.
ms.assetid: 7454ceb9-d4ec-44d1-8245-0f2766a56501
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Restricting Service

This example restricts a service using the Windows Firewall with Advanced Security APIs.


```VB
'  This VBScript file includes sample code that restricts  
'  a service using the Microsoft Windows Firewall APIs.


option explicit

' IP protocols
const NET_FW_IP_PROTOCOL_TCP                  = 6
const NET_FW_IP_PROTOCOL_UDP                  = 17

' Action
const NET_FW_ACTION_BLOCK                     = 0
const NET_FW_ACTION_ALLOW                     = 1

' Direction
const NET_FW_RULE_DIR_IN                      = 1
const NET_FW_RULE_DIR_OUT                     = 2


' Create the FwPolicy2 object.
Dim fwPolicy2
Set fwPolicy2 = CreateObject("HNetCfg.FwPolicy2")

' Get the Service Restriction object for the local firewall policy.
Dim ServiceRestriction
Set ServiceRestriction = fwPolicy2.ServiceRestriction

' Put in block-all inbound and block-all outbound Windows Service Hardening (WSH) networking rules for the service
ServiceRestriction.RestrictService "TermService", "%systemDrive%\WINDOWS\system32\svchost.exe", TRUE, FALSE

' If the service requires sending/receiving certain type of traffic, then add "allow" WSH rules as follows

' Get the collection of Windows Service Hardening networking rules
Dim wshRules
Set wshRules = ServiceRestriction.Rules

' Add inbound WSH allow rules
Dim NewInboundRule
Set NewInboundRule = CreateObject("HNetCfg.FWRule")
NewInboundRule.Name = "Allow only TCP 3389 inbound to service"
NewInboundRule.ApplicationName = "%systemDrive%\WINDOWS\system32\svchost.exe"
NewInboundRule.ServiceName = "TermService"
NewInboundRule.Protocol = NET_FW_IP_PROTOCOL_TCP
NewInboundRule.LocalPorts = 3389

NewInboundRule.Action = NET_FW_ACTION_ALLOW
NewInboundRule.Direction = NET_FW_RULE_DIR_IN
NewInboundRule.Enabled = true

wshRules.Add NewInboundRule

' Add outbound WSH allow rules
Dim NewOutboundRule
Set NewOutboundRule = CreateObject("HNetCfg.FWRule")
NewOutboundRule.Name = "Allow outbound traffic from service only from TCP 3389"
NewOutboundRule.ApplicationName = "%systemDrive%\WINDOWS\system32\svchost.exe"
NewOutboundRule.ServiceName = "TermService"
NewOutboundRule.Protocol = NET_FW_IP_PROTOCOL_TCP
NewOutboundRule.LocalPorts = 3389

NewOutboundRule.Action = NET_FW_ACTION_ALLOW
NewOutboundRule.Direction = NET_FW_RULE_DIR_OUT
NewOutboundRule.Enabled = true

wshRules.Add NewOutboundRule


```



 

 




