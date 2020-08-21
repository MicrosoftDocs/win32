---
title: Querying for Category 1 or 2 Schema Objects
description: The systemFlags attribute of attributeSchema and classSchema objects is an integer bitmask that contains flags that indicate additional system qualities of the attribute or class.
ms.assetid: 5cc8f296-df3e-4643-9694-543f069a2cc7
ms.tgt_platform: multiple
keywords:
- Querying for Category 1 or 2 Schema Objects AD
- object AD , querying for category 1 or 2 schema objects
- schema AD , querying for category 1 or 2 schema objects
ms.topic: article
ms.date: 05/31/2018
---

# Querying for Category 1 or 2 Schema Objects

The **systemFlags** attribute of **attributeSchema** and **classSchema** objects is an integer bitmask that contains flags that indicate additional system qualities of the attribute or class. The [**ADS\_SYSTEMFLAG\_ENUM**](/windows/win32/api/iads/ne-iads-ads_systemflag_enum) enumeration contains values that correspond to the bits you can set in the **systemFlags** attribute. There are additional **systemFlags** bits that you cannot set, such as the 0x10 bit which indicates whether the attribute or class is category 1 or category 2. The 0x10 bit is set for category 1 objects, which are the classes and attributes included in the base schema included with the system. The bit is not set for category 2 attributes and classes, which are extensions to the schema. If no **systemFlags** property exists on an **attributeSchema** or **classSchema** object, it is category 2.

The **LDAP\_MATCHING\_RULE\_BIT\_AND** matching rule can be used to search for objects that have the 0x10 flag set in the **systemFlags** attribute. For more information, see [Search Filter Syntax](/windows/desktop/ADSI/search-filter-syntax).

## Querying for Category 1

The following query string searches for category 1 attributes (**attributeSchema** objects with the 0x10 bit set in the **systemFlags** property).


```C++
(&(objectCategory=attributeSchema)(systemFlags:1.2.840.113556.1.4.803:=16) )
```



Be aware that, in the example above, the LDAP query syntax requires decimal values; therefore, the hex value of the flag must be converted to decimal. In this case, category 1 bit is 0x10 so the filter value must be specified as 16.

## Querying for Category 2

The following query string searches for category 2 attributes (**attributeSchema** objects that do not have the 0x10 bit set in the **systemFlags** property).


```C++
(&(objectCategory=attributeSchema)(!(systemFlags:1.2.840.113556.1.4.803:=16)))
```



Be aware that this query also returns **attributeSchema** objects that do not have a **systemFlags** property, and, therefore, implicitly do not have the specified flag set.

 

 