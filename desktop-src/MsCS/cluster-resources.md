---
title: Cluster.Resources property
description: Returns a ClusResources collection providing access to the resources in a cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'fdfdd1de-fa4a-4bfb-80e1-15b2141d488b'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Resources property Failover Cluster", "Resources property Failover Cluster , Cluster object", "Cluster object Failover Cluster , Resources property"]
topic_type:
- apiref
api_name:
- Cluster.Resources
- ISCluster.get_Resources
api_location:
- MsClus.dll
api_type:
- COM
---

# Cluster.Resources property

\[The **Resources** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns a [**ClusResources**](clusresources-collection.md) collection providing access to the [resources](resources.md) in a [*cluster*](c-gly.md#-wolf-cluster-gly).

This property is read-only.

## Syntax


```VB
Cluster.Resources
```



## Property value

A [**ClusResources**](clusresources-collection.md) collection that receives the cluster resources.

## Remarks

The [**ClusResources**](clusresources-collection.md) collection returned by the [**Cluster**](cluster-object.md) object's **Resources** property provides access to all the resources in the cluster. To retrieve information about all of the resources owned by a particular [group](groups.md), use the [**ClusResGroup.Resources**](clusresgroup-resources.md) property.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISCluster is defined as F2E606E4-2631-11D1-89F1-00A0C90D061E<br/>          |



## See also

<dl> <dt>

[**ClusResGroup.Resources**](clusresgroup-resources.md)
</dt> <dt>

[**ClusResources**](clusresources-collection.md)
</dt> <dt>

[**Cluster**](cluster-object.md)
</dt> </dl>

 

 





