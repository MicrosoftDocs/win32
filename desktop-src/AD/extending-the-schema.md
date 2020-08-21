---
title: Extending the Schema
description: The Active Directory directory service schema defines the attributes and classes used in Active Directory Domain Services.
ms.assetid: 1c7c1fa7-56d9-4b2d-9c48-aa10464064bc
ms.tgt_platform: multiple
keywords:
- Active Directory,using,schema,extending the schema
- schema AD ,extending the schema
ms.topic: article
ms.date: 05/31/2018
---

# Extending the Schema

The Active Directory directory service schema defines the attributes and classes used in Active Directory Domain Services. The base schema that is included the system contains a rich set of class definitions, such as **user**, **computer**, and **organizationalUnit**, and attribute definitions, such as **userPrincipalName**, **telephoneNumber**, and **objectSid**. The existing set of classes and attributes will be sufficient for most applications. However, the schema is extensible, which means that you can define new classes and attributes. This section discusses how to extend the Active Directory schema.

## When to Extend the Schema

If the existing classes and attributes do not fit with the type of data you want to store, you should extend the schema. It is important to note that schema additions are permanent; you can disable classes and attributes, but you can never remove them from the schema. Keep this in mind when you are testing code.

Also consider the size of the data that you want to store. Microsoft recommends that no attribute value exceed 500 kilobytes, including the sum of multivalued attributes. Also, objects should not exceed 1 megabyte in size. Consider also the number of instances of the data; if you add a new attribute to the [**User**](/windows/desktop/ADSchema/c-user) class on a system that has 100,000 users, this can use up considerable space.

Topics in this section include:

-   How to bind to the schema container and read the properties of existing classes and attributes.
-   How and when to extend the schema by defining new attributes and classes.
-   How to install schema extensions using LDIFDE, CSVDE, or programmatically with ADSI.

For more information and an overview of the Active Directory schema, including information about the schema implementation, class definitions, and attribute definitions, see [Active Directory Schema](active-directory-schema.md).

For more information, including reference pages for the predefined schema classes, attributes, and attribute syntaxes, see the Active Directory Schema Reference in the [Active Directory Domain Services Reference](active-directory-domain-services-reference.md).

 

 