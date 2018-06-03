---
title: RemoveResourceSettings method of the CIM\_VirtualSystemManagementService class
description: Removes virtual resource settings from a virtual system configuration.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: abb99c51-fb24-428c-b962-6280d96b10f2
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoveResourceSettings method
- RemoveResourceSettings method, CIM_VirtualSystemManagementService class
- CIM_VirtualSystemManagementService class, RemoveResourceSettings method
topic_type:
- apiref
api_name:
- CIM_VirtualSystemManagementService.RemoveResourceSettings
api_location:
- VMMS.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RemoveResourceSettings method of the CIM\_VirtualSystemManagementService class

Removes virtual resource settings from a virtual system configuration.

> [!Note]  
> When this method is applied to the current virtual system configuration, resource from the active virtual system might be removed.

 

## Syntax


```mof
uint32 RemoveResourceSettings(
  [in]  CIM_ResourceAllocationSettingData REF ResourceSettings[],
  [out] CIM_ConcreteJob                   REF Job
);
```



## Parameters

<dl> <dt>

*ResourceSettings* \[in\]
</dt> <dd>

An array that contains references to the [**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md) instances that represent the resource settings to remove.

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

**DMTF Reserved** (6 4095)
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

 

 





