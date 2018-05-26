---
title: ClusProperties.Item property
description: Returns a single property from a ClusProperties collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: df848e91-c89d-4985-9afc-1814f3180283
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Item property Failover Cluster
- Item property Failover Cluster , ClusProperties collection
- ClusProperties collection Failover Cluster , Item property
topic_type:
- apiref
api_name:
- ClusProperties.Item
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusProperties.Item property

\[The **Item** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns a single property from a [**ClusProperties**](clusproperties-collection.md) collection.

This property is read-only.

## Syntax


```VB
ClusProperties.Item( _
  ByVal varIndex _
)
```



## Property value

A [**ClusProperty**](clusproperty-object.md) object that receives the specified properties.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusProperties is defined as F2E60700-2631-11D1-89F1-00A0C90D061E<br/>   |



## See also

<dl> <dt>

[**ClusProperties**](clusproperties-collection.md)
</dt> <dt>

[**ClusProperty**](clusproperty-object.md)
</dt> <dt>

[**ClusProperties.Count**](clusproperties-count.md)
</dt> </dl>

 

 





