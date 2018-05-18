---
title: MigrateVirtualSystemToSystem method of the Msvm\_VirtualSystemMigrationService class
description: Migrates a virtual system to target system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '3e940c37-8626-4c65-83d2-69311ac516ab'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MigrateVirtualSystemToSystem method", "MigrateVirtualSystemToSystem method, Msvm_VirtualSystemMigrationService class", "Msvm_VirtualSystemMigrationService class, MigrateVirtualSystemToSystem method"]
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemMigrationService.MigrateVirtualSystemToSystem
api_location:
- VMMS.exe
api_type:
- COM
---

# MigrateVirtualSystemToSystem method of the Msvm\_VirtualSystemMigrationService class

Migrates a virtual system to target system.

## Syntax


```mof
uint32 MigrateVirtualSystemToSystem(
  [in]      CIM_ComputerSystem REF ComputerSystem,
  [in]      CIM_System         REF DestinationSystem,
  [in]      string                 MigrationSettingData,
  [in]      string                 NewSystemSettingData,
  [in]      string                 NewResourceSettingData[],
  [in, out] CIM_ComputerSystem REF NewComputerSystem,
  [in, out] CIM_ConcreteJob    REF Job
);
```



## Parameters

<dl> <dt>

*ComputerSystem* \[in\]
</dt> <dd>

A reference to the source virtual system to migrate.

</dd> <dt>

*DestinationSystem* \[in\]
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

*NewComputerSystem* \[in, out\]
</dt> <dd>

Reference to an instance of the CIM\_ComputerSystem class representing the virtual computer system after it has been migrated.

</dd> <dt>

*Job* \[in, out\]
</dt> <dd>

If the operation is to run asynchronously, this parameter will return a job for the operation.

</dd> </dl>

## Return value

The possible return values are:

<dl> <dt>


</dt> <dd>

0

Completed with No Error

</dd> <dt>


</dt> <dd>

1

Not Supported

</dd> <dt>


</dt> <dd>

2

Failed

</dd> <dt>


</dt> <dd>

3

Timeout

</dd> <dt>


</dt> <dd>

4

Invalid Parameter

</dd> <dt>


</dt> <dd>

5

Invalid State

</dd> <dt>


</dt> <dd>

6

Incompatible Parameters

</dd> <dt>


</dt> <dd>

7–4095

DMTF Reserved

</dd> <dt>


</dt> <dd>

4096

Method Parameters Checked - Job Started

</dd> <dt>


</dt> <dd>

4097–32767

Method Reserved

</dd> <dt>


</dt> <dd>

32768–65535

Vendor Specific

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**Msvm\_VirtualSystemMigrationService**](msvm-virtualsystemmigrationservice.md)
</dt> </dl>

 

 





