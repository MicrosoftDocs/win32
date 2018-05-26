---
title: ClusNetwork.PrivateROProperties property
description: ClusProperties collection containing the read-only private properties of a network.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e7e8667d-8d26-44d1-8ebd-a4704abbc637
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- PrivateROProperties property Failover Cluster
- PrivateROProperties property Failover Cluster , ClusNetwork object
- ClusNetwork object Failover Cluster , PrivateROProperties property
topic_type:
- apiref
api_name:
- ClusNetwork.PrivateROProperties
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusNetwork.PrivateROProperties property

\[The **PrivateROProperties** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns a [**ClusProperties**](clusproperties-collection.md) collection containing the read-only [private properties](private-properties.md) of a [network](networks.md).

This property is read-only.

## Syntax


```VB
ClusNetwork.PrivateROProperties
```



## Property value

A [**ClusProperties**](clusproperties-collection.md) collection to receive the read-only private properties of the network.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusNetwork is defined as F2E606F2-2631-11D1-89F1-00A0C90D061E<br/>      |



## See also

<dl> <dt>

[**ClusNetwork**](clusnetwork-object.md)
</dt> <dt>

[**ClusProperties**](clusproperties-collection.md)
</dt> </dl>

 

 





