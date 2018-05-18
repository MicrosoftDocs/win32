---
title: ModifyVirtualSystem method of the CIM\_VirtualSystemManagementService class
description: Modifies the settings for an existing virtual computer system.
ms.assetid: 'a4e99021-d72d-4d19-82d6-516b1c75efe5'
keywords: ["ModifyVirtualSystem method Hyper-V", "ModifyVirtualSystem method Hyper-V , CIM_VirtualSystemManagementService class", "CIM_VirtualSystemManagementService class Hyper-V , ModifyVirtualSystem method"]
topic_type:
- apiref
api_name:
- CIM_VirtualSystemManagementService.ModifyVirtualSystem
api_location:
- Root\virtualization
api_type:
- COM
---

# ModifyVirtualSystem method of the CIM\_VirtualSystemManagementService class

Modifies the settings for an existing virtual computer system.

## Syntax


```mof
uint32 ModifyVirtualSystem(
  [in]  CIM_ComputerSystem           REF ComputerSystem,
  [in]  string                           SystemSettingData,
  [out] CIM_VirtualSystemSettingData REF ModifiedSettingData,
  [out] CIM_ConcreteJob              REF Job
);
```



## Parameters

<dl> <dt>

*ComputerSystem* \[in\]
</dt> <dd>

A reference to the virtual computer system to be modified.

</dd> <dt>

*SystemSettingData* \[in\]
</dt> <dd>

An embedded instance of the [**CIM\_VirtualSystemSettingData**](https://msdn.microsoft.com/library/cc136954) class that describes the modified setting values for the virtual computer system.

</dd> <dt>

*ModifiedSettingData* \[out\]
</dt> <dd>

A reference to the [**CIM\_VirtualSystemSettingData**](https://msdn.microsoft.com/library/cc136954) instance that represents the object that was modified.

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

 

 





