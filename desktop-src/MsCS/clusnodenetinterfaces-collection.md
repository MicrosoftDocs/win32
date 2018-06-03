---
title: ClusNodeNetInterfaces collection
description: Provides access to the network interfaces installed in a node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d40bd8bd-b822-4069-bc9c-b7fefc66c8d0
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ClusNodeNetInterfaces collection Failover Cluster
- ClusNodeNetInterfaces collection Failover Cluster , described
topic_type:
- apiref
api_name:
- ClusNodeNetInterfaces
- ISClusNodeNet
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# ClusNodeNetInterfaces collection

\[The **ClusNodeNetInterfaces** collection is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Provides access to the [network interfaces](network-interfaces.md) installed in a [node](nodes.md).

## Members

The **ClusNodeNetInterfaces** collection has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ClusNodeNetInterfaces** collection has these methods.



| Method                                           | Description                                      |
|:-------------------------------------------------|:-------------------------------------------------|
| [**Refresh**](clusresgroupresources-refresh.md) | Refreshes the data in the collection.<br/> |



 

### Properties

The **ClusNodeNetInterfaces** collection has these properties.



| Property                                                | Access type          | Description                                                 |
|:--------------------------------------------------------|:---------------------|:------------------------------------------------------------|
| [**Count**](clusresgroupresources-count.md)<br/> | Read-only<br/> | Returns the number of objects in the collection.<br/> |
| [**Item**](clusresgroupresources-item.md)<br/>   | Read-only<br/> | Returns a single node from the collection.<br/>       |



 

## Remarks

A **ClusNodeNetInterfaces** collection:

-   Contains [**ClusNetInterface**](clusnetinterface-object.md) objects.
-   Is obtained from [**ClusNode.NetInterfaces**](clusnode-netinterfaces.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusNodeNet is defined as F2E606FC-2631-11D1-89F1-00A0C90D061E<br/>      |



## See also

<dl> <dt>

[Node Management Objects](node-management-objects.md)
</dt> </dl>

 

 





