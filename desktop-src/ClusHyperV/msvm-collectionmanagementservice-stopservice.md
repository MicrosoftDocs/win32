---
title: StopService method of the Msvm\_CollectionManagementService class
description: Stops the collection management service.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0b8f8d7a-47c8-49b4-b0e2-f19f63126e96
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- StopService method
- StopService method, Msvm_CollectionManagementService class
- Msvm_CollectionManagementService class, StopService method
topic_type:
- apiref
api_name:
- Msvm_CollectionManagementService.StopService
api_location:
- VMMS.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# StopService method of the Msvm\_CollectionManagementService class

Stops the collection management service.

## Syntax


```mof
uint32 StopService();
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
| Header<br/>                   | <dl> <dt>Sdoias.h</dt> </dl>                    |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**Msvm\_CollectionManagementService**](msvm-collectionmanagementservice.md)
</dt> </dl>

 

 





