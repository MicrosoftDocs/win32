---
title: Node Control Codes
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 39b59726-e00e-4011-a7bc-96698e12f1e4
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
description: 
keywords:
- node control codes Failover Cluster
- control codes Failover Cluster ,node
- nodes Failover Cluster ,control codes
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Node Control Codes

The [Failover Cluster API](the-server-cluster-api.md) defines the following [*external control codes*](e-gly.md#-wolf-external-control-code-gly) for [*nodes*](n-gly.md#-wolf-node-gly) (there are no [*internal control codes*](i-gly.md#-wolf-internal-control-code-gly) defined for nodes):

Node control codes use the **CLUS\_OBJECT\_NODE** value of the [**CLUSTER\_CONTROL\_OBJECT**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_control_object?branch=master) enumeration to indicate that the control code applies to cluster nodes. For more information about control codes, see [Control Code Architecture](control-code-architecture.md).

Node control codes are enumerated by the [**CLUSCTL\_NODE\_CODES**](/windows/previous-versions/ClusAPI/ne-clusapi-clusctl_node_codes?branch=master) enumeration.

## In this section

<dl> <dt>

[CLUSCTL\_NODE\_INJECT\_GEM\_FAULT](clusctl-node-inject-gem-fault.md)
</dt> <dd>

TBD.

</dd> <dt>

[CLUSCTL\_NODE\_SEND\_DUMMY\_GEM\_MESSAGES](clusctl-node-send-dummy-gem-messages.md)
</dt> <dd>

TBD.

</dd> <dt>

[CLUSCTL\_NODE\_INTRODUCE\_GEM\_REPAIR\_DELAY](clusctl-node-introduce-gem-repair-delay.md)
</dt> <dd>

TBD.

</dd> <dt>

[CLUSCTL\_NODE\_GET\_GEMID\_VECTOR](clusctl-node-get-gemid-vector.md)
</dt> <dd>

TBD.

</dd> <dt>

[CLUSCTL\_NODE\_BLOCK\_GEM\_SEND\_RECV](clusctl-node-block-gem-send-recv.md)
</dt> <dd>

TBD.

</dd> <dt>

[CLUSCTL\_NODE\_ENUM\_COMMON\_PROPERTIES](clusctl-node-enum-common-properties.md)
</dt> <dd>

Retrieves a list of the read/write [common property](common-properties.md) names for [nodes](nodes.md).

</dd> <dt>

[CLUSCTL\_NODE\_ENUM\_PRIVATE\_PROPERTIES](clusctl-node-enum-private-properties.md)
</dt> <dd>

Retrieves a list of [node](nodes.md) [private property](private-properties.md) names.

</dd> <dt>

[CLUSCTL\_NODE\_GET\_CHARACTERISTICS](clusctl-node-get-characteristics.md)
</dt> <dd>

Retrieves the intrinsic characteristics of a [node](nodes.md).

</dd> <dt>

[CLUSCTL\_NODE\_GET\_CLUSTER\_SERVICE\_ACCOUNT\_NAME](clusctl-node-get-cluster-service-account-name.md)
</dt> <dd>

Retrieves the user account name under which the cluster service is running on a [node](nodes.md).

</dd> <dt>

[CLUSCTL\_NODE\_GET\_COMMON\_PROPERTIES](clusctl-node-get-common-properties.md)
</dt> <dd>

Retrieves the read/write [common properties](common-properties.md) for a [node](nodes.md). Applications use this [control code](about-control-codes.md) as a [**ClusterNodeControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusternodecontrol?branch=master) parameter.

</dd> <dt>

[CLUSCTL\_NODE\_GET\_COMMON\_PROPERTY\_FMTS](clusctl-node-get-common-property-fmts.md)
</dt> <dd>

Reserved for future use.

</dd> <dt>

[CLUSCTL\_NODE\_GET\_FLAGS](clusctl-node-get-flags.md)
</dt> <dd>

Retrieves the flags that are set for a [node](nodes.md).

</dd> <dt>

[CLUSCTL\_NODE\_GET\_ID](clusctl-node-get-id.md)
</dt> <dd>

Retrieves the unique cluster identifier for a [node](nodes.md).

</dd> <dt>

[CLUSCTL\_NODE\_GET\_NAME](clusctl-node-get-name.md)
</dt> <dd>

Retrieves the name of a [node](nodes.md).

</dd> <dt>

[CLUSCTL\_NODE\_GET\_PRIVATE\_PROPERTIES](clusctl-node-get-private-properties.md)
</dt> <dd>

Retrieves the read/write [private properties](private-properties.md) for a [node](nodes.md).

</dd> <dt>

[CLUSCTL\_NODE\_GET\_PRIVATE\_PROPERTY\_FMTS](clusctl-node-get-private-property-fmts.md)
</dt> <dd>

The [CLUSCTL\_NODE\_GET\_PRIVATE\_PROPERTY\_FMTS](clusctl-node-get-private-property-fmts.md) [control code](about-control-codes.md) is not supported and fails with **ERROR\_INVALID\_FUNCTION**.

</dd> <dt>

[CLUSCTL\_NODE\_GET\_RO\_COMMON\_PROPERTIES](clusctl-node-get-ro-common-properties.md)
</dt> <dd>

Retrieves the read-only [common properties](common-properties.md) for a [node](nodes.md).

</dd> <dt>

[CLUSCTL\_NODE\_GET\_RO\_PRIVATE\_PROPERTIES](clusctl-node-get-ro-private-properties.md)
</dt> <dd>

Retrieves the read-only [private properties](private-properties.md) for a [node](nodes.md).

</dd> <dt>

[CLUSCTL\_NODE\_GET\_STUCK\_NODES](clusctl-node-get-stuck-nodes.md)
</dt> <dd>

Retrieves the bitmap that represents the set of [nodes](nodes.md) that the current [Global Update Manager](g-gly.md#-wolf-global-update-manager-gly) (GUM) lock owner is waiting for.

</dd> <dt>

[CLUSCTL\_NODE\_SET\_COMMON\_PROPERTIES](clusctl-node-set-common-properties.md)
</dt> <dd>

Updates the read/write [common properties](common-properties.md) for a [node](nodes.md).

</dd> <dt>

[CLUSCTL\_NODE\_SET\_PRIVATE\_PROPERTIES](clusctl-node-set-private-properties.md)
</dt> <dd>

Updates the read/write [private properties](private-properties.md) for a [node](nodes.md).

</dd> <dt>

[CLUSCTL\_NODE\_UNKNOWN](clusctl-node-unknown.md)
</dt> <dd>

verifies that [control codes](about-control-codes.md) are being processed on the node where execution of the control is directed.

</dd> <dt>

[CLUSCTL\_NODE\_VALIDATE\_COMMON\_PROPERTIES](clusctl-node-validate-common-properties.md)
</dt> <dd>

Verifies that a [property list](property-lists.md) contains valid [node](nodes.md) property names and values and that the list is properly formatted.

</dd> <dt>

[CLUSCTL\_NODE\_VALIDATE\_PRIVATE\_PROPERTIES](clusctl-node-validate-private-properties.md)
</dt> <dd>

Verifies that a [property list](property-lists.md) is properly formatted.

</dd> </dl>

## Related topics

<dl> <dt>

[Failover Cluster Control Codes](control-codes.md)
</dt> <dt>

[**ClusterNodeControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusternodecontrol?branch=master)
</dt> </dl>

 

 




