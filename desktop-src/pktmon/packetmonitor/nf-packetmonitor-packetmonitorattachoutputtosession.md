---
title: PacketMonitorAttachOutputToSession
description: This function is used to attach output to an existing session.
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
 - PacketMonitorAttachOutputToSession
---

# PacketMonitorAttachOutputToSession function

## Description

This function is used to attach output to an existing session.

## Syntax

```cpp
HRESULT
WINAPI
PacketMonitorAttachOutputToSession(
    _In_ PACKETMONITOR_SESSION session,
    _In_ VOID* outputHandle
    );
```

## Parameters

### [in] session

Session handle.

### [in] outputHandle

Handle to an existing output type. Currently, the only output type supported is Real Time Stream. Hence, the outputHandle here would be object of type ‘PACKETMONITOR_REALTIME_STREAM’ which was created using ‘PacketMonitorCreateRealtimeStream’.

## Returns

If SUCCESS, it returns S_OK, else an HRESULT error code.

## Remarks

An output will only become active and start receiving monitoring information once the session is activated. This API can be called either before or after the call to ‘PacketMonitorSetSessionActive’.

## See also

[Packet Monitor (Pktmon) reference](../pktmon-reference.md)
