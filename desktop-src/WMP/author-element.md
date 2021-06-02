---
title: AUTHOR Element
description: The AUTHOR element contains the name of the author of a Windows Media metafile or media clip.
ms.assetid: d80aad3d-4471-4310-8d43-2733ed83103c
keywords:
- AUTHOR Element Windows Media Player
topic_type:
- apiref
api_name:
- AUTHOR Element
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# AUTHOR Element

The **AUTHOR** element contains the name of the author of a Windows Media metafile or media clip.

``` syntax
<AUTHOR>   
   text string
</AUTHOR>
```

## Attributes

This element has no attributes.

## Parent/Child Elements



| Hierarchy       | Element            |
|-----------------|--------------------|
| Parent elements | **ASX**, **ENTRY** |
| Child elements  | None               |



 

## Remarks

This element contains a text string representing the name of the author of a Windows Media metafile or media clip. You can use the **AUTHOR** element within the **ASX** element and within **ENTRY** elements.

If this element appears in the **ASX** element, the text is displayed as **Show** information.

If this element appears in an **ENTRY** element, the text is displayed as the clip author.

Each parent **ASX** and **ENTRY** element should contain at most one child **AUTHOR** element. Multiple **AUTHOR** elements after the first will be ignored and will not be displayed.

## Examples


```XML
<ASX VERSION="3.0">
   <AUTHOR>Neal S.</AUTHOR>   <!-- Show author -->
   <ENTRY>
      <REF HREF="mms://example.microsoft.com/clip1.asf" />
      <AUTHOR>Robert P.</AUTHOR>  <!-- Clip author -->
   </ENTRY>
</ASX>

```



## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------|
| Version<br/> | Windows Media Player version 70 or later<br/> |



## See also

<dl> <dt>

[**Windows Media Metafile Elements Reference**](windows-media-metafile-elements-reference.md)
</dt> <dt>

[**Windows Media Metafile Reference**](windows-media-metafile-reference.md)
</dt> </dl>

 

 





