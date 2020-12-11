---
title: MPCALLBACK_DATA structure (MpClient.h)
description: Data passed to the callback function.
ms.assetid: EA8E6C1E-F80B-4247-B073-C78D49A354CF
keywords:
- MPCALLBACK_DATA structure Legacy Windows Environment Features
- PMPCALLBACK_DATA structure pointer Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MPCALLBACK_DATA
api_location:
- MpClient.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MPCALLBACK\_DATA structure

Data passed to the callback function.

## Syntax


```C++
typedef struct tagMPCALLBACK_DATA {
  MPNOTIFY        Notify;
  HRESULT         hResult;
  ULARGE_INTEGER  TimeStamp;
  MPCALLBACK_TYPE Type;
  union {
    PMPSTATUS_DATA         pStatusData;
    PMPSCAN_DATA           pScanData;
    PMPCLEAN_DATA          pCleanData;
    PMPCLEAN_PRECHECK_DATA pPrecheckData;
    PMPTHREAT_DATA         pThreatData;
    PMPSIGUPDATE_DATA      pSigUpdateData;
    PMPSAMPLE_DATA         pSampleData;
    PMPRESERVED_DATA       pReservedData;
    PMPCONFIGURATION_DATA  pConfigurationData;
    PMPFASTPATH_DATA       pFastPathData;
    PMPEXPIRATION_DATA     pExpirationData;
    PMPNIS_PRIVATE_DATA    pNISPrivateData;
    PMPHEALTH_DATA         pHealthData;
    PMPENDOFLIFE_DATA      pEndOfLifeData;
    PMPMALWARETOAST_DATA   pMalwareToastData;
  } Data;
} MPCALLBACK_DATA, *PMPCALLBACK_DATA;
```



## Members

<dl> <dt>

**Notify**
</dt> <dd>

Type: **[**MPNOTIFY**](mpnotify.md)**

</dd> <dd>

Change notification to report.

</dd> <dt>

**hResult**
</dt> <dd>

Type: **HRESULT**

</dd> <dd>

Error code, in case of an internal failure.

</dd> <dt>

**TimeStamp**
</dt> <dd>

Type: **ULARGE\_INTEGER**

</dd> <dd>

Current timestamp.

</dd> <dt>

**Type**
</dt> <dd>

Type: **[**MPCALLBACK\_TYPE**](mpcallback-type.md)**

</dd> <dd>

Callback special data type.

</dd> <dt>

**Data**
</dt> <dd>

Callback special data. The pointer to the appropriate structure depends on the value of **Type**.

<dl> <dt>

**pStatusData**
</dt> <dd>

Type: **PMPSTATUS\_DATA**

</dd> <dd>

When **Type** == **MPCALLBACK\_STATUS**. See [**MPSTATUS\_DATA**](mpstatus-data.md).

</dd> <dt>

**pScanData**
</dt> <dd>

Type: **PMPSCAN\_DATA**

</dd> <dd>

When **Type** == **MPCALLBACK\_SCAN**. See [**MPSCAN\_DATA**](mpscan-data.md).

</dd> <dt>

**pCleanData**
</dt> <dd>

Type: **PMPCLEAN\_DATA**

</dd> <dd>

When **Type** == **MPCALLBACK\_CLEAN**. See [**MPCLEAN\_DATA**](mpclean-data.md).

</dd> <dt>

**pPrecheckData**
</dt> <dd>

Type: **PMPCLEAN\_PRECHECK\_DATA**

</dd> <dd>

When **Type** == **MPCALLBACK\_PRECHECK**. See [**MPCLEAN\_PRECHECK\_DATA**](mpclean-precheck-data.md).

</dd> <dt>

**pThreatData**
</dt> <dd>

Type: **PMPTHREAT\_DATA**

</dd> <dd>

When **Type** == **MPCALLBACK\_THREAT**. See [**MPTHREAT\_DATA**](mpthreat-data.md).

</dd> <dt>

**pSigUpdateData**
</dt> <dd>

Type: **PMPSIGUPDATE\_DATA**

</dd> <dd>

When **Type** == **MPCALLBACK\_SIGUPDATE**. See [**MPSIGUPDATE\_DATA**](mpsigupdate-data.md).

</dd> <dt>

**pSampleData**
</dt> <dd>

Type: **PMPSAMPLE\_DATA**

</dd> <dd>

When **Type** == **MPCALLBACK\_SAMPLE**. See [**MPSAMPLE\_DATA**](mpsample-data.md).

</dd> <dt>

**pReservedData**
</dt> <dd>

Type: **PMPRESERVED\_DATA**

</dd> <dd>

When **Type** == **MPCALLBACK\_RESERVED**. See [**MPRESERVED\_DATA**](mpreserved-data.md).

</dd> <dt>

**pConfigurationData**
</dt> <dd>

Type: **PMPCONFIGURATION\_DATA**

</dd> <dd>

When **Type** == **MPCALLBACK\_CONFIGURATION\_NOTIFICATION**. See [**MPCONFIGURATION\_DATA**](mpconfiguration-data.md).

</dd> <dt>

**pFastPathData**
</dt> <dd>

Type: **PMPFASTPATH\_DATA**

</dd> <dd>

When **Type** == **MPCALLBACK\_FASTPATH**. See [**MPFASTPATH\_DATA**](mpfastpath-data.md).

</dd> <dt>

**pExpirationData**
</dt> <dd>

Type: **PMPEXPIRATION\_DATA**

</dd> <dd>

When **Type** == **MPCALLBACK\_PRODUCT\_EXPIRATION**. See [**MPEXPIRATION\_DATA**](mpexpiration-data.md).

</dd> <dt>

**pNISPrivateData**
</dt> <dd>

Type: **PMPNIS\_PRIVATE\_DATA**

</dd> <dd>

When **Type** == **MPCALLBACK\_NIS\_PRIVATE**. See [**MPNIS\_PRIVATE\_DATA**](mpnis-private-data.md).

</dd> <dt>

**pHealthData**
</dt> <dd>

Type: **PMPHEALTH\_DATA**

</dd> <dd>

When **Type** == **MPCALLBACK\_HEALTH**. See [**MPHEALTH\_DATA**](mphealth-data.md).

</dd> <dt>

**pEndOfLifeData**
</dt> <dd>

Type: **PMPENDOFLIFE\_DATA**

</dd> <dd>

When **Type** == **MPCALLBACK\_ENDOFLIFE**. See [**MPENDOFLIFE\_DATA**](mpendoflife-data.md).

</dd> <dt>

**pMalwareToastData**
</dt> <dd>

Type: **PMPMALWARETOAST\_DATA**

</dd> <dd>

When **Type** == **MPCALLBACK\_MALWARETOAST**. See [**MPMALWARETOAST\_DATA**](mpmalwaretoast-data.md).

</dd> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>MpClient.h</dt> </dl> |



## See also

<dl> <dt>

[**MPCALLBACK\_TYPE**](mpcallback-type.md)
</dt> <dt>

[**MPCLEAN\_DATA**](mpclean-data.md)
</dt> <dt>

[**MPCLEAN\_PRECHECK\_DATA**](mpclean-precheck-data.md)
</dt> <dt>

[**MPCONFIGURATION\_DATA**](mpconfiguration-data.md)
</dt> <dt>

[**MPENDOFLIFE\_DATA**](mpendoflife-data.md)
</dt> <dt>

[**MPEXPIRATION\_DATA**](mpexpiration-data.md)
</dt> <dt>

[**MPFASTPATH\_DATA**](mpfastpath-data.md)
</dt> <dt>

[**MPHEALTH\_DATA**](mphealth-data.md)
</dt> <dt>

[**MPMALWARETOAST\_DATA**](mpmalwaretoast-data.md)
</dt> <dt>

[**MPNIS\_PRIVATE\_DATA**](mpnis-private-data.md)
</dt> <dt>

[**MPNOTIFY**](mpnotify.md)
</dt> <dt>

[**MPRESERVED\_DATA**](mpreserved-data.md)
</dt> <dt>

[**MPSAMPLE\_DATA**](mpsample-data.md)
</dt> <dt>

[**MPSCAN\_DATA**](mpscan-data.md)
</dt> <dt>

[**MPSIGUPDATE\_DATA**](mpsigupdate-data.md)
</dt> <dt>

[**MPSTATUS\_DATA**](mpstatus-data.md)
</dt> <dt>

[**MPTHREAT\_DATA**](mpthreat-data.md)
</dt> </dl>

 

 





