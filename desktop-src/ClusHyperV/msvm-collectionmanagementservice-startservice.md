---
title: StartService method of the Msvm\_CollectionManagementService class
description: Starts the collection management service.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 41477bb5-69bc-42b5-a9fe-a5cbb9fcf915
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- StartService method
- StartService method, Msvm_CollectionManagementService class
- Msvm_CollectionManagementService class, StartService method
topic_type:
- apiref
api_name:
- Msvm_CollectionManagementService.StartService
api_location:
- VMMS.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# StartService method of the Msvm\_CollectionManagementService class

Starts the collection management service.

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

[**Msvm\_CollectionManagementService**](msvm-collectionmanagementservice.md)
</dt> </dl>

 

 





