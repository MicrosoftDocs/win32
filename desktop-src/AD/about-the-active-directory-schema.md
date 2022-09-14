---
title: About the Active Directory Schema
description: Every object in Active Directory Domain Services is an instance of an object class defined in the Active Directory schema.
ms.assetid: 8fc9cd2d-8fed-4fda-918c-79b01f9a19bb
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# About the Active Directory Schema

Every object in Active Directory Domain Services is an instance of an object class defined in the Active Directory schema. An object class represents a category of objects, such as users, printers, or application programs, that share a set of common characteristics. The definition for each object class contains a list of the attributes that can be used to describe instances of the class. For example, the User class has attributes such as **givenName**, **surname**, and **streetAddress**. The list of attributes for a class is divided into those that an object of that class must contain, and additional attributes that an object may contain. The directory is arranged in a hierarchy; the definition of each class also lists the classes whose objects can be parents of objects of a given class—this controls the shape of the directory hierarchy.

The schema also formally defines each attribute. The definition for each attribute includes unique identifiers for the attribute, the syntax for the attribute (that is, the data type for the attribute's values), optional range limits for the attribute values, whether the attribute can have only one value or multiple values, and whether the attribute is indexed. The directory schema defines each attribute exactly once—object class definitions contain references to the attributes defined in the schema. For example, the "description" attribute is defined only once and is referenced by many object classes. This is different than a relational database schema, where the "attributes" (columns) are separately defined for each table.

 

 




