---
title: CreateSnapshot method of the CIM\_VirtualSystemSnapshotService class
description: Creates a snapshot of a virtual system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 62772841-b8d8-4a32-8dc7-e8d6ee1469fe
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CreateSnapshot method
- CreateSnapshot method, CIM_VirtualSystemSnapshotService class
- CIM_VirtualSystemSnapshotService class, CreateSnapshot method
topic_type:
- apiref
api_name:
- CIM_VirtualSystemSnapshotService.CreateSnapshot
api_location:
- VMMS.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CreateSnapshot method of the CIM\_VirtualSystemSnapshotService class

Creates a snapshot of a virtual system.

## Syntax


```mof
uint32 CreateSnapshot(
  [in]      CIM_ComputerSystem           REF AffectedSystem,
  [in]      string                           SnapshotSettings,
  [in]      uint16                           SnapshotType,
  [in, out] CIM_VirtualSystemSettingData REF ResultingSnapshot,
  [out]     CIM_ConcreteJob              REF Job
);
```



## Parameters

<dl> <dt>

*AffectedSystem* \[in\]
</dt> <dd>

A reference to the virtual system that is the source of the snapshot.

</dd> <dt>

*SnapshotSettings* \[in\]
</dt> <dd>

The parameter settings for the snapshot.

</dd> <dt>

*SnapshotType* \[in\]
</dt> <dd>

The requested snapshot type.

The possible values are.

<dt>

<span id="Full_Snapshot"></span><span id="full_snapshot"></span><span id="FULL_SNAPSHOT"></span>

**Full Snapshot** (2)


</dt> <dd></dd> <dt>

<span id="Disk_Snapshot"></span><span id="disk_snapshot"></span><span id="DISK_SNAPSHOT"></span>

**Disk Snapshot** (3)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>4 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 65535</dd> </dl> </dd> <dt>

*ResultingSnapshot* \[in, out\]
</dt> <dd>

A reference to the new virtual system snapshot.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

A reference to a job for the operation, when the operation runs for long period of time. The use of the job is optional.

If a job is created, the [**CIM\_AffectedJobElement**](cim-affectedjobelement.md) class must be used to associate the job with the [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md) instance that represents the new snapshot.

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
| Header<br/>                   | <dl> <dt>Dbdaoint.h</dt> </dl>                  |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**CIM\_VirtualSystemSnapshotService**](cim-virtualsystemsnapshotservice.md)
</dt> </dl>

 

 





