---
title: ClusNetworks collection
description: Provides access to the networks in a cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '7dba0985-16bc-4bda-9f37-275032c07811'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["ClusNetworks collection Failover Cluster", "ClusNetworks collection Failover Cluster , described"]
topic_type:
- apiref
api_name:
- ClusNetworks
- ISClusNetworks
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusNetworks collection

\[The **ClusNetworks** collection is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Provides access to the [networks](networks.md) in a [*cluster*](c-gly.md#-wolf-cluster-gly).

## Members

The **ClusNetworks** collection has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ClusNetworks** collection has these methods.



| Method                                  | Description                                      |
|:----------------------------------------|:-------------------------------------------------|
| [**Refresh**](clusnetworks-refresh.md) | Refreshes the data in the collection.<br/> |



 

### Properties

The **ClusNetworks** collection has these properties.



| Property                                       | Access type          | Description                                                 |
|:-----------------------------------------------|:---------------------|:------------------------------------------------------------|
| [**Count**](clusnetworks-count.md)<br/> | Read-only<br/> | Returns the number of objects in the collection.<br/> |
| [**Item**](clusnetworks-item.md)<br/>   | Read-only<br/> | Returns a single network from the collection.<br/>    |



 

## Remarks

A **ClusNetworks** collection:

-   Contains [**ClusNetwork**](clusnetwork-object.md) objects.
-   Is obtained from [**Cluster.Networks**](cluster-networks.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusNetworks is defined as F2E606F4-2631-11D1-89F1-00A0C90D061E<br/>     |



## See also

<dl> <dt>

[Cluster Management Objects](cluster-management-objects.md)
</dt> </dl>

 

 





