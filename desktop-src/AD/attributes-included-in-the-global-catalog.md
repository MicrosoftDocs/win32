---
title: Including Attributes in the Global Catalog
description: The global catalog of a forest includes a partial replica of every object in the forest.
ms.assetid: 185467ed-7bcf-41e9-9862-02412009c437
ms.tgt_platform: multiple
keywords:
- Attributes Included in the Global Catalog AD
- Attributes AD ,included in the global catalog
ms.topic: article
ms.date: 05/31/2018
---

# Including Attributes in the Global Catalog

The global catalog of a forest includes a partial replica of every object in the forest. For each object, the global catalog includes only a subset of each object's attributes. The [**isMemberOfPartialAttributeSet**](/windows/desktop/ADSchema/a-ismemberofpartialattributeset) attribute of an [**attributeSchema**](/windows/desktop/ADSchema/c-attributeschema) object is set to **TRUE** if the attribute is replicated to the global catalog.

Attributes with the following characteristics are appropriate for storage in the global catalog:

-   The attribute is globally interesting, either because the attribute is required for locating objects that can occur anywhere in the forest, or because read access to the attribute is valuable even when the full object is not accessible. An example of the first type is the [**location**](/windows/desktop/ADSchema/a-location) attribute, which can be used to find a [**printQueue**](/windows/desktop/ADSchema/c-printqueue) object. An example of the second type is [**telephoneNumber**](/windows/desktop/ADSchema/a-telephonenumber), because you can call someone even if you cannot access a full replica of their [**user**](/windows/desktop/ADSchema/c-user) object.
-   The volatility of the attribute is very low. This is important, because if an attribute class is included in the global catalog, changes to every value of that attribute class throughout the enterprise forest are replicated to all global catalog servers in the enterprise.
-   The size of the attribute value is small. "Small" is highly subjective: when placing an attribute in the global catalog, consider the impact of replicating the attribute to all global catalog servers in the enterprise. The smaller the attribute, the lower the impact. Because replication occurs only when the attribute changes, the impact of replication is also smaller as volatility decreases, so a large attribute with very low volatility may have a smaller overall impact than a small attribute with high volatility.

When deciding whether or not to place an attribute in the global catalog remember that you are trading increased replication and increased disk storage on global catalog servers for, potentially, faster query performance. Typically, you would use the global catalog to search for an object of interest so you can read selected attributes of the object. If the attributes you are interested in are replicated to the global catalog, you can read them directly from the global catalog. Alternately, to read attributes that are not replicated to the global catalog, you must perform additional steps to retrieve them. In this case, after searching the global catalog to find the object of interest, you must read the object's distinguished name from the global catalog, use the DN to bind directly to a full replica of the object, which may be on a different server, and finally read the non-global-catalog attributes from the full replica of the object.

Frequently queried and referenced attributes, such as employee name and phone number, are good to include in the global catalog. An infrequently referenced attribute such as "driverVersion" for printers is best left out of the global catalog.

 

 