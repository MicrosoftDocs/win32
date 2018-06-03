---
title: Enabling RemoteAdmin
description: Enabling RemoteAdmin
ms.assetid: 0408b6bc-04c4-4069-8e33-fd1a80378ef8
keywords:
- Windows Firewall
- using
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Enabling RemoteAdmin

The following sample shows the process for enabling RemoteAdmin for a specific subnet and some other options.


```VB

Option Explicit

' Set constants
Const NET_FW_SCOPE_ALL = 0
Const NET_FW_SCOPE_LOCAL_SUBNET = 1

'Declare variables
Dim RASettings

' Create the firewall manager object.
Dim fwMgr
Set fwMgr = CreateObject("HNetCfg.FwMgr")

' Get the current profile for the local firewall policy.
Dim profile
Set profile = fwMgr.LocalPolicy.CurrentProfile

set RASettings = profile.RemoteAdminSettings

' Enable RemoteAdmin traffic from the 12.1.1.64 subnet
RASettings.Enabled = TRUE
RASettings.RemoteAddresses = "12.1.1.64/255.255.255.240"

'Use this line if you want to disable RemoteAdmin
'RASettings.Enabled = FALSE
'Use this line if you want to scope RemoteAdmin to ANY
'Use RemoteAddresses or Scope, but not both
'RASettings.RemoteAddesses = "*"
'RASettings.Scope = NET_FW_SCOPE_ALL


```



 

 




