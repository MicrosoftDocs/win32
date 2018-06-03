---
title: AddSystemComponentSettings method of the Msvm\_VirtualSystemManagementService class
description: Adds generic settings to a virtual system configuration.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ee9bc8ca-6fac-4db3-aceb-86c06d44b10e
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddSystemComponentSettings method
- AddSystemComponentSettings method, Msvm_VirtualSystemManagementService class
- Msvm_VirtualSystemManagementService class, AddSystemComponentSettings method
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementService.AddSystemComponentSettings
api_location:
- VMMS.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AddSystemComponentSettings method of the Msvm\_VirtualSystemManagementService class

Adds generic settings to a virtual system configuration.

## Syntax


```mof
uint32 AddSystemComponentSettings(
  [in]  Msvm_VirtualSystemSettingData   REF AffectedConfiguration,
  [in]  string                              ComponentSettings[],
  [out] Msvm_SystemComponentSettingData REF ResultingComponentSettings[],
  [out] CIM_ConcreteJob                 REF Job
);
```



## Parameters

<dl> <dt>

*AffectedConfiguration* \[in\]
</dt> <dd>

A [**Msvm\_VirtualSystemSettingData**](msvm-virtualsystemsettingdata.md) reference describing the affected configuration.

</dd> <dt>

*ComponentSettings* \[in\]
</dt> <dd>

A collection of component settings.

</dd> <dt>

*ResultingComponentSettings* \[out\]
</dt> <dd>

On success, contains a collection of Msvm\_ConcreteSettingData references that describe the added component settings.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

A reference to an optional job for the operation if the operation is run asynchronously.

</dd> </dl>

## Return value

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

**DMTF Reserved** (5 4095)
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
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md)
</dt> </dl>

 

 





