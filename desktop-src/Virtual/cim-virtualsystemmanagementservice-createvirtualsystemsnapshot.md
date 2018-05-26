---
title: CreateVirtualSystemSnapshot method of the CIM\_VirtualSystemManagementService class
description: Creates a snapshot of a virtual computer system.
ms.assetid: ac6f2340-ec01-4686-9587-015e5c607ddc
keywords:
- CreateVirtualSystemSnapshot method Hyper-V
- CreateVirtualSystemSnapshot method Hyper-V , CIM_VirtualSystemManagementService class
- CIM_VirtualSystemManagementService class Hyper-V , CreateVirtualSystemSnapshot method
topic_type:
- apiref
api_name:
- CIM_VirtualSystemManagementService.CreateVirtualSystemSnapshot
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

# CreateVirtualSystemSnapshot method of the CIM\_VirtualSystemManagementService class

Creates a snapshot of a virtual computer system.

## Syntax


```mof
uint32 CreateVirtualSystemSnapshot(
  [in]  CIM_ComputerSystem           REF SourceSystem,
  [out] CIM_VirtualSystemSettingData REF SnapshotSettingData,
  [out] CIM_ConcreteJob              REF Job
);
```



## Parameters

<dl> <dt>

*SourceSystem* \[in\]
</dt> <dd>

A reference to the virtual computer system to be snapshotted.

</dd> <dt>

*SnapshotSettingData* \[out\]
</dt> <dd>

The [**CIM\_VirtualSystemSettingData**](https://msdn.microsoft.com/library/cc136954) instance that was created to represent the snapshot.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

An optional reference that is returned if the operation is executed asynchronously. If present, the returned reference to an instance of [**CIM\_ConcreteJob**](https://msdn.microsoft.com/library/cc136808) can be used to monitor progress and to obtain the result of the method.

</dd> </dl>

## Return value

If this method is executed synchronously, it returns 0 if it succeeds. If this method is executed asynchronously, it returns 4096 and the *Job* output parameter can be used to track the progress of the asynchronous operation. Any other return value indicates an error.

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

 

 





