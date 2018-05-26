---
title: Enumerating Firewall Rules with a Matching Group String
description: This example enumerates Windows Firewall rules with a matching grouping string using the Windows Firewall with Advanced Security APIs.VB This VBScript file includes sample code that enumerates  Windows Firewall rules with a matching grouping string  using the Microsoft Windows Firewall APIs. Option Explicit Dim CurrentProfiles Dim InterfaceArray Dim LowerBound Dim UpperBound Dim iterate Dim rule  Profile Type Const NET\_FW\_PROFILE2\_DOMAIN 1 Const NET\_FW\_PROFILE2\_PRIVATE 2 Const NET\_FW\_PROFILE2\_PUBLIC 4  Protocol Const NET\_FW\_IP\_PROTOCOL\_TCP 6 Const NET\_FW\_IP\_PROTOCOL\_UDP 17 Const NET\_FW\_IP\_PROTOCOL\_ICMPv4 1 Const NET\_FW\_IP\_PROTOCOL\_ICMPv6 58  Direction Const NET\_FW\_RULE\_DIR\_IN 1 Const NET\_FW\_RULE\_DIR\_OUT 2  Action Const NET\_FW\_ACTION\_BLOCK 0 Const NET\_FW\_ACTION\_ALLOW 1  Create the FwPolicy2 object. Dim fwPolicy2 Set fwPolicy2 CreateObject( \ 0034;HNetCfg.FwPolicy2 \ 0034;) CurrentProfiles fwPolicy2.CurrentProfileTypes // The returned CurrentProfiles bitmask can have more than 1 bit set if multiple profiles // are active or current at the same time if ( CurrentProfiles AND NET\_FW\_PROFILE2\_DOMAIN ) then WScript.Echo( \ 0034;Domain Firewall Profile is active \ 0034;) end if if ( CurrentProfiles AND NET\_FW\_PROFILE2\_PRIVATE ) then WScript.Echo( \ 0034;Private Firewall Profile is active \ 0034;) end if if ( CurrentProfiles AND NET\_FW\_PROFILE2\_PUBLIC ) then WScript.Echo( \ 0034;Public Firewall Profile is active \ 0034;) end if  Get the Rules object Dim RulesObject Set RulesObject fwPolicy2.Rules  Print all the rules. WScript.Echo( \ 0034;Rules \ 0034;) For Each rule In Rulesobject if rule.Grouping \ 0034; firewallapi.dll,-23255 \ 0034; then WScript.Echo( \ 0034; Rule Name \ 0034; rule.Name) WScript.Echo( \ 0034;
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---------------------------------------------- \ 0034;) WScript.Echo( \ 0034; Description \ 0034; rule.Description) WScript.Echo( \ 0034; Application Name \ 0034; rule.ApplicationName) WScript.Echo( \ 0034; Service Name \ 0034; rule.ServiceName) Select Case rule.Protocol Case NET\_FW\_IP\_PROTOCOL\_TCP WScript.Echo( \ 0034; IP Protocol TCP. \ 0034;) Case NET\_FW\_IP\_PROTOCOL\_UDP WScript.Echo( \ 0034; IP Protocol UDP. \ 0034;) Case NET\_FW\_IP\_PROTOCOL\_ICMPv4 WScript.Echo( \ 0034; IP Protocol UDP. \ 0034;) Case NET\_FW\_IP\_PROTOCOL\_ICMPv6 WScript.Echo( \ 0034; IP Protocol UDP. \ 0034;) Case Else WScript.Echo( \ 0034; IP Protocol \ 0034; rule.Protocol) End Select if rule.Protocol NET\_FW\_IP\_PROTOCOL\_TCP or rule.Protocol NET\_FW\_IP\_PROTOCOL\_UDP then WScript.Echo( \ 0034; Local Ports \ 0034; rule.LocalPorts) WScript.Echo( \ 0034; Remote Ports \ 0034; rule.RemotePorts) WScript.Echo( \ 0034; LocalAddresses \ 0034; rule.LocalAddresses) WScript.Echo( \ 0034; RemoteAddresses \ 0034; rule.RemoteAddresses) end if if rule.Protocol NET\_FW\_IP\_PROTOCOL\_ICMPv4 or rule.Protocol NET\_FW\_IP\_PROTOCOL\_ICMPv6 then WScript.Echo( \ 0034; ICMP Type and Code \ 0034; rule.IcmpTypesAndCodes) end if Select Case rule.Direction Case NET\_FW\_RULE\_DIR\_IN WScript.Echo( \ 0034; Direction In \ 0034;) Case NET\_FW\_RULE\_DIR\_OUT WScript.Echo( \ 0034; Direction Out \ 0034;) End Select WScript.Echo( \ 0034; Enabled \ 0034; rule.Enabled) WScript.Echo( \ 0034; Edge \ 0034; rule.EdgeTraversal) Select Case rule.Action Case NET\_FW\_ACTION\_ALLOW WScript.Echo( \ 0034; Action Allow \ 0034;) Case NET\_FW\_ACTION\_BLOCk WScript.Echo( \ 0034; Action Block \ 0034;) End Select WScript.Echo( \ 0034; Grouping \ 0034; rule.Grouping) WScript.Echo( \ 0034; Interface Types \ 0034; rule.InterfaceTypes) InterfaceArray rule.Interfaces if IsEmpty(InterfaceArray) then WScript.Echo( \ 0034;There are no excluded interfaces \ 0034;) else LowerBound LBound(InterfaceArray) UpperBound UBound(InterfaceArray) WScript.Echo( \ 0034;Excluded interfaces \ 0034;) for iterate LowerBound To UpperBound WScript.Echo( \ 0034; \ 0034; InterfaceArray(iterate)) Next end if end if Next
ms.assetid: 7ce10f9b-f9e2-4cda-b3da-6ccd4de26683
---

# Enumerating Firewall Rules with a Matching Group String

This example enumerates Windows Firewall rules with a matching grouping string using the Windows Firewall with Advanced Security APIs.


```VB
'   This VBScript file includes sample code that enumerates
'   Windows Firewall rules with a matching grouping string 
'   using the Microsoft Windows Firewall APIs.


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

' Print all the rules.
WScript.Echo("Rules:")

For Each rule In Rulesobject
    if rule.Grouping = "@firewallapi.dll,-23255" then
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
            Case NET_FW_ACTION_ALLOW  WScript.Echo("  Action:          Allow")
            Case NET_FW_ACTION_BLOCk  WScript.Echo("  Action:          Block")
        End Select
        WScript.Echo("  Grouping:           " & rule.Grouping)
        WScript.Echo("  Interface Types:    " & rule.InterfaceTypes)
        InterfaceArray = rule.Interfaces
        if IsEmpty(InterfaceArray) then
            WScript.Echo("There are no excluded interfaces")
        else
            LowerBound = LBound(InterfaceArray)
            UpperBound = UBound(InterfaceArray)
            WScript.Echo("Excluded interfaces: ")
            for iterate = LowerBound To UpperBound
                WScript.Echo("    " & InterfaceArray(iterate))
            Next
        end if
    end if
Next
```



 

 




