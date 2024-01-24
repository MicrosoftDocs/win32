---
title: WM/Lyrics Attribute
description: The WM/Lyrics attribute is the lyrics of the content.
ms.assetid: 125a2a51-81f2-478a-a9e9-234662a17bc0
keywords:
- WM/Lyrics Attribute Windows Media Player
topic_type:
- apiref
api_name:
- WM/Lyrics
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# WM/Lyrics Attribute

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **WM/Lyrics** attribute is the lyrics of the content.

## Applies To

-   [Audio Items](audio-item-attributes.md)
-   [CD Tracks](cd-track-attributes.md)
-   [Commonly Used Windows Media File Attributes](commonly-used-windows-media-file-attributes.md)

## Remarks

This attribute is stored in both the library (or cache) and the digital media file.

**Lyrics** is an alias for this attribute.

The Windows Media Format SDK constant for this attribute is g\_wszWMLyrics.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





