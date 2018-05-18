---
title: CheckVirtualSystemIsMigratableToHost method of the Msvm\_VirtualSystemMigrationService class
description: Verifies whether a pending virtual system migration to a host is likely to succeed.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '1950557f-a796-4489-a7f1-d709d2baea5c'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CheckVirtualSystemIsMigratableToHost method", "CheckVirtualSystemIsMigratableToHost method, Msvm_VirtualSystemMigrationService class", "Msvm_VirtualSystemMigrationService class, CheckVirtualSystemIsMigratableToHost method"]
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemMigrationService.CheckVirtualSystemIsMigratableToHost
api_location:
- VMMS.exe
api_type:
- COM
---

# CheckVirtualSystemIsMigratableToHost method of the Msvm\_VirtualSystemMigrationService class

Verifies whether a pending virtual system migration to a host is likely to succeed.

> [!Note]  
> Due to dynamic resource availability, this method does not guarantee that the pending migration will always succeed.

 

## Syntax


```mof
uint32 CheckVirtualSystemIsMigratableToHost(
  [in]      CIM_ComputerSystem REF ComputerSystem,
  [in]      string                 DestinationHost,
  [in]      string                 MigrationSettingData,
  [in]      string                 NewSystemSettingData,
  [in]      string                 NewResourceSettingData[],
  [in, out] boolean                IsMigratable
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

*IsMigratable* \[in, out\]
</dt> <dd>

**true** if the virtual system can be successfully migrated to the host; otherwise, **false**.

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

7–4096

DMTF Reserved

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

 

 





