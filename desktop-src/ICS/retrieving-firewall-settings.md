---
title: Retrieving Firewall Settings
description: This example reads Windows Firewall settings per profile using the Windows Firewall with Advanced Security APIs.VB This VBScript file includes sample code that reads Windows Firewall  settings per profile using the Microsoft Windows Firewall APIs.
ms.assetid: 904d0500-ef90-43ae-90c5-b74af2fdc72e
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Retrieving Firewall Settings

This example reads Windows Firewall settings per profile using the Windows Firewall with Advanced Security APIs.


```VB
'    This VBScript file includes sample code that reads Windows Firewall  
'    settings per profile using the Microsoft Windows Firewall APIs.


option explicit

Dim CurrentProfiles
Dim LowerBound
Dim UpperBound
Dim iterate
Dim excludedinterfacesarray

' Profile Type
Const NET_FW_PROFILE2_DOMAIN = 1
Const NET_FW_PROFILE2_PRIVATE = 2
Const NET_FW_PROFILE2_PUBLIC = 4

' Action
Const NET_FW_ACTION_BLOCK = 0
Const NET_FW_ACTION_ALLOW = 1


' Create the FwPolicy2 object.
Dim fwPolicy2
Set fwPolicy2 = CreateObject("HNetCfg.FwPolicy2")

CurrentProfiles = fwPolicy2.CurrentProfileTypes

'// The returned 'CurrentProfiles' bitmask can
'// have more than 1 bit set if multiple profiles 
'// are active or current at the same time

if ( CurrentProfiles AND NET_FW_PROFILE2_DOMAIN ) then
   if fwPolicy2.FirewallEnabled(NET_FW_PROFILE2_DOMAIN) = TRUE then
      WScript.Echo("Firewall is ON on domain profile.")
   else
      WScript.Echo("Firewall is OFF on domain profile.")
   end if
end if

if ( CurrentProfiles AND NET_FW_PROFILE2_PRIVATE ) then
   if fwPolicy2.FirewallEnabled(NET_FW_PROFILE2_PRIVATE) = TRUE then
      WScript.Echo("Firewall is ON on private profile.")
   else
      WScript.Echo("Firewall is OFF on private profile.")
   end if
end if

if ( CurrentProfiles AND NET_FW_PROFILE2_PUBLIC ) then
   if fwPolicy2.FirewallEnabled(NET_FW_PROFILE2_PUBLIC) = TRUE then
      WScript.Echo("Firewall is ON on public profile.")
   else
      WScript.Echo("Firewall is OFF on public profile.")
   end if
end if
```



 

 




