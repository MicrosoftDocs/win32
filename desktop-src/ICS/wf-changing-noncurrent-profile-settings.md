---
title: Changing Settings in the Non-current Profile
description: Changing Settings in the Non-current Profile
ms.assetid: 5db288bf-88e0-4296-bab3-b3ec5e509f2b
keywords:
- Windows Firewall
- using
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Changing Settings in the Non-current Profile

The following example demonstrates changing settings in the non-current profile.


```VB
Option Explicit

'Set Constants
Const NET_FW_PROFILE_DOMAIN = 0
Const NET_FW_PROFILE_STANDARD = 1

'Declare variables
Dim profiletype

' Create the firewall manager object.
Dim fwMgr
Set fwMgr = CreateObject("HNetCfg.FwMgr")

' Get the current profile for the local firewall policy.
Dim profile
Set profile = fwMgr.LocalPolicy.CurrentProfile
profiletype = profile.Type

' Now get the profile that isn't current.
If profiletype = NET_FW_PROFILE_DOMAIN Then
   set profile = fwMgr.LocalPolicy.GetProfileByType(NET_FW_PROFILE_STANDARD)
Else
   set profile = fwMgr.LocalPolicy.GetProfileByType(NET_FW_PROFILE_DOMAIN)
End If

profile.IcmpSettings.AllowInboundEchoRequest = TRUE

```



 

 




