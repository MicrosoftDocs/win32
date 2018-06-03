---
title: ClusterNames.DomainName property
description: Returns the name of the domain from which the ClusterNames collection came.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2425b375-be4e-4e8f-8b76-68c6fcc7fa92
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- DomainName property Failover Cluster
- DomainName property Failover Cluster , ClusterNames collection
- ClusterNames collection Failover Cluster , DomainName property
topic_type:
- apiref
api_name:
- ClusterNames.DomainName
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusterNames.DomainName property

\[The **DomainName** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the name of the domain from which the [**ClusterNames**](clusternames-collection.md) collection came.

This property is read-only.

## Syntax


```VB
ClusterNames.DomainName
```



## Property value

**String** that receives the name of the current domain.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusterNames is defined as F2E606EC-2631-11D1-89F1-00A0C90D061E<br/>     |



## See also

<dl> <dt>

[**ClusterNames**](clusternames-collection.md)
</dt> </dl>

 

 





