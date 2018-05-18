---
title: DeleteResourcePool method of the CIM\_ResourcePoolConfigurationService class
description: Starts a job to delete a resource pool.
ms.assetid: 'c7ba97aa-3783-4f02-913c-1aae87bc2e01'
keywords: ["DeleteResourcePool method Hyper-V", "DeleteResourcePool method Hyper-V , CIM_ResourcePoolConfigurationService class", "CIM_ResourcePoolConfigurationService class Hyper-V , DeleteResourcePool method"]
topic_type:
- apiref
api_name:
- CIM_ResourcePoolConfigurationService.DeleteResourcePool
api_location:
- Root\virtualization
api_type:
- COM
---

# DeleteResourcePool method of the CIM\_ResourcePoolConfigurationService class

Starts a job to delete a resource pool. The delete operation will fail and this method will return 6 (in use) if there are unfinished resource allocation when this method is called. If the deleted resource pool is a root resource pool, all of its host resources are returned back to the underlying system.

## Syntax


```mof
uint32 DeleteResourcePool(
  [in]  CIM_ResourcePool REF Pool,
  [out] CIM_ConcreteJob  REF Job,
  [out] string               Error
);
```



## Parameters

<dl> <dt>

*Pool* \[in\]
</dt> <dd>

A reference to the resource pool to delete.

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

**DMTF Reserved** (8–4095)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Method Reserved** (4097–32767)
</dt> <dt>

**Vendor Specific** (32768–65535)
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

 

 





