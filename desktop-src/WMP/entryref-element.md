---
title: ENTRYREF Element
description: The ENTRYREF element points to the ENTRY elements in an external metafile.
ms.assetid: ba39db39-fa90-455b-b278-ca866ce0b69c
keywords:
- ENTRYREF Element Windows Media Player
topic_type:
- apiref
api_name:
- ENTRYREF Element
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# ENTRYREF Element

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **ENTRYREF** element points to the **ENTRY** elements in an external metafile.

``` syntax
<ENTRYREF
   HREF = "URL"
/>
```

## Attributes

**HREF** (required)

URL to a referenced metafile.

**CLIENTBIND**

This attribute is no longer supported.

## Parent/Child Elements



| Hierarchy       | Elements                       |
|-----------------|--------------------------------|
| Parent elements | **ASX**, **EVENT**, **REPEAT** |
| Child elements  | None                           |



 

## Remarks

This element points to the contents of an external metafile. Windows Media Player processes the **ENTRY** elements of the referenced metafile as if they were included in the primary metafile at the position of the **ENTRYREF** element. However, it skips any **ENTRY** elements in the referenced metafile that have the **SKIPIFREF** attribute set to YES.

Windows Media Player 7.0, 7.1, and Windows Media Player for Windows XP ignore any **ENTRYREF** elements in the referenced metafile. Thus, metafiles can only be nested one level deep when using these versions of the Player. Windows Media Player also ignores the **ASX** element in the referenced file along with its attributes. Windows Media Player 9 Series or later supports nesting metafiles up to five levels deep.

The URL specified in the **HREF** attribute becomes the base URL for any relative URLs in the external metafile. This URL is used when an entry from the external metafile is playing and the user adds it to the library.

## Examples


```XML
<ASX VERSION="3.0">
   <TITLE>Example of Using EntryRef</TITLE>
   <ENTRYREF HREF="https://sample.microsoft.com/metafile.asx" />
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

 

 





