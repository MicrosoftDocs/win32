---
title: Structure and Union Attributes
description: Use the switch\_\ attributes to specify the characteristic of a union in a remote procedure call. Use the ignore attribute to designate certain structure or union members as local to the client application.
ms.assetid: e06e5184-fa92-4446-964b-d56d0e5f2872
keywords:
- IDL MIDL , attributes, structure and union
ms.topic: article
ms.date: 05/31/2018
---

# Structure and Union Attributes

Use the **switch\_**\* attributes to specify the characteristic of a union in a remote procedure call. Use the [**ignore**](ignore.md) attribute to designate certain structure or union members as local to the client application.



| Attribute                           | Usage                                                                                                                         |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| [**switch**](switch.md)            | Selects the discriminant for an encapsulated union.                                                                           |
| [**switch\_is**](switch-is.md)     | Identifies the discriminant for a nonencapsulated union.                                                                      |
| [**switch\_type**](switch-type.md) | Identifies the type of the discriminant for a nonencapsulated union.                                                          |
| [**ignore**](ignore.md)            | Designates that a pointer contained in a structure or union and the object indicated by the pointer is not to be transmitted. |



 

You can also use the [array and sized pointer attributes](array-and-sized-pointer-attributes.md) to specify characteristics of structure or union members.

 

 




