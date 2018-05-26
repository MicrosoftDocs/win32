---
title: ChangeParentResourcePool method of the CIM\_ResourcePoolConfigurationService class
description: Starts a job to change the parent resource pool of a resource pool.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8e3af19d-33f3-4424-9775-e78dc184f4fd
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ChangeParentResourcePool method
- ChangeParentResourcePool method, CIM_ResourcePoolConfigurationService class
- CIM_ResourcePoolConfigurationService class, ChangeParentResourcePool method
topic_type:
- apiref
api_name:
- CIM_ResourcePoolConfigurationService.ChangeParentResourcePool
api_location:
- VMMS.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ChangeParentResourcePool method of the CIM\_ResourcePoolConfigurationService class

Starts a job to change the parent resource pool of a resource pool.

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

A reference to the child resource pool.

</dd> <dt>

*ParentPool* \[in\]
</dt> <dd>

An array that contains references to the parent pool.

</dd> <dt>

*Settings* \[in\]
</dt> <dd>

An array that contains an embedded instance of [**CIM\_SettingData**](cim-settingdata.md) that represents the settings for the parent resource pool.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

A reference to the job for the operation. When the job is finished this parameter can be set to **NULL**.

</dd> </dl>

## Return value

The possible values are:

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

 

 





