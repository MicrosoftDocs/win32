---
title: ClusResources.Item property
description: Retrieves a single ClusResource object from the ClusResources collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4d28c219-a308-4e07-9521-a80066ec91e3
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Item property Failover Cluster
- Item property Failover Cluster , ClusResources collection
- ClusResources collection Failover Cluster , Item property
topic_type:
- apiref
api_name:
- ClusResources.Item
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusResources.Item property

\[The **Item** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Retrieves a single [**ClusResource**](clusresource-object.md) object from the [**ClusResources**](clusresources-collection.md) collection.

This property is read-only.

## Syntax


```VB
ClusResources.Item( _
  ByVal varIndex _
)
```



## Property value

A [**ClusResource**](clusresource-object.md) object that receives the specified [resource](resources.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusResources is defined as F2E6070C-2631-11D1-89F1-00A0C90D061E<br/>    |



## See also

<dl> <dt>

[**ClusResource**](clusresource-object.md)
</dt> <dt>

[**ClusResources**](clusresources-collection.md)
</dt> <dt>

[**ClusResources.Count**](clusresources-count.md)
</dt> </dl>

 

 





