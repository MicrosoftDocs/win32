---
description: Mounts the specified PCI device so that it can be used by the host computer system.
ms.assetid: 2a07174e-c221-4c04-81b8-5968aa67e235
title: MountAssignableDevice method of the Msvm_AssignableDeviceService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_AssignableDeviceService.MountAssignableDevice
api_type: 
- COM
api_location: 
- vmms.exe
---

# MountAssignableDevice method of the Msvm\_AssignableDeviceService class

Mounts the specified PCI device so that it can be used by the host computer system.

## Syntax


```mof
uint32 MountAssignableDevice(
  [in]  string              DeviceInstancePath,
  [in]  string              DeviceLocationPath,
  [out] string              MountedDeviceInstancePath,
  [out] CIM_ConcreteJob REF Job
);
```



## Parameters

<dl> <dt>

*DeviceInstancePath* \[in\]
</dt> <dd>

String containing the device instance path to a device.

</dd> <dt>

*DeviceLocationPath* \[in\]
</dt> <dd>

String containing the device location path to a device.

</dd> <dt>

*MountedDeviceInstancePath* \[out\]
</dt> <dd>

String containing the device instance path to the mounted device.

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

 

 




