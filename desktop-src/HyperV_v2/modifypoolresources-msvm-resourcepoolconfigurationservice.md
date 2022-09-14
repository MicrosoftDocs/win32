---
description: Changes the parent pool resource settings for resources assigned to a child pool.
ms.assetid: 419fca70-5f15-4593-80ac-ef2af2c3dde5
title: ModifyPoolResources method of the Msvm_ResourcePoolConfigurationService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_ResourcePoolConfigurationService.ModifyPoolResources
api_type: 
- COM
api_location: 
- vmms.exe
---

# ModifyPoolResources method of the Msvm\_ResourcePoolConfigurationService class

Changes the parent pool resource settings for resources assigned to a child pool.

## Syntax


```mof
uint32 ModifyPoolResources(
  [in]  CIM_ResourcePool REF ChildPool,
  [in]  CIM_ResourcePool REF ParentPools[],
  [in]  string               AllocationSettings[],
  [out] CIM_ConcreteJob  REF Job
);
```



## Parameters

<dl> <dt>

*ChildPool* \[in\]
</dt> <dd>

A reference to an instance of the [**CIM\_ResourcePool**](cim-resourcepool.md) class that represents the child pool to modify.

</dd> <dt>

*ParentPools* \[in\]
</dt> <dd>

An array of [**CIM\_ResourcePool**](cim-resourcepool.md) references that represent the new parent pools to assign to the child pool.

</dd> <dt>

*AllocationSettings* \[in\]
</dt> <dd>

An optional array of one or more embedded instances of the [**Msvm\_ResourceAllocationSettingData**](msvm-resourceallocationsettingdata.md) class that are used to specify the pool allocation related settings.

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

 

