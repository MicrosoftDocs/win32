---
title: RemoveResourcesFromResourcePool method of the CIM\_ResourcePoolConfigurationService class
description: Starts a job to remove resources from a resource pool. The updated resource pool will be a root pool with no parent pool.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: cbcd0aff-bc2b-43e1-9b8f-ca0e6294c381
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoveResourcesFromResourcePool method
- RemoveResourcesFromResourcePool method, CIM_ResourcePoolConfigurationService class
- CIM_ResourcePoolConfigurationService class, RemoveResourcesFromResourcePool method
topic_type:
- apiref
api_name:
- CIM_ResourcePoolConfigurationService.RemoveResourcesFromResourcePool
api_location:
- VMMS.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RemoveResourcesFromResourcePool method of the CIM\_ResourcePoolConfigurationService class

Starts a job to remove resources from a resource pool. The updated resource pool will be a root pool with no parent pool.

## Syntax


```mof
uint32 RemoveResourcesFromResourcePool(
  [in]  CIM_LogicalDevice REF HostResources[],
  [in]  CIM_ResourcePool  REF Pool,
  [out] CIM_ConcreteJob   REF Job
);
```



## Parameters

<dl> <dt>

*HostResources* \[in\]
</dt> <dd>

An array of references to logical devices to remove from the resource pool.

</dd> <dt>

*Pool* \[in\]
</dt> <dd>

The resource pool from which to remove resources.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

A reference to the job for the operation. When the job is finished this parameter can be set to **NULL**.

</dd> </dl>

## Return value

The possible return values are:

<dl> <dt>

**Job Completed with No Error** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Unknown** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Failed** (4)
</dt> <dt>

**Invalid Parameter** (5)
</dt> <dt>

**In Use** (6)
</dt> <dt>

**Incorrect ResourceType for the Pool** (7)
</dt> <dt>

**DMTF Reserved** (8 4095)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Size Not Supported** (4097)
</dt> <dt>

**Method Reserved** (4098 32767)
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

[**CIM\_ResourcePoolConfigurationService**](cim-resourcepoolconfigurationservice.md)
</dt> </dl>

 

 





