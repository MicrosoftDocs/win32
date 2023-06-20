---
title: Bitrate Attribute
description: The Bitrate attribute is the bit rate of the item, in bits per second.
ms.assetid: '19117ca7-fad3-469e-8208-c0b899e13919'
keywords:
- Bitrate Attribute Windows Media Player
topic_type:
- apiref
api_name:
- Bitrate
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Bitrate Attribute

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **Bitrate** attribute is the bit rate of the item, in bits per second.

## Applies To

-   [Audio Items](audio-item-attributes.md)
-   [Commonly Used Windows Media Files](commonly-used-windows-media-file-attributes.md)
-   [Other Items](other-item-attributes.md)
-   [Radio Items](radio-item-attributes.md)
-   [Video Items](video-item-attributes.md)

## Remarks

This attribute is stored in both the library and the digital media file.

The Windows Media Format SDK constant for this attribute is g\_wszWMBitrate.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





