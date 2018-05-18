---
title: ClusApplication object
description: Provides access to the DomainNames and ClusterNames collections and opens a connection to a specified cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '2f837658-18f5-44c9-b743-1980a616e71a'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["ClusApplication object Failover Cluster", "ClusApplication object Failover Cluster , described"]
topic_type:
- apiref
api_name:
- ClusApplication
- ISClusApplication
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusApplication object

\[The **ClusApplication** object is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

The **ClusApplication** object provides access to the [**DomainNames**](domainnames-collection.md) and [**ClusterNames**](clusternames-collection.md) collections and opens a connection to a specified [*cluster*](c-gly.md#-wolf-cluster-gly).

## Members

The **ClusApplication** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ClusApplication** object has these methods.



| Method                                             | Description                                 |
|:---------------------------------------------------|:--------------------------------------------|
| [**OpenCluster**](clusapplication-opencluster.md) | Opens a connection to a cluster.<br/> |



 

### Properties

The **ClusApplication** object has these properties.



| Property                                                        | Description                                                   |
|:----------------------------------------------------------------|:--------------------------------------------------------------|
| [**ClusterNames**](clusapplication-clusternames.md)<br/> | Returns the names of all the clusters in a domain.<br/> |
| [**DomainNames**](clusapplication-domainnames.md)<br/>   | Returns the names of all available domains.<br/>        |



 

## Remarks

**ClusApplication** is a top-level object, allowing new object instances to be created.

## Examples


```VB
Dim objApplication as ClusApplication
Set objApplication = New ClusApplication
```



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusApplication is defined as F2E606E6-2631-11D1-89F1-00A0C90D061E<br/>  |



## See also

<dl> <dt>

[Application Management Objects](application-management-objects.md)
</dt> </dl>

 

 





