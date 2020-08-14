---
title: Finding a List of Attributes To Query
description: When searching for objects of a particular class, comparisons in your search filter should specify attributes that actually exist on the objects of that class.
ms.assetid: 19d52933-e4b0-414f-9785-871e624da07b
ms.tgt_platform: multiple
keywords:
- Finding a List of Attributes To Query AD
ms.topic: article
ms.date: 05/31/2018
---

# Finding a List of Attributes To Query

When searching for objects of a particular class, comparisons in your search filter should specify attributes that actually exist on the objects of that class. To get the list attributes on an object of a particular class, bind to that class in the abstract schema and retrieve the [**IADsClass.MandatoryProperties**](/windows/desktop/ADSI/iadsclass-property-methods) and **IADsClass.OptionalProperties** properties. For more information, see [Reading the Abstract Schema](reading-the-abstract-schema.md).

In addition, all objects inherit from the top abstract class. Therefore, any attribute in **top** can exist, although it may not be set, on any object.

If searching the global catalog, ensure that you specify attributes in the global catalog. Attributes included in the global catalog have the **isMemberOfPartialAttributeSet** set to **TRUE** on their **attributeSchema** objects. Be aware that this data is not available in the abstract schema; read it from the **attributeSchema** object in the schema container.

In the global catalog, a back link attribute can be queried only if both of the following conditions are met: First, the attribute is marked for inclusion in the global catalog. Second, the corresponding forward link is also marked for inclusion in the global catalog. This applies to query filters as well as query results. For more information, see [Linked Attributes](linked-attributes.md).

In addition, some attributes, mostly on the user object, are constructed. Query filters cannot contain constructed attributes. Constructed attributes cannot be evaluated in query filters; however, they can be returned in query results. This applies to all the naming contexts and the global catalog. Attributes that are constructed have **ADS\_SYSTEMFLAG\_ATTR\_IS\_CONSTRUCTED** (0x00000004) in the **systemFlags** property on their **attributeSchema** objects.

> [!Note]  
> For more information about predefined classes and attributes included with the system, see [Active Directory Domain Services Reference](active-directory-domain-services-reference.md). These pages list mandatory and optional attributes of each object class. For attributes, the reference page indicates whether the attribute is indexed, constructed, linked, or in the global catalog.

 

 

 