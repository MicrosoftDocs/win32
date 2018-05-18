---
title: CheckVirtualSystemIsMigratableToSystem method of the CIM\_VirtualSystemMigrationService class
description: Verifies whether a pending virtual system migration to a system is likely to succeed.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '05a8c30a-7149-4d3c-8dff-32f8fa6981c2'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CheckVirtualSystemIsMigratableToSystem method", "CheckVirtualSystemIsMigratableToSystem method, CIM_VirtualSystemMigrationService class", "CIM_VirtualSystemMigrationService class, CheckVirtualSystemIsMigratableToSystem method"]
topic_type:
- apiref
api_name:
- CIM_VirtualSystemMigrationService.CheckVirtualSystemIsMigratableToSystem
api_location:
- VMMS.exe
api_type:
- COM
---

# CheckVirtualSystemIsMigratableToSystem method of the CIM\_VirtualSystemMigrationService class

Verifies whether a pending virtual system migration to a system is likely to succeed.

> [!Note]  
> Due to dynamic resource availability, this method does not guarantee that the pending migration will always succeed.

 

## Syntax


```mof
uint32 CheckVirtualSystemIsMigratableToSystem(
  [in]  CIM_ComputerSystem REF ComputerSystem,
  [in]  CIM_System         REF DestinationSystem,
  [in]  string                 MigrationSettingData,
  [in]  string                 NewSystemSettingData,
  [in]  string                 NewResourceSettingData[],
  [out] boolean                IsMigratable
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

*IsMigratable* \[out\]
</dt> <dd>

**true** if the virtual system can be successfully migrated; otherwise, **false**.

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

**DMTF Reserved** (7–4096)
</dt> <dt>

**Method Reserved** (4097–32767)
</dt> <dt>

**Vendor Specific** (32768–65535)
</dt> </dl>

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

[**CIM\_VirtualSystemMigrationService**](cim-virtualsystemmigrationservice.md)
</dt> </dl>

 

 





