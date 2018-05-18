---
title: Changing Settings in a Specific Profile
description: Changing Settings in a Specific Profile
ms.assetid: '03e42a39-619a-4e84-9634-ee3e7a2325ad'
keywords: ["Windows Firewall", "using"]
---

# Changing Settings in a Specific Profile

The following example demonstrates changing settings in a specific profile.


```VB
Option Explicit

'Set Constants
Const NET_FW_PROFILE_DOMAIN = 0
Const NET_FW_PROFILE_STANDARD = 1

'Declare variables
' Create the firewall manager object.
Dim fwMgr
Set fwMgr = CreateObject("HNetCfg.FwMgr")

' Get the current profile for the local firewall policy.
Dim profile
set profile = fwMgr.LocalPolicy.GetProfileByType(NET_FW_PROFILE_STANDARD)

profile.IcmpSettings.AllowInboundEchoRequest = TRUE

'Use this line if you want to disable the setting.
'profile.IcmpSettings.AllowInboundEchoRequest = FALSE


```



 

 




