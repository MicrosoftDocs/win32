---
title: CreateChildResourcePool method of the CIM\_ResourcePoolConfigurationService class
description: Starts a job to create a resource pool from a parent resource pool.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 86ee1590-9ebc-4d58-8783-92b19a1cdf45
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CreateChildResourcePool method
- CreateChildResourcePool method, CIM_ResourcePoolConfigurationService class
- CIM_ResourcePoolConfigurationService class, CreateChildResourcePool method
topic_type:
- apiref
api_name:
- CIM_ResourcePoolConfigurationService.CreateChildResourcePool
api_location:
- VMMS.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CreateChildResourcePool method of the CIM\_ResourcePoolConfigurationService class

Starts a job to create a resource pool from a parent resource pool.

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

A user relevant name for the new resource pool.

</dd> <dt>

*Settings* \[in\]
</dt> <dd>

An array that contains an embedded instance of [**CIM\_SettingData**](cim-settingdata.md) that represents the settings for the parent resource pool.

</dd> <dt>

*ParentPool* \[in\]
</dt> <dd>

The parent resource pool.

</dd> <dt>

*Pool* \[out\]
</dt> <dd>

A reference to the new resource pool.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

A reference to the job for the operation. When the job is finished this parameter can be set to **NULL**.

</dd> </dl>

## Return value

The possible values:

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

**DMTF Reserved** (9 4095)
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

 

 





