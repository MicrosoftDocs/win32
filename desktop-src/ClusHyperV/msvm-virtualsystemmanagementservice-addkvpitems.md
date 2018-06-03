---
title: AddKvpItems method of the Msvm\_VirtualSystemManagementService class
description: Adds key-value pairs to a virtual system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b8b41ff8-b85a-4e85-9326-7f5c2ae52be3
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddKvpItems method
- AddKvpItems method, Msvm_VirtualSystemManagementService class
- Msvm_VirtualSystemManagementService class, AddKvpItems method
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementService.AddKvpItems
api_location:
- VMMS.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AddKvpItems method of the Msvm\_VirtualSystemManagementService class

Adds key-value pairs to a virtual system.

## Syntax


```mof
uint32 AddKvpItems(
  [in]  CIM_ComputerSystem REF TargetSystem,
  [in]  string                 DataItems[],
  [out] CIM_ConcreteJob    REF Job
);
```



## Parameters

<dl> <dt>

*TargetSystem* \[in\]
</dt> <dd>

A reference to the virtual computer system that receives the added key-value pairs.

</dd> <dt>

*DataItems* \[in\]
</dt> <dd>

An array that contains the key-value pairs to add. Each element of the array is an embedded instance of the [**Msvm\_KvpExchangeDataItem**](https://msdn.microsoft.com/library/windows/desktop/hh850171) class. This method fails if any of the key-value pairs already exists on the target system. This array can contain up to 128 elements.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

A reference to an optional job for the operation if the operation is run asynchronously.

</dd> </dl>

## Return value

The possible values are:

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Failed** (32768)
</dt> <dt>

**Access Denied** (32769)
</dt> <dt>

**Not Supported** (32770)
</dt> <dt>

**Status is unknown** (32771)
</dt> <dt>

**Timeout** (32772)
</dt> <dt>

**Invalid parameter** (32773)
</dt> <dt>

**System is in use** (32774)
</dt> <dt>

**Invalid state for this operation** (32775)
</dt> <dt>

**Incorrect data type** (32776)
</dt> <dt>

**System is not available** (32777)
</dt> <dt>

**Out of memory** (32778)
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

 

 





