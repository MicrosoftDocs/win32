---
description: Starts a job to create a root ResourcePool. The ResourcePool will be scoped to the same System as this Service.
ms.assetid: 357880dc-125a-452c-89f5-44cd17684436
title: CreateResourcePool method of the CIM_ResourcePoolConfigurationService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_ResourcePoolConfigurationService.CreateResourcePool
api_type: 
- COM
api_location: 
- vmms.exe
---

# CreateResourcePool method of the CIM\_ResourcePoolConfigurationService class

Starts a job to create a root ResourcePool. The ResourcePool will be scoped to the same System as this Service.

## Syntax


```mof
uint32 CreateResourcePool(
  [in]  string                ElementName,
  [in]  CIM_LogicalDevice REF HostResources[],
  [in]  string                ResourceType,
  [out] CIM_ResourcePool  REF Pool,
  [out] CIM_ConcreteJob   REF Job
);
```



## Parameters

<dl> <dt>

*ElementName* \[in\]
</dt> <dd>

A end user relevant name for the pool being created. If **NULL**, then a system supplied default name can be used. The value will be stored in the **ElementName** property for the created pool.

</dd> <dt>

*HostResources* \[in\]
</dt> <dd>

Array of zero or more [**CIM\_LogicalDevice**](cim-logicaldevice.md) devices that are used to create the Pool or modify the source extents. All elements in the array must be of the same type.

</dd> <dt>

*ResourceType* \[in\]
</dt> <dd>

The type of resources the created pool will manage. If *HostResources* contains elements, this property must mach their type.

</dd> <dt>

*Pool* \[out\]
</dt> <dd>

On success, returns a reference to the resulting [**CIM\_ResourcePool**](cim-resourcepool.md). When a Job is returned, this may be **NULL**, in which case, the client must use the Job to find the resulting ResourcePool once the Job completes.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

Reference to a [**CIM\_ConcreteJob**](cim-concretejob.md) that represents the job (may be null if job completed).

</dd> </dl>

## Return value

Returns a 0 on success; otherwise, returns an error.

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

**DMTF Reserved** (..)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Size Not Supported** (4097)
</dt> <dt>

**Method Reserved** (4098..32767)
</dt> <dt>

**Vendor Specific** (32768..65535)
</dt> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                                  |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                       |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_ResourcePoolConfigurationService**](cim-resourcepoolconfigurationservice.md)
</dt> </dl>

 

 




