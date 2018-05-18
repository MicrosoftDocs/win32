---
title: Changing Object Names
description: Cluster-aware applications typically allow administrators to control changes to existing cluster object names.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'c2aa451c-516d-47cf-9876-1666795d4a6b'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["cluster objects Failover Cluster ,changing names"]
---

# Changing Object Names

[*Cluster-aware applications*](c-gly.md#-wolf-cluster-aware-application-gly) typically allow administrators to control changes to existing [cluster object](cluster-objects.md) names. As an analogy, most applications allow users to control path and file name changes. In both cases, the user is in the best position to assess the impact of the name change on other applications and to choose a name that is consistent with other names.

The following API elements can be used to safely change object names.



| Name to change           | Function to use                                                     |
|--------------------------|---------------------------------------------------------------------|
| cluster name<br/>  | [**SetClusterName**](setclustername.md)<br/>                 |
| group name<br/>    | [**SetClusterGroupName**](setclustergroupname.md)<br/>       |
| network name<br/>  | [**SetClusterNetworkName**](setclusternetworkname.md)<br/>   |
| resource name<br/> | [**SetClusterResourceName**](setclusterresourcename.md)<br/> |



 

> [!Note]  
>
> -   [Resource DLLs](resource-dlls.md) are notified of [*cluster*](c-gly.md#-wolf-cluster-gly) and [resource](resources.md) name changes with the [CLUSCTL\_RESOURCE\_CLUSTER\_NAME\_CHANGED](clusctl-resource-cluster-name-changed.md) and [CLUSCTL\_RESOURCE\_SET\_NAME](clusctl-resource-set-name.md) control codes.
> -   Object names are stored as [read-only](read-only-properties.md)[common properties](common-properties.md). Thus it is possible to change object names using the [cluster database access functions](cluster-database-access-functions.md), but it is dangerous to do so. The cluster database access functions may not generate all of the required notifications, resulting in unusable objects or an unusable cluster.

 

 

 





