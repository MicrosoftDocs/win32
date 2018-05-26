---
title: ClusNetworks.Item property
description: A single ClusNetwork object from the ClusNetworks collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: da8248ab-70a2-4ca9-abf0-8aa3afe87298
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Item property Failover Cluster
- Item property Failover Cluster , ClusNetworks collection
- ClusNetworks collection Failover Cluster , Item property
topic_type:
- apiref
api_name:
- ClusNetworks.Item
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusNetworks.Item property

\[The **Item** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Retrieves a single [**ClusNetwork**](clusnetwork-object.md) object from the [**ClusNetworks**](clusnetworks-collection.md) collection.

This property is read-only.

## Syntax


```VB
ClusNetworks.Item( _
  ByVal varIndex _
)
```



## Property value

A [**ClusNetwork**](clusnetwork-object.md) object that receives the specified [network](networks.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusNetworks is defined as F2E606F4-2631-11D1-89F1-00A0C90D061E<br/>     |



## See also

<dl> <dt>

[**ClusNetwork**](clusnetwork-object.md)
</dt> <dt>

[**ClusNetworks**](clusnetworks-collection.md)
</dt> <dt>

[**ClusNetworks.Count**](clusnetworks-count.md)
</dt> </dl>

 

 





