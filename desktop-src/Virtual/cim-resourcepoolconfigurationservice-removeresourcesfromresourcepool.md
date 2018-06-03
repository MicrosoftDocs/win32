---
title: RemoveResourcesFromResourcePool method of the CIM\_ResourcePoolConfigurationService class
description: Starts a job to remove resources from a resource pool. The updated resource pool will be a root pool with no parent pool.
ms.assetid: 2810441d-bbea-401e-8da2-f54644ccd35b
keywords:
- RemoveResourcesFromResourcePool method Hyper-V
- RemoveResourcesFromResourcePool method Hyper-V , CIM_ResourcePoolConfigurationService class
- CIM_ResourcePoolConfigurationService class Hyper-V , RemoveResourcesFromResourcePool method
topic_type:
- apiref
api_name:
- CIM_ResourcePoolConfigurationService.RemoveResourcesFromResourcePool
api_location:
- Root\virtualization
api_type:
- COM
ms.technology: desktop
ms.prod: windows
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
  [out] CIM_ConcreteJob   REF Job,
  [out] string                Error
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

</dd> <dt>

*Error* \[out\]
</dt> <dd>

Contains an error message, if relevent.

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



|                      |                                                                                                      |
|----------------------|------------------------------------------------------------------------------------------------------|
| Namespace<br/> | Root\\virtualization<br/>                                                                      |
| MOF<br/>       | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ResourcePoolConfigurationService**](cim-resourcepoolconfigurationservice.md)
</dt> </dl>

 

 





