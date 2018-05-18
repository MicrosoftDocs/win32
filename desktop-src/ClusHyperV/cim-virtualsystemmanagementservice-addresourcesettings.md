---
title: AddResourceSettings method of the CIM\_VirtualSystemManagementService class
description: Adds resources to a virtual system configuration.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'f1c0154a-ea7c-4117-8b6e-4376ecef0272'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["AddResourceSettings method", "AddResourceSettings method, CIM_VirtualSystemManagementService class", "CIM_VirtualSystemManagementService class, AddResourceSettings method"]
topic_type:
- apiref
api_name:
- CIM_VirtualSystemManagementService.AddResourceSettings
api_location:
- VMMS.exe
api_type:
- COM
---

# AddResourceSettings method of the CIM\_VirtualSystemManagementService class

Adds resources to a virtual system configuration.

> [!Note]  
> When this method is applied to a stateful virtual system configuration, the resources are added to the active virtual system.

 

## Syntax


```mof
uint32 AddResourceSettings(
  [in]  CIM_VirtualSystemSettingData      REF AffectedConfiguration,
  [in]  string                                ResourceSettings[],
  [out] CIM_ResourceAllocationSettingData REF ResultingResourceSettings[],
  [out] CIM_ConcreteJob                   REF Job
);
```



## Parameters

<dl> <dt>

*AffectedConfiguration* \[in\]
</dt> <dd>

A reference to the virtual system configuration that receives the resources.

</dd> <dt>

*ResourceSettings* \[in\]
</dt> <dd>

An array that contains embedded instance of the [**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md) class that represent the resource settings to add to the virtual system configuration.

</dd> <dt>

*ResultingResourceSettings* \[out\]
</dt> <dd>

An array that contains references to [**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md) instances that represent the resource settings that were added to the virtual system configuration.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

If the operation is to run asynchronously, this parameter will return a job for the operation.

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

[**CIM\_VirtualSystemManagementService**](cim-virtualsystemmanagementservice.md)
</dt> </dl>

 

 





