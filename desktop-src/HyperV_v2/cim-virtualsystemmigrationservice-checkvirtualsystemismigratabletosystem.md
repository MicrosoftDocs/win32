---
description: "Learn more about: CheckVirtualSystemIsMigratableToSystem method of the CIM_VirtualSystemMigrationService class"
ms.assetid: d3f7c926-804f-4c7c-8964-a8e464155417
title: CheckVirtualSystemIsMigratableToSystem method of the CIM_VirtualSystemMigrationService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_VirtualSystemMigrationService.CheckVirtualSystemIsMigratableToSystem
api_type: 
- COM
api_location: 
- vmms.exe
---

# CheckVirtualSystemIsMigratableToSystem method of the CIM\_VirtualSystemMigrationService class

Method to perform a pre-check to determine whether a virtual system is likely to be successfully migrated to a target system. This method does not guarantee that a subsequent migration will always succeed, due to dynamic resource availability. Return code description:

## Syntax


```mof
uint32 CheckVirtualSystemIsMigratableToSystem(
  [in]  CIM_ComputerSystem REF ComputerSystem,
  [in]  CIM_System         REF DestinationSystem,
  [in]  string                 MigrationSettingData,
  [in]  string                 NewSystemSettingData,
  [in]  string                 NewResourceSettingData[],
  [out] boolean                IsMigratable
);
```



## Parameters

<dl> <dt>

*ComputerSystem* \[in\]
</dt> <dd>

[**CIM\_ComputerSystem**](cim-computersystem.md) instance referencing the source virtual computer system to be migrated.

</dd> <dt>

*DestinationSystem* \[in\]
</dt> <dd>

[**CIM\_System**](cim-system.md) instance referencing the destination system onto which to migrate the virtual system.

</dd> <dt>

*MigrationSettingData* \[in\]
</dt> <dd>

String containing an embedded instance of the [**CIM\_VirtualSystemMigrationSettingData**](cim-virtualsystemmigrationsettingdata.md) class representing migration settings applicable to the migration operation.

</dd> <dt>

*NewSystemSettingData* \[in\]
</dt> <dd>

String containing an embedded instance of the [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md) class representing new properties applicable to the virtual system after it is migrated.

</dd> <dt>

*NewResourceSettingData* \[in\]
</dt> <dd>

Array of strings each containing an embedded instance of the [**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md) class representing new properties applicable to virtual resources in the scope of the virtual system after it is migrated.

</dd> <dt>

*IsMigratable* \[out\]
</dt> <dd>

The migration check result indicating whether or not the virtual system can be successfully migrated.

</dd> </dl>

## Return value

Returns a 0 on success; otherwise, returns an error.



| Return code/value                                                                                                                                                | Description                                                                                                                                                                                                                                                                                                                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**Completed with No Error**</dt> <dt>0</dt> </dl>    | Check performed; result reported through the value of the \[Out\] *IsMigratable* parameter.<br/>                                                                                                                                                                                                                                                                          |
| <dl> <dt>**Not Supported**</dt> <dt>1</dt> </dl>              | Method not supported by implementation. No result reported through the value of the \[Out\] *IsMigratable* parameter.<br/>                                                                                                                                                                                                                                                |
| <dl> <dt>**Failed**</dt> <dt>2</dt> </dl>                     | Check failed for unspecified reasons. No result reported through the value of the \[Out\] *IsMigratable* parameter.<br/>                                                                                                                                                                                                                                                  |
| <dl> <dt>**Timeout**</dt> <dt>3</dt> </dl>                    | Check timed out. No result reported through the value of the \[Out\] *IsMigratable* parameter.<br/>                                                                                                                                                                                                                                                                       |
| <dl> <dt>**Invalid Parameter**</dt> <dt>4</dt> </dl>          | One or more parameters are formally invalid. For example, the value of the *DestinationSystem* parameter does not comprise a valid object path. No result reported through the value of the \[Out\] *IsMigratable* parameter.<br/>                                                                                                                                        |
| <dl> <dt>**Invalid State**</dt> <dt>5</dt> </dl>              | The source virtual system, the source host system or the target host system are in a state that does allow initiation of the requested virtual system migration; this may be a temporary condition. No result reported through the value of the \[Out\] *IsMigratable* parameter.<br/>                                                                                    |
| <dl> <dt>**Incompatible Parameters**</dt> <dt>6</dt> </dl>    | One or more input parameters are incompatible as a set, or with respect to the target host. For example the value of the *NewSettingData* parameter contains properties that are not supported by the target host system identified by the value of the *DestinationSystem* parameter. No result reported through the value of the \[Out\] *IsMigratable* parameter.<br/> |
| <dl> <dt>**DMTF Reserved**</dt> <dt>..</dt> </dl>             |                                                                                                                                                                                                                                                                                                                                                                                 |
| <dl> <dt>**Method Reserved**</dt> <dt>4097..32767</dt> </dl>  |                                                                                                                                                                                                                                                                                                                                                                                 |
| <dl> <dt>**Vendor Specific**</dt> <dt>32768..65535</dt> </dl> |                                                                                                                                                                                                                                                                                                                                                                                 |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                                  |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                       |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_VirtualSystemMigrationService**](cim-virtualsystemmigrationservice.md)
</dt> </dl>

 

 




