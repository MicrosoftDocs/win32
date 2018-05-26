---
title: ModifyFeatureSettings method of the Msvm\_VirtualSystemManagementService class
description: Modifies the feature settings of an ethernet connection of a virtual machine.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 88bdddfa-fa03-43a4-934b-961b0e3f0c87
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ModifyFeatureSettings method
- ModifyFeatureSettings method, Msvm_VirtualSystemManagementService class
- Msvm_VirtualSystemManagementService class, ModifyFeatureSettings method
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementService.ModifyFeatureSettings
api_location:
- VMMS.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ModifyFeatureSettings method of the Msvm\_VirtualSystemManagementService class

Modifies the feature settings of an ethernet connection of a virtual machine.

## Syntax


```mof
uint32 ModifyFeatureSettings(
  [in]  string                                        FeatureSettings[],
  [out] Msvm_EthernetSwitchPortFeatureSettingData REF ResultingFeatureSettings[],
  [out] CIM_ConcreteJob                           REF Job
);
```



## Parameters

<dl> <dt>

*FeatureSettings* \[in\]
</dt> <dd>

An array that contains embedded instances of [**Msvm\_EthernetSwitchPortFeatureSettingData**](https://msdn.microsoft.com/library/windows/desktop/hh850146) that describe the changes to the current feature settings of the ethernet connection. All instances must have a valid **InstanceID** property in order to identify the feature settings to modify.

</dd> <dt>

*ResultingFeatureSettings* \[out\]
</dt> <dd>

An array of references to [**Msvm\_EthernetSwitchPortFeatureSettingData**](https://msdn.microsoft.com/library/windows/desktop/hh850146) instances that represent the modified feature settings.

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

**Incompatible Parameters** (6)
</dt> <dt>

**DMTF Reserved** (7 4095)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Method Reserved** (4097 32768)
</dt> <dt>

**Vendor Specific** (32768 65535)
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

[**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md)
</dt> </dl>

 

 





