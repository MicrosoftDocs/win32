---
title: ClusDisks.Item property
description: ClusDisk object that represents a single disk from a ClusDisks collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '4199a230-1e1d-45d5-b93b-5f12b58c8f35'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Item property Failover Cluster", "Item property Failover Cluster , ClusDisks class", "ClusDisks class Failover Cluster , Item property"]
topic_type:
- apiref
api_name:
- ClusDisks.Item
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusDisks.Item property

\[The **Item** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns a [**ClusDisk**](clusdisk-object.md) object that represents a single disk from a [**ClusDisks**](clusdisks-collection.md) collection.

This property is read-only.

## Syntax


```VB
ClusDisks.Item( _
  ByVal varIndex _
)
```



## Property value

A [**ClusDisk**](clusdisk-object.md) object that receives the specified properties.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusDisks is defined as F2E60726-2631-11D1-89F1-00A0C90D061E<br/>        |



## See also

<dl> <dt>

[**ClusDisks**](clusdisks-collection.md)
</dt> <dt>

[**ClusDisk**](clusdisk-object.md)
</dt> <dt>

[**ClusDisks.Count**](clusdisks-count.md)
</dt> </dl>

 

 





