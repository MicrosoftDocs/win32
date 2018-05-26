---
title: RemoveBootSourceSettings method of the Msvm\_VirtualSystemManagementService class
description: Removes virtual resource settings from a virtual machine configuration.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a959025b-a252-46c8-8284-9a87b4bdb7bc
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoveBootSourceSettings method
- RemoveBootSourceSettings method, Msvm_VirtualSystemManagementService class
- Msvm_VirtualSystemManagementService class, RemoveBootSourceSettings method
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementService.RemoveBootSourceSettings
api_location:
- VMMS.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RemoveBootSourceSettings method of the Msvm\_VirtualSystemManagementService class

Removes virtual resource settings from a virtual machine configuration.

## Syntax


```mof
uint32 RemoveBootSourceSettings(
  [in]  CIM_SettingData REF BootSourceSettings[],
  [out] CIM_ConcreteJob REF Job
);
```



## Parameters

<dl> <dt>

*BootSourceSettings* \[in\]
</dt> <dd>

An array that contains a reference to the virtual resource settings to remove.

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

**DMTF Reserved** (6 4095)
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

 

 





