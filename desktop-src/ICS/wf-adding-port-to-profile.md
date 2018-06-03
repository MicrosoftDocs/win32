---
title: Adding a Port to Current Profile
description: Adding a port to a current profile that is enabled and scoped to all Internet protocols.
ms.assetid: 55ddb35a-92d7-49dd-83d7-2336fb93178e
keywords:
- Windows Firewall
- using
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Adding a Port to Current Profile

Adding a port to a current profile that is enabled and scoped to all Internet protocols.


```VB
Option Explicit
On Error GoTo 0

'Set Constants
Const NET_FW_IP_PROTOCOL_UDP = 17
Const NET_FW_IP_PROTOCOL_TCP = 6

Const NET_FW_SCOPE_ALL = 0
Const NET_FW_SCOPE_LOCAL_SUBNET = 1

'Declare variables
Dim errornum

' Create the firewall manager object.
Dim fwMgr
Set fwMgr = CreateObject("HNetCfg.FwMgr")

' Get the current profile for the local firewall policy.
Dim profile
Set profile = fwMgr.LocalPolicy.CurrentProfile

Dim port
Set port = CreateObject("HNetCfg.FWOpenPort")

port.Name = "HTTP"
port.Protocol = NET_FW_IP_PROTOCOL_TCP
port.Port = 80

'If using Scope, don't use RemoteAddresses
port.Scope = NET_FW_SCOPE_ALL
'Use this line to scope the port to Local Subnet only
'port.Scope = NET_FW_SCOPE_LOCAL_SUBNET

port.Enabled = TRUE
'Use this line instead if you want to add the port, but disabled
'port.Enabled = FALSE

On Error Resume Next
profile.GloballyOpenPorts.Add port
errornum = Err.Number

If errornum <> 0 Then
    WScript.Echo("Adding the port failed. Error Number: " & errornum)
End If

```



 

 




