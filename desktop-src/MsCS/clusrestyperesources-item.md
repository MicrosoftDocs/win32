---
title: ClusResTypeResources.Item property
description: Returns a single ClusResource object from a ClusResTypeResources collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 701b9974-934b-401d-a7e0-13246b5d5606
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Item property Failover Cluster
- Item property Failover Cluster , ClusResTypeResources class
- ClusResTypeResources class Failover Cluster , Item property
topic_type:
- apiref
api_name:
- ClusResTypeResources.Item
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusResTypeResources.Item property

\[The **Item** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns a single [**ClusResource**](clusresource-object.md) object from a [**ClusResTypeResources**](clusrestyperesources-collection.md) collection.

This property is read-only.

## Syntax


```VB
ClusResTypeResources.Item( _
  ByVal varIndex _
)
```



## Property value

A [**ClusResource**](clusresource-object.md) object that receives the specified resource.

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>                 |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>       |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl>     |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl>     |
| IID<br/>                      | IID\_ISClusResTypeResources is defined as F2E60714-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[**ClusResource**](clusresource-object.md)
</dt> <dt>

[**ClusResTypeResources**](clusrestyperesources-collection.md)
</dt> <dt>

[**ClusResTypeResources.Count**](clusrestyperesources-count.md)
</dt> </dl>

 

 





