---
title: ApplySnapshot method of the CIM\_VirtualSystemSnapshotService class
description: Applies a virtual system snapshot to the virtual system to the source virtual system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6dfe843b-fac6-491e-9b3c-0dd7c21d2522
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ApplySnapshot method
- ApplySnapshot method, CIM_VirtualSystemSnapshotService class
- CIM_VirtualSystemSnapshotService class, ApplySnapshot method
topic_type:
- apiref
api_name:
- CIM_VirtualSystemSnapshotService.ApplySnapshot
api_location:
- VMMS.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ApplySnapshot method of the CIM\_VirtualSystemSnapshotService class

Applies a virtual system snapshot to the virtual system to the source virtual system.

## Syntax


```mof
uint32 ApplySnapshot(
  [in]  CIM_VirtualSystemSettingData REF Snapshot,
  [out] CIM_ConcreteJob              REF Job
);
```



## Parameters

<dl> <dt>

*Snapshot* \[in\]
</dt> <dd>

A reference to the virtual system snapshot to apply.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

A reference to a job for the operation, when the operation runs for long period of time. The use of a job is optional.

</dd> </dl>

## Return value

The possible return values are.

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Failed** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Invalid Parameter** (4)
</dt> <dt>

**Invalid State** (5)
</dt> <dt>

**Invalid Type** (6)
</dt> <dt>

**DMTF Reserved** (7 4095)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Method Reserved** (4097 32767)
</dt> <dt>

**Vendor Specific** (32768 65535)
</dt> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**CIM\_VirtualSystemSnapshotService**](cim-virtualsystemsnapshotservice.md)
</dt> </dl>

 

 





