---
title: ClusPropertyValues.Item property
description: Single property value from a ClusPropertyValues collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8980e2ed-3822-4ecf-80d7-f3be42e92161
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Item property Failover Cluster
- Item property Failover Cluster , ClusPropertyValues collection
- ClusPropertyValues collection Failover Cluster , Item property
topic_type:
- apiref
api_name:
- ClusPropertyValues.Item
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusPropertyValues.Item property

\[The **Item** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns a single [*property value*](https://www.bing.com/search?q=*property value*) from a [**ClusPropertyValues**](cluspropertyvalues-collection.md) collection.

This property is read-only.

## Syntax


```VB
ClusPropertyValues.Item( _
  ByVal varIndex _
)
```



## Property value

A [**ClusPropertyValue**](cluspropertyvalue-object.md) object that receives the specified property value.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>               |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>     |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl>   |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl>   |
| IID<br/>                      | IID\_ISClusPropertyValues is defined as F2E6071C-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[**ClusPropertyValues**](cluspropertyvalues-collection.md)
</dt> <dt>

[**ClusProperty**](clusproperty-object.md)
</dt> <dt>

[**ClusPropertyValues.Count**](cluspropertyvalues-count.md)
</dt> </dl>

 

 





