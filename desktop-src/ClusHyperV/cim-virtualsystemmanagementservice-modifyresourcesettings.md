---
title: ModifyResourceSettings method of the CIM\_VirtualSystemManagementService class
description: Updates the settings for a virtual resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d635bafa-7ca1-430e-9180-c0f266d20cf0
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ModifyResourceSettings method
- ModifyResourceSettings method, CIM_VirtualSystemManagementService class
- CIM_VirtualSystemManagementService class, ModifyResourceSettings method
topic_type:
- apiref
api_name:
- CIM_VirtualSystemManagementService.ModifyResourceSettings
api_location:
- VMMS.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ModifyResourceSettings method of the CIM\_VirtualSystemManagementService class

Updates the settings for a virtual resource.

## Syntax


```mof
uint32 ModifyResourceSettings(
  [in]  string                                ResourceSettings[],
  [out] CIM_ResourceAllocationSettingData REF ResultingResourceSettings[],
  [out] CIM_ConcreteJob                   REF Job
);
```



## Parameters

<dl> <dt>

*ResourceSettings* \[in\]
</dt> <dd>

An array that contains embedded instances of the [**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md) class that describe the settings to update.

> [!Note]  
> The [**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md) must have a valid **InstanceID** property value that identifies the virtual resource to update.

 

</dd> <dt>

*ResultingResourceSettings* \[out\]
</dt> <dd>

An array that contains references to the [**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md) instances that represent the updated resource settings.

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

**Invalid State** (5)
</dt> <dt>

**Incompatible Parameters** (6)
</dt> <dt>

**DMTF Reserved** (7 4095)
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

[**CIM\_VirtualSystemManagementService**](cim-virtualsystemmanagementservice.md)
</dt> </dl>

 

 





