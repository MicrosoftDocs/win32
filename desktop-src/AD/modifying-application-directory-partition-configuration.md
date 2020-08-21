---
title: Modifying Application Directory Partition Configuration
description: An application directory partition can be modified by changing certain attributes of the crossRef object that represents the application directory partition.
ms.assetid: c4db5b3f-7d80-46a0-8a3a-9b1eb3c9f7b1
ms.tgt_platform: multiple
keywords:
- Modifying Application Directory Partition Configuration AD
- Application Directory Partitions AD , Modifying Configuration
ms.topic: article
ms.date: 05/31/2018
---

# Modifying Application Directory Partition Configuration

An application directory partition can be modified by changing certain attributes of the [**crossRef**](/windows/desktop/ADSchema/c-crossref) object that represents the application directory partition. To locate the [**crossRef**](/windows/desktop/ADSchema/c-crossref) object that represents a particular application directory partition, search the Partitions container for a **crossRef** object that has an [**nCName**](/windows/desktop/ADSchema/a-ncname) attribute value that is equal to the distinguished name of the application directory partition. The distinguished name of the **crossRef** object can then be used to bind to the **crossRef** object.

The following table lists attributes of the [**crossRef**](/windows/desktop/ADSchema/c-crossref) object that can be modified.

| Attribute                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                       |
|--------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**msDS-Replication-Notify-First-DSA-Delay**](/windows/desktop/ADSchema/a-msds-replication-notify-first-dsa-delay)           | Specifies the delay, in seconds, after an originating object change before the first replication partner is notified. For more information, see [Application Directory Partition Replication](application-directory-partition-replication.md).                                                                                                   |
| [**msDS-Replication-Notify-Subsequent-DSA-Delay**](/windows/desktop/ADSchema/a-msds-replication-notify-subsequent-dsa-delay) | Specifies the delay, in seconds, between subsequent notifications to the second, third, and so on replication partners. For more information, see [Application Directory Partition Replication](application-directory-partition-replication.md).                                                                                                 |
| [**msDS-SDReferenceDomain**](/windows/desktop/ADSchema/a-msds-sdreferencedomain)                                             | Identifies the domain that the security subsystem uses to interpret local domain references in the [**nTSecurityDescriptor**](/windows/desktop/ADSchema/a-ntsecuritydescriptor) attributes of objects in that application directory partition. For more information, see [Application Directory Partition Security](application-directory-partition-security.md). |
| [**msDS-NC-Replica-Locations**](/windows/desktop/ADSchema/a-msds-nc-replica-locations)                                       | Contains the distinguished name of the [**nTDSDSA**](/windows/desktop/ADSchema/c-ntdsdsa) object for each domain controller that hosts a replica of the application directory partition. For more information, see [Adding or Deleting an Application Directory Partition Replica](adding-or-deleting-an-application-directory-partition-replica.md).            |



 

 

 