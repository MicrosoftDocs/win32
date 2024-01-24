---
title: TITLE Element (metafile)
description: The TITLE element defines a text string specifying the title for an ASX or ENTRY element.
ms.assetid: d7ad7f00-fcf2-456d-a106-98bf0a258b81
keywords:
- TITLE Element (metafile) Windows Media Player
topic_type:
- apiref
api_name:
- TITLE Element (metafile)
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# TITLE Element (metafile)

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **TITLE** element defines a text string specifying the title for an **ASX** or **ENTRY** element.

``` syntax
<TITLE>
   text string
</TITLE>
```

## Attributes

This element has no attributes.

## Parent/Child Elements



| Hierarchy       | Elements           |
|-----------------|--------------------|
| Parent elements | **ASX**, **ENTRY** |
| Child elements  | None               |



 

## Remarks

This element defines a text string that specifies the title of an **ASX** or **ENTRY** element. The title is displayed in the display panel and **Properties** dialog box.

When this element appears within an **ASX** element, the text is displayed as **Show** information. When this element appears within an **ENTRY** element, the text is displayed as **Clip** information.

If a **MOREINFO** element is also used with the associated (parent) element, it is the title text that the user clicks to access the URL defined in the **MOREINFO** element.

Each parent **ASX** and **ENTRY** element should contain at most one child **TITLE** element. Multiple **TITLE** elements after the first will be ignored and will not be displayed.

## Examples


```XML
<ASX VERSION="3.0">
   <TITLE>Title of the Show</TITLE>
   <ENTRY>
      <TITLE>Title of the Clip</TITLE>
      <REF HREF="mms://example.microsoft.com/clip1.asf" />
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

 

 





