---
title: ApplySnapshot method of the Msvm\_VirtualSystemSnapshotService class
description: Applies a virtual machine snapshot to the virtual machine that it was created from.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 65689801-c739-49a7-81dd-7654d6b1ae9f
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ApplySnapshot method
- ApplySnapshot method, Msvm_VirtualSystemSnapshotService class
- Msvm_VirtualSystemSnapshotService class, ApplySnapshot method
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemSnapshotService.ApplySnapshot
api_location:
- VMMS.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ApplySnapshot method of the Msvm\_VirtualSystemSnapshotService class

Applies a virtual machine snapshot to the virtual machine that it was created from.

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

A reference to the [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md) instance that represents the virtual machine snapshot to apply.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

A reference to an optional job for the operation if the operation is run asynchronously.

</dd> </dl>

## Return value

The possible return values are:

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

 

 





