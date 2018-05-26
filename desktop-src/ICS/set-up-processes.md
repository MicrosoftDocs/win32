---
title: Set-up Processes
description: You should add the firewall rules during component installation by using the Windows Firewall public COM APIs.
ms.assetid: cd18bf2e-3027-45ba-ba65-5055a6a446c5
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Set-up Processes

You should add the firewall rules during component installation by using the Windows Firewall public COM APIs. This is done by means of the [**INetFwPolicy2**](/windows/previous-versions/Netfw/nn-netfw-inetfwpolicy2?branch=master) interface by creating a firewall rule and calling [**INetFwRules::Add**](/windows/previous-versions/Netfw/nf-netfw-inetfwrules-add?branch=master). Any firewall rule groups that you need to enable should also be done at this time by using [**INetFwPolicy2::EnableRuleGroup**](/windows/previous-versions/Netfw/nf-netfw-inetfwpolicy2-enablerulegroup?branch=master).

In addition, Windows services should also create Windows Service Hardening (WSH) network rules at this time using the WSH COM APIs. This is done by means of the [**INetFWServiceRestriction**](/windows/previous-versions/Netfw/nn-netfw-inetfwservicerestriction?branch=master) interface by calling the [**INetFWServiceRestriction::RestrictService**](/windows/previous-versions/Netfw/nf-netfw-inetfwservicerestriction-restrictservice?branch=master) method. Note that there may be a small time lag before the newly-added rule is applied.

## Creating rules for applications

A VBscript file which includes sample code for adding an application rule using the Windows Firewall with Advanced Security APIs can be found in the topic [Adding an Application Rule](adding-an-application-exception.md).

## Creating rules for a driver/code running in the system process

This VBScript file includes sample code for adding an Application rule using the Microsoft Windows Firewall APIs.


```VB
'--********************************************************************/
'  This VBScript file includes sample code for adding an Application
'  rule using the Microsoft Windows Firewall APIs.
'--********************************************************************/

option explicit

Dim CurrentProfile

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

CurrentProfile = fwPolicy2.CurrentProfileTypes

'Create a Rule Object.
Dim NewRule
Set NewRule = CreateObject("HNetCfg.FWRule")

NewRule.Name = "Name of the Feature> - <SubFeature> (<Protocol>-<Dir>-<Counter>)"
NewRule.Description = "<Dir>bound rule for <Name of the Feature> to allow ... [<UDP/TCP> <Port>]"
NewRule.Applicationname = "System"
NewRule.Protocol = NET_FW_IP_PROTOCOL_TCP
NewRule.LocalPorts = 12345
NewRule.Enabled = TRUE
NewRule.Grouping = "@firewallapi.dll,-23255"
NewRule.Profiles = CurrentProfile
NewRule.Action = NET_FW_ACTION_ALLOW

'Add a new rule
RulesObject.Add NewRule 
```



## Creating firewall rules for Windows services

A VBscript file which includes sample code for adding a service rule using the Windows Firewall with Advanced Security APIs can be found in the topic [Adding a Service Rule](adding-a-service-exception.md).

## Restricting a service using Windows Service Hardening

A VBscript file which includes sample code for restricting a service using the Windows Firewall with Advanced Security APIs can be found in the topic [Restricting Service](restricting-service.md).

## Creating Windows Service Hardening firewall rules

In addition to creating firewall rules for your services, you need to create similar WSH rules. WSH rules are enforced even when Windows Firewall is off and provide an additional layer of protection for servcies.

To create WSH firewall rules:

1.  Retrieve the Service Restriction object and add Block-All inbound and Block-All outbound WSH rules.
2.  Add specific firewall rules targeting the WSH store. An example of code to do this is shown below.

This VBScript file includes sample code for creating WSH rules using the Microsoft Windows Firewall APIs.


```VB
'  This VBScript file includes sample code for creating WSH
'  rules using the Microsoft Windows Firewall APIs.


option explicit


' IP Protocols
const NET_FW_IP_PROTOCOL_TCP = 6
const NET_FW_IP_PROTOCOL_UDP = 17

' Action
const NET_FW_ACTION_BLOCK = 0
const NET_FW_ACTION_ALLOW = 1

' Direction
const NET_FW_RULE_DIR_IN = 1
const NET_FW_RULE_DIR_OUT = 2

' Create the FwPolicy2 object.
Dim fwPolicy2
Set fwPolicy2 = CreateObject("HNetCfg.FwPolicy2")

' Get the Service Restriction object for the local firewall policy
Dim ServiceRestriction
Set ServiceRestriction = fwPolicy2.ServiceRestriction

' Put in block-all inbound and block-all outbound WSH networking rules for the service
ServiceRestriction.RestrictService "TermService", "%systemDrive%\WINDOWS\system32\svchost.exe", TRUE, FALSE

'If the service requires sending/receiving certain type of traffic, then add "allow" WSH rules as follows

' Get the collection of WSH networking rules
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
NewInboundRule.Direction =  NET_FW_RULE_DIR_IN
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
NewOutboundRule.Direction =  NET_FW_RULE_DIR_OUT
NewOutboundRule.Enabled = true

wshRules.Add NewOutboundRule
```



## Uninstall

Any firewall rules that were added during component installation should be removed via the [**INetFwPolicy2**](/windows/previous-versions/Netfw/nn-netfw-inetfwpolicy2?branch=master) interface by creating a firewall rule and calling [**INetFwRules::Remove()**](/windows/previous-versions/Netfw/nf-netfw-inetfwrules-remove?branch=master). During uninstall the state of other firewall rule groups should not be modified or disabled.

This VBScript file includes sample code for adding an Application rule using the Microsoft Windows Firewall APIs and then removing it.


```VB
'--********************************************************************/
'  This VBScript file includes sample code for adding an Application
'  rule using the Microsoft Windows Firewall APIs and then removing it.
'--********************************************************************/

option explicit

Dim CurrentProfile

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

CurrentProfile = fwPolicy2.CurrentProfileTypes

'Create a Rule Object.
Dim NewRule
Set NewRule = CreateObject("HNetCfg.FWRule")

NewRule.Name = "<Name of the Feature> - <SubFeature> (<Protocol>-<Dir>-<Counter>)"

'Remove the rule added
RulesObject.Remove NewRule.Name
```



## Rollback

In the event that the component installation has failed, the firewall rules that were added should be rolled back by uninstalling them.

## Servicing

Servicing should be performed by removing rules that are no longer required by the new version of the feature and by adding new rules that are now required. Any existing rules that need to be modified should have their parameters modified with the [**INetFwRule**](/windows/previous-versions/Netfw/nn-netfw-inetfwrule?branch=master) APIs. The enabled and disabled state of existing rules should not be modified.

 

 




