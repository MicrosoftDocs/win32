---
title: Disabling the Firewall per Interface
description: This example disables the firewall on a per interface basis using the Windows Firewall with Advanced Security APIs.VB This VBScript file includes sample code that disables the firewall  on a per interface basis using the Microsoft Windows Firewall APIs. option explicit  Profile Type Const NET\_FW\_PROFILE2\_DOMAIN 1 Const NET\_FW\_PROFILE2\_PRIVATE 2 Const NET\_FW\_PROFILE2\_PUBLIC 4 Dim CurrentProfiles Dim InterfaceArray Dim LowerBound Dim UpperBound Dim iterate  Keep firewall ON exept for a specific interface  Create the FwPolicy2 object. Dim fwPolicy2 Set fwPolicy2 CreateObject( \ 0034;HNetCfg.FwPolicy2 \ 0034;) CurrentProfiles fwPolicy2.CurrentProfileTypes  The returned CurrentProfiles bitmask can have more than 1 bit set if multiple profiles  are active or current at the same time if ( CurrentProfiles AND NET\_FW\_PROFILE2\_DOMAIN ) then if fwPolicy2.FirewallEnabled(NET\_FW\_PROFILE2\_DOMAIN) TRUE then fwPolicy2.FirewallEnabled(NET\_FW\_PROFILE2\_DOMAIN) TRUE end if Exclude Interfaces such that the firewall is OFF on those interfaces. InterfaceArray Array( \ 0034;Local Area Connection \ 0034;) LowerBound LBound(InterfaceArray) UpperBound UBound(InterfaceArray) WScript.Echo( \ 0034; Excluded interfaces in Domain profile \ 0034;) for iterate LowerBound To UpperBound WScript.Echo( \ 0034; \ 0034; InterfaceArray(iterate)) Next fwPolicy2.ExcludedInterfaces(NET\_FW\_PROFILE2\_DOMAIN) InterfaceArray end if if ( CurrentProfiles AND NET\_FW\_PROFILE2\_PRIVATE ) then if fwPolicy2.FirewallEnabled(NET\_FW\_PROFILE2\_PRIVATE) TRUE then fwPolicy2.FirewallEnabled(NET\_FW\_PROFILE2\_PRIVATE) TRUE end if Exclude Interfaces such that the firewall is OFF on those interfaces. InterfaceArray Array( \ 0034;Local Area Connection \ 0034;) LowerBound LBound(InterfaceArray) UpperBound UBound(InterfaceArray) WScript.Echo( \ 0034; Excluded interfaces in Private profile \ 0034;) for iterate LowerBound To UpperBound WScript.Echo( \ 0034; \ 0034; InterfaceArray(iterate)) Next fwPolicy2.ExcludedInterfaces(NET\_FW\_PROFILE2\_PRIVATE) InterfaceArray end if if ( CurrentProfiles AND NET\_FW\_PROFILE2\_PUBLIC ) then if fwPolicy2.FirewallEnabled(NET\_FW\_PROFILE2\_PUBLIC) TRUE then fwPolicy2.FirewallEnabled(NET\_FW\_PROFILE2\_PUBLIC) TRUE end if Exclude Interfaces such that the firewall is OFF on those interfaces. InterfaceArray Array( \ 0034;Local Area Connection \ 0034;) LowerBound LBound(InterfaceArray) UpperBound UBound(InterfaceArray) WScript.Echo( \ 0034; Excluded interfaces in Public profile \ 0034;) for iterate LowerBound To UpperBound WScript.Echo( \ 0034; \ 0034; InterfaceArray(iterate)) Next fwPolicy2.ExcludedInterfaces(NET\_FW\_PROFILE2\_PUBLIC) InterfaceArray end if
ms.assetid: cda0879f-393a-4358-bfdd-6a93887648f3
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Disabling the Firewall per Interface

This example disables the firewall on a per interface basis using the Windows Firewall with Advanced Security APIs.


```VB
'  This VBScript file includes sample code that disables the firewall 
'  on a per interface basis using the Microsoft Windows Firewall APIs.


option explicit


' Profile Type
Const NET_FW_PROFILE2_DOMAIN = 1
Const NET_FW_PROFILE2_PRIVATE = 2
Const NET_FW_PROFILE2_PUBLIC = 4

Dim CurrentProfiles
Dim InterfaceArray
Dim LowerBound
Dim UpperBound
Dim iterate

' Keep firewall ON exept for a specific interface


' Create the FwPolicy2 object.
Dim fwPolicy2

Set fwPolicy2 = CreateObject("HNetCfg.FwPolicy2")

CurrentProfiles = fwPolicy2.CurrentProfileTypes

' The returned 'CurrentProfiles' bitmask can have more than 1 bit set if multiple profiles 
' are active or current at the same time

if ( CurrentProfiles AND NET_FW_PROFILE2_DOMAIN ) then
   if fwPolicy2.FirewallEnabled(NET_FW_PROFILE2_DOMAIN) <> TRUE then
      fwPolicy2.FirewallEnabled(NET_FW_PROFILE2_DOMAIN) = TRUE
   end if

   'Exclude Interfaces such that the firewall is OFF on those interfaces.
   InterfaceArray = Array("Local Area Connection")
   LowerBound = LBound(InterfaceArray)
   UpperBound = UBound(InterfaceArray)
   WScript.Echo("   Excluded interfaces in Domain profile: ")    
   for iterate = LowerBound To UpperBound
      WScript.Echo("    " & InterfaceArray(iterate))
   Next
   fwPolicy2.ExcludedInterfaces(NET_FW_PROFILE2_DOMAIN) = InterfaceArray
end if

if ( CurrentProfiles AND NET_FW_PROFILE2_PRIVATE ) then
   if fwPolicy2.FirewallEnabled(NET_FW_PROFILE2_PRIVATE) <> TRUE then
      fwPolicy2.FirewallEnabled(NET_FW_PROFILE2_PRIVATE) = TRUE
   end if

   'Exclude Interfaces such that the firewall is OFF on those interfaces.
   InterfaceArray = Array("Local Area Connection")
   LowerBound = LBound(InterfaceArray)
   UpperBound = UBound(InterfaceArray)
   WScript.Echo("   Excluded interfaces in Private profile: ")    
   for iterate = LowerBound To UpperBound
      WScript.Echo("    " & InterfaceArray(iterate))
   Next
   fwPolicy2.ExcludedInterfaces(NET_FW_PROFILE2_PRIVATE) = InterfaceArray
end if

if ( CurrentProfiles AND NET_FW_PROFILE2_PUBLIC ) then
   if fwPolicy2.FirewallEnabled(NET_FW_PROFILE2_PUBLIC) <> TRUE then
      fwPolicy2.FirewallEnabled(NET_FW_PROFILE2_PUBLIC) = TRUE
   end if

   'Exclude Interfaces such that the firewall is OFF on those interfaces.
   InterfaceArray = Array("Local Area Connection")
   LowerBound = LBound(InterfaceArray)
   UpperBound = UBound(InterfaceArray)
   WScript.Echo("   Excluded interfaces in Public profile: ")    
   for iterate = LowerBound To UpperBound
      WScript.Echo("    " & InterfaceArray(iterate))
   Next
   fwPolicy2.ExcludedInterfaces(NET_FW_PROFILE2_PUBLIC) = InterfaceArray
end if

```



 

 




