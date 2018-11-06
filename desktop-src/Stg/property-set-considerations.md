---
title: Property Set Considerations
description: It is strongly recommended that property sets be kept small because the property set stream is read into memory before a single property can be read or written.
ms.assetid: 520db05e-81cd-40ef-af89-471d7194c634
keywords:
- Property Set Considerations
ms.topic: article
ms.date: 05/31/2018
---

# Property Set Considerations

It is strongly recommended that property sets be kept small because the property set stream is read into memory before a single property can be read or written. "small" means less than 32 kilobytes of data. This rarely presents a problem because typically, "in-line" properties will be small items such as descriptive strings, keywords, time stamps, counts, author names, globally unique identifiers (GUIDs), class identifiers (CLSIDs), and so forth.

To store larger chunks of data, or in cases where the total size of a set of related properties far exceeds the recommended amount, the use of nonsimple types such as **VT\_STREAM** and **VT\_STORAGE** are strongly recommended. These are not stored within the property set stream, so they do not significantly affect the initial overhead of the first accessing and writing of a property. There is a minimal overhead as the property set stream contains the name of the sibling stream- or storage-valued property and this takes an additional small amount of time to process.

For more information, see:

-   [IPropertySetStorage Implementation Considerations](ipropertysetstorage-implementation-considerations.md)
-   [Storing Property Sets](storing-property-sets.md)
-   [Performance Characteristics](performance-characteristics.md)
-   [Implementing the Summary Information Property Set](implementing-the-summary-information-property-set.md)

 

 




