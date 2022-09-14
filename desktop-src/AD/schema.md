---
title: Schema (AD DS)
description: Active Directory schema is implemented as a set of object class instances stored in the directory.
ms.assetid: 77c297ca-0dfc-4545-9832-4202e066822b
ms.tgt_platform: multiple
keywords:
- Active Directory schema Active Directory
ms.topic: article
ms.date: 05/31/2018
---

# Schema (AD DS)

Active Directory schema is implemented as a set of object class instances stored in the directory. This is very different than many directories that have a schema but store it as a text file read at startup. Storing the schema in the directory has many advantages. For example, user applications can read it to discover what objects and properties are available.

Active Directory schema can be updated dynamically. That is, an application can extend the schema with new attributes and classes and use the extensions immediately. Schema updates are accomplished by creating or modifying the schema objects stored in the directory. Like every object in Active Directory, access-control lists (ACLs) protect schema objects, so authorized users only may alter the schema.

For more information, see [Active Directory Schema](active-directory-schema.md).

 

 




