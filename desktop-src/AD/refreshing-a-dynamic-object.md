---
title: Refreshing a Dynamic Object
description: A client can refresh the Time To Live (TTL) of a given directory entry to keep it alive in one of two ways Performing an LDAP update to the value of its entryTTL attribute before the entry is garbage collected.
ms.assetid: 5f51013c-b278-4ef7-a235-b238eed79a35
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Refreshing a Dynamic Object

A client can refresh the Time To Live (TTL) of a given directory entry to keep it alive in one of two ways:

-   Performing an LDAP update to the value of its **entryTTL** attribute before the entry is garbage collected. This method of refreshing a dynamic entry in the directory is an additional (optional) feature of Active Directory Domain Services that is not specified by RFC 2589.
-   Performing an LDAP extended operation with an OID of 1.3.6.1.4.1.1466.101.119.1 for TTL refresh, as stipulated in the RFC 2589. This OID is defined as **LDAP\_TTL\_EXTENDED\_OP\_OID** in WINLDAP.H.

 
**Remark***:
Dynamic objects are removed by Garbage Collector when they have expired, there is no phase of the object being a tombstone when it has expired. You need to be careful with the AD replication latency when you refresh objects. You have to ensure that the update to refresh the TTL arrives early enough so all replicas of the naming context (full and global catalog) see the refresh transaction before the object expires locally.

 




