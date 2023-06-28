---
title: AcquisitionTimeYearMonth Attribute
description: The AcquisitionTimeYearMonth attribute is the year and month part of the date and time the item was added to the library.
ms.assetid: 9fed9c82-5807-4dc8-87f8-c97254e7d9dc
keywords:
- AcquisitionTimeYearMonth Attribute Windows Media Player
topic_type:
- apiref
api_name:
- AcquisitionTimeYearMonth
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AcquisitionTimeYearMonth Attribute

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **AcquisitionTimeYearMonth** attribute is the year and month part of the date and time the item was added to the library.

## Applies To

-   [Audio Items](audio-item-attributes.md)
-   [Other Items](other-item-attributes.md)
-   [Photo Items](photo-item-attributes.md)
-   [Playlists](playlist-attributes-ref.md)
-   [Radio Items](radio-item-attributes.md)
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

 

 





