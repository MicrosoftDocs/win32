---
title: ModifyResourceSettings method of the Msvm\_VirtualSystemManagementService class
description: Modifies virtual resource settings.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2bd3e378-1a57-429b-9016-c31d01c03719
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ModifyResourceSettings method
- ModifyResourceSettings method, Msvm_VirtualSystemManagementService class
- Msvm_VirtualSystemManagementService class, ModifyResourceSettings method
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementService.ModifyResourceSettings
api_location:
- VMMS.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ModifyResourceSettings method of the Msvm\_VirtualSystemManagementService class

Modifies virtual resource settings.

## Syntax


```mof
uint32 ModifyResourceSettings(
  [in]  string                                ResourceSettings[],
  [out] CIM_ResourceAllocationSettingData REF ResultingResourceSettings[],
  [out] CIM_ConcreteJob                   REF Job
);
```



## Parameters

<dl> <dt>

*ResourceSettings* \[in\]
</dt> <dd>

An array that contains embedded instances of [**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md) that contain the changes to make.

</dd> <dt>

*ResultingResourceSettings* \[out\]
</dt> <dd>

An array that contains references to the [**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md) instances that represent the modified resource settings.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

A reference to an optional job for the operation if the operation is run asynchronously.

</dd> </dl>

## Return value

The possible return values are:

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Failed** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Invalid Parameter** (4)
</dt> <dt>

**Invalid State** (5)
</dt> <dt>

**Incompatible Parameters** (6)
</dt> <dt>

**DMTF Reserved** (7 4095)
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

[**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md)
</dt> </dl>

 

 





