---
title: ModifyServiceSettings method of the Msvm\_VirtualSystemMigrationService class
description: Modifies the setting data for the migration service.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f9970165-b16a-477c-8c70-f5fbdd00cbf7
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ModifyServiceSettings method
- ModifyServiceSettings method, Msvm_VirtualSystemMigrationService class
- Msvm_VirtualSystemMigrationService class, ModifyServiceSettings method
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemMigrationService.ModifyServiceSettings
api_location:
- VMMS.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ModifyServiceSettings method of the Msvm\_VirtualSystemMigrationService class

Modifies the setting data for the migration service.

## Syntax


```mof
uint32 ModifyServiceSettings(
  [in]  string              ServiceSettingData,
  [out] CIM_ConcreteJob REF Job
);
```



## Parameters

<dl> <dt>

*ServiceSettingData* \[in\]
</dt> <dd>

An embedded instance of the [**Msvm\_VirtualSystemManagementServiceSettingData**](msvm-virtualsystemmanagementservicesettingdata.md) class that contains the new service settings.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

A reference to an optional job for the operation if the operation is run asynchronously.

</dd> </dl>

## Return value

This method returns one of the following values.

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

 

 





