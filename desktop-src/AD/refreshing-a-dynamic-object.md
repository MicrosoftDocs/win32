---
title: Refreshing a Dynamic Object
description: A client can refresh the Time To Live (TTL) of a given directory entry to keep it alive in one of two ways Performing an LDAP update to the value of its entryTTL attribute before the entry is garbage collected.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '5f51013c-b278-4ef7-a235-b238eed79a35'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
---

# Refreshing a Dynamic Object

A client can refresh the Time To Live (TTL) of a given directory entry to keep it alive in one of two ways:

-   Performing an LDAP update to the value of its **entryTTL** attribute before the entry is garbage collected. This method of refreshing a dynamic entry in the directory is an additional (optional) feature of Active Directory Domain Services that is not specified by RFC 2589.
-   Performing an LDAP extended operation with an OID of 1.3.6.1.4.1.1466.101.119.1 for TTL refresh, as stipulated in the RFC 2589. This OID is defined as **LDAP\_TTL\_EXTENDED\_OP\_OID** in WINLDAP.H.

 

 




