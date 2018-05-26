---
title: GetServiceAccessPoints method of the CIM\_ReplicationService class
description: Get (or start a job to get) ServiceAccessPoints associated with a peer system. If a job is started, once the job completes, examine the AffectedJobElement associations for the peer systems ServiceAccessPoints.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: bc760873-3853-4b42-be2c-7a4b5f6fb09c
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetServiceAccessPoints method iSCSI Software Target API
- GetServiceAccessPoints method iSCSI Software Target API , CIM_ReplicationService class
- CIM_ReplicationService class iSCSI Software Target API , GetServiceAccessPoints method
topic_type:
- apiref
api_name:
- CIM_ReplicationService.GetServiceAccessPoints
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetServiceAccessPoints method of the CIM\_ReplicationService class

Get (or start a job to get) ServiceAccessPoints associated with a peer system. If a job is started, once the job completes, examine the AffectedJobElement associations for the peer system's ServiceAccessPoints.

## Syntax


```mof
uint32 GetServiceAccessPoints(
  [in]  CIM_ComputerSystem     REF System,
  [out] CIM_ConcreteJob        REF Job,
  [out] CIM_ServiceAccessPoint REF ServiceAccessPoints[]
);
```



## Parameters

<dl> <dt>

*System* \[in\]
</dt> <dd>

This parameter specifies the peer system.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

Reference to the job (may be NULL if the task completed).

</dd> <dt>

*ServiceAccessPoints* \[out\]
</dt> <dd>

List of ServiceAccessPoints for the supplied System.

</dd> </dl>

## Return value

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Unspecified Error** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Failed** (4)
</dt> <dt>

**Invalid Parameter** (5)
</dt> <dt>

**In Use** (6)
</dt> <dt>

**DMTF Reserved** (7 4095)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Method Reserved** (4097 32767)
</dt> <dt>

**Vendor Specific** (32768 4294967295)
</dt> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

**CIM\_ReplicationService**
</dt> </dl>

 

 





