---
title: AddBootSourceSettings method of the Msvm\_VirtualSystemManagementService class
description: Adds boot sources to a stateful virtual system configuration.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '6d4cd92a-a20f-4ee5-8168-27c0716f1d53'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["AddBootSourceSettings method", "AddBootSourceSettings method, Msvm_VirtualSystemManagementService class", "Msvm_VirtualSystemManagementService class, AddBootSourceSettings method"]
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementService.AddBootSourceSettings
api_location:
- VMMS.exe
api_type:
- COM
---

# AddBootSourceSettings method of the Msvm\_VirtualSystemManagementService class

Adds boot sources to a stateful virtual system configuration.

## Syntax


```mof
uint32 AddBootSourceSettings(
  [in]  CIM_VirtualSystemSettingData REF AffectedConfiguration,
  [in]  string                           BootSourceSettings[],
  [out] CIM_SettingData              REF ResultingBootSourceSettings[],
  [out] CIM_ConcreteJob              REF Job
);
```



## Parameters

<dl> <dt>

*AffectedConfiguration* \[in\]
</dt> <dd>

A reference to the virtual system configuration.

</dd> <dt>

*BootSourceSettings* \[in\]
</dt> <dd>

An array that contains references to instances of [**Msvm\_BootSourceSettingData**](https://msdn.microsoft.com/library/windows/desktop/dn280573) that represent properties of the boot sources.

</dd> <dt>

*ResultingBootSourceSettings* \[out\]
</dt> <dd>

An array that contains embedded instances of [**CIM\_SettingData**](cim-settingdata.md) that describe the virtual aspects of the virtual resources to add to the virtual system.

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

**DMTF Reserved** (5–4095)
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

 

 





