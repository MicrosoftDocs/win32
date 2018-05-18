---
title: ClusResTypes.Item property
description: Returns a single ClusResType object from a ClusResTypes collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '09535510-1824-4491-a638-04ffe944e932'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Item property Failover Cluster", "Item property Failover Cluster , ClusResTypes collection", "ClusResTypes collection Failover Cluster , Item property"]
topic_type:
- apiref
api_name:
- ClusResTypes.Item
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusResTypes.Item property

\[The **Item** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns a single [**ClusResType**](clusrestype-object.md) object from a [**ClusResTypes**](clusrestypes-collection.md) collection.

This property is read-only.

## Syntax


```VB
ClusResTypes.Item( _
  ByVal varIndex _
)
```



## Property value

A [**ClusResType**](clusrestype-object.md) object that receives the specified [resource type](resource-types.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusResTypes is defined as F2E60712-2631-11D1-89F1-00A0C90D061E<br/>     |



## See also

<dl> <dt>

[**ClusResType**](clusrestype-object.md)
</dt> <dt>

[**ClusResTypes**](clusrestypes-collection.md)
</dt> <dt>

[**ClusResTypes.Count**](clusrestypes-count.md)
</dt> </dl>

 

 





