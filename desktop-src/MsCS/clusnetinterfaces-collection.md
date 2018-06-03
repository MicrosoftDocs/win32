---
title: ClusNetInterfaces collection
description: Provides access to the network interfaces in a cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7d0dc4fd-733c-4a2a-9136-7dc0089b213d
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ClusNetInterfaces collection Failover Cluster
- ClusNetInterfaces collection Failover Cluster , described
topic_type:
- apiref
api_name:
- ClusNetInterfaces
- ISClusNetInterfaces
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# ClusNetInterfaces collection

\[The **ClusNetInterfaces** collection is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Provides access to the [network interfaces](network-interfaces.md) in a [*cluster*](https://www.bing.com/search?q=*cluster*).

## Members

The **ClusNetInterfaces** collection has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ClusNetInterfaces** collection has these methods.



| Method                                       | Description                                      |
|:---------------------------------------------|:-------------------------------------------------|
| [**Refresh**](clusnetinterfaces-refresh.md) | Refreshes the data in the collection.<br/> |



 

### Properties

The **ClusNetInterfaces** collection has these properties.



| Property                                            | Access type          | Description                                                        |
|:----------------------------------------------------|:---------------------|:-------------------------------------------------------------------|
| [**Count**](clusnetinterfaces-count.md)<br/> | Read-only<br/> | Returns the number of objects in the collection.<br/>        |
| [**Item**](clusnetinterfaces-item.md)<br/>   | Read-only<br/> | Returns a single network interface from the collection.<br/> |



 

## Remarks

A **ClusNetInterfaces** collection:

-   Contains [**ClusNetInterface**](clusnetinterface-object.md) objects.
-   Is obtained from [**Cluster.NetInterfaces**](cluster-netinterfaces.md).

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>              |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>    |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl>  |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl>  |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl>  |
| IID<br/>                      | IID\_ISClusNetInterfaces is defined as F2E606F0-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[Cluster Management Objects](cluster-management-objects.md)
</dt> </dl>

 

 





