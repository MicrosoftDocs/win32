---
title: Groupset Common Properties
description: Common properties for groupsets are data values stored in the cluster database that describe the identity and behavior of each groupset in a cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1EF21AA6-4F3C-47FF-81D3-F1E2DF0AAC6F
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- groupset properties Failover Cluster
- groupset properties Failover Cluster , common
- properties Failover Cluster ,groupset properties
- properties Failover Cluster ,groupset properties, common
- groupset Failover Cluster ,properties
- groupset Failover Cluster ,properties, common
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Groupset Common Properties

[Common properties](common-properties.md) for groupsets are data values stored in the [cluster database](cluster-database.md) that describe the identity and behavior of each groupset in a [*cluster*](c-gly.md#-wolf-cluster-gly). Common properties for groupsets follow.

## In this section

<dl> <dt>

[**IsGlobal**](collection-isglobal.md)
</dt> <dd>

Indicates whether this set must be started and ready before any other sets should be started.

</dd> <dt>

[**Name**](collection-name.md)
</dt> <dd>

The name of the collection.

</dd> <dt>

[**ReadyCount**](collection-readycount.md)
</dt> <dd>

Indicates how many groups in a set must have met the [**ReadySetting**](collection-readysetting.md) criteria before the set is considered to be ready.

</dd> <dt>

[**ReadyDelay**](collection-readydelay.md)
</dt> <dd>

Indicates how much time (in seconds) should be pass after the [**ReadySetting**](collection-readysetting.md) criteria is met is before any sets dependent on to the group set are allowed to start.

</dd> <dt>

[**ReadySetting**](collection-readysetting.md)
</dt> <dd>

Indicates what condition is used to indicate a group set is ready.

</dd> <dt>

[**StartupCount**](startupcount.md)
</dt> <dd>

Startup count.

</dd> <dt>

[**StartupDelay**](startupdelay.md)
</dt> <dd>

The group set delay in seconds.

</dd> <dt>

[**StartupSetting**](startupsetting.md)
</dt> <dd>

Startup setting.

</dd> <dt>

[**StatusInformation**](collection-statusinformation.md)
</dt> <dd>

Contains information about the status of the groupset.

</dd> </dl>

## Related topics

<dl> <dt>

[Cluster Object Common Properties](common-properties-ref.md)
</dt> </dl>

 

 




