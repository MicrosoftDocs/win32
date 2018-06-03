---
title: ClusResource.Dependencies property
description: dependencies of a resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 33539a29-1533-44fa-853d-9d4f1b3f1cca
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Dependencies property Failover Cluster
- Dependencies property Failover Cluster , ClusResource class
- ClusResource class Failover Cluster , Dependencies property
topic_type:
- apiref
api_name:
- ClusResource.Dependencies
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusResource.Dependencies property

\[The **Dependencies** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Retrieves the [dependencies](resource-dependencies.md) of a [resource](resources.md).

This property is read-only.

## Syntax


```VB
ClusResource.Dependencies
```



## Property value

On successful return, contains a [**ClusResDependencies**](clusresdependencies-collection.md) collection.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusResource is defined as F2E6070A-2631-11D1-89F1-00A0C90D061E<br/>     |



## See also

<dl> <dt>

[**ClusResDependencies**](clusresdependencies-collection.md)
</dt> <dt>

[**ClusResource**](clusresource-object.md)
</dt> <dt>

[**ClusResources**](clusresources-collection.md)
</dt> </dl>

 

 





