---
title: PlaylistIndex Attribute
description: The PlaylistIndex attribute is the index of the media item in its parent playlist.
ms.assetid: 65b629d4-115c-487c-b260-4bbea38dcea7
keywords:
- PlaylistIndex Attribute Windows Media Player
topic_type:
- apiref
api_name:
- PlaylistIndex
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# PlaylistIndex Attribute

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **PlaylistIndex** attribute is the index of the media item in its parent playlist.

## Applies To

-   [Audio Items](audio-item-attributes.md)
-   [CD Tracks](cd-track-attributes.md)
-   [Other Items](other-item-attributes.md)
-   [Video Items](video-item-attributes.md)

## Remarks

This attribute is a temporary attribute. It is not stored in the library or the digital media file.

Media items can be playlist elements. This attribute is the zero-based index that represents the position of the media item in the playlist. If the media item is not part of a playlist, the value of this attribute is an empty string ("").

## Requirements



| Requirement | Value |
|--------------------|------------------------------------|
| Version<br/> | Windows Media Player 11<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





