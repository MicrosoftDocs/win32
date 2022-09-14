---
title: Section
description: The section is the third part of the property set stream and contains the actual property set values.
ms.assetid: cb392072-116e-4dca-bd70-5f82f86d8c98
ms.topic: article
ms.date: 05/31/2018
---

# Section

The section is the third part of the property set stream and contains the actual property set values.

A section contains:

-   Byte count for the section which is inclusive of the byte count itself.
-   Array of 32-bit Property ID/Offset pairs.
-   Array of property Type Indicators/Value pairs.

Offsets are the distance from the start of the section to the start of the property (type, value) pair. This allows a section to be copied as an array of bytes without any translation of internal structure.

The following pseudo-structures illustrate the format of a section.

``` syntax
typedef struct tagPROPERTYSECTIONHEADER 
{ 
    DWORD  cbSection ;    // Size of Section 
    DWORD  cProperties ;  // Count of Properties in section 
} PROPERTYSECTIONHEADER; 
 
typedef struct tagPROPERTYIDOFFSET 
{ 
    DWORD  propid;    // Name of property 
    DWORD  dwOffset;  // Offset from start of section to property 
} PROPERTYIDOFFSET; 
 
typedef struct tagSERIALIZEDPROPERTYVALUE 
{ 
    DWORD  dwType;    // Property Type 
    BYTE   rgb[];     // Property Value 
} SERIALIZEDPROPERTYVALUE ;
```

 

 




