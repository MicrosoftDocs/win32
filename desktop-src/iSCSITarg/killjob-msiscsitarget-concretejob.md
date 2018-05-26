---
title: KillJob method of the MSISCSITARGET\_ConcreteJob class
description: Terminates this job and any underlying processes immediately, and removes any associations that contain this job.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 75cc417f-56fb-49c1-9725-d58fad42190c
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- KillJob method iSCSI Software Target API
- KillJob method iSCSI Software Target API , MSISCSITARGET_ConcreteJob class
- MSISCSITARGET_ConcreteJob class iSCSI Software Target API , KillJob method
topic_type:
- apiref
api_name:
- MSISCSITARGET_ConcreteJob.KillJob
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# KillJob method of the MSISCSITARGET\_ConcreteJob class

Terminates this job and any underlying processes immediately, and removes any associations that contain this job. This method is deprecated. Instead, use the [**RequestStateChange**](requeststatechange-msiscsitarget-concretejob.md) method to distinguish between an orderly shutdown and an immediate shutdown without cleanup.

This method is inherited from the [**CIM\_Job**](https://msdn.microsoft.com/library/aa387873) class.

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

**Access Denied** (5)
</dt> <dt>

**Not Found** (6)
</dt> <dt>

**DMTF Reserved** (7 32767)
</dt> <dt>

**Vendor Specific** (32768 65535)
</dt> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SmIScsiTargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSISCSITARGET\_ConcreteJob**](msiscsitarget-concretejob.md)
</dt> </dl>

 

 





