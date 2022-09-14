---
title: MPTHREAT_DETECTION enumeration (MpClient.h)
description: Possible known bad threat detection types.
ms.assetid: 14FCA9BD-A9A1-488B-B8E8-88DE0DF18F27
keywords:
- MPTHREAT_DETECTION enumeration Legacy Windows Environment Features
- PMPTHREAT_DETECTION enumeration pointer Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MPTHREAT_DETECTION
api_location:
- MpClient.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MPTHREAT\_DETECTION enumeration

Possible known bad threat detection types.

## Syntax


```C++
typedef enum tagMPTHREAT_DETECTION { 
  MP_THREAT_DETECTION_CONCRETE    = 0,
  MP_THREAT_DETECTION_HEURISTIC   = 1,
  MP_THREAT_DETECTION_GENERIC     = 2,
  MP_THREAT_DETECTION_SUSPICIOUS  = 4,
  MP_THREAT_DETECTION_FASTPATH    = 8
} MPTHREAT_DETECTION, *PMPTHREAT_DETECTION;
```



## Constants

<dl> <dt>

<span id="MP_THREAT_DETECTION_CONCRETE"></span><span id="mp_threat_detection_concrete"></span>**MP\_THREAT\_DETECTION\_CONCRETE**
</dt> <dd>

Threat was detected via concrete signatures.

</dd> <dt>

<span id="MP_THREAT_DETECTION_HEURISTIC"></span><span id="mp_threat_detection_heuristic"></span>**MP\_THREAT\_DETECTION\_HEURISTIC**
</dt> <dd>

Threat was detected via heuristic.

</dd> <dt>

<span id="MP_THREAT_DETECTION_GENERIC"></span><span id="mp_threat_detection_generic"></span>**MP\_THREAT\_DETECTION\_GENERIC**
</dt> <dd>

Threat was detected via generic signatures.

</dd> <dt>

<span id="MP_THREAT_DETECTION_SUSPICIOUS"></span><span id="mp_threat_detection_suspicious"></span>**MP\_THREAT\_DETECTION\_SUSPICIOUS**
</dt> <dd>

Threat was detected via behavior monitoring.

</dd> <dt>

<span id="MP_THREAT_DETECTION_FASTPATH"></span><span id="mp_threat_detection_fastpath"></span>**MP\_THREAT\_DETECTION\_FASTPATH**
</dt> <dd>

Threat was detected via fastpath.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>MpClient.h</dt> </dl> |



 

 





