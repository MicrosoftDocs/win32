---
title: DestroySnapshot method of the CIM\_VirtualSystemSnapshotService class
description: Deletes a virtual system snapshot. As a side effect, if other snapshots are dependent on this snapshot, this method might also delete the dependent snapshots.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '56880346-46fa-4adc-8324-13403585d6a8'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DestroySnapshot method", "DestroySnapshot method, CIM_VirtualSystemSnapshotService class", "CIM_VirtualSystemSnapshotService class, DestroySnapshot method"]
topic_type:
- apiref
api_name:
- CIM_VirtualSystemSnapshotService.DestroySnapshot
api_location:
- VMMS.exe
api_type:
- COM
---

# DestroySnapshot method of the CIM\_VirtualSystemSnapshotService class

Deletes a virtual system snapshot. As a side effect, if other snapshots are dependent on this snapshot, this method might also delete the dependent snapshots.

## Syntax


```mof
uint32 DestroySnapshot(
  [in]  CIM_VirtualSystemSettingData REF AffectedSnapshot,
  [out] CIM_ConcreteJob              REF Job
);
```



## Parameters

<dl> <dt>

*AffectedSnapshot* \[in\]
</dt> <dd>

Reference to the affected virtual system snapshot.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

A reference to a job for the operation, when the operation runs for long period of time. The use of the job is optional.

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

**DMTF Reserved** (7–4095)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Method Reserved** (4097–32767)
</dt> <dt>

**Vendor Specific** (32768–65535)
</dt> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**CIM\_VirtualSystemSnapshotService**](cim-virtualsystemsnapshotservice.md)
</dt> </dl>

 

 





