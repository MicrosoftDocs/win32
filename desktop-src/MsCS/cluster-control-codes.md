---
title: Cluster Control Codes
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'cabd9d59-7ace-4081-9de1-7645c882a64d'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
description: 
keywords: ["cluster control codes Failover Cluster", "control codes Failover Cluster ,cluster", "clusters Failover Cluster ,control codes"]
---

# Cluster Control Codes

The [Failover Cluster API](the-server-cluster-api.md) defines the following [*external control codes*](e-gly.md#-wolf-external-control-code-gly) for [*clusters*](c-gly.md#-wolf-cluster-gly) (there are no [*internal control codes*](i-gly.md#-wolf-internal-control-code-gly) defined for clusters):

Cluster control codes use the **CLUS\_OBJECT\_CLUSTER** value of the [**CLUSTER\_CONTROL\_OBJECT**](cluster-control-object.md) enumeration to indicate that the control code applies to clusters. For more information about control codes, see [Control Code Architecture](control-code-architecture.md).

Cluster control codes are enumerated by the [**CLUSCTL\_CLUSTER\_CODES**](clusctl-cluster-codes.md) enumeration.

## In this section

<dl> <dt>

[CLUSCTL\_CLUSTER\_CHECK\_VOTER\_DOWN](clusctl-cluster-check-voter-down.md)
</dt> <dd>

Queries the server for whether taking a quorum resource offline or stopping an active node will cause the cluster to lose quorum.

</dd> <dt>

[CLUSCTL\_CLUSTER\_CHECK\_VOTER\_EVICT](clusctl-cluster-check-voter-evict.md)
</dt> <dd>

Queries the server for whether evicting the designated configured node from the cluster or changing the cluster quorum configuration will cause the loss of quorum.

</dd> <dt>

[CLUSCTL\_CLUSTER\_CLEAR\_NODE\_CONNECTION\_INFO](clusctl-cluster-clear-node-connection-info.md)
</dt> <dd>

TBD. Applications use this control code as a parameter to the [**ClusterControl**](clustercontrol.md) function.

</dd> <dt>

[CLUSCTL\_CLUSTER\_ENUM\_COMMON\_PROPERTIES](clusctl-cluster-enum-common-properties.md)
</dt> <dd>

Retrieves a list of the read/write cluster [common property](common-properties.md) names.

</dd> <dt>

[CLUSCTL\_CLUSTER\_ENUM\_PRIVATE\_PROPERTIES](clusctl-cluster-enum-private-properties.md)
</dt> <dd>

Retrieves a list of the cluster [private property](private-properties.md) names.

</dd> <dt>

[CLUSCTL\_CLUSTER\_GET\_CLUSDB\_TIMESTAMP](clusctl-cluster-get-clusdb-timestamp.md)
</dt> <dd>

Retrieves a cluster database timestamp for a cluster.

</dd> <dt>

[CLUSCTL\_CLUSTER\_GET\_COMMON\_PROPERTIES](clusctl-cluster-get-common-properties.md)
</dt> <dd>

Retrieves the read/write cluster [common properties](common-properties.md) for a cluster.

</dd> <dt>

[CLUSCTL\_CLUSTER\_GET\_COMMON\_PROPERTY\_FMTS](clusctl-cluster-get-common-property-fmts.md)
</dt> <dd>

Retrieves a [property list](property-lists.md) describing the format of each cluster [common property](cluster-common-properties.md).

</dd> <dt>

[CLUSCTL\_CLUSTER\_GET\_FQDN](clusctl-cluster-get-fqdn.md)
</dt> <dd>

Retrieves the fully qualified domain name (FQDN) of a [cluster](c-gly.md#-wolf-cluster-gly).

</dd> <dt>

[CLUSCTL\_CLUSTER\_GET\_GUM\_LOCK\_OWNER](clusctl-cluster-get-gum-lock-owner.md)
</dt> <dd>

Retrieves the name of the current [Global Update Manager](g-gly.md#-wolf-global-update-manager-gly) (GUM) lock owner for a [cluster](c-gly.md#-wolf-cluster-gly).

</dd> <dt>

[CLUSCTL\_CLUSTER\_GET\_PRIVATE\_PROPERTIES](clusctl-cluster-get-private-properties.md)
</dt> <dd>

Retrieves the read/write [private properties](private-properties.md) for a cluster.

</dd> <dt>

[CLUSCTL\_CLUSTER\_GET\_PRIVATE\_PROPERTY\_FMTS](clusctl-cluster-get-private-property-fmts.md)
</dt> <dd>

The [CLUSCTL\_CLUSTER\_GET\_PRIVATE\_PROPERTY\_FMTS](clusctl-cluster-get-private-property-fmts.md) [control code](about-control-codes.md) is not supported and fails with **ERROR\_INVALID\_FUNCTION**.

</dd> <dt>

[CLUSCTL\_CLUSTER\_GET\_RO\_COMMON\_PROPERTIES](clusctl-cluster-get-ro-common-properties.md)
</dt> <dd>

Retrieves the read-only common properties for a cluster.

</dd> <dt>

[CLUSCTL\_CLUSTER\_GET\_RO\_PRIVATE\_PROPERTIES](clusctl-cluster-get-ro-private-properties.md)
</dt> <dd>

Retrieves the read-only private properties for a cluster.

</dd> <dt>

[CLUSCTL\_CLUSTER\_GET\_SHARED\_VOLUME\_ID](clusctl-cluster-get-shared-volume-id.md)
</dt> <dd>

verifies that a path is on a CSV and returns the resource identifier of the CSV and the volume offset of the specific volume

</dd> <dt>

[CLUSCTL\_CLUSTER\_GET\_STORAGE\_CONFIG\_ATTRIBUTES](clusctl-cluster-get-storage-config-attributes.md)
</dt> <dd>

Retrieves the storage configuration attributes for a cluster.

</dd> <dt>

[CLUSCTL\_CLUSTER\_GET\_STORAGE\_CONFIGURATION](clusctl-cluster-get-storage-configuration.md)
</dt> <dd>

Retrieves the storage configuration for a cluster.

</dd> <dt>

[CLUSCTL\_CLUSTER\_REMOVE\_NODE](clusctl-cluster-remove-node.md)
</dt> <dd>

Removes a node from a cluster.

</dd> <dt>

[CLUSCTL\_CLUSTER\_SET\_ACCOUNT\_ACCESS](clusctl-cluster-set-account-access.md)
</dt> <dd>

Updates the account access settings for a cluster.

</dd> <dt>

[CLUSCTL\_CLUSTER\_SET\_DNS\_DOMAIN](clusctl_cluster_set_dns_domain.md)
</dt> <dd>

Updates the DNS domain settings for a cluster.

</dd> <dt>

[CLUSCTL\_CLUSTER\_SET\_CLUSTER\_S2D\_CACHE\_METADATA\_RESERVE\_BYTES](clusctl-cluster-set-cluster-s2d-cache-metadata-reserve-bytes.md)
</dt> <dd>

Sets the size of Storage Spaces Direct (S2D) metadata reserve.

</dd> <dt>

[CLUSCTL\_CLUSTER\_SET\_CLUSTER\_S2D\_ENABLED](clusctl-cluster-set-cluster-das-mode-enabled.md)
</dt> <dd>

Enables or disabled Storage Spaces Direct (S2D) on a cluster.

</dd> <dt>

[CLUSCTL\_CLUSTER\_SET\_COMMON\_PROPERTIES](clusctl-cluster-set-common-properties.md)
</dt> <dd>

Updates the read/write common properties for a cluster.

</dd> <dt>

[CLUSCTL\_CLUSTER\_SET\_PRIVATE\_PROPERTIES](clusctl-cluster-set-private-properties.md)
</dt> <dd>

Updates the read/write [private properties](private-properties.md) for a cluster.

</dd> <dt>

[CLUSCTL\_CLUSTER\_SET\_STORAGE\_CONFIGURATION](clusctl-cluster-set-storage-configuration.md)
</dt> <dd>

Updates a storage configuration for a cluster.

</dd> <dt>

[CLUSCTL\_CLUSTER\_SHUTDOWN](clusctl-cluster-shutdown.md)
</dt> <dd>

Instructs the server to inform every active node in the cluster to stop participating in the cluster.

</dd> <dt>

[CLUSCTL\_CLUSTER\_UNKNOWN](clusctl-cluster-unknown.md)
</dt> <dd>

verifies that [control codes](about-control-codes.md) are being processed on the node where execution of the control is directed.

</dd> <dt>

[CLUSCTL\_CLUSTER\_VALIDATE\_COMMON\_PROPERTIES](clusctl-cluster-validate-common-properties.md)
</dt> <dd>

Verifies that a [property list](property-lists.md) contains valid cluster property names and values and that the list is properly formatted.

</dd> <dt>

[CLUSCTL\_CLUSTER\_VALIDATE\_PRIVATE\_PROPERTIES](clusctl-cluster-validate-private-properties.md)
</dt> <dd>

Verifies that a [property list](property-lists.md) is properly formatted. Applications use this [control code](about-control-codes.md) as a [**ClusterControl**](clustercontrol.md) parameter.

</dd> </dl>

## Related topics

<dl> <dt>

[Failover Cluster Control Codes](control-codes.md)
</dt> <dt>

[**ClusterControl**](clustercontrol.md)
</dt> </dl>

 

 




