---
title: WM/MediaClassPrimaryID Attribute
description: The WM/MediaClassPrimaryID attribute is a GUID specifying one of the primary media classes music, non-music audio, video, or other.
ms.assetid: eb78f4a9-7c18-4cad-bb34-fd1ff15bad4f
keywords:
- WM/MediaClassPrimaryID Attribute Windows Media Player
topic_type:
- apiref
api_name:
- WM/MediaClassPrimaryID
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# WM/MediaClassPrimaryID Attribute

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **WM/MediaClassPrimaryID** attribute is a GUID specifying one of the primary media classes: music, non-music audio, video, or other.

## Applies To

-   [Audio Items](audio-item-attributes.md)
-   [Commonly Used Windows Media File Attributes](commonly-used-windows-media-file-attributes.md)
-   [Other Items](other-item-attributes.md)
-   [Photo Items](photo-item-attributes.md)
-   [Playlists](playlist-attributes-ref.md)
-   [Radio Items](radio-item-attributes.md)
-   [Video Items](video-item-attributes.md)

## Remarks

This attribute is stored in both the library and the digital media file.

**MediaClassPrimaryID** is an alias for this attribute.

The Windows Media Format SDK constant for this attribute is g\_wszWMMediaClassPrimaryID.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later (The photo item is supported only in Windows Media Player 10 or later)<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





