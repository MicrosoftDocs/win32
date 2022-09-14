---
title: Application Directory Partition Replication
description: Application directory partitions are most often used to store dynamic data.
ms.assetid: b5fbec54-ee1a-4fe6-b4b7-67fc4e77d043
ms.tgt_platform: multiple
keywords:
- Application Directory Partition Replication AD
- Application directory partitions AD , Replication
ms.topic: article
ms.date: 05/31/2018
---

# Application Directory Partition Replication

Application directory partitions are most often used to store dynamic data. Because data changes more often than the configuration data for a forest, the replication scope and frequency of an application directory partition can be set for each partition. The replication features of Active Directory Domain Services can be utilized, but the replication data can be fine-tuned to suit the type of data stored on the partition.

The operating system does not enforce a maximum number of replicas, but the number of replicas should be kept to a minimum to reduce the performance impact of replicating the dynamic application directory partition data.

The KCC generates and maintains the replication topology for an application directory partition.

## Application Directory Partition Replication Within a Site

The replication intervals that control intra-site replication of an application directory partition can be configured. This enables the dynamic data in an application directory partition to be synchronized more promptly than the more static data in a domain partition. For more information about programmatically configuring an application directory partition, see [Modifying Application Directory Partition Configuration](modifying-application-directory-partition-configuration.md).

Two attributes on the application directory partition's [**crossRef**](/windows/desktop/ADSchema/c-crossref) object and two registry values on each Windows 2000 and later domain controller control the latency of initiating an originating change notification to replication partners within a site.

-   The [**msDS-Replication-Notify-First-DSA-Delay**](/windows/desktop/ADSchema/a-msds-replication-notify-first-dsa-delay) attribute of a [**crossRef**](/windows/desktop/ADSchema/c-crossref) object specifies the delay, in seconds, after an originating object change before the first replication partner is notified. A registry value on each domain controller can specify a similar value. In a Windows Server 2003 forest, the default first delay is 15 seconds. In a mixed-mode forest, the default first delay is five minutes.
-   The [**msDS-Replication-Notify-Subsequent-DSA-Delay**](/windows/desktop/ADSchema/a-msds-replication-notify-subsequent-dsa-delay) attribute of a [**crossRef**](/windows/desktop/ADSchema/c-crossref) object specifies the delay, in seconds, between subsequent notifications to the second, third, and so on replication partners. A registry value on each domain controller can specify a similar value. In a Windows Server 2003 forest, the default subsequent delay is 3 seconds. In a mixed-mode forest, the default subsequent delay is 30 seconds.

The [**crossRef**](/windows/desktop/ADSchema/c-crossref) attributes apply to all domain controllers hosting a replica of the application directory partition and affect only replication of the application directory partition identified by the **crossRef** object. The registry values apply only to the domain controller on which they are set, and affect intra-site replication for all partitions that the domain controller is hosting. If neither the **crossRef** attributes nor its registry values are set, a domain controller uses the default values. If the registry values are set, they override any values set in the **crossRef** object. By default, the registry and **crossRef** values are not set, so the default values are used. This enables an administrator to speed up replication for all replicas of an application directory partition by setting the **crossRef** values, while enabling finer tuning with the registry settings on each domain controller.

Beginning with Windows Server 2003, domain partitions also use these attributes of the [**crossRef**](/windows/desktop/ADSchema/c-crossref) object to control intra-site replication latency. This is a change from previous server versions in which the delay intervals were controlled by registry values on each domain controller. When the forest is upgraded to Windows Server 2003, the existing registry values are preserved only if they have been modified from the default values. The domain controllers notification intervals in the registry override the notification intervals stored on the partition **crossRef** object.

## Application Directory Partition Replication Across Sites

The replicas of an application directory partition that are located across sites observe the inter-site replication schedule as done for domain partition and global catalog replication. However, replicas of an application directory partition are more often located within a site when hosting truly volatile data because inter-site replication latency may not be acceptable to get the replicas to be consistent with each other.

## Application Directory Partitions Are Not Replicated To Global Catalogs

Objects in an application directory partition are not replicated to the global catalog. The application directory partition is envisioned as hosting dynamic data and objects for which it may neither be sensible, nor feasible to replicate the objects widely. For this reason, the application directory partition offers controlled scope and frequency of replication. Because of this, there is no reason to allow these objects to replicate to the global catalog and hence be distributed across the entire forest where a global catalog server exists. This does not restrict objects in an application directory partition from using attributes in the schema marked as [**isMemberOfPartialAttributeSet**](/windows/desktop/ADSchema/a-ismemberofpartialattributeset). As with any domain controller, a global catalog server can still be configured to be a full replica of an application directory partition.

 

 