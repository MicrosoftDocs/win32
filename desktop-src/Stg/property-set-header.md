---
title: Property Set Header
description: At the beginning of the property set stream is a header. It consists of a byte-order indicator, a format version, the originating operating system version, the class identifier (CLSID), and a reserved field.
ms.assetid: 6f4531d5-99d8-43ff-b6c1-5975b7527fc0
keywords:
- Property Set Header Structured Storage
ms.topic: article
ms.date: 05/31/2018
---

# Property Set Header

At the beginning of the property set stream is a header. It consists of a byte-order indicator, a format version, the originating operating system version, the class identifier (CLSID), and a reserved field.

The following pseudo-structure illustrates the header.

``` syntax
typedef struct tagPROPERTYSETHEADER 
{ 
    // Header 
    WORD   wByteOrder ;  // Always 0xFFFE 
    WORD   wFormat ;     // Always 0 
    DWORD   dwOSVer ;    // System version 
    CLSID  clsID ;       // Application CLSID 
    DWORD  reserved ;    // Should be 1 
} PROPERTYSETHEADER;
```

 

 




