---
title: WM/ContentDistributor Attribute
description: The WM/ContentDistributor attribute is the name of the distributor of the item.
ms.assetid: 45f548a4-4059-464c-af93-1ba09e6b8d1e
keywords:
- WM/ContentDistributor Attribute Windows Media Player
topic_type:
- apiref
api_name:
- WM/ContentDistributor
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# WM/ContentDistributor Attribute

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **WM/ContentDistributor** attribute is the name of the distributor of the item.

## Applies To

-   [Audio Items](audio-item-attributes.md)
-   [Commonly Used Windows Media File Attributes](commonly-used-windows-media-file-attributes.md)
-   [Playlists](playlist-attributes-ref.md)
-   [Video Items](video-item-attributes.md)

## Remarks

This attribute is stored in both the library and the digital media file.

**ContentDistributor** is an alias for this attribute.

The Windows Media Format SDK constant for this attribute is g\_wszWMContentDistributor.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





