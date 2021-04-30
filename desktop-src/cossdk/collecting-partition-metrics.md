---
description: Collecting Partition Metrics
ms.assetid: 2dc35011-24fa-49df-9cf8-96db2de39efa
title: Collecting Partition Metrics
ms.topic: article
ms.date: 05/31/2018
---

# Collecting Partition Metrics

In some cases, an organization might want to collect information on COM+ application use for the purposes of monitoring, capacity planning, and resource accounting.

For example, an application service provider (ASP) might want to charge a customer for its resource usage. To do this, COM+ allows you to collect event and metrics information on a per-partition basis.

The way to collect this information for a specific partition is by specifying, for each COM+ instrumentation interface, the partition ID member within the standard event structure. The event structure is the first value of a COM+ instrumentation interface. For more information, see [COM+ Instrumentation Interfaces](com--instrumentation-interfaces.md).

## Related topics

<dl> <dt>

[Configuring the Partition Cache](configuring-the-partition-cache.md)
</dt> <dt>

[Grouping Applications into Partitions](grouping-applications-into-partitions.md)
</dt> <dt>

[Managing Local Partitions](managing-local-partitions.md)
</dt> <dt>

[Managing Partitions Within Active Directory](managing-partitions-within-active-directory.md)
</dt> <dt>

[Setting Administrative Rights for a Partition](setting-administrative-rights-for-a-partition.md)
</dt> </dl>

 

 



