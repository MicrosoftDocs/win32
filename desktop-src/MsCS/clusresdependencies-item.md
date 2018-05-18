---
title: ClusResDependencies.Item property
description: Retrieves a single resource from a ClusResDependencies collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '9f455180-433c-4beb-9470-0db1976ffac1'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Item property Failover Cluster", "Item property Failover Cluster , ClusResDependencies class", "ClusResDependencies class Failover Cluster , Item property"]
topic_type:
- apiref
api_name:
- ClusResDependencies.Item
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusResDependencies.Item property

\[The **Item** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Retrieves a single [resource](resources.md) from a [**ClusResDependencies**](clusresdependencies-collection.md) collection.

This property is read-only.

## Syntax


```VB
ClusResDependencies.Item( _
  ByVal varIndex _
)
```



## Property value

A [**ClusResource**](clusresource-object.md) object that receives the specified resource.

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>                |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>      |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl>    |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl>    |
| IID<br/>                      | IID\_ISClusResDependencies is defined as F2E60704-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[**ClusResDependencies**](clusresdependencies-collection.md)
</dt> <dt>

[**ClusResDependencies.Count**](clusresdependencies-count.md)
</dt> <dt>

[**ClusResource**](clusresource-object.md)
</dt> </dl>

 

 





