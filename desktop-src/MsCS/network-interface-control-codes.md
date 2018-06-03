---
title: Network Interface Control Codes
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: adc97081-e778-426d-8296-9dea9f22a4e4
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
description: 
keywords:
- network interface control codes Failover Cluster
- control codes Failover Cluster ,network interface
- network interfaces Failover Cluster ,control codes
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Network Interface Control Codes

The [Failover Cluster API](the-server-cluster-api.md) defines the following [*external control codes*](https://www.bing.com/search?q=*external control codes*) for [network interfaces](network-interfaces.md) (there are no [*internal control codes*](https://www.bing.com/search?q=*internal control codes*) defined for network interfaces):

Network interface control codes use the **CLUS\_OBJECT\_NETINTERFACE** value of the [**CLUSTER\_CONTROL\_OBJECT**](/previous-versions/windows/desktop/api/ClusAPI/ne-clusapi-cluster_control_object) enumeration to indicate that the control code applies to cluster network interfaces. For more information about control codes, see [Control Code Architecture](control-code-architecture.md).

Network interface control codes are enumerated by the [**CLUSCTL\_NETINTERFACE\_CODES**](/previous-versions/windows/desktop/api/ClusAPI/ne-clusapi-clusctl_netinterface_codes) enumeration.

## In this section

<dl> <dt>

[CLUSCTL\_NETINTERFACE\_ENUM\_COMMON\_PROPERTIES](clusctl-netinterface-enum-common-properties.md)
</dt> <dd>

Retrieves a list of the read/write [network interface](network-interfaces.md) [common property](common-properties.md) names.

</dd> <dt>

[CLUSCTL\_NETINTERFACE\_ENUM\_PRIVATE\_PROPERTIES](clusctl-netinterface-enum-private-properties.md)
</dt> <dd>

Retrieves a list of the [network interface](network-interfaces.md) [private properties](private-properties.md).

</dd> <dt>

[CLUSCTL\_NETINTERFACE\_GET\_CHARACTERISTICS](clusctl-netinterface-get-characteristics.md)
</dt> <dd>

retrieves the intrinsic characteristics of a [network interface](network-interfaces.md).

</dd> <dt>

[CLUSCTL\_NETINTERFACE\_GET\_COMMON\_PROPERTIES](clusctl-netinterface-get-common-properties.md)
</dt> <dd>

Retrieves the read/write [common properties](common-properties.md) for a [network interface](network-interfaces.md).

</dd> <dt>

[CLUSCTL\_NETINTERFACE\_GET\_COMMON\_PROPERTY\_FMTS](clusctl-netinterface-get-common-property-fmts.md)
</dt> <dd>

Reserved for future use.

</dd> <dt>

[CLUSCTL\_NETINTERFACE\_GET\_FLAGS](clusctl-netinterface-get-flags.md)
</dt> <dd>

Retrieves the flags that are set for a [network interface](network-interfaces.md).

</dd> <dt>

[CLUSCTL\_NETINTERFACE\_GET\_ID](clusctl-netinterface-get-id.md)
</dt> <dd>

Retrieves the [cluster database](cluster-database.md) subkey identifier for a [network interface](network-interfaces.md).

</dd> <dt>

[CLUSCTL\_NETINTERFACE\_GET\_NAME](clusctl-netinterface-get-name.md)
</dt> <dd>

Retrieves the name of a [network interface](network-interfaces.md).

</dd> <dt>

[CLUSCTL\_NETINTERFACE\_GET\_NETWORK](clusctl-netinterface-get-network.md)
</dt> <dd>

Retrieves the name of the [network](networks.md) to which a [network interface](network-interfaces.md) is connected.

</dd> <dt>

[CLUSCTL\_NETINTERFACE\_GET\_NODE](clusctl-netinterface-get-node.md)
</dt> <dd>

Retrieves the name of the [node](nodes.md) in which a [network interface](network-interfaces.md) is installed. Applications use this [control code](about-control-codes.md) as a [**ClusterNetInterfaceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusternetinterfacecontrol) parameter.

</dd> <dt>

[CLUSCTL\_NETINTERFACE\_GET\_PRIVATE\_PROPERTIES](clusctl-netinterface-get-private-properties.md)
</dt> <dd>

Retrieves the read/write [private properties](private-properties.md) for a [network interface](network-interfaces.md).

</dd> <dt>

[CLUSCTL\_NETINTERFACE\_GET\_PRIVATE\_PROPERTY\_FMTS](clusctl-netinterface-get-private-property-fmts.md)
</dt> <dd>

The [CLUSCTL\_NETINTERFACE\_GET\_PRIVATE\_PROPERTY\_FMTS](clusctl-netinterface-get-private-property-fmts.md) [control code](about-control-codes.md) is not supported and fails with **ERROR\_INVALID\_FUNCTION**.

</dd> <dt>

[CLUSCTL\_NETINTERFACE\_GET\_RO\_COMMON\_PROPERTIES](clusctl-netinterface-get-ro-common-properties.md)
</dt> <dd>

Retrieves the read-only [common properties](common-properties.md) for a [network interface](network-interfaces.md).

</dd> <dt>

[CLUSCTL\_NETINTERFACE\_GET\_RO\_PRIVATE\_PROPERTIES](clusctl-netinterface-get-ro-private-properties.md)
</dt> <dd>

Retrieves the read-only [private properties](private-properties.md) for a [network interface](network-interfaces.md).

</dd> <dt>

[CLUSCTL\_NETINTERFACE\_SET\_COMMON\_PROPERTIES](clusctl-netinterface-set-common-properties.md)
</dt> <dd>

Updates the read/write [common properties](common-properties.md) for a [network interface](network-interfaces.md).

</dd> <dt>

[CLUSCTL\_NETINTERFACE\_SET\_PRIVATE\_PROPERTIES](clusctl-netinterface-set-private-properties.md)
</dt> <dd>

Updates the read/write [private properties](private-properties.md) for a [network interface](network-interfaces.md).

</dd> <dt>

[CLUSCTL\_NETINTERFACE\_UNKNOWN](clusctl-netinterface-unknown.md)
</dt> <dd>

verifies that the network interface control code verifies that control codes are being processed on the node where execution of the control is directed.

</dd> <dt>

[CLUSCTL\_NETINTERFACE\_VALIDATE\_COMMON\_PROPERTIES](clusctl-netinterface-validate-common-properties.md)
</dt> <dd>

Verifies that a [property list](property-lists.md) contains valid [network interface](network-interfaces.md) property names

</dd> <dt>

[CLUSCTL\_NETINTERFACE\_VALIDATE\_PRIVATE\_PROPERTIES](clusctl-netinterface-validate-private-properties.md)
</dt> <dd>

Verifies that a [property list](property-lists.md) is properly formatted.

</dd> </dl>

## Related topics

<dl> <dt>

[Failover Cluster Control Codes](control-codes.md)
</dt> <dt>

[**ClusterNetInterfaceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusternetinterfacecontrol)
</dt> </dl>

 

 




