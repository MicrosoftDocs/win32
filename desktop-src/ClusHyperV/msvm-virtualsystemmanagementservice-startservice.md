---
title: StartService method of the Msvm\_VirtualSystemManagementService class
description: Starts the virtual system management service.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3ded2109-c6aa-439f-b2fe-1260055e02f7
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- StartService method
- StartService method, Msvm_VirtualSystemManagementService class
- Msvm_VirtualSystemManagementService class, StartService method
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementService.StartService
api_location:
- VMMS.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# StartService method of the Msvm\_VirtualSystemManagementService class

Starts the virtual system management service.

## Syntax


```mof
uint32 StartService();
```



## Parameters

This method has no parameters.

## Return value

The possible return values are:

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Not supported** (1)
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

 

 





