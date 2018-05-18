---
title: ClusNetInterfaces.Item property
description: Retrieves a single network interface from a ClusNetInterfaces collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '4fa4270b-9fad-481a-ac53-c8a7d5c55949'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Item property Failover Cluster", "Item property Failover Cluster , ClusNetInterfaces collection", "ClusNetInterfaces collection Failover Cluster , Item property"]
topic_type:
- apiref
api_name:
- ClusNetInterfaces.Item
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusNetInterfaces.Item property

\[The **Item** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Retrieves a single [network interface](network-interfaces.md) from a [**ClusNetInterfaces**](clusnetinterfaces-collection.md) collection.

This property is read-only.

## Syntax


```VB
ClusNetInterfaces.Item( _
  ByVal varIndex _
)
```



## Property value

A [**ClusNetInterface**](clusnetinterface-object.md) object that receives the specified network interface.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>              |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>    |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl>  |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl>  |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl>  |
| IID<br/>                      | IID\_ISClusNetInterfaces is defined as F2E606F0-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[**ClusNetInterface**](clusnetinterface-object.md)
</dt> <dt>

[**ClusNetInterfaces**](clusnetinterfaces-collection.md)
</dt> <dt>

[**ClusNetInterfaces.Count**](clusnetinterfaces-count.md)
</dt> </dl>

 

 





