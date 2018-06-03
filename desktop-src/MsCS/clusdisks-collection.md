---
title: ClusDisks collection
description: Provides access to the cluster-capable Physical Disks available to a resource type.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2823ccb2-5fb2-4e37-b842-340703165871
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ClusDisks collection Failover Cluster
- ClusDisks collection Failover Cluster , described
topic_type:
- apiref
api_name:
- ClusDisks
- ISClusDisks
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# ClusDisks collection

\[The **ClusDisks** collection is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Provides access to the [*cluster-capable*](https://www.bing.com/search?q=*cluster-capable*) [Physical Disks](creating-physical-disk-resources.md) available to a [resource type](resource-types.md).

## Members

The **ClusDisks** collection has these types of members:

-   [Properties](#properties)

### Properties

The **ClusDisks** collection has these properties.



| Property                                              | Description                                                 |
|:------------------------------------------------------|:------------------------------------------------------------|
| [**Count**](clusdisks-count.md)<br/>           | Returns the number of objects in the collection.<br/> |
| [**Item**](clusresgroupresources-item.md)<br/> | Returns a single object from the collection.<br/>     |



 

## Remarks

A **ClusDisks** collection contains [**ClusDisk**](clusdisk-object.md) objects. It is obtained from [**ClusResType.AvailableDisks**](clusrestype-availabledisks.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusDisks is defined as F2E60726-2631-11D1-89F1-00A0C90D061E<br/>        |



## See also

<dl> <dt>

[Property Management Objects](property-management-objects.md)
</dt> </dl>

 

 





