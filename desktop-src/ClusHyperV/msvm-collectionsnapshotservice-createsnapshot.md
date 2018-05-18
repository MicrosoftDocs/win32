---
title: CreateSnapshot method of the Msvm\_CollectionSnapshotService class
description: Creates a snapshot of a virtual system collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '929fc76a-baf2-44bb-98f4-6d3784beacb0'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CreateSnapshot method", "CreateSnapshot method, Msvm_CollectionSnapshotService class", "Msvm_CollectionSnapshotService class, CreateSnapshot method"]
topic_type:
- apiref
api_name:
- Msvm_CollectionSnapshotService.CreateSnapshot
api_location:
- VMMS.exe
api_type:
- COM
---

# CreateSnapshot method of the Msvm\_CollectionSnapshotService class

Creates a snapshot of a virtual system collection.

## Syntax


```mof
uint32 CreateSnapshot(
  [in]      CIM_CollectionOfMSEs REF Collection,
  [in]      string                   SnapshotSettings,
  [in]      uint16                   SnapshotType,
  [in, out] CIM_Collection       REF ResultingSnapshotCollection,
  [out]     CIM_ConcreteJob      REF Job
);
```



## Parameters

<dl> <dt>

*Collection* \[in\]
</dt> <dd>

Reference to the affected virtual system collection.

</dd> <dt>

*SnapshotSettings* \[in\]
</dt> <dd>

The settings for the snapshot.

</dd> <dt>

*SnapshotType* \[in\]
</dt> <dd>

The snapshot type.

The possible values are:

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Standard_Snapshot"></span><span id="standard_snapshot"></span><span id="STANDARD_SNAPSHOT"></span>

**Standard Snapshot** (1)


</dt> <dd></dd> <dt>

<span id="Recovery_Snapshot"></span><span id="recovery_snapshot"></span><span id="RECOVERY_SNAPSHOT"></span>

**Recovery Snapshot** (2)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>3–32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768–65535</dd> </dl> </dd> <dt>

*ResultingSnapshotCollection* \[in, out\]
</dt> <dd>

A reference to the new snapshot.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

An optional reference that is returned if the operation is executed asynchronously. If present, the returned reference to an instance of CIM\_ConcreteJob can be used to monitor progress and to obtain the result of the method.

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
| Header<br/>                   | <dl> <dt>Dbdaoint.h</dt> </dl>                  |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**Msvm\_CollectionSnapshotService**](msvm-collectionsnapshotservice.md)
</dt> </dl>

 

 





