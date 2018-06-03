---
title: clusrefobject handle property
description: Retrieves a raw handle to the cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: E2E5F212-34C8-4A27-BAEE-759C0C707C85
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- handle property Failover Cluster
- handle property Failover Cluster , clusrefobject interface
- clusrefobject interface Failover Cluster , handle property
topic_type:
- apiref
api_name:
- clusrefobject.handle
- clusrefobject.get_handle
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# clusrefobject::handle property

Retrieves a raw handle to the cluster.

This property is read-only.

## Syntax


```VB
.handle
```



## Property value

A **ULONG\_PTR** that represents the raw handle to the cluster.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusRefObject is defined as f2e60702-2631-11d1-89f1-00a0c90d061e<br/>    |



## See also

<dl> <dt>

[**ClusRefObject**](clusrefobject.md)
</dt> </dl>

 

 





