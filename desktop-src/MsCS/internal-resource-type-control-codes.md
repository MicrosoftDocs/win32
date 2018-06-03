---
title: Internal Resource Type Control Codes
description: The following lists all of the internal resource type control codes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c72bfbe4-3893-4605-b942-0d47c391010c
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- resource type control codes Failover Cluster ,internal
- control codes Failover Cluster ,resource type,internal
- resource types Failover Cluster ,control codes, internal
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Internal Resource Type Control Codes

The following lists all of the internal resource type control codes.

## In this section

<dl> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_CLUSTER\_VERSION\_CHANGED](clusctl-resource-type-cluster-version-changed.md)
</dt> <dd>

[Internal](internal-control-codes.md). Indicates that the [cluster version](https://www.bing.com/search?q=cluster version) has changed. [Resource DLLs](resource-dlls.md) receive this [control code](about-control-codes.md) through the [**ResourceTypeControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_type_control_routine) entry point, which is called once for every resource type supported by the DLL.

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_EVICT\_NODE](clusctl-resource-type-evict-node.md)
</dt> <dd>

[Internal](internal-control-codes.md). Indicates that a [node](nodes.md) is being permanently removed from the cluster. [Resource DLLs](resource-dlls.md) receive this [control code](about-control-codes.md) through the [**ResourceTypeControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_type_control_routine) entry point, which is called once for every resource type supported by the DLL.

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_FIXUP\_ON\_UPGRADE](clusctl-resource-type-fixup-on-upgrade.md)
</dt> <dd>

[Internal](internal-control-codes.md). Indicates that a [node](nodes.md) in the [cluster](https://www.bing.com/search?q=cluster) has just completed an upgrade of the [Cluster service](cluster-service.md). [Resource DLLs](resource-dlls.md) receive this [control code](about-control-codes.md) through the [**ResourceTypeControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_type_control_routine) entry point function, which is called once for every resource type supported by the DLL.

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_HOLD\_IO](clusctl-resource-type-hold-io.md)
</dt> <dd>

The [CLUSCTL\_RESOURCE\_TYPE\_HOLD\_IO](clusctl-resource-type-hold-io.md) [control code](about-control-codes.md) is reserved for future use.

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_INSTALL\_NODE](clusctl-resource-type-install-node.md)
</dt> <dd>

[Internal](internal-control-codes.md). Indicates that a new [node](nodes.md) has been added to the [cluster](https://www.bing.com/search?q=cluster). [Resource DLLs](resource-dlls.md) receive this [control code](about-control-codes.md) through the [**ResourceTypeControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_type_control_routine) entry point function, which is called once for every resource type supported by the DLL.

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_PREPARE\_UPGRADE](clusctl-resource-type-prepare-upgrade.md)
</dt> <dd>

[Internal](internal-control-codes.md). Indicates that a [node](nodes.md) in the [cluster](https://www.bing.com/search?q=cluster) is preparing for an upgrade of the [Cluster service](cluster-service.md). [Resource DLLs](resource-dlls.md) receive this [control code](about-control-codes.md) through the [**ResourceTypeControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_type_control_routine) entry point function, which is called once for every resource type supported by the DLL.

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_REPLICATION\_GET\_LOG\_INFO](clusctl-resource-type-replication-get-log-info.md)
</dt> <dd>

[Internal](internal-control-codes.md). Retrieves log information from a replication group.

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_RESUME\_IO](clusctl-resource-type-resume-io.md)
</dt> <dd>

The [CLUSCTL\_RESOURCE\_TYPE\_RESUME\_IO](clusctl-resource-type-resume-io.md) [control code](about-control-codes.md) is reserved for future use.

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_STARTING\_PHASE1](clusctl-resource-type-starting-phase1.md)
</dt> <dd>

An [internal control code](internal-control-codes.md) that indicates that the [Cluster service](cluster-service.md) is starting on one of the [cluster](https://www.bing.com/search?q=cluster) nodes. [Resource DLLs](resource-dlls.md) receive this [control code](about-control-codes.md) through the [**ResourceTypeControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_type_control_routine) entry point function, which is called once for every resource type supported by the DLL.

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_STARTING\_PHASE2](clusctl-resource-type-starting-phase2.md)
</dt> <dd>

An [internal control code](internal-control-codes.md) that indicates that a node in the [cluster](https://www.bing.com/search?q=cluster) has just completed a startup of the [Cluster service](https://www.bing.com/search?q=Cluster service). [Resource DLLs](resource-dlls.md) receive this [control code](about-control-codes.md) through the [**ResourceTypeControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_type_control_routine) entry point function, which is called once for every [resource type](https://www.bing.com/search?q=resource type) supported by the DLL.

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_UPGRADE\_COMPLETED](clusctl-resource-type-upgrade-completed.md)
</dt> <dd>

[Internal](internal-control-codes.md). Indicates that a [node](nodes.md) in the [cluster](https://www.bing.com/search?q=cluster) is preparing for an upgrade of the [Cluster service](cluster-service.md). [Resource DLLs](resource-dlls.md) receive this [control code](about-control-codes.md) through the [**ResourceTypeControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_type_control_routine) entry point function, which is called once for every resource type supported by the DLL.

</dd> </dl>

## Related topics

<dl> <dt>

[Resource Type Control Codes](resource-type-control-codes.md)
</dt> <dt>

[**ClusterResourceTypeControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcetypecontrol)
</dt> <dt>

[**ResourceTypeControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_type_control_routine)
</dt> </dl>

 

 




