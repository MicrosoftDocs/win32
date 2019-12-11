---
title: Object Identifiers (AD DS)
description: Object Identifiers (OIDs) are unique numeric values issued by various issuing authorities to uniquely identify data elements, syntaxes, and other parts of distributed applications.
ms.assetid: a8f5a1c7-eda3-4430-b959-daef13c00a1b
ms.tgt_platform: multiple
keywords:
- object identifiers AD
ms.topic: article
ms.date: 05/31/2018
---

# Object Identifiers (AD DS)

Object Identifiers (OIDs) are unique numeric values issued by various issuing authorities to uniquely identify data elements, syntaxes, and other parts of distributed applications. OIDs are found in OSI applications, X.500 Directories, SNMP, and other applications where uniqueness is important. OIDs are based on a tree structure, in which a superior issuing authority, such as the ISO, allocates a branch of the tree to a subauthority, who in turn can allocate subbranches.

The LDAP protocol (RFC 2251) requires a directory service to identify object classes, attributes, and syntaxes with OIDs. This is part of the LDAP X.500 legacy.

OIDs in Active Directory Domain Services include some issued by the ISO for X.500 classes and attributes, and some issued by Microsoft and other issuing authorities. OID notation is a dotted string of numbers, for example "1.2.840.113556.1.5.9", which is described in the following table.



| Value  | Meaning          | Description                                              |
|--------|------------------|----------------------------------------------------------|
| 1      | ISO              | Identifies the root authority.                           |
| 2      | ANSI             | Group designation assigned by ISO.                       |
| 840    | USA              | Country/region designation assigned by the group.        |
| 113556 | Microsoft        | Organization designation assigned by the country/region. |
| 1      | Active Directory | Assigned by the organization.                            |
| 5      | Classes          | Assigned by the organization.                            |
| 9      | **user** class   | Assigned by the organization.                            |



 

For more information, and a discussion of two procedures used to obtain valid OIDs for use in extending the Active Directory schema, see [Obtaining an Object Identifier](obtaining-an-object-identifier.md).

 

 




