---
title: Guidelines for Binding to the Schema
description: There are two ways to bind to the Active Directory schema Bind directly to the schema container or to a classSchema or attributeSchema object in the schema container.
ms.assetid: 8c10415e-136c-476c-993c-b6dc459b5bf4
ms.tgt_platform: multiple
keywords:
- Guidelines for Binding to the Schema AD
- Schema AD , Binding to
ms.topic: article
ms.date: 05/31/2018
---

# Guidelines for Binding to the Schema

There are two ways to bind to the Active Directory schema:

-   Bind directly to the schema container or to a **classSchema** or **attributeSchema** object in the schema container. The **classSchema** or **attributeSchema** objects contain complete, formal definitions of every class and attribute that can exist in an Active Directory Domain forest. For more information, see [Reading attributeSchema and classSchema Objects](reading-attributeschema-and-classschema-objects.md).
-   Bind to the abstract schema or to a class or attribute entry in the abstract schema. The abstract schema contains only a subset of the data about each class and attribute, but the data is in a format that is easy to retrieve and use. For more information, see [The Abstract Schema](the-abstract-schema.md) and [Reading the Abstract Schema](reading-the-abstract-schema.md).

To modify or extend the schema, bind directly to the schema container. To read the class and attribute definitions, it is usually easier to read from the abstract schema.

It is easier to read from the abstract schema for the following reasons:

-   ADSI provides special binding techniques and a set of interfaces to read the abstract schema.
-   The ADSI interfaces that work with the abstract schema return data in a format appropriate for use in other ADSI interfaces. For example, [**IADsClass**](/windows/desktop/api/iads/nn-iads-iadsclass) and [**IADsProperty**](/windows/desktop/api/iads/nn-iads-iadsproperty) typically use **lDAPDisplayName** strings to report attribute and class names, even though this data is stored in the directory in the form of object identifiers (OIDs). The **lDAPDisplayName** format is convenient because other ADSI interfaces use it to refer to classes and attributes in search filters and elsewhere.
-   The abstract schema entry for an object class contains data collected from multiple **classSchema** objects. For example, the possible parents, mandatory attributes, and optional attributes for an object class are the union of these attributes from the class's superclasses and auxiliary classes. If you read from the actual schema container, you need to collect data from the various **classSchema** objects that the class was derived from. If you read from the abstract schema, the data is in one place.

You should bind directly to the schema container rather than using the abstract schema in the following cases:

-   To get specific attributes not exposed in the abstract schema. For example, **oMSyntax**, **attributeSchema**, **defaultSecurityDescriptor**, and other attributes are not exposed in the abstract schema.
-   To query for **attributeSchema** and **classSchema** objects. To search for classes or attributes that match a specified filter, bind to the schema container and perform a one-level search.
-   To add or modify attributes or classes. The abstract schema is read-only; you cannot use it to modify or extend the schema. Be aware that modifications must be made at the domain controller that is the schema master. For more information, see [Prerequisites for Installing a Schema Extension](prerequisites-for-installing-a-schema-extension.md).

 

 