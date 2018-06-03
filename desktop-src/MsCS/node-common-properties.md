---
title: Node Common Properties
description: Common properties for nodes are data values stored in the cluster database that describe the identity and behavior of each node in a cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f56a0ce9-9a53-4c40-bab9-02a370ed2b47
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- node properties Failover Cluster
- properties Failover Cluster ,node (common) properties
- nodes Failover Cluster ,properties
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Node Common Properties

[Common properties](common-properties.md) for [nodes](nodes.md) are data values stored in the [cluster database](cluster-database.md) that describe the identity and behavior of each node in a [*cluster*](https://www.bing.com/search?q=*cluster*).

## In this section

<dl> <dt>

[**AdminExtensions**](nodes-adminextensions.md)
</dt> <dd>

This property is not supported.

</dd> <dt>

[**BuildNumber**](nodes-buildnumber.md)
</dt> <dd>

Specifies the build number of the version of the operating system installed on a [node](nodes.md). The following table summarizes the attributes of the [**BuildNumber**](nodes-buildnumber.md) property.

</dd> <dt>

[**CSDVersion**](nodes-csdversion.md)
</dt> <dd>

Specifies the name of the most recent service pack installed on the [node](nodes.md) (if any). The following table summarizes the attributes of the [**CSDVersion**](nodes-csdversion.md) property.

</dd> <dt>

[**Description**](nodes-description.md)
</dt> <dd>

Provides comments about the [node](nodes.md). The following table summarizes the attributes of the **Description** property.

</dd> <dt>

[**DynamicWeight**](nodes-dynamicweight.md)
</dt> <dd>

Controls the current weight that is attributed to the node because of dynamic quorum.

</dd> <dt>

[**EnableEventLogReplication**](nodes-enableeventlogreplication.md)
</dt> <dd>

Controls whether a [node's](nodes.md) system, application, and security event log entries are replicated in the event logs of all other [cluster](https://www.bing.com/search?q=cluster) nodes.

</dd> <dt>

[**FaultDomain**](nodes-faultdomain.md)
</dt> <dd>

Contains the fault domains for a node.

</dd> <dt>

[**FaultDomainId**](nodes-faultdomainid.md)
</dt> <dd>

Specifies the ID of the fault domain for a node.

</dd> <dt>

[**MajorVersion**](nodes-majorversion.md)
</dt> <dd>

Specifies the integer component of the version of the operating system installed on the [node](nodes.md). The following table summarizes the attributes of the **MajorVersion** property.

</dd> <dt>

[**MinorVersion**](nodes-minorversion.md)
</dt> <dd>

Specifies the decimal component of the version of the operating system installed on the [node](nodes.md). The following table summarizes the attributes of the **MinorVersion** property.

</dd> <dt>

[**Manufacturer**](nodes-manufacturer.md)
</dt> <dd>

Contains the name of the manufacturer of the [node](nodes.md). The following table summarizes the attributes of the [**Manufacturer**](nodes-manufacturer.md) property.

</dd> <dt>

[**Model**](nodes-model.md)
</dt> <dd>

Contains the model of the [node](nodes.md). The following table summarizes the attributes of the [**Model**](nodes-model.md) property.

</dd> <dt>

[**NodeDrainStatus**](nodes-nodedrainstatus.md)
</dt> <dd>

Specifies the status of a node drain.

</dd> <dt>

[**NodeDrainTarget**](nodes-nodedraintarget.md)
</dt> <dd>

Contains the node identifier of the drain target during a targeted drain.

</dd> <dt>

[**NodeHighestVersion**](nodes-nodehighestversion.md)
</dt> <dd>

Specifies the highest possible version of the [Cluster service](cluster-service.md) with which the [node](nodes.md) can join or communicate. The following table summarizes the attributes of the **NodeHighestVersion** property.

</dd> <dt>

[**NodeLowestVersion**](nodes-nodelowestversion.md)
</dt> <dd>

Specifies the lowest possible version of the [Cluster service](cluster-service.md) with which the [node](nodes.md) can join or communicate. The following table summarizes the attributes of the [**NodeLowestVersion**](nodes-nodelowestversion.md) property.

</dd> <dt>

[**NodeName**](nodes-nodename.md)
</dt> <dd>

Provides the name of the [node](nodes.md). The following table summarizes the attributes of the [**NodeName**](nodes-nodename.md) property.

</dd> <dt>

[**NodeWeight**](nodes-nodeweight.md)
</dt> <dd>

Specifies a configurable weight to give to the node, which determines whether the node participates in quorum.

</dd> <dt>

[**SerialNumber**](nodes-serialnumber.md)
</dt> <dd>

Contains the serial number of the [node](nodes.md). The following table summarizes the attributes of the [**SerialNumber**](nodes-serialnumber.md) property.

</dd> <dt>

[**StatusInformation**](statusinformation.md)
</dt> <dd>

Provides information about the status of a [node](nodes.md).

</dd> </dl>

## Related topics

<dl> <dt>

[Cluster Object Common Properties](common-properties-ref.md)
</dt> <dt>

[Getting Node Information](getting-node-information.md)
</dt> </dl>

 

 




