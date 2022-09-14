---
description: An enhanced metafile is an array of records.
ms.assetid: af3261c7-2113-4777-97c0-504f23022550
title: Enhanced Metafile Records
ms.topic: article
ms.date: 05/31/2018
---

# Enhanced Metafile Records

An enhanced metafile is an array of records. A metafile record is a variable-length [**ENHMETARECORD**](/windows/win32/api/wingdi/ns-wingdi-enhmetarecord) structure. At the beginning of every enhanced metafile record is an [**EMR**](/windows/win32/api/wingdi/ns-wingdi-emr) structure, which contains two members. The first member, iType, identifies the record type that is, the GDI function whose parameters are contained in the record. Because the structures are variable in length, the other member, nSize, contains the size of the record. Immediately following the nSize member are the remaining parameters, if any, of the GDI function. The remainder of the structure contains additional data that is dependent on the record type.

The first record in an enhanced metafile is always the [**ENHMETAHEADER**](/windows/win32/api/wingdi/ns-wingdi-enhmetaheader) structure, which is the enhanced-metafile header. The header specifies the following information:

-   Size of the metafile, in bytes
-   Dimensions of the picture frame, in device units
-   Dimensions of the picture frame, in .01-millimeter units
-   Number of records in the metafile
-   Offset to an optional text description
-   Size of the optional palette
-   Resolution of the original device, in pixels
-   Resolution of the original device, in millimeters

An optional text description can follow the header record. The text description describes the picture and the author's name. The optional palette specifies the colors used to create the enhanced metafile. The remaining records identify the GDI functions used to create the picture. The following hexadecimal output corresponds to a record generated for a call to the [**SetMapMode**](/windows/desktop/api/Wingdi/nf-wingdi-setmapmode) function.


```C++
00000011 0000000C 00000004 
```



The value 0x00000011 specifies the record type (corresponds to the EMR\_SETMAPMODE constant defined in the file Wingdi.h). The value 0x0000000C specifies the length of the record, in bytes. The value 0x00000004 identifies the mapping mode (corresponds to the MM\_LOENGLISH constant defined in the [**SetMapMode**](/windows/desktop/api/Wingdi/nf-wingdi-setmapmode) function).

For a list of additional record types, see [Metafile Structures](metafile-structures.md).

 

 



