---
title: MPTHREAT_STATS structure (MpClient.h)
description: Threat-related statistics.
ms.assetid: 78B7E2A8-1BB4-4610-8E90-1F8ECBE740A8
keywords:
- MPTHREAT_STATS structure Legacy Windows Environment Features
- PMPTHREAT_STATS structure pointer Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MPTHREAT_STATS
api_location:
- MpClient.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MPTHREAT\_STATS structure

Threat-related statistics.

## Syntax


```C++
typedef struct tagMPTHREAT_STATS {
  UINT ThreatCount;
  UINT SuspiciousThreatCount;
  UINT Reserved[4];
} MPTHREAT_STATS, *PMPTHREAT_STATS;
```



## Members

<dl> <dt>

**ThreatCount**
</dt> <dd>

Type: **UINT**

</dd> <dd>

Number of threats detected.

</dd> <dt>

**SuspiciousThreatCount**
</dt> <dd>

Type: **UINT**

</dd> <dd>

Number of threats detected with behavior monitoring.

</dd> <dt>

**Reserved**
</dt> <dd>

Type: **UINT\[4\]**

</dd> <dd>

Fields reserved for future use.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>MpClient.h</dt> </dl> |



 

 





