---
title: ABSTRACT Element
description: The ABSTRACT element contains text that describes the associated ASX, BANNER, or ENTRY element.
ms.assetid: 7866fee8-1778-433a-be2f-9df0baa1c13e
keywords:
- ABSTRACT Element Windows Media Player
topic_type:
- apiref
api_name:
- ABSTRACT Element
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# ABSTRACT Element

The **ABSTRACT** element contains text that describes the associated **ASX**, **BANNER**, or **ENTRY** element.

``` syntax
<ABSTRACT>
   text string
</ABSTRACT>
      
```

## Attributes

This element has no attributes.

## Parent/Child Elements



| Hierarchy | Elements                       |
|-----------|--------------------------------|
| Parent    | **ASX**, **ENTRY**, **BANNER** |
| Child     | None                           |



 

## Remarks

If this element appears within an **ASX** element, the text displays as a ToolTip when the mouse hovers over the show title.

If this element appears within an **ENTRY** element, the text displays as a ToolTip when the mouse hovers over the clip title.

If this element appears within a **BANNER** element, the text displays as a ToolTip for the banner graphic.

Use only one **ABSTRACT** element per scope. Only the first **ABSTRACT** element within the scope of another element is used when a metafile file is processed. Any subsequent **ABSTRACT** elements in that scope are ignored.

## Examples


```XML
<ASX VERSION="3.0">
    <TITLE>The Title of the Show<TITLE>
    <ABSTRACT>
        Brief description of the show. 
    </ABSTRACT>

<ENTRY>    
    <REF HREF="YourMediaFilename.asf" />
    <TITLE>The Title of the Track</TITLE>
    <ABSTRACT>
        Brief description of the track.
    </ABSTRACT>
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

 

 





