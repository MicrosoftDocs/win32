---
title: Group Control Codes
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 41f93d49-c021-4fcb-9d38-f801702b9e51
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
description: 
keywords:
- group control codes Failover Cluster
- control codes Failover Cluster ,group
- groups Failover Cluster ,control codes
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Group Control Codes

The [Failover Cluster API](the-server-cluster-api.md) defines the following [*external control codes*](https://www.bing.com/search?q=*external control codes*) for [*groups*](https://www.bing.com/search?q=*groups*) (there are no [*internal control codes*](https://www.bing.com/search?q=*internal control codes*) defined for groups):

Group control codes use the **CLUS\_OBJECT\_GROUP** value of the [**CLUSTER\_CONTROL\_OBJECT**](/previous-versions/windows/desktop/api/ClusAPI/ne-clusapi-cluster_control_object) enumeration to indicate that the control code applies to cluster groups. For more information about control codes, see [Control Code Architecture](control-code-architecture.md).

Group control codes are enumerated by the [**CLUSCTL\_GROUP\_CODES**](/previous-versions/windows/desktop/api/ClusAPI/ne-clusapi-clusctl_group_codes) enumeration.

## In this section

<dl> <dt>

[CLUSCTL\_GROUP\_ENUM\_COMMON\_PROPERTIES](clusctl-group-enum-common-properties.md)
</dt> <dd>

Retrieves a list of the read/write [group common property](group-common-properties.md) names for a [group](groups.md).

</dd> <dt>

[CLUSCTL\_GROUP\_ENUM\_PRIVATE\_PROPERTIES](clusctl-group-enum-private-properties.md)
</dt> <dd>

Retrieves a list of the private property names for a [group](groups.md).

</dd> <dt>

[CLUSCTL\_GROUP\_GET\_CHARACTERISTICS](clusctl-group-get-characteristics.md)
</dt> <dd>

Retrieves the intrinsic characteristics of a [group](groups.md).

</dd> <dt>

[CLUSCTL\_GROUP\_GET\_COMMON\_PROPERTIES](clusctl-group-get-common-properties.md)
</dt> <dd>

Retrieves the read/write [group common properties](group-common-properties.md) for a [group](groups.md). Applications use this [control code](about-control-codes.md) as a [**ClusterGroupControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clustergroupcontrol) parameter.

</dd> <dt>

[CLUSCTL\_GROUP\_GET\_COMMON\_PROPERTY\_FMTS](clusctl-group-get-common-property-fmts.md)
</dt> <dd>

Retrieves a [property list](property-lists.md) describing the format of each [group common property](group-common-properties.md).

</dd> <dt>

[CLUSCTL\_GROUP\_GET\_FAILURE\_INFO](clusctl-group-get-failure-info.md)
</dt> <dd>

Retrieves information about a group failure.

</dd> <dt>

[CLUSCTL\_GROUP\_GET\_FLAGS](clusctl-group-get-flags.md)
</dt> <dd>

Retrieves the flags that are set for a [group](groups.md).

</dd> <dt>

[CLUSCTL\_GROUP\_GET\_ID](clusctl-group-get-id.md)
</dt> <dd>

Retrieves the [cluster database](cluster-database.md) subkey identifier for a [group](groups.md).

</dd> <dt>

[CLUSCTL\_GROUP\_GET\_LAST\_MOVE\_TIME](clusctl-group-get-last-move-time.md)
</dt> <dd>

Gets the last time a resource group moved.

</dd> <dt>

[CLUSCTL\_GROUP\_GET\_NAME](clusctl-group-get-name.md)
</dt> <dd>

Retrieves the name of a [group](groups.md).

</dd> <dt>

[CLUSCTL\_GROUP\_GET\_PRIVATE\_PROPERTIES](clusctl-group-get-private-properties.md)
</dt> <dd>

Retrieves the read/write [private properties](private-properties.md) for a [group](groups.md).

</dd> <dt>

[CLUSCTL\_GROUP\_GET\_PRIVATE\_PROPERTY\_FMTS](clusctl-group-get-private-property-fmts.md)
</dt> <dd>

The [CLUSCTL\_NETINTERFACE\_GET\_PRIVATE\_PROPERTY\_FMTS](clusctl-netinterface-get-private-property-fmts.md) [control code](about-control-codes.md) is not supported and fails with **ERROR\_INVALID\_FUNCTION**.

</dd> <dt>

[CLUSCTL\_GROUP\_GET\_PROVIDER\_COLLECTIONS](clusctl-group-get-provider-collections.md)
</dt> <dd>

Retrieves the collections that come from providers by specifying a group.

</dd> <dt>

[CLUSCTL\_GROUP\_GET\_PROVIDER\_GROUPS](clusctl-group-get-provider-groups.md)
</dt> <dd>

Retrieves the groups that come from providers by specifying a group.

</dd> <dt>

[CLUSCTL\_GROUP\_GET\_RO\_COMMON\_PROPERTIES](clusctl-group-get-ro-common-properties.md)
</dt> <dd>

Retrieves the read-only common properties for a group.

</dd> <dt>

[CLUSCTL\_GROUP\_GET\_RO\_PRIVATE\_PROPERTIES](clusctl-group-get-ro-private-properties.md)
</dt> <dd>

Retrieves the read-only private properties for a group.

</dd> <dt>

[CLUSCTL\_GROUP\_QUERY\_DELETE](clusctl-group-query-delete.md)
</dt> <dd>

The [CLUSCTL\_GROUP\_QUERY\_DELETE](clusctl-group-query-delete.md) [control code](about-control-codes.md) is reserved for future use.

</dd> <dt>

[CLUSCTL\_GROUP\_SET\_COMMON\_PROPERTIES](clusctl-group-set-common-properties.md)
</dt> <dd>

Updates the read/write [common properties](common-properties.md) for a [group](groups.md).

</dd> <dt>

[CLUSCTL\_GROUP\_SET\_PRIVATE\_PROPERTIES](clusctl-group-set-private-properties.md)
</dt> <dd>

Updates the read/write [private properties](private-properties.md) for a [group](groups.md).

</dd> <dt>

[CLUSCTL\_GROUP\_UNKNOWN](clusctl-group-unknown.md)
</dt> <dd>

verifies that control codes are being processed on the node where execution of the control is directed.

</dd> <dt>

[CLUSCTL\_GROUP\_VALIDATE\_COMMON\_PROPERTIES](clusctl-group-validate-common-properties.md)
</dt> <dd>

Verifies that a [property list](property-lists.md) contains valid [group](groups.md) property names and values and that the list is properly formatted.

</dd> <dt>

[CLUSCTL\_GROUP\_VALIDATE\_PRIVATE\_PROPERTIES](clusctl-group-validate-private-properties.md)
</dt> <dd>

Verifies that a [group](groups.md) [private](private-properties.md) [property list](property-lists.md) is properly formatted.

</dd> </dl>

## Related topics

<dl> <dt>

[Failover Cluster Control Codes](control-codes.md)
</dt> <dt>

[**ClusterGroupControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clustergroupcontrol)
</dt> </dl>

 

 




