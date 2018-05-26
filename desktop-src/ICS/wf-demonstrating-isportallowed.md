---
title: Demonstrating IsPortAllowed
description: Demonstrating IsPortAllowed
ms.assetid: 0083cec4-8581-4743-87d8-517edf33f2ea
keywords:
- Windows Firewall
- using
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Demonstrating IsPortAllowed

The following example demonstrates uses of the [**IsPortAllowed**](/windows/previous-versions/Netfw/nf-netfw-inetfwmgr-isportallowed?branch=master) function.


```VB

Option Explicit

' Set constants
Const NET_FW_IP_VERSION_V4 = 0
Const NET_FW_IP_VERSION_V6 = 1
Const NET_FW_IP_VERSION_ANY = 2

Const NET_FW_IP_PROTOCOL_UDP = 17
Const NET_FW_IP_PROTOCOL_TCP = 6

' Declare variables
Dim Allowed, Restricted

Allowed = FALSE
Restricted = TRUE
' Create the firewall manager object.
Dim fwMgr
Set fwMgr = CreateObject("HNetCfg.FwMgr")

' First a reminder on the various arguments:
' IsPortAllowed( imagefilename, ipversion, portnumber, localaddress, protocol, allowed, restricted)

fwMgr.IsPortAllowed vbNullString, NET_FW_IP_VERSION_V4, 5500, "172.31.86.122", NET_FW_IP_PROTOCOL_TCP, Allowed, Restricted
WScript.Echo("Is TCP port 5500 allowed on interface 172.31.86.122? Allowed: " & Allowed & "  Restricted: " & Restricted)

fwMgr.IsPortAllowed "C:\Program Files\Windows Media Player\wmplayer.exe", NET_FW_IP_VERSION_ANY, 0, vbNullString, 0, Allowed, Restricted
WScript.Echo("Is Windows Media Player allowed on all interfaces? Allowed: " & Allowed & "  Restricted: " & Restricted)

fwMgr.IsPortAllowed "C:\Program Files\Windows Media Player\wmplayer.exe", NET_FW_IP_VERSION_V4, 8800, vbNullString, NET_FW_IP_PROTOCOL_TCP, Allowed, Restricted
WScript.Echo("Is Windows Media Player allowed on TCP port 8800 on all interfaces? Allowed: " & Allowed & "  Restricted: " & Restricted)

fwMgr.IsPortAllowed "C:\Program Files\Windows Media Player\wmplayer.exe", NET_FW_IP_VERSION_V6, 0, "3ffe:8311:ffff:f28f:ad9d:c61d:39a6:12fb", 0, Allowed, Restricted
WScript.Echo("Is Windows Media Player allowed on interface 3ffe:8311:ffff:f28f:ad9d:c61d:39a6:12fb? Allowed: " & Allowed & "  Restricted: " & Restricted)



```



 

 




