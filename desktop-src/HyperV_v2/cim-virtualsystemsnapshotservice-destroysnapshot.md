---
description: Destroy an existing virtual system snapshot. This method may as a side effect destroy other snapshots that are dependent on the affected snapshot.
ms.assetid: 69f60d0e-50ef-4a38-ad4b-88534b7fb3f8
title: DestroySnapshot method of the CIM_VirtualSystemSnapshotService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_VirtualSystemSnapshotService.DestroySnapshot
api_type: 
- COM
api_location: 
- vmms.exe
---

# DestroySnapshot method of the CIM\_VirtualSystemSnapshotService class

Destroy an existing virtual system snapshot. This method may as a side effect destroy other snapshots that are dependent on the affected snapshot.

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

A [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md) reference to the affected virtual system snapshot.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

If the operation is long running, then optionally a [**CIM\_ConcreteJob**](cim-concretejob.md) representing the job may be returned.

> [!Note]  
> This parameter was read/write in Windows 8.1.

 

</dd> </dl>

## Return value

Returns a 0 on success; otherwise, returns an error.

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

**DMTF Reserved** (..)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Method Reserved** (4097..32767)
</dt> <dt>

**Vendor Specific** (32768..65535)
</dt> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                                  |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                       |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_VirtualSystemSnapshotService**](cim-virtualsystemsnapshotservice.md)
</dt> </dl>

 

 




