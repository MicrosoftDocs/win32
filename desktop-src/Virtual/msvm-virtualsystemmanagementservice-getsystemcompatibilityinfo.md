---
title: GetSystemCompatibilityInfo method of the Msvm\_VirtualSystemManagementService class
description: Generates an opaque BLOB of data that contains compatibility information for the specified system.
ms.assetid: 'c21a9de1-e196-444e-ac4d-99a016aec4a6'
keywords: ["GetSystemCompatibilityInfo method Hyper-V", "GetSystemCompatibilityInfo method Hyper-V , Msvm_VirtualSystemManagementService class", "Msvm_VirtualSystemManagementService class Hyper-V , GetSystemCompatibilityInfo method"]
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementService.GetSystemCompatibilityInfo
api_location:
- Root\Virtualization
api_type:
- COM
---

# GetSystemCompatibilityInfo method of the Msvm\_VirtualSystemManagementService class

Generates an opaque BLOB of data that contains compatibility information for the specified system.

## Syntax


```mof
uint32 GetSystemCompatibilityInfo(
  [in]  CIM_ComputerSystem REF ComputerSystem,
  [out] uint8                  CompatibilityInfo[]
);
```



## Parameters

<dl> <dt>

*ComputerSystem* \[in\]
</dt> <dd>

Type: **CIM\_ComputerSystem**

A reference to a [**CIM\_ComputerSystem**](https://msdn.microsoft.com/library/aa387219) class that represents the VM to retrieve compatibility information. If the *ComputerSystem* parameter refers to the hosting computer system, the data returned in the *CompatibilityInfo* parameter can be used to determine whether any of the VMs on the hosting computer system can be quickly migrated to another hosting computer system.

</dd> <dt>

*CompatibilityInfo* \[out\]
</dt> <dd>

Type: **uint8\[\]**

An opaque blob of data that can be passed to the [**CheckSystemCompatibilityInfo**](msvm-virtualsystemmanagementservice-checksystemcompatibilityinfo.md) method on another hosting computer system to confirm compatibility.

</dd> </dl>

## Return value

Type: **uint32**

This method returns one of the following values.



| Return code/value                                                                                                                                                                | Description                                                                                                                                                                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**Completed with No Error**</dt> <dt>0</dt> </dl>                    | The operation completed with no error.<br/>                                                                                                                                                                                                                                                                                                          |
| <dl> <dt>**Method Parameters Checked - Job Started**</dt> <dt>4096</dt> </dl> | The system has started.<br/>                                                                                                                                                                                                                                                                                                                         |
| <dl> <dt>**Failed**</dt> <dt>32768</dt> </dl>                                 | The operation failed.<br/>                                                                                                                                                                                                                                                                                                                           |
| <dl> <dt>**Access Denied**</dt> <dt>32769</dt> </dl>                          | The user does not have the permissions required to complete this operation.<br/>                                                                                                                                                                                                                                                                     |
| <dl> <dt>**Not Supported**</dt> <dt>32770</dt> </dl>                          | The operation is not supported.<br/>                                                                                                                                                                                                                                                                                                                 |
| <dl> <dt>**Status is unknown**</dt> <dt>32771</dt> </dl>                      | The operation failed due to an unknown status.<br/>                                                                                                                                                                                                                                                                                                  |
| <dl> <dt>**Timeout**</dt> <dt>32772</dt> </dl>                                | The operation did not complete due to a time-out.<br/>                                                                                                                                                                                                                                                                                               |
| <dl> <dt>**Invalid parameter**</dt> <dt>32773</dt> </dl>                      | The operation did not complete due to a parameter that is not valid.<br/>                                                                                                                                                                                                                                                                            |
| <dl> <dt>**System is in use**</dt> <dt>32774</dt> </dl>                       | The operation did not complete because a required service is in use.<br/>                                                                                                                                                                                                                                                                            |
| <dl> <dt>**Invalid state for this operation**</dt> <dt>32775</dt> </dl>       | The system represented by the *ComputerSystem* parameter is in a transitional state (for example, Starting, Stopping, Saving) or a snapshot operation is in progress. Please wait for the operation to complete and call the [**GetSystemCompatibilityInfo**](msvm-virtualsystemmanagementservice-getsystemcompatibilityinfo.md) method again.<br/> |
| <dl> <dt>**Incorrect data type**</dt> <dt>32776</dt> </dl>                    | The operation failed due to an incorrect data type.<br/>                                                                                                                                                                                                                                                                                             |
| <dl> <dt>**System is not available**</dt> <dt>32777</dt> </dl>                | The operation failed because a required system service is not available.<br/>                                                                                                                                                                                                                                                                        |
| <dl> <dt>**Out of memory**</dt> <dt>32778</dt> </dl>                          | The operation did not complete because there is insufficient memory available.<br/>                                                                                                                                                                                                                                                                  |



 

## Remarks

The **GetSystemCompatibilityInfo** method is used in conjunction with [**CheckSystemCompatibilityInfo**](msvm-virtualsystemmanagementservice-checksystemcompatibilityinfo.md) to determine whether a quick or live migration of a VM to another hosting computer system is possible without first trying the migration. The compatibility information is dependent on the current **EnabledState** property of the system specified in the *ComputerSystem* parameter. In addition, the compatibility information for a VM may change when a snapshot is applied or the system is restarted. A VM in the Disabled state (**EnabledState** property value of 3) is compatible with more systems than one in the Suspended or Enabled states (**EnabledState** property value of 32769 or 2.)

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
</dt> </dl>

 

 





