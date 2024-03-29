---
title: RecordingTimeYear Attribute
description: The RecordingTimeYear attribute is the year part of the date of the original recording, for items where this date is different from the release date.
ms.assetid: 6516905f-162b-44ce-ac82-56b039e910f2
keywords:
- RecordingTimeYear Attribute Windows Media Player
topic_type:
- apiref
api_name:
- RecordingTimeYear
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# RecordingTimeYear Attribute

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **RecordingTimeYear** attribute is the year part of the date of the original recording, for items where this date is different from the release date.

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

 

 





