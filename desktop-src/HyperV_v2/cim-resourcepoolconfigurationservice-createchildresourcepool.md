---
description: Start a job to create a sub-pool from a parent pool using the specified allocation settings.
ms.assetid: 9b09221a-7c4e-4648-a2a8-012df1818c3e
title: CreateChildResourcePool method of the CIM_ResourcePoolConfigurationService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_ResourcePoolConfigurationService.CreateChildResourcePool
api_type: 
- COM
api_location: 
- vmms.exe
---

# CreateChildResourcePool method of the CIM\_ResourcePoolConfigurationService class

Start a job to create a sub-pool from a parent pool using the specified allocation settings.

## Syntax


```mof
uint32 CreateChildResourcePool(
  [in]  string               ElementName,
  [in]  string               Settings[],
  [in]  CIM_ResourcePool REF ParentPool[],
  [out] CIM_ResourcePool REF Pool,
  [out] CIM_ConcreteJob  REF Job
);
```



## Parameters

<dl> <dt>

*ElementName* \[in\]
</dt> <dd>

A end user relevant name for the pool being created. If **NULL**, then a system supplied default name can be used. The value will be stored in the **ElementName** property for the created element.

</dd> <dt>

*Settings* \[in\]
</dt> <dd>

String containing a representation of a [**CIM\_SettingData**](cim-settingdata.md) instance that is used to specify the settings for the child Pool.

</dd> <dt>

*ParentPool* \[in\]
</dt> <dd>

A [**CIM\_ResourcePool**](cim-resourcepool.md) from which to create the new Pool.

</dd> <dt>

*Pool* \[out\]
</dt> <dd>

A [**CIM\_ResourcePool**](cim-resourcepool.md) that references the resulting pool.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

Reference to the job (may be null if job completed).

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

**Insufficient Resources** (8)
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

 

 




