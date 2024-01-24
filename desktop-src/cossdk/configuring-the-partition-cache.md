---
description: The COM+ partitions feature includes a partition cache. This cache stores user-to-partition mappings and is designed to avoid repetitive Active Directory access.
ms.assetid: 8c3a269d-1933-4df6-aefb-f1f5587f1f42
title: Configuring the Partition Cache
ms.topic: article
ms.date: 05/31/2018
---

# Configuring the Partition Cache

The COM+ partitions feature includes a partition cache. This cache stores user-to-partition mappings and is designed to avoid repetitive Active Directory access.

## Changing Cache Size

The partition cache consists of three tables, whose size can be modified to enhance performance. These tables consist of the number of SID entries in the cache, the number of OU entries in the cache, and the number of partition entries in the cache.

To change these table sizes, administrators can modify the values of a registry key. The registry key and its values are as follows:

**HKLM\\SOFTWARE\\Microsoft\\COM3\\PartitionCache**



| Key values                         | Description                                                                                                                                                                                                                                                                                                                                                                                                  |
|------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **NumSidEntries**<br/>       | Contains the REG\_DWORD value for the number of SID entries in the cache (default=512). This value should be set to a value greater than the number of unique identities that a machine will be servicing in the cache invalidation time window.<br/>                                                                                                                                                  |
| **NumNameEntries**<br/>      | Contains the REG\_DWORD value for the number of OU name entries in the cache (default=64). This value should be set to a value greater than the number of unique OU names that a machine will be servicing in the cache invalidation time window.<br/>                                                                                                                                                 |
| **NumPartitionEntries**<br/> | Contains the REG\_DWORD value for the number of partition entries in the cache (default=1024).<br/> In the cache invalidation time window, the DWORD value should be set to a number greater than the number of unique partitions that a machine will be servicing. This is because a component's context can include a partition ID for a partition that does not reside on that machine. <br/> |
| **EntryExpiration**<br/>     | Contains the REG\_DWORD value for the tick count (each tick = ~7 minutes) until a cache entry becomes invalid (default=4 (~28 minutes)).<br/>                                                                                                                                                                                                                                                          |



 

## Flushing the Cache

Because COM+ caches the default partition for users, you might want to call this method after changing the default partition for a user in the Active Directory. Administrators can do this programmatically by calling the [**FlushPartitionCache**](/windows/desktop/api/ComAdmin/nf-comadmin-icomadmincatalog2-flushpartitioncache) method.

## Related topics

<dl> <dt>

[Collecting Partition Metrics](collecting-partition-metrics.md)
</dt> <dt>

[Grouping Applications into Partitions](grouping-applications-into-partitions.md)
</dt> <dt>

[Managing Local Partitions](managing-local-partitions.md)
</dt> <dt>

[Managing Partitions Within Active Directory](managing-partitions-within-active-directory.md)
</dt> <dt>

[Setting Administrative Rights for a Partition](setting-administrative-rights-for-a-partition.md)
</dt> </dl>

 

 




