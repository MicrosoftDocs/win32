---
title: Enumerating Firewall Rules
description: This example enumerates Windows Firewall rules using the Windows Firewall with Advanced Security APIs.VB' This VBScript file includes sample code that enumerates ' Windows Firewall rules using the Microsoft Windows Firewall APIs.
ms.assetid: 503ba384-9e20-45f4-be5d-cd9a1576c097
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Enumerating Firewall Rules

This example enumerates Windows Firewall rules using the Windows Firewall with Advanced Security APIs.


```VB
'  This VBScript file includes sample code that enumerates
'  Windows Firewall rules using the Microsoft Windows Firewall APIs.


Option Explicit

Dim CurrentProfiles
Dim InterfaceArray
Dim LowerBound
Dim UpperBound
Dim iterate
Dim rule

' Profile Type
Const NET_FW_PROFILE2_DOMAIN = 1
Const NET_FW_PROFILE2_PRIVATE = 2
Const NET_FW_PROFILE2_PUBLIC = 4

' Protocol
Const NET_FW_IP_PROTOCOL_TCP = 6
Const NET_FW_IP_PROTOCOL_UDP = 17
Const NET_FW_IP_PROTOCOL_ICMPv4 = 1
Const NET_FW_IP_PROTOCOL_ICMPv6 = 58

' Direction
Const NET_FW_RULE_DIR_IN = 1
Const NET_FW_RULE_DIR_OUT = 2

' Action
Const NET_FW_ACTION_BLOCK = 0
Const NET_FW_ACTION_ALLOW = 1


' Create the FwPolicy2 object.
Dim fwPolicy2
Set fwPolicy2 = CreateObject("HNetCfg.FwPolicy2")

CurrentProfiles = fwPolicy2.CurrentProfileTypes

'// The returned 'CurrentProfiles' bitmask can have more than 1 bit set if multiple profiles 
'//   are active or current at the same time

if ( CurrentProfiles AND NET_FW_PROFILE2_DOMAIN ) then
   WScript.Echo("Domain Firewall Profile is active")
end if

if ( CurrentProfiles AND NET_FW_PROFILE2_PRIVATE ) then
   WScript.Echo("Private Firewall Profile is active")
end if

if ( CurrentProfiles AND NET_FW_PROFILE2_PUBLIC ) then
   WScript.Echo("Public Firewall Profile is active")
end if

' Get the Rules object
Dim RulesObject
Set RulesObject = fwPolicy2.Rules

' Print all the rules in currently active firewall profiles.
WScript.Echo("Rules:")

For Each rule In Rulesobject
    if rule.Profiles And CurrentProfiles then
        WScript.Echo("  Rule Name:          " & rule.Name)
        WScript.Echo("   ----------------------------------------------")
        WScript.Echo("  Description:        " & rule.Description)
        WScript.Echo("  Application Name:   " & rule.ApplicationName)
        WScript.Echo("  Service Name:       " & rule.ServiceName)
        Select Case rule.Protocol
            Case NET_FW_IP_PROTOCOL_TCP    WScript.Echo("  IP Protocol:        TCP.")
            Case NET_FW_IP_PROTOCOL_UDP    WScript.Echo("  IP Protocol:        UDP.")
            Case NET_FW_IP_PROTOCOL_ICMPv4 WScript.Echo("  IP Protocol:        UDP.")
            Case NET_FW_IP_PROTOCOL_ICMPv6 WScript.Echo("  IP Protocol:        UDP.")
            Case Else                      WScript.Echo("  IP Protocol:        " & rule.Protocol)
        End Select
        if rule.Protocol = NET_FW_IP_PROTOCOL_TCP or rule.Protocol = NET_FW_IP_PROTOCOL_UDP then
            WScript.Echo("  Local Ports:        " & rule.LocalPorts)
            WScript.Echo("  Remote Ports:       " & rule.RemotePorts)
            WScript.Echo("  LocalAddresses:     " & rule.LocalAddresses)
            WScript.Echo("  RemoteAddresses:    " & rule.RemoteAddresses)
        end if
        if rule.Protocol = NET_FW_IP_PROTOCOL_ICMPv4 or rule.Protocol = NET_FW_IP_PROTOCOL_ICMPv6 then
            WScript.Echo("  ICMP Type and Code:    " & rule.IcmpTypesAndCodes)
        end if
        Select Case rule.Direction
            Case NET_FW_RULE_DIR_IN  WScript.Echo("  Direction:          In")
            Case NET_FW_RULE_DIR_OUT WScript.Echo("  Direction:          Out")
        End Select
        WScript.Echo("  Enabled:            " & rule.Enabled)
        WScript.Echo("  Edge:               " & rule.EdgeTraversal)
        Select Case rule.Action
            Case NET_FW_ACTION_ALLOW  WScript.Echo("  Action:             Allow")
            Case NET_FW_ACTION_BLOCk  WScript.Echo("  Action:             Block")
        End Select
        WScript.Echo("  Grouping:           " & rule.Grouping)
        WScript.Echo("  Edge:               " & rule.EdgeTraversal)
        WScript.Echo("  Interface Types:    " & rule.InterfaceTypes)
        InterfaceArray = rule.Interfaces
        if IsEmpty(InterfaceArray) then
            WScript.Echo("  Interfaces:         All")
        else
            LowerBound = LBound(InterfaceArray)
            UpperBound = UBound(InterfaceArray)
            WScript.Echo("  Interfaces:     ")
            for iterate = LowerBound To UpperBound
                WScript.Echo("       " & InterfaceArray(iterate))
            Next
        end if

        WScript.Echo("")
    end if
Next
```



 

 




