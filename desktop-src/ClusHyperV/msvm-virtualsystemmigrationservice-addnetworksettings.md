---
title: AddNetworkSettings method of the Msvm\_VirtualSystemMigrationService class
description: Adds migration network settings for the virtual system migration service.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'd0abb18f-0152-4d1a-b992-ac58f85b080f'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["AddNetworkSettings method", "AddNetworkSettings method, Msvm_VirtualSystemMigrationService class", "Msvm_VirtualSystemMigrationService class, AddNetworkSettings method"]
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemMigrationService.AddNetworkSettings
api_location:
- VMMS.exe
api_type:
- COM
---

# AddNetworkSettings method of the Msvm\_VirtualSystemMigrationService class

Adds migration network settings for the virtual system migration service.

## Syntax


```mof
uint32 AddNetworkSettings(
  [in]  string              NetworkSettings[],
  [out] CIM_ConcreteJob REF Job
);
```



## Parameters

<dl> <dt>

*NetworkSettings* \[in\]
</dt> <dd>

An array that contains embedded instances of [**Msvm\_VirtualSystemMigrationNetworkSettingData**](https://msdn.microsoft.com/library/windows/desktop/hh859780) that contain the network settings to add.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

A reference to an optional job for the operation if the operation is run asynchronously.

</dd> </dl>

## Return value

The possible return values are:

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
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**Msvm\_VirtualSystemMigrationService**](msvm-virtualsystemmigrationservice.md)
</dt> </dl>

 

 





