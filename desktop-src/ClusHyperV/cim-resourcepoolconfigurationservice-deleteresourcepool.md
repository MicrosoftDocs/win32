---
title: DeleteResourcePool method of the CIM\_ResourcePoolConfigurationService class
description: Starts a job to delete a resource pool.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c32446b3-23b9-40ac-83d3-af01fd00a3ac
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DeleteResourcePool method
- DeleteResourcePool method, CIM_ResourcePoolConfigurationService class
- CIM_ResourcePoolConfigurationService class, DeleteResourcePool method
topic_type:
- apiref
api_name:
- CIM_ResourcePoolConfigurationService.DeleteResourcePool
api_location:
- VMMS.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DeleteResourcePool method of the CIM\_ResourcePoolConfigurationService class

Starts a job to delete a resource pool. The delete operation will fail and this method will return 6 (in use) if there are unfinished resource allocation when this method is called. If the deleted resource pool is a root resource pool, all of its host resources are returned back to the underlying system.

## Syntax


```mof
uint32 DeleteResourcePool(
  [in]  CIM_ResourcePool REF Pool,
  [out] CIM_ConcreteJob  REF Job
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

[**CIM\_ResourcePoolConfigurationService**](cim-resourcepoolconfigurationservice.md)
</dt> </dl>

 

 





