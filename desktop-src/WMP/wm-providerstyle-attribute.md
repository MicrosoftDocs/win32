---
title: WM/ProviderStyle Attribute
description: The WM/ProviderStyle attribute is the style of the item assigned by the provider of the attribute values.
ms.assetid: 43994d6b-0d71-4f2c-834a-47bbcd32b461
keywords:
- WM/ProviderStyle Attribute Windows Media Player
topic_type:
- apiref
api_name:
- WM/ProviderStyle
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# WM/ProviderStyle Attribute

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **WM/ProviderStyle** attribute is the style of the item assigned by the provider of the attribute values.

## Applies To

-   [Audio Items](audio-item-attributes.md)
-   [CD Playlists](cd-playlist-attributes.md)
-   [CD Tracks](cd-track-attributes.md)
-   [Commonly Used Windows Media File Attributes](commonly-used-windows-media-file-attributes.md)
-   [Video Items](video-item-attributes.md)

## Remarks

This attribute is stored in both the library (or cache) and the digital media file.

**Style** is an alias for this attribute.

The Windows Media Format SDK constant for this attribute is g\_wszWMProviderStyle.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





