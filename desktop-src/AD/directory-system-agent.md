---
title: Directory System Agent
description: The directory system agent (DSA) is a collection of services and processes that run on each domain controller and provides access to the data store.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: a921a822-6b2e-4a84-8112-0ae516443667
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- directory system agent Active Directory
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Directory System Agent

The [*directory system agent*](https://msdn.microsoft.com/library/ms681901#-ds-directory-system-agent) (DSA) is a collection of services and processes that run on each domain controller and provides access to the data store. The data store is the physical store of directory data located on a hard disk. In Active Directory Domain Services, the DSA is part of the local system authority (LSA) subsystem. Clients access the directory using one of the following mechanisms supported by the DSA:

-   LDAP clients connect to the DSA using the Lightweight Directory Access Protocol (LDAP). Active Directory Domain Services support LDAP 3.0, defined by RFC 3377, and LDAP 2.0, defined by RFC 1777. Windows clients use LDAP 3.0 to connect to the DSA.
-   MAPI clients such as Microsoft Exchange Server connect to the DSA using the MAPI remote procedure call interface.
-   The DSAs in Active Directory Domain Services connect to each other to perform replication using a proprietary remote procedure call interface.

 

 




