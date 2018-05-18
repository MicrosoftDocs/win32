---
title: ClusResGroupResources.Item property
description: Returns a single resource from the ClusResGroupResources collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '5eba54e1-5c55-46b0-97b9-0104cfb4134c'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Item property Failover Cluster", "Item property Failover Cluster , ClusResGroupResources class", "ClusResGroupResources class Failover Cluster , Item property"]
topic_type:
- apiref
api_name:
- ClusResGroupResources.Item
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusResGroupResources.Item property

\[The **Item** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns a single [resource](resources.md) from the [**ClusResGroupResources**](clusresgroupresources-collection.md) collection.

This property is read-only.

## Syntax


```VB
ClusResGroupResources.Item( _
  ByVal varIndex _
)
```



## Property value

A [**ClusResource**](clusresource-object.md) object that receives the specified resource.

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>                  |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>        |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl>      |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl>      |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl>      |
| IID<br/>                      | IID\_ISClusResGroupResources is defined as F2E606EA-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[**ClusResGroupResources**](clusresgroupresources-collection.md)
</dt> <dt>

[**ClusResource**](clusresource-object.md)
</dt> <dt>

[**ClusResGroupResources.Count**](clusresgroupresources-count.md)
</dt> </dl>

 

 





