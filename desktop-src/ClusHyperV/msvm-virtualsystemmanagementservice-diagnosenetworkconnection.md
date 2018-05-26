---
title: DiagnoseNetworkConnection method of the Msvm\_VirtualSystemManagementService class
description: Diagnoses the network connectivity of a VM in a Windows Network Virtualization Environment.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e388c120-50d2-4647-ad4f-7ca1145c196e
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DiagnoseNetworkConnection method
- DiagnoseNetworkConnection method, Msvm_VirtualSystemManagementService class
- Msvm_VirtualSystemManagementService class, DiagnoseNetworkConnection method
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementService.DiagnoseNetworkConnection
api_location:
- clushyperv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DiagnoseNetworkConnection method of the Msvm\_VirtualSystemManagementService class

Diagnoses the network connectivity of a VM in a Windows Network Virtualization Environment.

## Syntax


```mof
uint32 DiagnoseNetworkConnection(
  [in]  Msvm_EthernetPortAllocationSettingData REF TargetNetworkAdapter,
  [in]  string                                     DiagnosticSettings,
  [out] string                                     DiagnosticInformation,
  [out] CIM_ConcreteJob                        REF Job
);
```



## Parameters

<dl> <dt>

*TargetNetworkAdapter* \[in\]
</dt> <dd>

A reference to the [**Msvm\_EthernetPortAllocationSettingData**](https://msdn.microsoft.com/library/windows/desktop/hh850134) that represents the network adapter of the virtual machine.

</dd> <dt>

*DiagnosticSettings* \[in\]
</dt> <dd>

The diagnostic settings to use.

</dd> <dt>

*DiagnosticInformation* \[out\]
</dt> <dd>

On success, returns the network connection diagnostic information.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

A reference to an optional job for the operation if the operation is run asynchronously.

</dd> </dl>

## Return value

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

**DMTF Reserved** (5 4095)
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
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Clushyperv.dll</dt> </dl>              |



## See also

<dl> <dt>

[**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md)
</dt> </dl>

 

 





