---
title: ClusNodes collection
description: Provides access to the nodes in a cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f35d610f-014a-48cf-aaa4-93e320bcd890
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ClusNodes collection Failover Cluster
- ClusNodes collection Failover Cluster , described
topic_type:
- apiref
api_name:
- ClusNodes
- ISClusNodes
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# ClusNodes collection

\[The **ClusNodes** collection is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Provides access to the [nodes](nodes.md) in a [*cluster*](https://www.bing.com/search?q=*cluster*).

## Members

The **ClusNodes** collection has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ClusNodes** collection has these methods.



| Method                               | Description                                      |
|:-------------------------------------|:-------------------------------------------------|
| [**Refresh**](clusnodes-refresh.md) | Refreshes the data in the collection.<br/> |



 

### Properties

The **ClusNodes** collection has these properties.



| Property                                    | Access type          | Description                                                 |
|:--------------------------------------------|:---------------------|:------------------------------------------------------------|
| [**Count**](clusnodes-count.md)<br/> | Read-only<br/> | Returns the number of objects in the collection.<br/> |
| [**Item**](clusnodes-item.md)<br/>   | Read-only<br/> | Returns a single node from the collection.<br/>       |



 

## Remarks

A **ClusNodes** collection:

-   Contains [**ClusNode**](clusnode-object.md) objects.
-   Is obtained from [**Cluster.Nodes**](cluster-nodes.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusNodes is defined as F2E606FA-2631-11D1-89F1-00A0C90D061E<br/>        |



## See also

<dl> <dt>

[Cluster Management Objects](cluster-management-objects.md)
</dt> </dl>

 

 





