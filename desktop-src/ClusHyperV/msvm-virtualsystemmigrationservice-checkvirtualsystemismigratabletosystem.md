---
title: CheckVirtualSystemIsMigratableToSystem method of the Msvm\_VirtualSystemMigrationService class
description: Verifies whether a pending virtual system migration to a system is likely to succeed.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f31df329-11e9-41d1-b8bd-fb00b93abf98
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CheckVirtualSystemIsMigratableToSystem method
- CheckVirtualSystemIsMigratableToSystem method, Msvm_VirtualSystemMigrationService class
- Msvm_VirtualSystemMigrationService class, CheckVirtualSystemIsMigratableToSystem method
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemMigrationService.CheckVirtualSystemIsMigratableToSystem
api_location:
- VMMS.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CheckVirtualSystemIsMigratableToSystem method of the Msvm\_VirtualSystemMigrationService class

Verifies whether a pending virtual system migration to a system is likely to succeed.

> [!Note]  
> Due to dynamic resource availability, this method does not guarantee that the pending migration will always succeed.

 

## Syntax


```mof
uint32 CheckVirtualSystemIsMigratableToSystem(
  [in]      CIM_ComputerSystem REF ComputerSystem,
  [in]      CIM_System         REF DestinationSystem,
  [in]      string                 MigrationSettingData,
  [in]      string                 NewSystemSettingData,
  [in]      string                 NewResourceSettingData[],
  [in, out] boolean                IsMigratable
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

A reference to the computer system that will receive the migrated virtual system.

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

*IsMigratable* \[in, out\]
</dt> <dd>

**true** if the virtual system can be successfully migrated; otherwise, **false**.

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

7 4096

DMTF Reserved

</dd> <dt>


</dt> <dd>

4097 32767

Method Reserved

</dd> <dt>


</dt> <dd>

32768 65535

Vendor Specific

</dd> </dl>

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

 

 





