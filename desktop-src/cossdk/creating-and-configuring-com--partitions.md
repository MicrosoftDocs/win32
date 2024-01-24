---
description: Administrators can use COM+ to programmatically create and configure COM+ partitions.
ms.assetid: 15f0cd9a-cd40-49df-85b8-15c4e626f8ee
title: Creating and Configuring COM+ Partitions
ms.topic: article
ms.date: 05/31/2018
---

# Creating and Configuring COM+ Partitions

Administrators can use COM+ to programmatically create and configure COM+ partitions. In fact, all creation and configuration tasks that an administrator can do from the Component Services or the Active Directory Users and Computers administrative tools can be done by using COM+ collections, objects, and interfaces or through the Active Directory System Interface (ADSI).

**Windows XP:** The ability to create, configure, or delegate COM+ partitions is not available. The global partition is the only COM+ partition available.

**Windows 2000:  ** The COM+ partitions service is not available in Windows 2000.

> [!Note]  
> The COM+ partitions service is not enabled by default. To use the COM+ partitions service, you must enable it through the Component Services administration tool or by changing the PartitionsEnabled property on the [**LocalComputer**](localcomputer.md) collection to True.

 

To accomplish partition-related tasks, COM+ provides the following programming elements:

-   Methods and properties of the [**ICOMAdminCatalog2**](/windows/desktop/api/ComAdmin/nn-comadmin-icomadmincatalog2) interface on the [**COMAdminCatalog**](comadmincatalog.md) class:
    -   [**CurrentPartition**](/windows/desktop/api/ComAdmin/nf-comadmin-icomadmincatalog2-put_currentpartition) property.
    -   [**CurrentPartitionID**](/windows/desktop/api/ComAdmin/nf-comadmin-icomadmincatalog2-get_currentpartitionid) property.
    -   [**CurrentPartitionName**](/windows/desktop/api/ComAdmin/nf-comadmin-icomadmincatalog2-get_currentpartitionname) property.
    -   [**FlushPartitionCache**](/windows/desktop/api/ComAdmin/nf-comadmin-icomadmincatalog2-flushpartitioncache) method.
    -   [**GetPartitionID**](/windows/desktop/api/ComAdmin/nf-comadmin-icomadmincatalog2-getpartitionid) method.
    -   [**GetPartitionName**](/windows/desktop/api/ComAdmin/nf-comadmin-icomadmincatalog2-getpartitionname) method.
    -   [**GlobalPartitionID**](/windows/desktop/api/ComAdmin/nf-comadmin-icomadmincatalog2-get_globalpartitionid) property.
-   A set of COM+ objects for creating and managing partitions in Active Directory.
-   A COM+ registry key, **PartitionCache**, for changing the partition cache size.
-   A set of partitions-related [COM+ Administration Collections](com--administration-collections.md):
    -   [**Partitions**](partitions.md) collection.
    -   [**PartitionUsers**](partitionusers.md) collection.
    -   [**RolesForPartition**](rolesforpartition.md) collection.
    -   [**UsersInPartitionRole**](usersinpartitionrole.md) collection.
-   Properties of other [COM+ Administration Collections](com--administration-collections.md):
    -   PartitionID property on the [**ApplicationInstances**](applicationinstances.md) collection.
    -   AppPartitionID property on the [**Applications**](applications.md) collection.
    -   PartitionDescription, PartitionID, and PartitionName properties on the [**FilesForImport**](filesforimport.md) collection.
    -   DSPartitionLookupEnabled, LocalPartitionLookupEnabled, and PartitionsEnabled properties on the [**LocalComputer**](localcomputer.md) collection.
    -   EventClassPartitionID and SubscriberPartitionID properties on the [**SubscriptionsForComponent**](subscriptionsforcomponent.md) collection.
    -   EventClassPartitionID and SubscriberPartitionID properties on the [**TransientSubscriptions**](transientsubscriptions.md) collection.

## Related topics

<dl> <dt>

[Collecting Partition Metrics](collecting-partition-metrics.md)
</dt> <dt>

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

 

 



