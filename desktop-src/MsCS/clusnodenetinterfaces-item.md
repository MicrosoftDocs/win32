---
title: ClusNodeNetInterfaces.Item property
description: Single network interface from a ClusNodeNetInterfaces collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8c7291dd-53cf-4ba4-99af-a38527ef453d
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Item property Failover Cluster
- Item property Failover Cluster , ClusNodeNetInterfaces collection
- ClusNodeNetInterfaces collection Failover Cluster , Item property
topic_type:
- apiref
api_name:
- ClusNodeNetInterfaces.Item
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusNodeNetInterfaces.Item property

\[The **Item** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns a single [network interface](network-interfaces.md) from a [**ClusNodeNetInterfaces**](clusnodenetinterfaces-collection.md) collection.

This property is read-only.

## Syntax


```VB
ClusNodeNetInterfaces.Item( _
  ByVal varIndex _
)
```



## Property value

A [**ClusNetInterface**](clusnetinterface-object.md) object that receives the specified network interface.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusNodeNet is defined as F2E606FC-2631-11D1-89F1-00A0C90D061E<br/>      |



## See also

<dl> <dt>

[**ClusNetInterface**](clusnetinterface-object.md)
</dt> <dt>

[**ClusNodeNetInterfaces**](clusnodenetinterfaces-collection.md)
</dt> <dt>

[**ClusNodeNetInterfaces.Count**](clusnodenetinterfaces-count.md)
</dt> </dl>

 

 





