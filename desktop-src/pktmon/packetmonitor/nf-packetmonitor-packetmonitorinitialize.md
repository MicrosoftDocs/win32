---
title: PacketMonitorInitialize
description: Initializes the handle to packet monitor.
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
 - PacketMonitorInitialize
---

# PacketMonitorInitialize function

## Description

Initializes the handle to packet monitor.

Initializes Packet Monitor, and returns a handle to the Packet Monitor. Packet Monitor (Pktmon) is an in-box, cross-component network diagnostics tool for Windows. You can use it for packet capture, packet drop detection, packet filtering, and counting. To get the multisession and packet-streaming capabilities of Packet Monitor, your user mode application needs to first open a handle to Pktmon.

## Syntax

```cpp
HRESULT
WINAPI
PacketMonitorInitialize (
    _In_ UINT32 apiVersion,
    _Reserved_ void* reserved,
    _Out_ PACKETMONITOR_HANDLE* handle
    );
```

## Parameters

### [in] apiVersion

The version of the packet monitor API that the caller supports. Current Version is - PACKETMONITOR_API_VERSION_1_0(0x00010000)

### [in] reserved

This parameter is reserved and must be NULL.

### [out] handle

A pointer to a variable that receives a handle to the packet monitor driver. This will be of type - PACKETMONITOR_HANDLE.
This is declared in as ‘DECLARE_HANDLE(PACKETMONITOR_HANDLE)’.

## Returns

If the function succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code.
If something besides the current supported version is requested, it returns 'HRESULT_FROM_WIN32(ERROR_REVISION_MISMATCH)' i.e. 0x8007051A.

## Remarks

The packet monitor allows applications to capture and filter network packets on the local machine. 
To use the packet monitor, the caller must first call PacketMonitorInitialize to initialize the packet monitor and obtain a handle to it. Then, the caller can control the packet monitor through these API calls by passing the handle.

PacketMonitorUninitialize – Uninitialize and close handle to PacketMonitor.

PacketMonitorCreateLiveSession – Creates an individual packet monitor session.

PacketMonitorEnumDataSources – Get list of Data sources a.k.a. components.

PacketMonitorCreateRealtimeStream – Create a real time packet streaming object for a session.

The packet monitor requires administrator privileges to run. 

## See also

[Packet Monitor (Pktmon) reference](../pktmon-reference.md)
