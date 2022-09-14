---
title: Format Identifier/Offset Pair
description: The second part of the property set stream contains one Format Identifier/Offset Pair.
ms.assetid: cc3a748d-e81c-45da-b04f-ea986158a4d1
ms.topic: article
ms.date: 05/31/2018
---

# Format Identifier/Offset Pair

The second part of the property set stream contains one Format Identifier/Offset Pair. The FMTID is the name of the property set; it uniquely identifies how to interpret the contents of the following section. The Offset is the distance, in bytes, from the start of the whole stream to where the section begins.

The following structure is helpful in handling Format Identifier/Offset Pairs.

``` syntax
typedef struct tagFORMATIDOFFSET 
{ 
    FMTID  fmtid ;     // Name of the section. 
    DWORD  dwOffset ;  // Offset for the section. 
} FORMATIDOFFSET;
```

 

 




