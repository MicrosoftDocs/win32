---
description: The FOURCCMap class provides conversion between GUID media subtypes and old-style FOURCC 32-bit media tags.
ms.assetid: f77f1da9-34f6-44a0-9f1a-7db2e5a26268
title: FOURCCMap class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FOURCCMap
api_type: 
- COM
api_location: 
---

# FOURCCMap class

![fourccmap class hierarchy](images/fourcc01.png)

The **FOURCCMap** class provides conversion between **GUID** media subtypes and old-style **FOURCC** 32-bit media tags. In the original Windows multimedia APIs, media types were tagged with 32-bit values created from four 8-bit characters and were known as **FOURCC**s. DirectShow media types have **GUID**s for the subtype, partly because these are simpler to create (creation of a new **FOURCC** requires its registration with Microsoft). Because **FOURCC**s are unique, a one-to-one mapping has been made possible by allocating a range of 4,000 million **GUID**s representing **FOURCC**s. This range is all **GUID**s of the form:

`XXXXXXXX-0000-0010-8000-00AA00389B71`

This class simplifies conversion between **GUID**s and **FOURCC**s. This is for compatibility only. It is recommended that all new media subtypes be represented by **GUID**s created by Guidgen.exe or a similar tool, and not by mapping **FOURCC**s.

The object is derived from a **GUID**, with no extra data members, and can be cast to a **GUID**. The object can be passed a **FOURCC** at construction time. The default constructor will initialize the **FOURCC** to zero.

The [**GetFOURCC**](fourccmap-getfourcc.md) and [**SetFOURCC**](fourccmap-setfourcc.md) methods do not check that the fixed portions of the **GUID** correspond to the **FOURCC** range. Thus, if you cast a pointer to a **GUID** into a pointer to a **FOURCC** and then set or get the **FOURCC** field, you also need to check separately that the **GUID** is within the **FOURCC** range.

## Member Functions



| Label | Value |
|------------------------------------------|----------------------------------------------------------|
| [**FOURCCMap**](fourccmap-fourccmap.md) | Constructor method.                                      |
| [**GetFOURCC**](fourccmap-getfourcc.md) | Retrieves the **FOURCC** from a **FOURCCMap** object.    |
| [**SetFOURCC**](fourccmap-setfourcc.md) | Sets the **FOURCC** portion of the **FOURCCMap** object. |



 

 

 



