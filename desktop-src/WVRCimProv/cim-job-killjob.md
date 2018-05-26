---
title: KillJob method of the CIM\_Job class
description: Terminates this job and any underlying processes immediately, and removes any associations that contain this job.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c6106812-08f8-418b-b0bd-a567c366f278
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- KillJob method
- KillJob method, CIM_Job class
- CIM_Job class, KillJob method
topic_type:
- apiref
api_name:
- CIM_Job.KillJob
api_location:
- WvrCimProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# KillJob method of the CIM\_Job class

Terminates this job and any underlying processes immediately, and removes any associations that contain this job. This method is deprecated. Instead, use the [**RequestStateChange**](cim-concretejob-requeststatechange.md) method to distinguish between an orderly shutdown and an immediate shutdown without cleanup.

## Syntax


```mof
uint32 KillJob(
  [in] boolean DeleteOnKill
);
```



## Parameters

<dl> <dt>

*DeleteOnKill* \[in\]
</dt> <dd>

Indicates whether the job should be automatically deleted upon termination. This parameter takes precedence over the **DeleteOnCompletion** property.

</dd> </dl>

## Return value

<dl> <dt>

**Success** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Unknown** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Failed** (4)
</dt> <dt>

**Access Denied** (6)
</dt> <dt>

**Not Found** (7)
</dt> <dt>

**DMTF Reserved** (8 32767)
</dt> <dt>

**Vendor Specific** (32768 65535)
</dt> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\StorageReplica<br/>                                       |
| MOF<br/>                      | <dl> <dt>WVRCimProv.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WvrCimProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Job**](cim-job.md)
</dt> </dl>

 

 





