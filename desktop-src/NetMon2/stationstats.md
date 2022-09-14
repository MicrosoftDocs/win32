---
description: The STATIONSTATS structure provides statistics about a specific station described by the current capture.
ms.assetid: f85d53d6-f496-4242-875f-e173c76b046a
title: STATIONSTATS structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- STATIONSTATS
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# STATIONSTATS structure

The **STATIONSTATS** structure provides statistics about a specific [*station*](s.md) described by the current capture.

## Syntax


```C++
typedef struct _STATIONSTATS {
  DWORD NextStationStats;
  DWORD SessionPartnerList;
  DWORD Flags;
  BYTE  StationAddress[6];
  WORD  Pad;
  DWORD TotalPacketsReceived;
  DWORD TotalDirectedPacketsSent;
  DWORD TotalBroadcastPacketsSent;
  DWORD TotalMulticastPacketsSent;
  DWORD TotalBytesReceived;
  DWORD TotalBytesSent;
} STATIONSTATS, *LPSTATIONSTATS;
```



## Members

<dl> <dt>

**NextStationStats**
</dt> <dd>

Index of the next station recorded in the **STATIONSTATS** structure array.

</dd> <dt>

**SessionPartnerList**
</dt> <dd>

Index of the station partner list.

</dd> <dt>

**Flags**
</dt> <dd>

This member is obsolete.

</dd> <dt>

**StationAddress**
</dt> <dd>

The MAC address of the station.

</dd> <dt>

**Pad**
</dt> <dd>

**DWORD** alignment.

</dd> <dt>

**TotalPacketsReceived**
</dt> <dd>

Total number of packets sent to the station.

</dd> <dt>

**TotalDirectedPacketsSent**
</dt> <dd>

Total number of directed packets sent by the station.

</dd> <dt>

**TotalBroadcastPacketsSent**
</dt> <dd>

Total number of broadcast-directed packets (MAC address FF FF FF FF FF FF) sent by the station.

</dd> <dt>

**TotalMulticastPacketsSent**
</dt> <dd>

Total number of multicast packets (Group bit set in destination address) sent by the station.

</dd> <dt>

**TotalBytesReceived**
</dt> <dd>

Total number of bytes sent to the station.

</dd> <dt>

**TotalBytesSent**
</dt> <dd>

Total number of bytes sent by the station.

</dd> </dl>

## Remarks

Network Monitor stores session and station information in two associated arrays. whose elements are [SESSIONSTATS](sessionstats.md) and **STATIONSTATS** structures respectively. The members of these structures can be used to navigate between them. For example, to move to the next station use **NextStationStats**. To jump to the session partner list in the SESSIONSTATS array, use the index provided in **SessionPartnerList**.

> [!Note]  
> The **STATIONSTATS** array contains an element for each station used during the current capture. The algorithm Network Monitor uses to add elements to this array is based on the most efficient way to record information while the capture is in progress. Consequently, the next station is not always the next element in the array.

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



## See also

<dl> <dt>

[IDelaydC::GetConversationStatistics](idelaydc-getconversationstatistics.md)
</dt> <dt>

[IRTC::GetConversationStatistics](irtc-getconversationstatistics.md)
</dt> <dt>

[IStats::GetConversationStatistics](istats-getconversationstatistics.md)
</dt> </dl>

 

 




