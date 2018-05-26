---
title: Group Common Properties
description: Common properties for groups are data values stored in the cluster database that describe the identity and behavior of each group in a cluster. Common properties for groups follow.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: bc13356c-06d8-400e-9fe0-3afbda4f228a
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- group properties Failover Cluster
- properties Failover Cluster ,group (common) properties
- groups Failover Cluster , properties
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Group Common Properties

[Common properties](common-properties.md) for [groups](groups.md) are data values stored in the [cluster database](cluster-database.md) that describe the identity and behavior of each group in a [*cluster*](c-gly.md#-wolf-cluster-gly). Common properties for groups follow.

## In this section

<dl> <dt>

[**AdminExtensions**](groups-adminextensions.md)
</dt> <dd>

This property is not supported.

</dd> <dt>

[**AntiAffinityClassNames**](groups-antiaffinityclassnames.md)
</dt> <dd>

Used to identify [groups](groups.md) that should not be hosted on the same cluster [node](nodes.md). The following table summarizes the attributes of the [**AntiAffinityClassNames**](groups-antiaffinityclassnames.md) property.

</dd> <dt>

[**AutoFailbackType**](groups-autofailbacktype.md)
</dt> <dd>

Specifies whether the [group](groups.md) should automatically be failed back to the [node](nodes.md) identified as its preferred owner when that node comes back online following a [failover](failover.md).

</dd> <dt>

[**CCFEpoch**](ccfepoch.md)
</dt> <dd>

Specifies the current CCF epoch of a resource group.

</dd> <dt>

[**ColdStartSetting**](groups-coldstartsetting.md)
</dt> <dd>

Specifies the cold start settings for a group cluster.

</dd> <dt>

[**DefaultOwner**](groups-defaultowner.md)
</dt> <dd>

Specifies the number of the last node that the resource group was activated on or explicitly moved to.

</dd> <dt>

[**Description**](groups-description.md)
</dt> <dd>

Provides comments about the [group](groups.md). The following table summarizes the attributes of the **Description** property.

</dd> <dt>

[**FailbackWindowEnd**](groups-failbackwindowend.md)
</dt> <dd>

Provides the latest time that the [group](groups.md) can be [failed back](failback.md) to the [node](nodes.md) identified as its [preferred owner](p-gly.md#-wolf-preferred-owner-gly) node. The following table summarizes the attributes of the [**FailbackWindowEnd**](groups-failbackwindowend.md) property.

</dd> <dt>

[**FailbackWindowStart**](groups-failbackwindowstart.md)
</dt> <dd>

Provides the earliest time (that is, local time as kept by the [cluster](c-gly.md#-wolf-cluster-gly)) that the group can be [failed back](failback.md) to the [node](nodes.md) identified as its [preferred owner](p-gly.md#-wolf-preferred-owner-gly) node. The following table summarizes the attributes of the [**FailbackWindowStart**](groups-failbackwindowstart.md) property.

</dd> <dt>

[**FailoverPeriod**](groups-failoverperiod.md)
</dt> <dd>

Specifies a number of hours during which a maximum number of [failover](failover.md) attempts, specified by [**FailoverThreshold**](groups-failoverthreshold.md), can occur. The following table summarizes the attributes of the [**FailoverPeriod**](groups-failoverperiod.md) property.

</dd> <dt>

[**FailoverThreshold**](groups-failoverthreshold.md)
</dt> <dd>

Specifies the maximum number of [failover](failover.md) attempts that can be made on a [group](groups.md) within a time interval defined by [**FailoverPeriod**](groups-failoverperiod.md). The following table summarizes the attributes of the [**FailoverThreshold**](groups-failoverthreshold.md) property.

</dd> <dt>

[**GroupStartDelay**](groupstartdelay.md)
</dt> <dd>

TBD

</dd> <dt>

[**GroupType**](groups-grouptype.md)
</dt> <dd>

Specifies the type of the resource group.

</dd> <dt>

[**Name**](groups-name.md)
</dt> <dd>

Specifies the name of the [group](groups.md). The following table summarizes the attributes of the [**Name**](groups-name.md) property.

</dd> <dt>

[**PersistentState**](groups-persistentstate.md)
</dt> <dd>

Specifies whether a [group](groups.md) should be automatically brought online when the [cluster](c-gly.md#-wolf-cluster-gly) forms. The following table summarizes the attributes of the **PersistentState** property.

</dd> <dt>

[**PreferredSite**](group-preferredsite.md)
</dt> <dd>

Specifies the preferred site for a group of site-aware clusters.

</dd> <dt>

[**Priority**](groups-priority.md)
</dt> <dd>

The priority value of the resource group.

</dd> <dt>

[**ResiliencyPeriod**](resiliencyperiod.md)
</dt> <dd>

Specifies the resiliency period for a group, in seconds.

</dd> <dt>

[**StatusInformation**](groups-statusinformation.md)
</dt> <dd>

Contains information about the status of the group.

</dd> </dl>

## Related topics

<dl> <dt>

[Cluster Object Common Properties](common-properties-ref.md)
</dt> <dt>

[Getting Group Information](getting-group-information.md)
</dt> </dl>

 

 




