---
title: The Abstract Schema
description: The schema container contains all of the classSchema and attributeSchema objects that define the classes and attributes that can exist in a directory forest.
ms.assetid: 688fccf7-37ce-4eea-b4ff-b0b3223a964e
ms.tgt_platform: multiple
keywords:
- The Abstract Schema AD
ms.topic: article
ms.date: 05/31/2018
---

# The Abstract Schema

The schema container contains all of the **classSchema** and **attributeSchema** objects that define the classes and attributes that can exist in a directory forest. The schema container also contains an object named Aggregate of class **subSchema**. This **subSchema** object is known as the abstract schema.

The abstract schema contains a subset of the data stored in the **classSchema** and **attributeSchema** objects. Its purpose is to provide a simple and efficient mechanism for retrieving the frequently used elements of the class and attribute definitions. For example, to retrieve the optional and mandatory attributes of an object class, bind to multiple objects to collect the **mayContain**, **mustContain**, **systemMayContain**, and **systemMustContain** values from the class and all its superclasses, as well as from any auxiliary classes of the class and its superclasses. The abstract schema conveniently collects all this data in a single object.

As with any object in Active Directory Domain Services, you can bind to the **subSchema** object and read its attributes, parsing the string values to retrieve the desired data. However, ADSI provides a set of interfaces that make it much easier to read the abstract schema. For more information, see [Reading the Abstract Schema](reading-the-abstract-schema.md).

The following table lists key attributes of a **subSchema** object.



| Attribute                 | Description                                                                                                                                                                                                                                                                               |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **attributeTypes**        | A multi-valued attribute that contains strings that represent each attribute in the schema. Each value contains the **attributeID**, **lDAPDisplayName**, **attributeSyntax**, **rangeLower**, **rangeUpper**, and an item that indicates whether the attribute can have multiple values. |
| **extendedAttributeInfo** | A multi-valued attribute that contains strings that represent additional data for each attribute. Each value contains the **attributeID**, **lDAPDisplayName**, **schemaIDGUID**, and **attributeSecurityGUID**.                                                                          |
| **extendedClassInfo**     | A multi-valued attribute that contains strings that represent additional data for each class. Each value contains the **governsID**, **lDAPDisplayName**, and **schemaIDGUID** of the class.                                                                                              |
| **objectClasses**         | A multi-valued attribute that contains strings that represent each class in the schema. Each value contains the **governsID**, **lDAPDisplayName**, **mustContain**, **mayContain**, and so on.                                                                                           |



 

 

 




