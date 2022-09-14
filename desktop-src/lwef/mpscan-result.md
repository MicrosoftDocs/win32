---
title: MPSCAN_RESULT structure (MpClient.h)
description: The results of a scan.
ms.assetid: 9031A371-092A-4175-BE1D-90442A5BED2D
keywords:
- MPSCAN_RESULT structure Legacy Windows Environment Features
- PMPSCAN_RESULT structure pointer Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MPSCAN_RESULT
api_location:
- MpClient.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MPSCAN\_RESULT structure

The results of a scan.

## Syntax


```C++
typedef struct tagMPSCAN_RESULT {
  MPSCAN_TYPE      ScanType;
  MPSOURCE         Source;
  GUID             ScanGuid;
  ULARGE_INTEGER   StartTime;
  ULARGE_INTEGER   EndTime;
  MPTHREAT_STATS   ThreatStats;
  MPRESOURCE_STATS ResourceStats;
  ULONGLONG        SignatureVersion;
} MPSCAN_RESULT, *PMPSCAN_RESULT;
```



## Members

<dl> <dt>

**ScanType**
</dt> <dd>

Type: **[**MPSCAN\_TYPE**](mpscan-type.md)**

</dd> <dd>

Scan type. See [**MPSCAN\_TYPE**](mpscan-type.md).

</dd> <dt>

**Source**
</dt> <dd>

Type: **[**MPSOURCE**](mpsource.md)**

</dd> <dd>

Scan source, such as user or system initiated. See [**MPSOURCE**](mpsource.md).

</dd> <dt>

**ScanGuid**
</dt> <dd>

Type: **GUID**

</dd> <dd>

Scan identifier.

</dd> <dt>

**StartTime**
</dt> <dd>

Type: **ULARGE\_INTEGER**

</dd> <dd>

Scan start time.

</dd> <dt>

**EndTime**
</dt> <dd>

Type: **ULARGE\_INTEGER**

</dd> <dd>

Scan end time.

</dd> <dt>

**ThreatStats**
</dt> <dd>

Type: **[**MPTHREAT\_STATS**](mpthreat-stats.md)**

</dd> <dd>

Threat-related statistics. See [**MPTHREAT\_STATS**](mpthreat-stats.md).

</dd> <dt>

**ResourceStats**
</dt> <dd>

Type: **[**MPRESOURCE\_STATS**](mpresource-stats.md)**

</dd> <dd>

Resource-related statistics. See [**MPRESOURCE\_STATS**](mpresource-stats.md).

</dd> <dt>

**SignatureVersion**
</dt> <dd>

Type: **ULONGLONG**

</dd> <dd>

Version of signature used for scan.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>MpClient.h</dt> </dl> |



## See also

<dl> <dt>

[**MPRESOURCE\_STATS**](mpresource-stats.md)
</dt> <dt>

[**MPSCAN\_TYPE**](mpscan-type.md)
</dt> <dt>

[**MPSOURCE**](mpsource.md)
</dt> <dt>

[**MPTHREAT\_STATS**](mpthreat-stats.md)
</dt> </dl>

 

 





