---
title: SetGuestNetworkAdapterConfiguration method of the Msvm\_VirtualSystemManagementService class
description: Configures the network adapters in a guest operating system. These configuration settings are applied immediately upon establishing communication with the KVP Exchange integration component that runs in the guest operating system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 23949634-a35f-469a-a292-aa3ed1d6f91c
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetGuestNetworkAdapterConfiguration method
- SetGuestNetworkAdapterConfiguration method, Msvm_VirtualSystemManagementService class
- Msvm_VirtualSystemManagementService class, SetGuestNetworkAdapterConfiguration method
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementService.SetGuestNetworkAdapterConfiguration
api_location:
- VMMS.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetGuestNetworkAdapterConfiguration method of the Msvm\_VirtualSystemManagementService class

Configures the network adapters in a guest operating system. These configuration settings are applied immediately upon establishing communication with the KVP Exchange integration component that runs in the guest operating system.

## Syntax


```mof
uint32 SetGuestNetworkAdapterConfiguration(
  [in]  CIM_ComputerSystem REF ComputerSystem,
  [in]  string                 NetworkConfiguration[],
  [out] CIM_ConcreteJob    REF Job
);
```



## Parameters

<dl> <dt>

*ComputerSystem* \[in\]
</dt> <dd>

A reference to the [**CIM\_ComputerSystem**](cim-computersystem.md) instance that contains the network adapters to configure.

</dd> <dt>

*NetworkConfiguration* \[in\]
</dt> <dd>

An array that contains embedded instances of [**Msvm\_GuestNetworkAdapterConfiguration**](https://msdn.microsoft.com/library/windows/desktop/hh850156) that describe the configuration settings for the network adapters. The **InstanceID** and **DHCPEnabled** properties must be specified in each instance.

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

 

 





