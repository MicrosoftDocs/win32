---
title: Naming Contexts and Directory Partitions
description: Each domain controller in a domain forest controlled by Active Directory Domain Services includes directory partitions.
ms.assetid: 77ac171c-2031-46d7-b81e-dd9ae0c70ccb
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Naming Contexts and Directory Partitions

Each domain controller in a domain forest controlled by Active Directory Domain Services includes [*directory partitions*](/previous-versions/windows/desktop/legacy/ms681901(v=vs.85)). Directory partitions are also known as [*naming contexts*](/previous-versions/windows/desktop/legacy/ms681918(v=vs.85)). A directory partition is a contiguous portion of the overall directory that has independent replication scope and scheduling data. By default, the Active Directory Domain Service for an enterprise contains the following partitions:

-   [*Schema Partition*](/previous-versions/windows/desktop/legacy/ms681936(v=vs.85)): The schema partition contains the **classSchema** and **attributeSchema** objects that define the types of objects that can exist in the forest. Every domain controller in the forest has a replica of the same schema partition.
-   [*Configuration Partition*](/previous-versions/windows/desktop/legacy/ms681898(v=vs.85)): The configuration partition contains replication topology and other configuration data that must be replicated throughout the forest. Every domain controller in the forest has a replica of the same configuration partition.
-   [*Domain Partition*](/previous-versions/windows/desktop/legacy/ms681901(v=vs.85)): The domain partition contains the directory objects, such as users and computers, associated with the local domain. A domain can have multiple domain controllers and a forest can have multiple domains. Each domain controller stores a full replica of the domain partition for its local domain, but does not store replicas of the domain partitions for other domains.

Windows Server 2003 introduces the *Application Directory Partition*, which provides the ability to control the scope of replication and allow the placement of replicas in a manner more suitable for dynamic data. For more information about application directory partitions, see [About Application Directory Partitions](about-application-directory-partitions.md).

For more information about how Active Directory Domain Services maintain consistency between the various replicas of a directory partition, see [Replication and Data Integrity](replication-and-data-integrity.md).

 

 
