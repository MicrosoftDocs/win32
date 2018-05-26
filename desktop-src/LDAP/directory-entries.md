---
title: Directory Entries
description: An LDAP directory is a collection of entries, which consist of one or more attributes each.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 4039df03-5550-4246-97cc-7894a790289e
ms.prod: windows-server-dev
ms.technology: active-directory-lightweight-directory-services
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Directory Entries

An LDAP directory is a collection of entries, which consist of one or more attributes each. Each attribute has one or more values and a type that determines the kind of information the values can hold and how those values behave during directory operations. The attribute types and object classes defined for LDAP clients are described in RFC 4510.

The entries are arranged hierarchically in a tree that is structured geographically and organizationally. Global entries, such as countries/regions, reside at the top of the tree, followed by state or national organizations, then organizational units, people, devices, or anything else that might be represented in a directory.

A directory entry is represented by its entry name, or relative distinguished name (RDN), and by its distinguished name (DN). The DN uniquely identifies each entry on a global level, and is derived by concatenating the RDN of an entry with the RDN of each of its ancestor entries.

 

 




