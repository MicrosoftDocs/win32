---
title: Copying Resource Configurations
description: Depending on the resource type of a resource, it may be possible to use an existing resource configuration as a template for a new resource configuration.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4c64ee7e-4658-4e5d-8319-5d8754a12781
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- resources Failover Cluster ,copying configurations
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Copying Resource Configurations

Depending on the [resource type](resource-types.md) of a [resource](resources.md), it may be possible to use an existing resource configuration as a template for a new resource configuration.

**To Copy a Resource Configuration**

1.  Get a handle to the original resource by calling [**OpenClusterResource**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_open_cluster_resource?branch=master).

2.  Get the resource type of the original resource. Call [**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master) with the [CLUSCTL\_RESOURCE\_GET\_RESOURCE\_TYPE](clusctl-resource-get-resource-type.md) control code.

3.  Create a resource of that type. (See [Creating Resources](creating-resources.md).) Note that the name of the new resource cannot be the same as the original if it is created in the same cluster.

4.  Duplicate the original resource's [read/write properties](read-write-properties.md):

    1.  Retrieve the original resource's read/write [common properties](common-properties.md) into a [property list](property-lists.md) by using [CLUSCTL\_RESOURCE\_GET\_COMMON\_PROPERTIES](clusctl-resource-get-common-properties.md).
    2.  Use the property list obtained in the previous step to set the new resource's read/write common properties with [CLUSCTL\_RESOURCE\_SET\_COMMON\_PROPERTIES](clusctl-resource-set-common-properties.md).
    3.  Retrieve the original's read/write [private properties](private-properties.md) into a property list using [CLUSCTL\_RESOURCE\_GET\_PRIVATE\_PROPERTIES](clusctl-resource-get-private-properties.md).
    4.  Use the property list obtained in the previous step to set the new resource's read/write private properties with [CLUSCTL\_RESOURCE\_SET\_PRIVATE\_PROPERTIES](clusctl-resource-set-private-properties.md).

5.  If the original resource has registry and crypto checkpoints, do the following:

    1.  Retrieve the original's crypto checkpoints using [CLUSCTL\_RESOURCE\_GET\_CRYPTO\_CHECKPOINTS](clusctl-resource-add-crypto-checkpoint.md).
    2.  Use the data obtained in the previous step and the Crypto API to create crypto keys for the new resource.
    3.  Checkpoint the crypto keys created in the previous step using [CLUSCTL\_RESOURCE\_ADD\_CRYPTO\_CHECKPOINT](clusctl-resource-add-crypto-checkpoint.md).
    4.  Retrieve the original's registry checkpoints using [CLUSCTL\_RESOURCE\_GET\_REGISTRY\_CHECKPOINTS](clusctl-resource-add-registry-checkpoint.md).
    5.  Use the registry functions to create registry keys for the new resource.
    6.  Checkpoint the registry keys created in the previous step using [CLUSCTL\_RESOURCE\_ADD\_REGISTRY\_CHECKPOINT](clusctl-resource-add-registry-checkpoint.md).

6.  Enumerate the dependencies of the original resource. See [Enumerating Objects](enumerating-objects.md).

7.  Repeat steps 2 through 6 for each dependency until the entire dependency tree has been copied.

 

 




