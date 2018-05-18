---
title: ClusPartitions collection
description: Provides access to the partitions of a Physical Disk.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '8a3c602a-a3b1-4b63-8dfa-36200c5c30ab'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["ClusPartitions collection Failover Cluster", "ClusPartitions collection Failover Cluster , described"]
topic_type:
- apiref
api_name:
- ClusPartitions
- ISClusPartitions
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusPartitions collection

\[The **ClusPartitions** collection is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Provides access to the partitions of a [Physical Disk](physical-disk.md).

## Members

The **ClusPartitions** collection has these types of members:

-   [Properties](#properties)

### Properties

The **ClusPartitions** collection has these properties.



| Property                                         | Access type          | Description                                                 |
|:-------------------------------------------------|:---------------------|:------------------------------------------------------------|
| [**Count**](cluspartitions-count.md)<br/> | Read-only<br/> | Returns the number of objects in the collection.<br/> |
| [**Item**](cluspartitions-item.md)<br/>   | Read-only<br/> | Returns a single object from the collection.<br/>     |



 

## Remarks

A **ClusPartitions** collection:

-   Contains [**ClusPartition**](cluspartition-object.md) objects.
-   Is obtained from [**ClusDisk.Partitions**](clusdisk-partitions.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusPartitions is defined as F2E60722-2631-11D1-89F1-00A0C90D061E<br/>   |



## See also

<dl> <dt>

[Property Management Objects](property-management-objects.md)
</dt> </dl>

 

 





