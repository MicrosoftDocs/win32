---
title: ClusResGroupResources.Count property
description: Number of resources in the ClusResGroupResources collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '26d90188-e3b7-4546-9305-a2fc50c09c28'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Count property Failover Cluster", "Count property Failover Cluster , ClusResGroupResources class", "ClusResGroupResources class Failover Cluster , Count property"]
topic_type:
- apiref
api_name:
- ClusResGroupResources.Count
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusResGroupResources.Count property

\[The **Count** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the number of [resources](resources.md) in the [**ClusResGroupResources**](clusresgroupresources-collection.md) collection.

This property is read-only.

## Syntax


```VB
ClusResGroupResources.Count
```



## Property value

**Long** indicating the number of resources in the collection.

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
</dt> </dl>

 

 





