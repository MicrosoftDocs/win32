---
title: About Application Directory Partitions
description: Developers who use ADSI or LDAP to store and access relatively static and globally data in Active Directory Domain Services may also prefer, for the sake of simplicity and uniformity, to continue using ADSI or LDAP access for their dynamic data requirements. Dynamic data changes more frequently than what has been recommended for storing in Active Directory Domain Services. Dynamic data typically changes more frequently than the replication latency involved in propagating the change to all replicas of the data.
ms.assetid: bf856c3a-9061-474a-a536-c87ca50d5f83
ms.tgt_platform: multiple
keywords:
- About Application Directory Partitions
- Application Directory Partitions, About
ms.topic: article
ms.date: 05/31/2018
---

# About Application Directory Partitions

Developers who use ADSI or LDAP to store and access relatively static and globally data in Active Directory Domain Services may also prefer, for the sake of simplicity and uniformity, to continue using ADSI or LDAP access for their dynamic data requirements. Dynamic data changes more frequently than what has been recommended for storing in Active Directory Domain Services. Dynamic data typically changes more frequently than the replication latency involved in propagating the change to all replicas of the data.

In Windows 2000, the support for dynamic data is limited. Storing dynamic data in a domain partition can be complicated. The data is replicated to all domain controllers in the domain which is often unnecessary and can result in inconsistent data due to replication latency. This can adversely impact network performance. In addition, domain partitions are not effective for applications that must replicate data across domain boundaries. Another option in Windows 2000 is to store dynamic data in attributes marked as non-replicated. However, this arrangement is limited in that it has a single point of failure, namely, the single domain controller housing the only copy of the object's non-replicated attributes.

Application directory partitions provide the ability to control the scope of replication and allow the placement of replicas in a manner more suitable for dynamic data. As a result, the application directory partition provides the capability of hosting dynamic data in the Active Directory Server, thus allowing ADSI/LDAP access to it, without significantly impacting network performance.

The Windows 2000 DNS service is an example of a service that can take advantage of application directory partitions. In Windows 2000, if the DNS service is optionally configured to use Active Directory Domain Services, the DNS zone data is stored in the Active Directory Server in a domain partition. That is, the data is replicated to all domain controllers in the domain, regardless of whether a DNS server is configured to run on the domain controller. This is an instance where full domain-wide replication is unnecessary. By storing the DNS zone data in an application directory partition, the service can redefine the scope of replication to only that subset of domain controllers in the domain that actually run the DNS server.

Consider the following scenarios for hosting a replica of an application directory partition:

-   A replica of an application directory partition can be created on any Windows Server 2003 operating system and later domain controller in an Active Directory Domain Services forest.
-   The set of domain controllers that host replicas of an application directory partition can be specified. Unlike a domain partition, an application directory partition is not required to replicate to all domain controllers in a domain, and it can replicate to domain controllers in different domains of the forest.
-   A domain controller with an application directory partition replica can coexist and function in a mixed-mode environment with other computers running Windows 2000 or Windows NT 4.0.

Types of data that can be stored in an application directory partition include:

-   An application directory partition can contain instances of any object type except security principals, such as users, computers, or groups.
-   Objects in an application directory partition can maintain DN-value references to other objects in the same application directory partition, to objects in the configuration and schema partitions, and to any naming context head (which is the top object of a directory partition, such as the **domainDNS** object at the top of an application directory partition).
-   For more information and an example of the type of dynamic data that could be stored in an application directory partition, see [Dynamic Objects](dynamic-objects.md). Dynamic objects are supported beginning with Windows Server 2003. Dynamic objects have a property that determines the time-to-live, after which the object is deleted by the Active Directory server.

Some limitations of application directory partitions include:

-   Objects in an application directory partition cannot maintain *DN-value references* to objects in other application directory partitions or domain partitions. (DN-value references are persistent references to a distinguished name value such as "CN=someuser,DC=corp,DC=Fabrikam,DC=com"). Likewise, objects in Domain, Configuration, and Schema partitions cannot maintain DN-value references to objects in an application directory partition. A DN-value reference can be maintained to the naming context head.() )
-   Objects in an application directory partition are not replicated to the Global Catalog. As with any domain controller, a global catalog server can also be configured to contain a full replica of an application directory partition, but the application directory partition data is completely separate from the global catalog data.
-   When an application directory partition replica is created, the Domain-Naming FSMO role must be on one of the Windows Server 2003 and later operating system domain controllers. After the application directory partition replica is created, the Domain Naming FSMO role can be assigned back to a Windows 2000 domain controller.
-   Application directory partition objects cannot be moved to other Active Directory partitions outside the partition in which they were created.

Other application directory partition features include:

-   The security and access control model for the application directory partition is the same as that for other partitions in Active Directory Domain Services.
-   The time intervals that control the latency of initiating an originating change notification to replication partners within a site can be configured separately for each application directory partition basis.
-   Application directory partitions can be named just as regular domains, attached anywhere in the Active Directory namespace where a domain can, and discovered using DNS even by down-level Windows 2000 systems.
-   An application directory partition can be created, its replication scope defined, and its configurable settings adjusted programmatically using standard LDAP and ADSI APIs. For more information about programmatically manipulating application directory partitions, see [Application Directory Partitions](application-directory-partitions.md).

 

 




