---
title: MPSTATUS_INFO structure (MpClient.h)
description: Status information for the malware protection manager.
ms.assetid: 614F14EC-64CC-4E3F-8A89-42AA1E0DC95D
keywords:
- MPSTATUS_INFO structure Legacy Windows Environment Features
- PMPSTATUS_INFO structure pointer Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MPSTATUS_INFO
api_location:
- MpClient.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MPSTATUS\_INFO structure

Status information for the malware protection manager.

## Syntax


```C++
typedef struct tagMPSTATUS_INFO {
  DWORD               ProductStatus;
  MPSCAN_RESULT       LastQuickScan;
  MPSCAN_RESULT       LastFullScan;
  MPTHREAT_STATS      ThreatStats;
  MPTHREAT_STATS_DATA ThreatState[MP_THREAT_STAT_MAX_VALUE+1];
  MPCOMPONENT_STATUS  Component[MPCOMPONENT_MAXVALUE+1];
  ULARGE_INTEGER      ProductExpirationTime;
} MPSTATUS_INFO, *PMPSTATUS_INFO;
```



## Members

<dl> <dt>

**ProductStatus**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Overall product status. This is a combination of bit flags from [**MPSTATUS\_FLAG**](mpstatus-flag.md).

</dd> <dt>

**LastQuickScan**
</dt> <dd>

Type: **[**MPSCAN\_RESULT**](mpscan-result.md)**

</dd> <dd>

Results of the last scan by the malware protection manager. See [**MPSCAN\_RESULT**](mpscan-result.md).

</dd> <dt>

**LastFullScan**
</dt> <dd>

Type: **[**MPSCAN\_RESULT**](mpscan-result.md)**

</dd> <dd>

Results of the last full scan by the malware protection manager. See [**MPSCAN\_RESULT**](mpscan-result.md).

</dd> <dt>

**ThreatStats**
</dt> <dd>

Type: **[**MPTHREAT\_STATS**](mpthreat-stats.md)**

</dd> <dd>

Active threat statistics. See [**MPTHREAT\_STATS**](mpthreat-stats.md).

</dd> <dt>

**ThreatState**
</dt> <dd>

Type: **[**MPTHREAT\_STATS\_DATA**](mpthreat-stats-data.md)\[MP\_THREAT\_STAT\_MAX\_VALUE+1\]**

</dd> <dd>

Additional threat statistics data, such as the number of threats. See [**MPTHREAT\_STATS\_DATA**](mpthreat-stats-data.md).

</dd> <dt>

**Component**
</dt> <dd>

Type: **[**MPCOMPONENT\_STATUS**](mpcomponent-status.md)\[MPCOMPONENT\_MAXVALUE+1\]**

</dd> <dd>

An array of statuses for multiple components. Use a value from the [**MPCOMPONENT\_ID**](mpcomponent-id.md) enumeration as an index into the array.

</dd> <dt>

**ProductExpirationTime**
</dt> <dd>

Type: **ULARGE\_INTEGER**

</dd> <dd>

Product expiration timestamp in UNC. This is valid only if the expiration status is set.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>MpClient.h</dt> </dl> |



## See also

<dl> <dt>

[**MPCOMPONENT\_ID**](mpcomponent-id.md)
</dt> <dt>

[**MPCOMPONENT\_STATUS**](mpcomponent-status.md)
</dt> <dt>

[**MPSCAN\_RESULT**](mpscan-result.md)
</dt> <dt>

[**MPSTATUS\_FLAG**](mpstatus-flag.md)
</dt> <dt>

[**MPTHREAT\_STATS**](mpthreat-stats.md)
</dt> <dt>

[**MPTHREAT\_STATS\_DATA**](mpthreat-stats-data.md)
</dt> </dl>

 

 





