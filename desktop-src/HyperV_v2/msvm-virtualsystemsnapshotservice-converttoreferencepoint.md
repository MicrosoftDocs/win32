---
description: Convert an existing virtual system snapshot to a reference point. The snapshot gets deleted as a side effect. Only recovery snapshots can be converted to reference points.
ms.assetid: c634d749-e18f-4a11-a574-2aee705c0722
title: ConvertToReferencePoint method of the Msvm_VirtualSystemSnapshotService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_VirtualSystemSnapshotService.ConvertToReferencePoint
api_type: 
- COM
api_location: 
- vmms.exe
---

# ConvertToReferencePoint method of the Msvm\_VirtualSystemSnapshotService class

Convert an existing virtual system snapshot to a reference point. The snapshot gets deleted as a side effect. Only recovery snapshots can be converted to reference points.

## Syntax


```mof
uint32 ConvertToReferencePoint(
  [in]      CIM_VirtualSystemSettingData     REF AffectedSnapshot,
  [in]      string                               ReferencePointSettings,
  [in, out] Msvm_VirtualSystemReferencePoint REF ResultingReferencePoint,
  [out]     CIM_ConcreteJob                  REF Job
);
```



## Parameters

<dl> <dt>

*AffectedSnapshot* \[in\]
</dt> <dd>

Reference to the affected virtual system snapshot.

</dd> <dt>

*ReferencePointSettings* \[in\]
</dt> <dd>

Parameter settings.

</dd> <dt>

*ResultingReferencePoint* \[in, out\]
</dt> <dd>

Resulting virtual system reference point

</dd> <dt>

*Job* \[out\]
</dt> <dd>

If the operation is long running, then optionally a job may be returned.

</dd> </dl>

## Return value

Returns a 0 on success; otherwise, returns one of the following values:

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
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                          |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**Msvm\_VirtualSystemSnapshotService**](msvm-virtualsystemsnapshotservice.md)
</dt> </dl>

 

 




