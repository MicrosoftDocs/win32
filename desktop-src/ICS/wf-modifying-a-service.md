---
title: Modifying a Service
description: Modifying a Service
ms.assetid: 59416aa4-ce17-4ce1-8dd8-21beb148d717
keywords:
- Windows Firewall
- using
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Modifying a Service

The following example demonstrates enabling a service, disabling one of its ports, and changing the scope of another.

``` syntax
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
Dim port

' Create the firewall manager object.
Dim fwMgr
Set fwMgr = CreateObject("HNetCfg.FwMgr")

' Get the current profile for the local firewall policy.
Dim profile
Set profile = fwMgr.LocalPolicy.CurrentProfile

Set service = profile.Services.Item(NET_FW_SERVICE_FILE_AND_PRINT)
service.Enabled = TRUE
' Use either Scope or RemoteAddresses, but not both
service.RemoteAddresses = "*"
'service.Scope = NET_FW_SCOPE_ALL

' The Service is Enabled and Scoped to All IP's. Now disable
' TCP 445 and scope TCP 139 to Local Subnet only.
For Each port In service.GloballyOpenPorts
    if port.Port = 445 Then port.Enabled = FALSE
    if port.Port = 139 Then port.Scope = NET_FW_SCOPE_LOCAL_SUBNET
Next
```

 

 




