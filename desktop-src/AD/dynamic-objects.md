---
title: Dynamic Objects
description: In Windows Server 2003 and later versions of Windows, Active Directory Domain Services provide support for storing dynamic entries in the directory.
ms.assetid: ac5779b6-f226-414c-92a9-091719b1515b
ms.tgt_platform: multiple
keywords:
- dynamic objects AD
ms.topic: article
ms.date: 05/31/2018
---

# Dynamic Objects

In Windows Server 2003 and later versions of Windows, Active Directory Domain Services provide support for storing dynamic entries in the directory. A dynamic entry is an object in the directory which has an associated time-to-live (TTL) value. The TTL for an entry is set when the entry is created. The time-to-live is automatically decremented, and when it expires the dynamic entry disappears. The client can cause a dynamic entry to remain longer than its current remaining life by refreshing (modifying) its TTL value. Clients that store dynamic data in the directory must periodically refresh that data to prevent it from disappearing.

Many applications and services that use LDAP to store and access relatively static and globally interesting data from an Active Directory server would also prefer to continue using LDAP access for their dynamic data needs. Moreover, for some applications, it may be desirable to off-load the task of garbage-collecting objects in the DS that have a limited useful life to the directory service. Application directory partitions (with the ability for controlled placement of replicas) and per-object TTLs together will provide the capability of hosting dynamic data in Active Directory Domain Services, thus allowing LDAP access to it.

A new auxiliary object class called **dynamicObject** with OID = 1.3.6.1.4.1.1466.101.119.2 will be defined in the base AD schema to be used by dynamic entries. This auxiliary class contains the attribute called **entryTTL** with OID = 1.3.6.1.4.1.1466.101.119.3 as a system-may-contain attribute. The value of this attribute is the "time in seconds" that the corresponding directory entry will continue to exist before disappearing from the directory. If the client does not supply a value for this attribute explicitly at object creation, then the DS provides a default value as specified later.

A new extended LDAP operation with OID = 1.3.6.1.4.1.1466.101.119.1 for client refresh of a dynamic entry in the directory will be defined and published in the **supportedExtension** attribute of the root DSE object.

In the actual implementation, **entryTTL** is a constructed attribute. The real object expiration time is stored as an absolute time when the object can be destroyed in a system-only attribute called **ms-DS-Entry-Time-To-Live**.

All dynamic objects have the following limitations:

-   A deleted dynamic object due to its TTL expiring does not leave a tombstone behind.
-   All DCs holding replicas of dynamic objects must run on Windows Server 2003.
-   Dynamic entries with TTL values are supported in all partitions except the Configuration partition and Schema partition.
-   Active Directory Domain Services do not publish the optional **dynamicSubtrees** attribute, as described in the RFC 2589, in the root DSE object.
-   Dynamic entries are handled similar to non-dynamic entries when processing search, compare, add, delete, modify, and modifyDN operations.
-   There is no way to change a static entry into a dynamic entry and vice-versa.
-   A non-dynamic entry cannot be added subordinate to a dynamic entry.

 

 




