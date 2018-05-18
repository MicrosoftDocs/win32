---
title: ExportVirtualSystem method of the CIM\_VirtualSystemManagementService class
description: Beginning with Windows Server 2008 R2 this method is deprecated.
ms.assetid: '299398da-2bfa-4ccd-8746-86d9af272267'
keywords: ["ExportVirtualSystem method Hyper-V", "ExportVirtualSystem method Hyper-V , CIM_VirtualSystemManagementService class", "CIM_VirtualSystemManagementService class Hyper-V , ExportVirtualSystem method"]
topic_type:
- apiref
api_name:
- CIM_VirtualSystemManagementService.ExportVirtualSystem
api_location:
- Root\virtualization
api_type:
- COM
---

# ExportVirtualSystem method of the CIM\_VirtualSystemManagementService class

Beginning with Windows Server 2008 R2 this method is deprecated.

## Syntax


```mof
uint32 ExportVirtualSystem(
  [in]  CIM_ComputerSystem REF ComputerSystem,
  [in]  boolean                CopyVmState,
  [in]  string                 ExportDirectory,
  [out] CIM_ConcreteJob    REF Job
);
```



## Parameters

<dl> <dt>

*ComputerSystem* \[in\]
</dt> <dd>

A reference to a [**CIM\_ComputerSystem**](https://msdn.microsoft.com/library/aa387219) that represents the virtual computer system to be exported.

</dd> <dt>

*CopyVmState* \[in\]
</dt> <dd>

Indicates whether the state, such as virtual hard disks, saved state files, and memory content files, will be exported.

</dd> <dt>

*ExportDirectory* \[in\]
</dt> <dd>

The fully qualified path of the directory to which the virtual computer system is to be exported. This directory can be reused for exporting multiple virtual machines. This method places each virtual computer system definition in a separate subdirectory under this path.

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



|                      |                                                                                                      |
|----------------------|------------------------------------------------------------------------------------------------------|
| Namespace<br/> | Root\\virtualization<br/>                                                                      |
| MOF<br/>       | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_VirtualSystemManagementService**](cim-virtualsystemmanagementservice.md)
</dt> </dl>

 

 





