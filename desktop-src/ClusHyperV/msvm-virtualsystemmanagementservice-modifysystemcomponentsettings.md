---
title: ModifySystemComponentSettings method of the Msvm\_VirtualSystemManagementService class
description: Modifies generic system component settings.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '53559014-9f6c-4932-ab98-ed444008eb9d'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["ModifySystemComponentSettings method", "ModifySystemComponentSettings method, Msvm_VirtualSystemManagementService class", "Msvm_VirtualSystemManagementService class, ModifySystemComponentSettings method"]
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementService.ModifySystemComponentSettings
api_location:
- VMMS.exe
api_type:
- COM
---

# ModifySystemComponentSettings method of the Msvm\_VirtualSystemManagementService class

Modifies generic system component settings.

## Syntax


```mof
uint32 ModifySystemComponentSettings(
  [in]  string                              ComponentSettings[],
  [out] Msvm_SystemComponentSettingData REF ResultingComponentSettings[],
  [out] CIM_ConcreteJob                 REF Job
);
```



## Parameters

<dl> <dt>

*ComponentSettings* \[in\]
</dt> <dd>

A collection of component settings to modify.

</dd> <dt>

*ResultingComponentSettings* \[out\]
</dt> <dd>

On success, returns a collection of Msvm\_ConcreteSettingData containing the updated component settings.

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
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md)
</dt> </dl>

 

 





