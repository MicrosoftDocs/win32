---
title: StartService method of the Msvm\_CollectionReferencePointService class
description: Starts the service.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: de509b42-757f-4b6b-b71c-a7e59b59f365
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- StartService method
- StartService method, Msvm_CollectionReferencePointService class
- Msvm_CollectionReferencePointService class, StartService method
topic_type:
- apiref
api_name:
- Msvm_CollectionReferencePointService.StartService
api_location:
- VMMS.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# StartService method of the Msvm\_CollectionReferencePointService class

Starts the service.

The [**StartService**](https://msdn.microsoft.com/library/aa393655) method puts the service in a started state.

## Syntax


```mof
uint32 StartService();
```



## Parameters

This method has no parameters.

## Return value

Returns "0" on success, otherwise returns a WMI error code.

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

[**Msvm\_CollectionReferencePointService**](msvm-collectionreferencepointservice.md)
</dt> </dl>

 

 





