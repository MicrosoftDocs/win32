---
title: Application Directory Partitions
description: In Windows Server 2003, Active Directory Domain Services support application directory partitions.
ms.assetid: 55c47803-c1ee-4888-bb19-103374ec9719
ms.tgt_platform: multiple
keywords:
- Application Directory Partitions AD
- Application Directory Partitions AD , Using
ms.topic: article
ms.date: 05/31/2018
---

# Application Directory Partitions

In Windows Server 2003, Active Directory Domain Services support application directory partitions. An application directory partition can contain a hierarchy of any type of objects, except security principals, and can be configured to replicate to any set of domain controllers in the forest. Unlike a domain partition, an application directory partition is not required to replicate to all domain controllers in a domain and the partition can replicate to domain controllers in different domains of the forest. For more information about application directory partitions, see [About Application Directory Partitions](about-application-directory-partitions.md).

An application directory partition can be created. modified and deleted using standard ADSI, LDAP and [System.DirectoryServices](/dotnet/api/system.directoryservices) operations. The security context required to create and modify an application directory partition is the same as that for creating a domain partition.

The following topics describe how to work with application directory partitions:

-   [Application Directory Partition Replication](application-directory-partition-replication.md)
-   [Application Directory Partition Security](application-directory-partition-security.md)
-   [Creating an Application Directory Partition](creating-an-application-directory-partition.md)
-   [Deleting an Application Directory Partition](deleting-an-application-directory-partition.md)
-   [Enumerating Application Directory Partitions in a Forest](enumerating-application-directory-partitions-in-a-forest.md)
-   [Locating an Application Directory Partition Host Server](locating-an-application-directory-partition-host-server.md)
-   [Adding or Deleting an Application Directory Partition Replica](adding-or-deleting-an-application-directory-partition-replica.md)
-   [Enumerating Replicas of an Application Directory Partition](enumerating-replicas-of-an-application-directory-partition.md)
-   [Modifying Application Directory Partition Configuration](modifying-application-directory-partition-configuration.md)

 

 