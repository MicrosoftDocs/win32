---
title: PacketMonitorUninitialize
description: Close handle to Pktmon.
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
 - PacketMonitorUninitialize
---

# PacketMonitorUninitialize function

## Description

Close handle to Pktmon.

Called to close handle to the driver which was obtained by calling ‘PacketMonitorInitialize’.

## Syntax

```cpp
VOID
WINAPI
PacketMonitorUninitialize (
    _In_ PACKETMONITOR_HANDLE handle
    );
```

## Parameters

### [in] handle

Handle which was previously retrieved from a call to ‘PacketMonitorInitialize’.

## See also

[Packet Monitor (Pktmon) reference](../pktmon-reference.md)
