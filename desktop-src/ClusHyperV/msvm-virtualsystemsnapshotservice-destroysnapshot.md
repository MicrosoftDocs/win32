---
title: DestroySnapshot method of the Msvm\_VirtualSystemSnapshotService class
description: Deletes a virtual system snapshot.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6d34fd04-d888-4b97-a9d0-985763f044cd
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DestroySnapshot method
- DestroySnapshot method, Msvm_VirtualSystemSnapshotService class
- Msvm_VirtualSystemSnapshotService class, DestroySnapshot method
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemSnapshotService.DestroySnapshot
api_location:
- VMMS.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DestroySnapshot method of the Msvm\_VirtualSystemSnapshotService class

Deletes a virtual system snapshot.

## Syntax


```mof
uint32 DestroySnapshot(
  [in]  CIM_VirtualSystemSettingData REF AffectedSnapshot,
  [out] CIM_ConcreteJob              REF Job
);
```



## Parameters

<dl> <dt>

*AffectedSnapshot* \[in\]
</dt> <dd>

A reference to a [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md) object that represents the virtual machine snapshot to delete.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

A reference to an optional job for the operation if the operation is run asynchronously.

</dd> </dl>

## Return value

This method returns one of the following values.

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

[**Msvm\_VirtualSystemSnapshotService**](msvm-virtualsystemsnapshotservice.md)
</dt> </dl>

 

 





