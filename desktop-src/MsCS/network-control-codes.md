---
title: Network Control Codes
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e9156fc0-688c-4a5b-9c78-91668bf2bd40
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
description: 
keywords:
- network control codes Failover Cluster
- control codes Failover Cluster ,network
- networks Failover Cluster ,control codes
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Network Control Codes

The [Failover Cluster API](the-server-cluster-api.md) defines the following [*external control codes*](e-gly.md#-wolf-external-control-code-gly) for [networks](networks.md) (there are no [*internal control codes*](i-gly.md#-wolf-internal-control-code-gly) defined for networks):

Network control codes use the **CLUS\_OBJECT\_NETWORK** value of the [**CLUSTER\_CONTROL\_OBJECT**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_control_object?branch=master) enumeration to indicate that the control code applies to cluster networks. For more information about control codes, see [Control Code Architecture](control-code-architecture.md).

Network control codes are enumerated by the [**CLUSCTL\_NETWORK\_CODES**](/windows/previous-versions/ClusAPI/ne-clusapi-clusctl_network_codes?branch=master) enumeration.

## In this section

<dl> <dt>

[CLUSCTL\_NETWORK\_ENUM\_COMMON\_PROPERTIES](clusctl-network-enum-common-properties.md)
</dt> <dd>

Retrieves a list of the read/write [common](common-properties.md) [network](networks.md) property names.

</dd> <dt>

[CLUSCTL\_NETWORK\_ENUM\_PRIVATE\_PROPERTIES](clusctl-network-enum-private-properties.md)
</dt> <dd>

Retrieves a list of [private property](private-properties.md) names for a [network](networks.md).

</dd> <dt>

[CLUSCTL\_NETWORK\_GET\_CHARACTERISTICS](clusctl-network-get-characteristics.md)
</dt> <dd>

Retrieves the intrinsic characteristics of a [network](networks.md).

</dd> <dt>

[CLUSCTL\_NETWORK\_GET\_COMMON\_PROPERTIES](clusctl-network-get-common-properties.md)
</dt> <dd>

Retrieves the read/write [common properties](common-properties.md) for a [network](networks.md).

</dd> <dt>

[CLUSCTL\_NETWORK\_GET\_COMMON\_PROPERTY\_FMTS](clusctl-network-get-common-property-fmts.md)
</dt> <dd>

Reserved for future use.

</dd> <dt>

[CLUSCTL\_NETWORK\_GET\_FLAGS](clusctl-network-get-flags.md)
</dt> <dd>

Retrieves the flags that are set for a [network](networks.md).

</dd> <dt>

[CLUSCTL\_NETWORK\_GET\_ID](clusctl-network-get-id.md)
</dt> <dd>

Retrieves the [cluster database](cluster-database.md) subkey identifier for a [network](networks.md).

</dd> <dt>

[CLUSCTL\_NETWORK\_GET\_NAME](clusctl-network-get-name.md)
</dt> <dd>

Retrieves the name of a [network](networks.md).

</dd> <dt>

[CLUSCTL\_NETWORK\_GET\_PRIVATE\_PROPERTIES](clusctl-network-get-private-properties.md)
</dt> <dd>

Retrieves the read/write [private properties](private-properties.md) for a [network](networks.md).

</dd> <dt>

[CLUSCTL\_NETWORK\_GET\_PRIVATE\_PROPERTY\_FMTS](clusctl-network-get-private-property-fmts.md)
</dt> <dd>

The [CLUSCTL\_NETWORK\_GET\_PRIVATE\_PROPERTY\_FMTS](clusctl-network-get-private-property-fmts.md) [control code](about-control-codes.md) is not supported and fails with **ERROR\_INVALID\_FUNCTION**.

</dd> <dt>

[CLUSCTL\_NETWORK\_GET\_RO\_COMMON\_PROPERTIES](clusctl-network-get-ro-common-properties.md)
</dt> <dd>

Retrieves the read-only [common properties](common-properties.md) for a [network](networks.md).

</dd> <dt>

[CLUSCTL\_NETWORK\_GET\_RO\_PRIVATE\_PROPERTIES](clusctl-network-get-ro-private-properties.md)
</dt> <dd>

Retrieves the read-only [private properties](private-properties.md) for a [network](networks.md).

</dd> <dt>

[CLUSCTL\_NETWORK\_SET\_COMMON\_PROPERTIES](clusctl-network-set-common-properties.md)
</dt> <dd>

Updates the read/write common properties for a [network](networks.md).

</dd> <dt>

[CLUSCTL\_NETWORK\_SET\_PRIVATE\_PROPERTIES](clusctl-network-set-private-properties.md)
</dt> <dd>

Updates the read/write [private properties](private-properties.md) for a [network](networks.md).

</dd> <dt>

[CLUSCTL\_NETWORK\_UNKNOWN](clusctl-network-unknown.md)
</dt> <dd>

verifies that control codes are being processed on the node where execution of the control is directed.

</dd> <dt>

[CLUSCTL\_NETWORK\_VALIDATE\_COMMON\_PROPERTIES](clusctl-network-validate-common-properties.md)
</dt> <dd>

Verifies that a [property list](property-lists.md) contains valid [network](networks.md) property names and values and that the list is properly formatted.

</dd> <dt>

[CLUSCTL\_NETWORK\_VALIDATE\_PRIVATE\_PROPERTIES](clusctl-network-validate-private-properties.md)
</dt> <dd>

Verifies that a [property list](property-lists.md) is properly formatted.

</dd> </dl>

## Related topics

<dl> <dt>

[Failover Cluster Control Codes](control-codes.md)
</dt> <dt>

[**ClusterNetworkControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusternetworkcontrol?branch=master)
</dt> <dt>

[**ExecuteNetworkControl Method of the MSCluster\_Network Class**](https://msdn.microsoft.com/library/cc512215)
</dt> <dt>

[**CLUSCTL\_NETWORK\_CODES**](/windows/previous-versions/ClusAPI/ne-clusapi-clusctl_network_codes?branch=master)
</dt> </dl>

 

 




