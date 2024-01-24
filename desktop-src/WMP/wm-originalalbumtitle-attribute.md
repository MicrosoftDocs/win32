---
title: WM/OriginalAlbumTitle Attribute
description: The WM/OriginalAlbumTitle attribute is the name of the album on which the track first appeared.
ms.assetid: e670c793-bae3-4dc5-92a1-4407cb2a094b
keywords:
- WM/OriginalAlbumTitle Attribute Windows Media Player
topic_type:
- apiref
api_name:
- WM/OriginalAlbumTitle
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# WM/OriginalAlbumTitle Attribute

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **WM/OriginalAlbumTitle** attribute is the name of the album on which the track first appeared.

## Applies To

-   [Music Files](music-file-attributes.md)

## Remarks

This attribute is stored only in a music file that is not in the library.

The Windows Media Format SDK constant for this attribute is g\_wszWMOriginalAlbumTitle.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





