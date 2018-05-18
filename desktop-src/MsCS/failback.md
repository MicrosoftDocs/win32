---
title: Failback
description: When a node becomes inactive for any reason, the Cluster service fails over any groups hosted by the node. When the node becomes active again, the Cluster service can fail back the groups originally hosted by the node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'dcb53180-86bf-4cba-bf93-9c19cbc127b8'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["failback Failover Cluster"]
---

# Failback

When a [node](nodes.md) becomes inactive for any reason, the [Cluster service](cluster-service.md) [fails over](failover.md) any [groups](groups.md) hosted by the node. When the node becomes active again, the Cluster service can fail back the groups originally hosted by the node.

The Cluster service fails back a group using the same procedures it performs during failover; that is, the Cluster service takes all of the [resources](resources.md) in the group offline, moves the group, and then brings all of the resources in the group online.

Administrators and developers can configure how and when failback occurs for a group by adjusting the group's [**AutoFailbackType**](groups-autofailbacktype.md), [**FailbackWindowStart**](groups-failbackwindowstart.md), and [**FailbackWindowEnd**](groups-failbackwindowend.md) properties. For information on using properties, see [Setting Properties](setting-properties.md).

 

 




