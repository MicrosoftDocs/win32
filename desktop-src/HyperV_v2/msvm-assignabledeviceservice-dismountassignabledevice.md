---
description: Dismounts the specified PCI device so that it can be assigned.
ms.assetid: 8ea3bc27-93ba-4db8-a4aa-cdfea225eaa9
title: DismountAssignableDevice method of the Msvm_AssignableDeviceService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_AssignableDeviceService.DismountAssignableDevice
api_type: 
- COM
api_location: 
- vmms.exe
---

# DismountAssignableDevice method of the Msvm\_AssignableDeviceService class

Dismounts the specified PCI device so that it can be assigned.

## Syntax


```mof
uint32 DismountAssignableDevice(
  [in]  string              DismountSettingData,
  [out] string              DismountedDeviceInstancePath,
  [out] CIM_ConcreteJob REF Job
);
```



## Parameters

<dl> <dt>

*DismountSettingData* \[in\]
</dt> <dd>

Embedded instance of a setting data object that specifies the PCI device to dismount.

</dd> <dt>

*DismountedDeviceInstancePath* \[out\]
</dt> <dd>

String containing the device instance path to the dismounted device.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

A reference to the job (can be null if the task is completed).

</dd> </dl>

## Return value

On success, returns 0 or 4096; otherwise, returns an error.

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
</dt> <dt>

**File not found** (32779)
</dt> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1703 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                          |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**Msvm\_AssignableDeviceService**](msvm-assignabledeviceservice.md)
</dt> </dl>

 

 




