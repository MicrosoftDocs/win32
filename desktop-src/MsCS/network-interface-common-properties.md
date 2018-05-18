---
title: Network Interface Common Properties
description: Common properties for network interfaces are data values stored in the cluster database that describe the identity and behavior of each network interface in a cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '4641238d-4b9e-40c7-9d5e-751d69be1912'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["network interface properties Failover Cluster", "properties Failover Cluster ,network interface (common) properties", "network interfaces Failover Cluster ,properties"]
---

# Network Interface Common Properties

[Common properties](common-properties.md) for [network interfaces](network-interfaces.md) are data values stored in the [cluster database](cluster-database.md) that describe the identity and behavior of each network interface in a [*cluster*](c-gly.md#-wolf-cluster-gly).

## In this section

<dl> <dt>

[**Adapter**](network-interfaces-adapter.md)
</dt> <dd>

Provides the name that is used to uniquely identify the [network interface](network-interfaces.md) in the [cluster](c-gly.md#-wolf-cluster-gly). The following table summarizes the attributes of the [**Adapter**](network-interfaces-adapter.md) property.

</dd> <dt>

[**AdapterId**](adapterid.md)
</dt> <dd>

Provides the **GUID** that is used to uniquely identify the network interface in the cluster.

</dd> <dt>

[**Address**](network-interfaces-address.md)
</dt> <dd>

Provides the primary network address that the [node](nodes.md) uses for the [network interface](network-interfaces.md). The following table summarizes the attributes of the [**Address**](network-interfaces-address.md) property.

</dd> <dt>

[**AdminExtensions**](network-interfaces-adminextensions.md)
</dt> <dd>

This property is not supported.

</dd> <dt>

[**Description**](network-interfaces-description.md)
</dt> <dd>

Provides comments about the [network interface](network-interfaces.md). The following table summarizes the attributes of the **Description** property.

</dd> <dt>

[**DhcpEnabled**](dhcpenabled.md)
</dt> <dd>

Indicates whether DHCP is enabled for the network interface resource.

</dd> <dt>

[**IPv4Addresses**](ipv4addresses-netifprop.md)
</dt> <dd>

IPv4 addresses for the network interface resource.

</dd> <dt>

[**IPv6Addresses**](ipv6addresses-netifprop.md)
</dt> <dd>

IPv4 addresses for the network interface resource.

</dd> <dt>

[**Name**](network-interfaces-name.md)
</dt> <dd>

Provides the cluster-generated name for the [network interface](network-interfaces.md). This name appears on the network interface's property sheets in [Cluster Administrator](cluster-administrator.md) and is the name passed to the [**OpenClusterNetInterface**](openclusternetinterface.md) function. The following table summarizes the attributes of the [**Name**](network-interfaces-name.md) property.

</dd> <dt>

[**Network**](network-interfaces-network.md)
</dt> <dd>

Provides the name of the [network](networks.md) to which the [network interface](network-interfaces.md) is connected. The following table summarizes the attributes of the [**Network**](network-interfaces-network.md) property.

</dd> <dt>

[**Node**](network-interfaces-node.md)
</dt> <dd>

Provides the name of the [node](nodes.md) in which the [network interface](network-interfaces.md) is installed. The following table summarizes the attributes of the [**Node**](network-interfaces-node.md) property.

</dd> </dl>

## Related topics

<dl> <dt>

[Cluster Object Common Properties](common-properties-ref.md)
</dt> <dt>

[Getting Network Interface Information](getting-network-interface-information.md)
</dt> </dl>

 

 




