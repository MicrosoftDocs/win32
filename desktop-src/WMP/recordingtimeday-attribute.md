---
title: RecordingTimeDay Attribute
description: The RecordingTimeDay attribute is the day part of the date of the original recording, for items where this date is different from the release date.
ms.assetid: fb2d9eb6-ea06-492c-839b-27f6bd3fd986
keywords:
- RecordingTimeDay Attribute Windows Media Player
topic_type:
- apiref
api_name:
- RecordingTimeDay
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# RecordingTimeDay Attribute

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **RecordingTimeDay** attribute is the day part of the date of the original recording, for items where this date is different from the release date.

## Applies To

-   [Audio Items](audio-item-attributes.md)
-   [Photo Items](photo-item-attributes.md)
-   [Video Items](video-item-attributes.md)

## Remarks

This attribute is stored only in the library.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------|
| Version<br/> | Windows Media Player 11<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





