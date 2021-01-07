---
description: The SESSIONSTATS structure provides statistics about a session.
ms.assetid: 51a6a601-634e-4d97-8c85-d3961400a2d1
title: SESSIONSTATS structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SESSIONSTATS
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# SESSIONSTATS structure

The **SESSIONSTATS** structure provides statistics about a [*session*](s.md).

## Syntax


```C++
typedef struct _SESSIONSTATS {
  DWORD NextSession;
  DWORD StationOwner;
  DWORD StationPartner;
  DWORD Flags;
  DWORD TotalPacketsSent;
} SESSIONSTATS, *LPSESSIONSTATS;
```



## Members

<dl> <dt>

**NextSession**
</dt> <dd>

Index of the station owner's next session.

</dd> <dt>

**StationOwner**
</dt> <dd>

Index of a owner station within the associated [STATIONSTATS](stationstats.md) structure array. The owner station is the station that initiated the session, the station that sent the packets of the session.

</dd> <dt>

**StationPartner**
</dt> <dd>

Index of the other station within the associated [STATIONSTATS](stationstats.md) structure array. The partner station is the station that received the packets of the session.

</dd> <dt>

**Flags**
</dt> <dd>

This member is obsolete.

</dd> <dt>

**TotalPacketsSent**
</dt> <dd>

Number of packets sent in the session.

</dd> </dl>

## Remarks

Network Monitor stores session and station information in two associated arrays, whose elements are **SESSIONSTATS** and [STATIONSTATS](stationstats.md) structures respectively. The members of these structures can be used to navigate between them. For example, to move to the next session for a specific station owner, use **NextSession**. To jump to the owner and partner station of the session in the STATIONSTATS array, use the index provided in **StationOwner** and **StationPartner**.

> [!Note]  
> The SESSIONSTATS array contains an element for each session in the current capture. The algorithm Network Monitor uses to add elements to the SESSIONSTATS array is based on efficiently recording information while the capture is in progress. Consequently, the next session for a specific owner station is not always the next element in the array.

 

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

 

 




