---
title: CDTrackEnabled Attribute
description: The CDTrackEnabled attribute indicates whether the track is enabled for playback.
ms.assetid: ebbc42bd-2d6c-47ae-9a3f-c6256b120d35
keywords:
- CDTrackEnabled Attribute Windows Media Player
topic_type:
- apiref
api_name:
- CDTrackEnabled
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# CDTrackEnabled Attribute

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **CDTrackEnabled** attribute indicates whether the track is enabled for playback.

## Applies To

-   [CD Tracks](cd-track-attributes.md)

## Remarks

This attribute is stored only in the library cache.

When playing a CD in Windows Media Player, the user may select a track and specify that it should not be played. This value of this attribute is True if the track can be played, or False if the user specified that the track should not be played.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





