---
title: MPTHREAT_STATS_DATA structure (MpClient.h)
description: Additional threat statistics data.
ms.assetid: 8C01C746-8FD8-4311-908D-D1F4E3488480
keywords:
- MPTHREAT_STATS_DATA structure Legacy Windows Environment Features
- PMPTHREAT_STATS_DATA structure pointer Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MPTHREAT_STATS_DATA
api_location:
- MpClient.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MPTHREAT\_STATS\_DATA structure

Additional threat statistics data.

## Syntax


```C++
typedef struct tagMPTHREAT_STATS_DATA {
  DWORD dwThreatCount;
} MPTHREAT_STATS_DATA, *PMPTHREAT_STATS_DATA;
```



## Members

<dl> <dt>

**dwThreatCount**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Number of threats.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>MpClient.h</dt> </dl> |



 

 





