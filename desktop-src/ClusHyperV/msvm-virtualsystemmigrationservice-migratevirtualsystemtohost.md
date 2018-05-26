---
title: MigrateVirtualSystemToHost method of the Msvm\_VirtualSystemMigrationService class
description: Migrates a virtual system or the storage of a virtual system to a destination host specified by a hostname.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 721f129f-c6e5-4927-adf7-6cd397768498
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MigrateVirtualSystemToHost method
- MigrateVirtualSystemToHost method, Msvm_VirtualSystemMigrationService class
- Msvm_VirtualSystemMigrationService class, MigrateVirtualSystemToHost method
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemMigrationService.MigrateVirtualSystemToHost
api_location:
- VMMS.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MigrateVirtualSystemToHost method of the Msvm\_VirtualSystemMigrationService class

Migrates a virtual system or the storage of a virtual system to a destination host specified by a hostname.

## Syntax


```mof
uint32 MigrateVirtualSystemToHost(
  [in]  CIM_ComputerSystem REF ComputerSystem,
  [in]  string                 DestinationHost,
  [in]  string                 MigrationSettingData,
  [in]  string                 NewSystemSettingData,
  [in]  string                 NewResourceSettingData[],
  [out] CIM_ConcreteJob    REF Job
);
```



## Parameters

<dl> <dt>

*ComputerSystem* \[in\]
</dt> <dd>

A reference to an instance of the [**Msvm\_ComputerSystem**](msvm-computersystem.md) class that represents the virtual computer system to migrate.

</dd> <dt>

*DestinationHost* \[in\]
</dt> <dd>

The name of the host system for the migration. The format of this name is specified by the **DestinationHostFormatsSupported** property of the [**Msvm\_VirtualSystemMigrationCapabilities**](https://msdn.microsoft.com/library/windows/desktop/hh859779) class associated with this class.

</dd> <dt>

*MigrationSettingData* \[in\]
</dt> <dd>

An embedded instance of the [**Msvm\_VirtualSystemMigrationSettingData**](https://msdn.microsoft.com/library/windows/desktop/hh859784) class that represents settings for the migration operation.

</dd> <dt>

*NewSystemSettingData* \[in\]
</dt> <dd>

An embedded instance of the [**Msvm\_VirtualSystemSettingData**](msvm-virtualsystemsettingdata.md) class that represents new properties applicable to the virtual system after it is migrated.

</dd> <dt>

*NewResourceSettingData* \[in\]
</dt> <dd>

An array of strings that contain an embedded instance of the [**Msvm\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/windows/desktop/hh850200) class that represents the new properties applicable to virtual resources of the virtual system after it is migrated.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

A reference to an optional job for the operation if the operation is run asynchronously.

</dd> </dl>

## Return value

This method returns one of the following values.

<dl> <dt>

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



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**Msvm\_VirtualSystemMigrationService**](msvm-virtualsystemmigrationservice.md)
</dt> </dl>

 

 





