---
title: CreateSubResourcePool method of the CIM\_ResourcePoolConfigurationService class
description: Start a job to create a sub-pool from a parent pool using the specified allocation settings.
ms.assetid: c7adf18f-870f-474f-bc9d-00e742b32b82
keywords:
- CreateSubResourcePool method Hyper-V
- CreateSubResourcePool method Hyper-V , CIM_ResourcePoolConfigurationService class
- CIM_ResourcePoolConfigurationService class Hyper-V , CreateSubResourcePool method
topic_type:
- apiref
api_name:
- CIM_ResourcePoolConfigurationService.CreateSubResourcePool
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

# CreateSubResourcePool method of the CIM\_ResourcePoolConfigurationService class

Start a job to create a sub-pool from a parent pool using the specified allocation settings

## Syntax


```mof
uint32 CreateSubResourcePool(
  [in]  string               ElementName,
  [in]  string               settings,
  [in]  CIM_ResourcePool REF ParentPool,
  [out] CIM_ResourcePool REF Pool,
  [out] CIM_ConcreteJob  REF Job,
  [out] string               Error
);
```



## Parameters

<dl> <dt>

*ElementName* \[in\]
</dt> <dd>

A end user relevant name for the pool being created. If NULL, then a system supplied default name can be used. The value will be stored in the 'ElementName' property for the created element.

</dd> <dt>

*settings* \[in\]
</dt> <dd>

String containing a representation of a CIM\_SettingData instance that is used to specify the settings for the child Pool.

</dd> <dt>

*ParentPool* \[in\]
</dt> <dd>

The Pool(s) from which to create the new Pool.

</dd> <dt>

*Pool* \[out\]
</dt> <dd>

A reference to the resulting pool.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

Reference to the job (may be null if job completed).

</dd> <dt>

*Error* \[out\]
</dt> <dd>

Contains an error message, if relevant.

</dd> </dl>

## Return value

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



|                      |                                                                                                      |
|----------------------|------------------------------------------------------------------------------------------------------|
| Namespace<br/> | Root\\virtualization<br/>                                                                      |
| MOF<br/>       | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ResourcePoolConfigurationService**](cim-resourcepoolconfigurationservice.md)
</dt> </dl>

 

 





