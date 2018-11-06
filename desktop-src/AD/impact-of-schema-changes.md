---
title: Impact of Schema Changes
description: This topic describes how a schema extension impacts the Active Directory forest.
ms.assetid: df604fb4-9256-4028-86d3-4ae1bc680324
ms.tgt_platform: multiple
keywords:
- Impact of Schema Changes AD
- schema AD , impact of changing the schema
ms.topic: article
ms.date: 05/31/2018
---

# Impact of Schema Changes

A schema extension impacts a domain forest controlled by Active Directory Domain Services in several ways:

-   Schema changes are global. There is a single schema for an entire forest. The schema is globally replicated: a copy of the schema exists on every DC in the forest. When you extend the schema, it is extended for the entire forest.
-   Schema object additions cannot be reversed. When a new class or attribute object is added to the schema, it cannot be removed. An existing attribute or class can be disabled, but not removed. For more information, see [Disabling Existing Classes and Attributes](disabling-existing-classes-and-attributes.md). Disabling a class or attribute does not affect existing instances of the class or attribute, but prevents the creation of new instances. You cannot disable an attribute if it is included in any class that is not disabled.
-   OIDs must be unique. When an attribute or class is added to the schema, no attribute or class with the same OID can be added. This is true even if a class or attribute has been disabled. For this reason it is you must use valid OIDs. Do not synthesize an OID, and do not reuse an existing OID. For more information about obtaining a valid OID, see [Obtaining a Root Object Identifier](obtaining-an-object-identifier.md).
-   Some changes can be made after creation:

    -   For a category 1 or category 2 class, you can add or remove values in the **possSuperiors** attribute. The **possSuperiors** values specify the object classes that can contain the class.
    -   For a category 1 or category 2 class, you can add or remove values in the **mayContain** attribute. The **mayContain** values specify the optional attributes, but may be present in an instance of the class.

-   The **lDAPDisplayName** for a Category 2 class or attribute can be changed after it has been created. Typically, you should not change the **lDAPDisplayName**. However, there is one legitimate reason for changing the LDAP name and that is if you made a mistake in defining the attribute or class and must create a new one to replace the old one. You do not have to rename the relative distinguished name (RDN) of the attribute or class schema to do this. When the LDAP name is changed this enables you to work around a mistake rather than rebuilding your whole Windows 2000 infrastructure. For more information, see [Disabling Existing Classes and Attributes](disabling-existing-classes-and-attributes.md).

    The **lDAPDisplayName** for predefined (category 1) classes or attributes cannot be changed. For more information about category 1 and 2 schema objects, see [Restrictions on Schema Extension](restrictions-on-schema-extension.md).

 

 




