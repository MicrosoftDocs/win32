---
title: AddFeatureSettings method of the Msvm\_VirtualSystemManagementService class
description: Adds feature settings to the configuration of an ethernet connection on a virtual machine.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5e95e521-8306-4d5d-b960-2fb75d6d74eb
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddFeatureSettings method
- AddFeatureSettings method, Msvm_VirtualSystemManagementService class
- Msvm_VirtualSystemManagementService class, AddFeatureSettings method
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementService.AddFeatureSettings
api_location:
- VMMS.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AddFeatureSettings method of the Msvm\_VirtualSystemManagementService class

Adds feature settings to the configuration of an ethernet connection on a virtual machine.

## Syntax


```mof
uint32 AddFeatureSettings(
  [in]  Msvm_EthernetPortAllocationSettingData    REF AffectedConfiguration,
  [in]  string                                        FeatureSettings[],
  [out] Msvm_EthernetSwitchPortFeatureSettingData REF ResultingFeatureSettings[],
  [out] CIM_ConcreteJob                           REF Job
);
```



## Parameters

<dl> <dt>

*AffectedConfiguration* \[in\]
</dt> <dd>

A reference to the ethernet connection.

</dd> <dt>

*FeatureSettings* \[in\]
</dt> <dd>

An array that contains embedded instances the [**Msvm\_EthernetSwitchPortFeatureSettingData**](https://msdn.microsoft.com/library/windows/desktop/hh850146) class that describes the feature settings to add to the connection configuration.

</dd> <dt>

*ResultingFeatureSettings* \[out\]
</dt> <dd>

An array that contains references to the [**Msvm\_EthernetSwitchPortFeatureSettingData**](https://msdn.microsoft.com/library/windows/desktop/hh850146) instances that represent the added feature settings.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

A reference to an optional job for the operation if the operation is run asynchronously.

If a job is used, the [**Msvm\_EthernetSwitchPortFeatureSettingData**](https://msdn.microsoft.com/library/windows/desktop/hh850146) instance that represents the added feature settings can be retrieved through the [**Msvm\_EthernetPortSettingDataComponent**](https://msdn.microsoft.com/library/windows/desktop/hh850137) instance that is associated with the [**Msvm\_EthernetPortAllocationSettingData**](https://msdn.microsoft.com/library/windows/desktop/hh850134) instance that represents the affected switch port.

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
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md)
</dt> </dl>

 

 





