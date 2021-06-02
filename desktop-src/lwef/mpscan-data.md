---
title: MPSCAN_DATA structure (MpClient.h)
description: Scan data passed to the callback.
ms.assetid: 6C9AAF1E-7566-43EE-A100-5112E9B8878C
keywords:
- MPSCAN_DATA structure Legacy Windows Environment Features
- PMPSCAN_DATA structure pointer Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MPSCAN_DATA
api_location:
- MpClient.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MPSCAN\_DATA structure

Scan data passed to the callback.

This structure contains cumulative threat and resource statistics. These stat fields are always valid.

## Syntax


```C++
typedef struct tagMPSCAN_DATA {
  MPSCAN_TYPE      ScanType;
  PMPRESOURCE_INFO ResourceInfo;
  MPRESOURCE_STATS ResourceStats;
  MPTHREAT_STATS   ThreatStats;
} MPSCAN_DATA, *PMPSCAN_DATA;
```



## Members

<dl> <dt>

**ScanType**
</dt> <dd>

Type: **[**MPSCAN\_TYPE**](mpscan-type.md)**

</dd> <dd>

Scan type.

</dd> <dt>

**ResourceInfo**
</dt> <dd>

Type: **PMPRESOURCE\_INFO**

</dd> <dd>

Resource information. See [**MPRESOURCE\_INFO**](mpresource-info.md).

</dd> <dt>

**ResourceStats**
</dt> <dd>

Type: **[**MPRESOURCE\_STATS**](mpresource-stats.md)**

</dd> <dd>

Resource-related cumulative statistics.

</dd> <dt>

**ThreatStats**
</dt> <dd>

Type: **[**MPTHREAT\_STATS**](mpthreat-stats.md)**

</dd> <dd>

Threat statistics with successful scan completions.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>MpClient.h</dt> </dl> |



## See also

<dl> <dt>

[**MPRESOURCE\_INFO**](mpresource-info.md)
</dt> <dt>

[**MPRESOURCE\_STATS**](mpresource-stats.md)
</dt> <dt>

[**MPSCAN\_TYPE**](mpscan-type.md)
</dt> <dt>

[**MPTHREAT\_STATS**](mpthreat-stats.md)
</dt> </dl>

 

 





