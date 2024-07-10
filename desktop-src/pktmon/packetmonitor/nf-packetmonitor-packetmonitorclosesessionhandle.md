---
title: PacketMonitorCloseSessionHandle
description: Closes handle to previously created session object.
ms.topic: reference
ms.date: 07/03/2024
topic_type:
 - APIRef
 - kbSyntax
api_type:
 - DllExport
api_location:
 - Pktmonapi.dll
api_name:
 - PacketMonitorCloseSessionHandle
---

# PacketMonitorCloseSessionHandle function

## Description

Closes handle to previously created session object.

This is called to close the handle to a previously created session object. Failure to close a session handle will result in leaked resources in the PktMon driver.

## Syntax

```cpp
VOID
WINAPI
PacketMonitorCloseSessionHandle(
    _In_ PACKETMONITOR_SESSION session
    );
```

## Parameters

### [in] session

Session Object previously created by calling ‘PacketMonitorCreateLiveSession’.

## See also

[Packet Monitor (Pktmon) reference](../pktmon-reference.md)
