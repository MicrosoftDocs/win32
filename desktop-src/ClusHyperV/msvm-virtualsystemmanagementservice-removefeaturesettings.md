---
title: RemoveFeatureSettings method of the Msvm\_VirtualSystemManagementService class
description: Removes feature settings from an ethernet connection on a virtual machine.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'cdd8b672-e34f-4e6d-a395-054366957e0d'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["RemoveFeatureSettings method", "RemoveFeatureSettings method, Msvm_VirtualSystemManagementService class", "Msvm_VirtualSystemManagementService class, RemoveFeatureSettings method"]
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementService.RemoveFeatureSettings
api_location:
- VMMS.exe
api_type:
- COM
---

# RemoveFeatureSettings method of the Msvm\_VirtualSystemManagementService class

Removes feature settings from an ethernet connection on a virtual machine.

## Syntax


```mof
uint32 RemoveFeatureSettings(
  [in]  Msvm_EthernetSwitchPortFeatureSettingData REF FeatureSettings[],
  [out] CIM_ConcreteJob                           REF Job
);
```



## Parameters

<dl> <dt>

*FeatureSettings* \[in\]
</dt> <dd>

An array that contains references to the [**Msvm\_EthernetSwitchPortFeatureSettingData**](https://msdn.microsoft.com/library/windows/desktop/hh850146) instances that represent the feature settings to remove.

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
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md)
</dt> </dl>

 

 





