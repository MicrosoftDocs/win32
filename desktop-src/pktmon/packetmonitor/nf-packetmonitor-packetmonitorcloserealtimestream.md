---
title: PacketMonitorCloseRealtimeStream
description: Used to close a handle to an already created Packet Monitor Real Time Stream Object.
ms.topic: reference
ms.date: 07/05/2024
topic_type:
 - APIRef
 - kbSyntax
api_type:
 - DllExport
api_location:
 - Pktmonapi.dll
api_name:
 - PacketMonitorCloseRealtimeStream
---

# PacketMonitorCloseRealtimeStream function

## Description

This function is used to close a handle to an already created Packet Monitor Real Time Stream Object. This will remove the stream output from its attached session. Packets won’t be observed on this stream after this call.

## Syntax

```cpp
VOID
WINAPI
PacketMonitorCloseRealtimeStream(
    _In_ PACKETMONITOR_REALTIME_STREAM realtimeStream
    );
```

## Parameters

### [in] realtimeStream

Handle to the stream. 

## See also

[Packet Monitor (Pktmon) reference](../pktmon-reference.md)
