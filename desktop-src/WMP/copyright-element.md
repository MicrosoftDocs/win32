---
title: COPYRIGHT Element (Msfeeds.h)
description: The COPYRIGHT element defines a text string specifying the copyright information for an ASX or ENTRY element.
ms.assetid: 264b92de-b10c-41b9-b219-727879079f15
keywords:
- COPYRIGHT Element Windows Media Player
topic_type:
- apiref
api_name:
- COPYRIGHT Element
api_location:
- msfeeds.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# COPYRIGHT Element

The **COPYRIGHT** element defines a text string specifying the copyright information for an **ASX** or **ENTRY** element.

``` syntax
<COPYRIGHT>
    text string
</COPYRIGHT>
```

## Attributes

This element has no attributes.

## Parent/Child Elements



| Hierarchy       | Elements           |
|-----------------|--------------------|
| Parent elements | **ASX**, **ENTRY** |
| Child elements  | None               |



 

## Remarks

This element defines a text string that specifies the copyright information for an **ASX** or **ENTRY** element.

When this element appears within an **ASX** element, the copyright string is displayed only as **Show** information. When this element appears within an **ENTRY** element, the text is displayed as clip information. Each parent **ASX** and **ENTRY** element should contain at most one child **COPYRIGHT** element. Multiple **COPYRIGHT** elements after the first will be ignored and will not be displayed.

The characters for copyright and trademark registration symbols (   or   ) may not display properly if the metafile is not encoded using the UTF-8 encoding scheme. In this case, to display either of these symbols properly for all users, you can use the ASCII equivalents (c) and (R) instead.

If the metafile is encoded using UTF-8, copyright and trademark symbols will display correctly.

## Examples


```XML
<COPYRIGHT>Copyright (c) 1998, Microsoft Corporation</COPYRIGHT>

```



## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/>                                 |
| Header<br/>  | <dl> <dt>Msfeeds.h</dt> </dl> |



## See also

<dl> <dt>

[**Adding Copyright Characters to Metafiles**](adding-copyright-characters-to-metafiles.md)
</dt> <dt>

[**Windows Media Metafile Elements Reference**](windows-media-metafile-elements-reference.md)
</dt> <dt>

[**Windows Media Metafile Reference**](windows-media-metafile-reference.md)
</dt> </dl>

 

 





