---
title: ClusNetworkNetInterfaces.Item property
description: Single network interface from a ClusNetworkNetInterfaces collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 17eeed87-ca6f-4894-bb4a-eeda8cdcfec9
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Item property Failover Cluster
- Item property Failover Cluster , ClusNetworkNetInterfaces collection
- ClusNetworkNetInterfaces collection Failover Cluster , Item property
topic_type:
- apiref
api_name:
- ClusNetworkNetInterfaces.Item
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusNetworkNetInterfaces.Item property

\[The **Item** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Retrieves a single [network interface](network-interfaces.md) from a [**ClusNetworkNetInterfaces**](clusnetworknetinterfaces-collection.md) collection.

This property is read-only.

## Syntax


```VB
ClusNetworkNetInterfaces.Item( _
  ByVal varIndex _
)
```



## Property value

A [**ClusNetInterface**](clusnetinterface-object.md) object that receives the specified network interface.

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>                     |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>           |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl>         |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl>         |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl>         |
| IID<br/>                      | IID\_ISClusNetworkNetInterfaces is defined as F2E606F6-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[**ClusNetworkNetInterfaces**](clusnetworknetinterfaces-collection.md)
</dt> <dt>

[**ClusNetInterface**](clusnetinterface-object.md)
</dt> <dt>

[**ClusNetworkNetInterfaces.Count**](clusnetworknetinterfaces-count.md)
</dt> </dl>

 

 





