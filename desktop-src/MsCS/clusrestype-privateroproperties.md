---
title: ClusResType.PrivateROProperties property
description: Returns the read-only private properties of a resource type.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 83cdc77c-3199-4d01-b71d-8337fd8314a9
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- PrivateROProperties property Failover Cluster
- PrivateROProperties property Failover Cluster , ClusResType object
- ClusResType object Failover Cluster , PrivateROProperties property
topic_type:
- apiref
api_name:
- ClusResType.PrivateROProperties
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusResType.PrivateROProperties property

\[The **PrivateROProperties** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the read-only [private properties](private-properties.md) of a [resource type](resource-types.md).

This property is read-only.

## Syntax


```VB
ClusResType.PrivateROProperties
```



## Property value

A [**ClusProperties**](clusproperties-collection.md) collection to receive the read-only private properties of the resource type.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusResType is defined as F2E60710-2631-11D1-89F1-00A0C90D061E<br/>      |



## See also

<dl> <dt>

[**ClusProperties**](clusproperties-collection.md)
</dt> <dt>

[**ClusResType**](clusrestype-object.md)
</dt> </dl>

 

 





