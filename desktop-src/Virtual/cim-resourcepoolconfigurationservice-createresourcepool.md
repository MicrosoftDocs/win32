---
title: CreateResourcePool method of the CIM\_ResourcePoolConfigurationService class
description: Starts a job to create a root resource pool. The resource pool will be scoped to the same system as this service.
ms.assetid: 6f9c8fe9-63e6-4e70-b35d-7a781c36245a
keywords:
- CreateResourcePool method Hyper-V
- CreateResourcePool method Hyper-V , CIM_ResourcePoolConfigurationService class
- CIM_ResourcePoolConfigurationService class Hyper-V , CreateResourcePool method
topic_type:
- apiref
api_name:
- CIM_ResourcePoolConfigurationService.CreateResourcePool
api_location:
- Root\virtualization
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CreateResourcePool method of the CIM\_ResourcePoolConfigurationService class

Starts a job to create a root resource pool. The resource pool will be scoped to the same system as this service.

## Syntax


```mof
uint32 CreateResourcePool(
  [in]  string                ElementName,
  [in]  CIM_LogicalDevice REF HostResources[],
  [in]  string                ResourceType,
  [out] CIM_ResourcePool  REF Pool,
  [out] CIM_ConcreteJob   REF Job,
  [out] string                Error
);
```



## Parameters

<dl> <dt>

*ElementName* \[in\]
</dt> <dd>

A user relevant name for the new resource pool.

</dd> <dt>

*HostResources* \[in\]
</dt> <dd>

Array of references to zero or more logical devices that are used to create the resource pool, or modify the source extents. All elements in the array must be of the same type.

</dd> <dt>

*ResourceType* \[in\]
</dt> <dd>

The type of resources that the new resource pool will manage. If the **HostResources** property contains elements, this property must mach that type.

</dd> <dt>

*Pool* \[out\]
</dt> <dd>

If this method returns successfully, this parameter contains a reference to the new resource pool. If this method returns a job, this parameter may be NULL, in which case, the client must use the job to find the new resource pool after the job completes.

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

The possible values are:

<dl> <dt>

**Job Completed with No Error**
</dt> <dd>

0

The job completed successfully.

</dd> <dt>

**Not Supported**
</dt> <dd>

1

</dd> <dt>

**Unknown**
</dt> <dd>

2

</dd> <dt>

**Timeout**
</dt> <dd>

3

</dd> <dt>

**Failed**
</dt> <dd>

4

</dd> <dt>

**Invalid Parameter**
</dt> <dd>

5

</dd> <dt>

**In Use**
</dt> <dd>

6

</dd> <dt>

**Incorrect ResourceType for the Pool**
</dt> <dd>

7

</dd> <dt>

**DMTF Reserved**
</dt> <dd>

8 4095

</dd> <dt>

**Method Parameters Checked - Job Started**
</dt> <dd>

4096

</dd> <dt>

**Size Not Supported**
</dt> <dd>

4097

</dd> <dt>

**Method Reserved**
</dt> <dd>

4098 32767

</dd> <dt>

**Vendor Specific**
</dt> <dd>

32768 65535

</dd> </dl>

## Requirements



|                      |                                                                                                      |
|----------------------|------------------------------------------------------------------------------------------------------|
| Namespace<br/> | Root\\virtualization<br/>                                                                      |
| MOF<br/>       | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ResourcePoolConfigurationService**](cim-resourcepoolconfigurationservice.md)
</dt> </dl>

 

 





