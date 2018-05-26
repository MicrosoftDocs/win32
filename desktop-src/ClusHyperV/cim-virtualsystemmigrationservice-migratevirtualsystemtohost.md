---
title: MigrateVirtualSystemToHost method of the CIM\_VirtualSystemMigrationService class
description: Migrates a virtual system to a target host.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e47767c3-f480-4303-8643-35c0f2bd255a
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MigrateVirtualSystemToHost method
- MigrateVirtualSystemToHost method, CIM_VirtualSystemMigrationService class
- CIM_VirtualSystemMigrationService class, MigrateVirtualSystemToHost method
topic_type:
- apiref
api_name:
- CIM_VirtualSystemMigrationService.MigrateVirtualSystemToHost
api_location:
- VMMS.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MigrateVirtualSystemToHost method of the CIM\_VirtualSystemMigrationService class

Migrates a virtual system to a target host.

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

A reference to the source virtual system to migrate.

</dd> <dt>

*DestinationHost* \[in\]
</dt> <dd>

The host system that will receive the migration. The format of this property is specified in the **DestinationHostFormatsSupported** property of the [**CIM\_VirtualSystemMigrationCapabilities**](cim-virtualsystemmigrationcapabilities.md) instance that is associated with the migration operation.

</dd> <dt>

*MigrationSettingData* \[in\]
</dt> <dd>

An embedded instance of the [**CIM\_VirtualSystemMigrationSettingData**](cim-virtualsystemmigrationsettingdata.md) class that represents the settings for the migration operation.

</dd> <dt>

*NewSystemSettingData* \[in\]
</dt> <dd>

An embedded instance of the [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md) class that represents new properties for the virtual system after migration is complete.

</dd> <dt>

*NewResourceSettingData* \[in\]
</dt> <dd>

Array that contains embedded instances of the [**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md) class that represents new properties for virtual resources of the virtual system after migration is complete.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

If the operation is to run asynchronously, this parameter will return a job for the operation.

</dd> </dl>

## Return value

The possible return values are:

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Failed** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Invalid Parameter** (4)
</dt> <dt>

**Invalid State** (5)
</dt> <dt>

**Incompatible Parameters** (6)
</dt> <dt>

**DMTF Reserved** (7 4095)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Method Reserved** (4097 32767)
</dt> <dt>

**Vendor Specific** (32768 65535)
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

[**CIM\_VirtualSystemMigrationService**](cim-virtualsystemmigrationservice.md)
</dt> </dl>

 

 





