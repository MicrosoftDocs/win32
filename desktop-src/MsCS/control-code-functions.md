---
title: Control Code Functions
description: Control code functions use control codes as parameters in order to perform cluster operations.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 89ae667e-6ad9-453e-b370-b3d6a67172a2
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- control codes Failover Cluster ,functions
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Control Code Functions

Control code functions use [control codes](control-codes.md) as parameters in order to perform cluster operations. Each control code function is an interface to a specific type of cluster object, and each control code defines an operation that the control code function can perform on that type of cluster object. There is one control code function for each cluster object. However, there are multiple control codes for each control code function.

## In this section

<dl> <dt>

[**ClusterControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clustercontrol)
</dt> <dd>

Initiates an operation that affects a [cluster](https://www.bing.com/search?q=cluster).

</dd> <dt>

[**ClusterGroupControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clustergroupcontrol)
</dt> <dd>

Initiates an operation that affects a [group](groups.md). The operation performed depends on the [control code](control-codes.md) passed to the *dwControlCode* parameter.

</dd> <dt>

[*ClusterGroupSetControl*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_group_groupset_control)
</dt> <dd>

Initiates an operation affecting a groupset.

</dd> <dt>

[**ClusterNetInterfaceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusternetinterfacecontrol)
</dt> <dd>

Initiates an operation that affects a [network interface](network-interfaces.md). The operation performed depends on the [control code](control-codes.md) passed to the *dwControlCode* parameter.

</dd> <dt>

[**ClusterNetworkControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusternetworkcontrol)
</dt> <dd>

Initiates an operation on a [network](networks.md). The operation performed depends on the [control code](control-codes.md) passed to the *dwControlCode* parameter.

</dd> <dt>

[**ClusterNodeControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusternodecontrol)
</dt> <dd>

Initiates an operation that affects a [node](nodes.md). The operation performed depends on the [control code](control-codes.md) passed to the *dwControlCode* parameter.

</dd> <dt>

[**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol)
</dt> <dd>

Initiates an operation affecting a [resource](resources.md). The operation performed depends on the [control code](control-codes.md) passed to the *dwControlCode* parameter.

</dd> <dt>

[**ClusterResourceControlAsUser**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrolasuser)
</dt> <dd>

Initiates an operation affecting a [resource](resources.md).

</dd> <dt>

[**ClusterResourceTypeControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcetypecontrol)
</dt> <dd>

Initiates an operation affecting a [resource type](resource-types.md). The operation performed depends on the [control code](control-codes.md) passed to the *dwControlCode* parameter.

</dd> <dt>

[**ClusterResourceTypeControlAsUser**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcetypecontrolasuser)
</dt> <dd>

Initiates an operation affecting a [resource type](resource-types.md).

</dd> </dl>

## Related topics

<dl> <dt>

[Failover Cluster Functions](failover-cluster-functions.md)
</dt> <dt>

[Failover Cluster Control Codes](control-codes.md)
</dt> <dt>

[About Control Codes](about-control-codes.md)
</dt> <dt>

[Using Control Codes](using-control-codes.md)
</dt> </dl>

 

 




