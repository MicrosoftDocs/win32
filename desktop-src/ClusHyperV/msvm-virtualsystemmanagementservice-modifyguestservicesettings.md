---
title: ModifyGuestServiceSettings method of the Msvm\_VirtualSystemManagementService class
description: Modifies guest service settings for a virtual system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '46eef441-ee0a-4030-8bcd-b864b024c605'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["ModifyGuestServiceSettings method", "ModifyGuestServiceSettings method, Msvm_VirtualSystemManagementService class", "Msvm_VirtualSystemManagementService class, ModifyGuestServiceSettings method"]
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementService.ModifyGuestServiceSettings
api_location:
- VMMS.exe
api_type:
- COM
---

# ModifyGuestServiceSettings method of the Msvm\_VirtualSystemManagementService class

Modifies guest service settings for a virtual system.

## Syntax


```mof
uint32 ModifyGuestServiceSettings(
  [in]  string              GuestServiceSettings[],
  [out] CIM_SettingData REF ResultingGuestServiceSettings[],
  [out] CIM_ConcreteJob REF Job
);
```



## Parameters

<dl> <dt>

*GuestServiceSettings* \[in\]
</dt> <dd>

A array that contains embedded instances of [**CIM\_SettingData**](cim-settingdata.md) that describe the modifications to make to the guest service settings. All instances must have a valid **InstanceID** property value.

</dd> <dt>

*ResultingGuestServiceSettings* \[out\]
</dt> <dd>

An array that contains references to [**CIM\_SettingData**](cim-settingdata.md) instances that represent the modified guest service settings.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

A reference to an optional job for the operation if the operation is run asynchronously.

</dd> </dl>

## Return value

The possible returns values are:

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

**DMTF Reserved** (7–4095)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
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

[**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md)
</dt> </dl>

 

 





