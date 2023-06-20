---
title: UserPlaycountAfternoon Attribute
description: The UserPlaycountAfternoon attribute is the number of times the item has been played between 12 00 and 17 00 local time.
ms.assetid: d02ac67b-6962-452d-9046-491b452447b0
keywords:
- UserPlaycountAfternoon Attribute Windows Media Player
topic_type:
- apiref
api_name:
- UserPlaycountAfternoon
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# UserPlaycountAfternoon Attribute

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **UserPlaycountAfternoon** attribute is the number of times the item has been played between 12:00 and 17:00 local time.

## Applies To

-   [Audio Items](audio-item-attributes.md)
-   [Other Items](other-item-attributes.md)
-   [Playlists](playlist-attributes-ref.md)
-   [Video Items](video-item-attributes.md)

## Remarks

This attribute is stored only in the library.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





