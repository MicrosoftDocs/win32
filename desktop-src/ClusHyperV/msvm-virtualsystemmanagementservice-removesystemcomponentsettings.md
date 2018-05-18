---
title: RemoveSystemComponentSettings method of the Msvm\_VirtualSystemManagementService class
description: Removes generic component settings from a virtual system configuration.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'f8a0b8eb-a352-4f24-97a8-281fcc6743e1'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["RemoveSystemComponentSettings method", "RemoveSystemComponentSettings method, Msvm_VirtualSystemManagementService class", "Msvm_VirtualSystemManagementService class, RemoveSystemComponentSettings method"]
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementService.RemoveSystemComponentSettings
api_location:
- VMMS.exe
api_type:
- COM
---

# RemoveSystemComponentSettings method of the Msvm\_VirtualSystemManagementService class

Removes generic component settings from a virtual system configuration.

## Syntax


```mof
uint32 RemoveSystemComponentSettings(
  [in]  Msvm_SystemComponentSettingData REF ComponentSettings[],
  [out] CIM_ConcreteJob                 REF Job
);
```



## Parameters

<dl> <dt>

*ComponentSettings* \[in\]
</dt> <dd>

reference to a collection of Msvm\_ConcreteSettingData references that describe the component settings to remove.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

A [**CIM\_ConcreteJob**](cim-concretejob.md) reference to an optional job for the operation if the operation is run asynchronously.

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

**DMTF Reserved** (6–4095)
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

 

 





