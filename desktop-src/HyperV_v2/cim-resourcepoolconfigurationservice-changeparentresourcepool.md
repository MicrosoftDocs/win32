---
description: Start a job to change a parent pool using the specified allocation settings.
ms.assetid: 2eea1a60-fbf0-49a7-8f79-52c62c295316
title: ChangeParentResourcePool method of the CIM_ResourcePoolConfigurationService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_ResourcePoolConfigurationService.ChangeParentResourcePool
api_type: 
- COM
api_location: 
- vmms.exe
---

# ChangeParentResourcePool method of the CIM\_ResourcePoolConfigurationService class

Start a job to change a parent pool using the specified allocation settings.

## Syntax


```mof
uint32 ChangeParentResourcePool(
  [in]  CIM_ResourcePool REF ChildPool,
  [in]  CIM_ResourcePool REF ParentPool[],
  [in]  string               Settings[],
  [out] CIM_ConcreteJob  REF Job
);
```



## Parameters

<dl> <dt>

*ChildPool* \[in\]
</dt> <dd>

A [**CIM\_ResourcePool**](cim-resourcepool.md) that references the child pool.

</dd> <dt>

*ParentPool* \[in\]
</dt> <dd>

A [**CIM\_ResourcePool**](cim-resourcepool.md) array that references the parent pool(s).

</dd> <dt>

*Settings* \[in\]
</dt> <dd>

Optional string containing a representation of a [**CIM\_SettingData**](cim-settingdata.md) instance that is used to specify the settings for the parent pool.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

A [**CIM\_ConcreteJob**](cim-concretejob.md) that references the job (may be **null** if job completed).

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

 

 




