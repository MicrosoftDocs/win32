---
title: ApplyVirtualSystemSnapshot method of the CIM\_VirtualSystemManagementService class
description: Applies the disk state, runtime state, and configuration values for a snapshot to the virtual computer system.
ms.assetid: 9d712c55-e2ea-4cf6-b18b-3b27de0bc9ae
keywords:
- ApplyVirtualSystemSnapshot method Hyper-V
- ApplyVirtualSystemSnapshot method Hyper-V , CIM_VirtualSystemManagementService class
- CIM_VirtualSystemManagementService class Hyper-V , ApplyVirtualSystemSnapshot method
topic_type:
- apiref
api_name:
- CIM_VirtualSystemManagementService.ApplyVirtualSystemSnapshot
api_location:
- Root\virtualization
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ApplyVirtualSystemSnapshot method of the CIM\_VirtualSystemManagementService class

Applies the disk state, runtime state, and configuration values for a snapshot to the virtual computer system.

## Syntax


```mof
uint32 ApplyVirtualSystemSnapshot(
  [in] CIM_ComputerSystem           REF ComputerSystem,
  [in] CIM_VirtualSystemSettingData REF SnapshotSettingData
);
```



## Parameters

<dl> <dt>

*ComputerSystem* \[in\]
</dt> <dd>

A reference to the [**CIM\_ComputerSystem**](https://msdn.microsoft.com/library/aa387219) instance to which the snapshot should be applied.

</dd> <dt>

*SnapshotSettingData* \[in\]
</dt> <dd>

A reference to the [**CIM\_VirtualSystemSettingData**](https://msdn.microsoft.com/library/cc136954) instance that represents the snapshot to be applied.

</dd> </dl>

## Return value

If this method is executed synchronously, it returns 0 if it succeeds. Any other return value indicates an error.

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Failed** (32768)
</dt> <dt>

**Access Denied** (32769)
</dt> <dt>

**Not Supported** (32770)
</dt> <dt>

**Status is unknown** (32771)
</dt> <dt>

**Timeout** (32772)
</dt> <dt>

**Invalid parameter** (32773)
</dt> <dt>

**System is in used** (32774)
</dt> <dt>

**Invalid state for this operation** (32775)
</dt> <dt>

**Incorrect data type** (32776)
</dt> <dt>

**System is not available** (32777)
</dt> <dt>

**Out of memory** (32778)
</dt> </dl>

## Requirements



|                      |                                                                                                      |
|----------------------|------------------------------------------------------------------------------------------------------|
| Namespace<br/> | Root\\virtualization<br/>                                                                      |
| MOF<br/>       | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_VirtualSystemManagementService**](cim-virtualsystemmanagementservice.md)
</dt> </dl>

 

 





