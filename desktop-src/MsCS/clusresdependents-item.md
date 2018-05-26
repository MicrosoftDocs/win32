---
title: ClusResDependents.Item property
description: Retrieves a single resource from a ClusResDependents collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 24deb6b6-1e1e-4878-a8fd-3c8496aa255f
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Item property Failover Cluster
- Item property Failover Cluster , ClusResDependents class
- ClusResDependents class Failover Cluster , Item property
topic_type:
- apiref
api_name:
- ClusResDependents.Item
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusResDependents.Item property

\[The **Item** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Retrieves a single [resource](resources.md) from a [**ClusResDependents**](clusresdependents-collection.md) collection.

This property is read-only.

## Syntax


```VB
ClusResDependents.Item( _
  ByVal varIndex _
)
```



## Property value

A [**ClusResource**](clusresource-object.md) object that receives the specified resource.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>              |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>    |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl>  |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl>  |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl>  |
| IID<br/>                      | IID\_ISClusResDependents is defined as F2E6072E-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[**ClusResDependents**](clusresdependents-collection.md)
</dt> <dt>

[**ClusResDependents.Count**](clusresdependents-count.md)
</dt> <dt>

[**ClusResource**](clusresource-object.md)
</dt> </dl>

 

 





