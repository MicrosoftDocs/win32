---
title: Naming Contexts and Directory Partitions
description: Each domain controller in a domain forest controlled by Active Directory Domain Services includes directory partitions.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 77ac171c-2031-46d7-b81e-dd9ae0c70ccb
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- Naming Contexts and Directory Partitions AD
- Naming Contexts AD , About
- Directory Partitions AD , About
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Naming Contexts and Directory Partitions

Each domain controller in a domain forest controlled by Active Directory Domain Services includes [*directory partitions*](https://msdn.microsoft.com/library/ms681901#-ds-directory-partition). Directory partitions are also known as [*naming contexts*](https://msdn.microsoft.com/library/ms681918#-ds-naming-context). A directory partition is a contiguous portion of the overall directory that has independent replication scope and scheduling data. By default, the Active Directory Domain Service for an enterprise contains the following partitions:

-   [*Schema Partition*](https://msdn.microsoft.com/library/ms681936#-ds-schema-partition): The schema partition contains the **classSchema** and **attributeSchema** objects that define the types of objects that can exist in the forest. Every domain controller in the forest has a replica of the same schema partition.
-   [*Configuration Partition*](https://msdn.microsoft.com/library/ms681898#-ds-configuration-partition): The configuration partition contains replication topology and other configuration data that must be replicated throughout the forest. Every domain controller in the forest has a replica of the same configuration partition.
-   [*Domain Partition*](https://msdn.microsoft.com/library/ms681901#-ds-domain-partition): The domain partition contains the directory objects, such as users and computers, associated with the local domain. A domain can have multiple domain controllers and a forest can have multiple domains. Each domain controller stores a full replica of the domain partition for its local domain, but does not store replicas of the domain partitions for other domains.

Windows Server 2003 introduces the *Application Directory Partition*, which provides the ability to control the scope of replication and allow the placement of replicas in a manner more suitable for dynamic data. For more information about application directory partitions, see [About Application Directory Partitions](about-application-directory-partitions.md).

For more information about how Active Directory Domain Services maintain consistency between the various replicas of a directory partition, see [Replication and Data Integrity](replication-and-data-integrity.md).

 

 




