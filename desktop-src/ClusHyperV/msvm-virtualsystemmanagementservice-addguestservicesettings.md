---
title: AddGuestServiceSettings method of the Msvm\_VirtualSystemManagementService class
description: Adds guest service settings to a virtual system configuration.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2dab8fd5-a84a-4468-8cd4-55e46ed0712f
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddGuestServiceSettings method
- AddGuestServiceSettings method, Msvm_VirtualSystemManagementService class
- Msvm_VirtualSystemManagementService class, AddGuestServiceSettings method
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementService.AddGuestServiceSettings
api_location:
- VMMS.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AddGuestServiceSettings method of the Msvm\_VirtualSystemManagementService class

Adds guest service settings to a virtual system configuration.

When applied to parts of a "current" virtual system configuration, as a side effect guest services of the active virtual system may be modified.

## Syntax


```mof
uint32 AddGuestServiceSettings(
  [in]  CIM_VirtualSystemSettingData REF AffectedConfiguration,
  [in]  string                           GuestServiceSettings[],
  [out] CIM_SettingData              REF ResultingGuestServiceSettings[],
  [out] CIM_ConcreteJob              REF Job
);
```



## Parameters

<dl> <dt>

*AffectedConfiguration* \[in\]
</dt> <dd>

A [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md) reference that describes the affected configuration.

</dd> <dt>

*GuestServiceSettings* \[in\]
</dt> <dd>

A collection of guest service settings.

</dd> <dt>

*ResultingGuestServiceSettings* \[out\]
</dt> <dd>

When successful, contains a collection of [**CIM\_SettingData**](cim-settingdata.md) references that describe the resulting guest service settings.

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

 

 





