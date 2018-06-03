---
title: ClusterNames collection
description: Provides access to the names of the clusters in a domain.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c4e29498-c4e2-4351-8eed-05bc73437485
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ClusterNames collection Failover Cluster
- ClusterNames collection Failover Cluster , described
topic_type:
- apiref
api_name:
- ClusterNames
- ISClusterNames
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# ClusterNames collection

\[The **ClusterNames** collection is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Provides access to the names of the [*clusters*](https://www.bing.com/search?q=*clusters*) in a domain.

## Members

The **ClusterNames** collection has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ClusterNames** collection has these methods.



| Method                                  | Description                                      |
|:----------------------------------------|:-------------------------------------------------|
| [**Refresh**](clusternames-refresh.md) | Refreshes the data in the collection.<br/> |



 

### Properties

The **ClusterNames** collection has these properties.



| Property                                                 | Description                                                                     |
|:---------------------------------------------------------|:--------------------------------------------------------------------------------|
| [**Count**](clusternames-count.md)<br/>           | Returns the number of clusters in the domain.<br/>                        |
| [**DomainName**](clusternames-domainname.md)<br/> | Returns the name of the domain that is the source of the collection.<br/> |
| [**Item**](clusternames-item.md)<br/>             | Returns a name of a cluster from the collection.<br/>                     |



 

## Remarks

A **ClusterNames** collection:

-   Contains cluster names.
-   Is obtained from [**ClusApplication.ClusterNames**](clusapplication-clusternames.md).

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

[Application Management Objects](application-management-objects.md)
</dt> </dl>

 

 





