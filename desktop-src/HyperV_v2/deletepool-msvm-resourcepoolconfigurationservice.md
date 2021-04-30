---
description: Deletes a resource pool.
ms.assetid: bc3111a4-9687-49ec-890e-190358230c53
title: DeletePool method of the Msvm_ResourcePoolConfigurationService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_ResourcePoolConfigurationService.DeletePool
api_type: 
- COM
api_location: 
- vmms.exe
---

# DeletePool method of the Msvm\_ResourcePoolConfigurationService class

Deletes a resource pool. To successfully delete a resource pool, no allocations can be outstanding or the delete will fail with 32774 (In Use). If the resource pool is a root resource pool, any host resources are returned back to the underlying system.

## Syntax


```mof
uint32 DeletePool(
  [in]  CIM_ResourcePool REF Pool,
  [out] CIM_ConcreteJob  REF Job
);
```



## Parameters

<dl> <dt>

*Pool* \[in\]
</dt> <dd>

A reference to an instance of the [**CIM\_ResourcePool**](cim-resourcepool.md) class that represents the pool to delete.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

If the operation is performed asynchronously, this method will return 4096, and this parameter will contain a reference to an object derived from [**CIM\_ConcreteJob**](/previous-versions//cc136808(v=vs.85)).

</dd> </dl>

## Return value

This method returns one of the following values.

<dl> <dt>

**Job Completed with No Error** (0)
</dt> <dt>

**DMTF Reserved** (..)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Method Reserved** (4097..32767)
</dt> <dt>

**Failed** (32768)
</dt> <dt>

**Access Denied** (32769)
</dt> <dt>

**Not Supported** (32770)
</dt> <dt>

**Unknown** (32771)
</dt> <dt>

**Timeout** (32772)
</dt> <dt>

**Invalid Parameter** (32773)
</dt> <dt>

**In Use** (32774)
</dt> <dt>

**Invalid State** (32775)
</dt> <dt>

**Incorrect Resource Type for the Pool** (32776)
</dt> <dt>

**Unavailable** (32777)
</dt> <dt>

**Out of Memory** (32778)
</dt> <dt>

**Vendor Reserved** (32779)
</dt> <dt>

**Insufficient Resources** (32780)
</dt> <dt>

**Object Not Found** (32781..32787)
</dt> <dt>

**Object Exists** (32788)
</dt> <dt>

**Vendor Specific** (32768..65535)
</dt> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**Msvm\_ResourcePoolConfigurationService**](msvm-resourcepoolconfigurationservice.md)
</dt> </dl>

 

