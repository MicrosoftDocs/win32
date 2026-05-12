---
title: PacketMonitorAddSingleDataSourceToSession
description: Adds a DataSource to a PacketMonitor Session.
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
 - PacketMonitorAddSingleDataSourceToSession
---

# PacketMonitorAddSingleDataSourceToSession function

## Description

This function adds a DataSource to a PacketMonitor Session. It tells Packet Monitor to only capture packets from the specified data source for the corresponding session. Multiple instances of this API call can be used to add a subset of Data Source list previously retrieved from ‘PacketMonitorEnumDataSources’.

## Syntax

```cpp
HRESULT
WINAPI
PacketMonitorAddSingleDataSourceToSession(
    _In_ PACKETMONITOR_SESSION session,
    _In_ PACKETMONITOR_DATA_SOURCE_SPECIFICATION const* dataSource
    );
```

## Parameters

### [in] session

Packet Monitor Session to which this Data Source will be applied as filter for Packet Monitoring. The session object can be retrieved by calling PacketMonitorCreateLiveSession. 

### [in] dataSource

Pointer to a PACKETMONITOR_DATA_SOURCE_SPECIFICATION having information about a Data Source which reports packets to the pktmon driver. 
This Data Source information is a subset from the Data Source list obtained by calling the function ‘PacketMonitorEnumDataSources’.

## Returns

If the function succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code.

## Remarks

‘PacketMonitorEnumDataSources’ should be called prior to this function. Multiple Data Sources can be added to the session by calling this function each time. 

The API can be called either before or after activating the session.

## See also

[Packet Monitor (Pktmon) reference](../pktmon-reference.md)
