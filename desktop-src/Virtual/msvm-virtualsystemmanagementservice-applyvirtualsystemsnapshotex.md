---
title: ApplyVirtualSystemSnapshotEx method of the Msvm\_VirtualSystemManagementService class
description: Applies the disk state, run-time state, and configuration values for a snapshot to the virtual computer system.
ms.assetid: '84dae118-7390-4ebc-8703-2843b470abf5'
keywords: ["ApplyVirtualSystemSnapshotEx method Hyper-V", "ApplyVirtualSystemSnapshotEx method Hyper-V , Msvm_VirtualSystemManagementService class", "Msvm_VirtualSystemManagementService class Hyper-V , ApplyVirtualSystemSnapshotEx method"]
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementService.ApplyVirtualSystemSnapshotEx
api_location:
- Root\Virtualization
api_type:
- COM
---

# ApplyVirtualSystemSnapshotEx method of the Msvm\_VirtualSystemManagementService class

Applies the disk state, run-time state, and configuration values for a snapshot to the virtual computer system. This information serves as the starting point for the virtual computer system when it is next activated. Any disk state, run-time state, or configuration values currently associated with the virtual computer system will be lost.

## Syntax


```mof
uint32 ApplyVirtualSystemSnapshotEx(
  [in]  CIM_ComputerSystem           REF ComputerSystem,
  [in]  CIM_VirtualSystemSettingData REF SnapshotSettingData,
  [out] CIM_ConcreteJob              REF Job
);
```



## Parameters

<dl> <dt>

*ComputerSystem* \[in\]
</dt> <dd>

Type: **CIM\_ComputerSystem**

A reference to the [**CIM\_ComputerSystem**](https://msdn.microsoft.com/library/aa387219) instance to which the snapshot should be applied.

</dd> <dt>

*SnapshotSettingData* \[in\]
</dt> <dd>

Type: **CIM\_VirtualSystemSettingData**

A reference to the [**CIM\_VirtualSystemSettingData**](https://msdn.microsoft.com/library/cc136954) instance that represents the snapshot to be applied.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

Type: **CIM\_ConcreteJob**

An optional reference that is returned if the operation is executed asynchronously. If present, the returned reference to an instance of [**CIM\_ConcreteJob**](https://msdn.microsoft.com/library/cc136808) can be used to monitor progress and obtain the result of the method.

</dd> </dl>

## Return value

Type: **uint32**

If this method is executed synchronously, it returns 0 if it succeeds. If this method is executed asynchronously, it returns 4096 and the *Job* output parameter can be used to track the progress of the asynchronous operation. Any other return value indicates an error. The return value can be one of the following values.

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

## Remarks

Access to the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                                    |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012<br/>                                                                       |
| Namespace<br/>                | Root\\Virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md)
</dt> <dt>

[**ApplySnapshot (V2)**](https://msdn.microsoft.com/library/windows/desktop/hh850022)
</dt> </dl>

 

 





