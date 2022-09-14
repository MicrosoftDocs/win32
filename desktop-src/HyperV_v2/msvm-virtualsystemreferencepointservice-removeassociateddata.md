---
description: RemoveAssociatedData method of the Msvm_VirtualSystemReferencePointService class - Removes the data log associated with the reference point.
ms.assetid: b6206bda-c195-4c6f-9b80-508c20b53ce5
title: RemoveAssociatedData method of the Msvm_VirtualSystemReferencePointService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_VirtualSystemReferencePointService.RemoveAssociatedData
api_type: 
- COM
api_location: 
- vmms.exe
---

# RemoveAssociatedData method of the Msvm\_VirtualSystemReferencePointService class

Removes the data log associated with the reference point.

## Syntax


```mof
uint32 RemoveAssociatedData(
  [in]  Msvm_VirtualSystemReferencePoint REF AffectedReferencePoint,
  [out] CIM_ConcreteJob                  REF Job
);
```



## Parameters

<dl> <dt>

*AffectedReferencePoint* \[in\]
</dt> <dd>

A reference to the [**Msvm\_VirtualSystemReferencePoint**](msvm-virtualsystemreferencepoint.md) instance which represents the reference point to be removed.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

An optional parameter for monitoring progress of the operation, which is used if the method could not be executed synchronously. If the operation is executing asynchronously, the return value is 4096.

</dd> </dl>

## Return value

On success, returns a 0 (Complete with No Error), or 4096 (Job Started); otherwise, return an error.

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

**System is in use** (32774)
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



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                          |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**Msvm\_VirtualSystemReferencePointService**](msvm-virtualsystemreferencepointservice.md)
</dt> </dl>

 

 




