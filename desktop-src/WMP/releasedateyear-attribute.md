---
title: ReleaseDateYear Attribute
description: The ReleaseDateYear attribute is the year part of the date of the original release of the item.
ms.assetid: e211d5ed-b337-4c34-9abe-03cc1ab92b81
keywords:
- ReleaseDateYear Attribute Windows Media Player
topic_type:
- apiref
api_name:
- ReleaseDateYear
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# ReleaseDateYear Attribute

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **ReleaseDateYear** attribute is the year part of the date of the original release of the item.

## Applies To

-   [Audio Items](audio-item-attributes.md)
-   [CD Tracks](cd-track-attributes.md)
-   [Video Items](video-item-attributes.md)

## Remarks

This attribute is stored only in the library database (or cache).

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------|
| Version<br/> | Windows Media Player 11<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





