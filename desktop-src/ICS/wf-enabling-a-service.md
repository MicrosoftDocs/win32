---
title: Enabling a Service
description: Enabling a Service
ms.assetid: 2535db99-3fca-456b-8529-f16992ae4901
keywords:
- Windows Firewall
- using
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Enabling a Service

The following example demonstrates enabling a service on the current profile.


```VB
Option Explicit

'Set Constants
Const NET_FW_SERVICE_FILE_AND_PRINT = 0
Const NET_FW_SERVICE_UPNP = 1
Const NET_FW_SERVICE_REMOTE_DESKTOP = 2

' Scope
Const NET_FW_SCOPE_ALL = 0
Const NET_FW_SCOPE_LOCAL_SUBNET = 1

'Declare variables
Dim service

' Create the firewall manager object.
Dim fwMgr
Set fwMgr = CreateObject("HNetCfg.FwMgr")

' Get the current profile for the local firewall policy.
Dim profile
Set profile = fwMgr.LocalPolicy.CurrentProfile

Set service  = profile.Services.Item(NET_FW_SERVICE_FILE_AND_PRINT)
service.Enabled = TRUE
' Use either Scope or RemoteAddresses, but not both
'service.RemoteAddresses = "*"
service.Scope = NET_FW_SCOPE_ALL

'Use this line to disable the service
'service.Enabled = FALSE

```



 

 




