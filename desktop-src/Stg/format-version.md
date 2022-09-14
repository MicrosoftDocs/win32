---
title: Format Version
description: The Format Version value is a WORD data type that is used to indicate the format version of this stream.
ms.assetid: 38362a45-4f49-4a85-aabe-452ff32c2812
ms.topic: article
ms.date: 05/31/2018
---

# Format Version

The Format Version value is a **WORD** data type that is used to indicate the format version of this stream. It may be zero or one. The format-version indicator should be checked when reading the property set. If it is not zero or one, then the stream was written to a different specification and cannot be read by code developed according to this specification.

Property sets with Format Version 1 are equivalent to Version 0, with the following additions:

-   **Case sensitive property names**. Property names are stored in the reserved dictionary property, [Property ID 0](/windows/desktop/Stg/reserved-property-identifiers). In version 1 property sets, these names can be case sensitive. Case sensitivity is determined by the reserved Behavior property, [Property ID 0x80000003](/windows/desktop/Stg/reserved-property-identifiers).
-   **Long property names**. Version 1 property sets, unlike version 0 property sets, are not limited in the length of property names. See [Property ID 0](/windows/desktop/Stg/reserved-property-identifiers) for more information on property names.
-   **Property types**. Version 1 property sets can hold all the property types that can be held in a version 0 property set plus some additional types. See the [**PROPVARIANT**](/windows/win32/api/propidlbase/ns-propidlbase-propvariant) structure for more information on these types.

 

 