---
title: BITS\_JOB\_TRANSFER\_POLICY enumeration
description: The BITS\_JOB\_TRANSFER\_POLICY enumeration defines ID values corresponding to DO properties.
ms.assetid: '4811ADBF-F097-4340-BFF2-52CC9556ACF6'
keywords: ["BITS_JOB_TRANSFER_POLICY enumeration", "BITS_JOB_TRANSFER_POLICY enumeration"]
topic_type:
- apiref
api_name:
- BITS_JOB_TRANSFER_POLICY
api_location:
- deliveryoptimization.h
api_type:
- HeaderDef
---

# BITS\_JOB\_TRANSFER\_POLICY enumeration

The **BITS\_JOB\_TRANSFER\_POLICY** enumeration defines ID values corresponding to DO properties.

## Syntax


```C++
typedef enum _BITS_JOB_TRANSFER_POLICY { 
  BITS_JOB_TRANSFER_POLICY_ALWAYS        = 0x800000ff,
  BITS_JOB_TRANSFER_POLICY_NOT_ROAMING   = 0x8000007f,
  BITS_JOB_TRANSFER_POLICY_NO_SURCHARGE  = 0x8000006f,
  BITS_JOB_TRANSFER_POLICY_STANDARD      = 0x80000067,
  BITS_JOB_TRANSFER_POLICY_UNRESTRICTED  = 0x80000021
} BITS_JOB_TRANSFER_POLICY;
```



## Constants

<dl> <dt>

<span id="BITS_JOB_TRANSFER_POLICY_ALWAYS"></span><span id="bits_job_transfer_policy_always"></span>**BITS\_JOB\_TRANSFER\_POLICY\_ALWAYS**
</dt> <dd>

Specifies that the job will be transferred when connectivity is available, regardless of the cost.

</dd> <dt>

<span id="BITS_JOB_TRANSFER_POLICY_NOT_ROAMING"></span><span id="bits_job_transfer_policy_not_roaming"></span>**BITS\_JOB\_TRANSFER\_POLICY\_NOT\_ROAMING**
</dt> <dd>

Specifies that the job will be transferred when connectivity is available, unless that connectivity is subject to roaming surcharges.

</dd> <dt>

<span id="BITS_JOB_TRANSFER_POLICY_NO_SURCHARGE"></span><span id="bits_job_transfer_policy_no_surcharge"></span>**BITS\_JOB\_TRANSFER\_POLICY\_NO\_SURCHARGE**
</dt> <dd>

Specifies that the job will be transferred only when connectivity is available which is not subject to a surcharge.

</dd> <dt>

<span id="BITS_JOB_TRANSFER_POLICY_STANDARD"></span><span id="bits_job_transfer_policy_standard"></span>**BITS\_JOB\_TRANSFER\_POLICY\_STANDARD**
</dt> <dd>

Specifies that the job will be transferred only when connectivity is available which is neither subject to a surcharge nor near exhaustion.

</dd> <dt>

<span id="BITS_JOB_TRANSFER_POLICY_UNRESTRICTED"></span><span id="bits_job_transfer_policy_unrestricted"></span>**BITS\_JOB\_TRANSFER\_POLICY\_UNRESTRICTED**
</dt> <dd>

Specifies that the job will be transferred only when connectivity is available which does not impose costs or traffic limits.

</dd> </dl>

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server, version 1709 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Deliveryoptimization.h</dt> </dl> |



 

 





