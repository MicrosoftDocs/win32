---
title: Standard Order of Preference
description: The Failover Cluster API may offer more than one way of performing a cluster operation. For example, the PendingTimeout property for a resource can be set through the following API elements.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'd19d7718-16af-43c3-b339-ca500626f57e'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["standard order of preference Failover Cluster", "order of preference Failover Cluster", "Failover Cluster API Failover Cluster , order of preference", "resource DLLs Failover Cluster ,order of preference", "cluster-aware applications Failover Cluster ,order of preference", "application types Failover Cluster ,cluster-aware applications,order of preference"]
---

# Standard Order of Preference

The [Failover Cluster API](the-server-cluster-api.md) may offer more than one way of performing a cluster operation. For example, the [**PendingTimeout**](resources-pendingtimeout.md) property for a [resource](resources.md) can be set through the following API elements.

[**ClusterResourceControl**](clusterresourcecontrol.md) with the [CLUSCTL\_RESOURCE\_SET\_COMMON\_PROPERTIES](clusctl-resource-set-common-properties.md) control code.

[**ResUtilSetPropertyParameterBlock**](resutilsetpropertyparameterblock.md)

[**ResUtilSetPropertyTable**](resutilsetpropertytable.md)

[**ClusterRegSetValue**](clusterregsetvalue.md)

If the Failover Cluster API offers more than one way of performing an operation on a cluster object, the following orders of preference is recommended.

## For cluster-aware applications

1.  Use a [control code function](control-code-functions.md) whenever possible. This maximizes the reliability and security of the operation, and ensures that [resource DLLs](resource-dlls.md) receive proper notification.
2.  Use a [cluster object management function](cluster-object-management-functions.md) if a control code operation is not possible.
3.  Use a [utility function](cluster-utility-functions.md).
4.  Use a [cluster database access functions](cluster-database-access-functions.md) as a last resort.

In general, try not to perform direct updates to the cluster database unless absolutely necessary.

A change to the [cluster database](cluster-database.md) typically has an impact on many different cluster elements. Using indirect API elements allows the Cluster service to ensure that the necessary notifications take place, and that the data is replicated to all nodes.

## For resource DLLs

1.  Use a cluster utility function or a cluster database access function (a "ResUtil" function). A [resource DLL](resource-dlls.md) is expected to access the cluster database, unlike a cluster-aware application.
2.  Use a control code function (but see Cautions).
3.  Use a cluster object management function.

In general, try not to use the Cluster API unless absolutely necessary.

The [Failover Cluster API](the-server-cluster-api.md) is not always available to resource DLLs because it depends on the [Cluster service](cluster-service.md). The [Resource API](resource-api.md), however, is always available to resource DLLs.

 

 




