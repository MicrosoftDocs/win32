---
title: BuyNow Attribute
description: The BuyNow attribute is a PARAM value for use in commercial interactions.
ms.assetid: 06b96992-a532-4c72-bb4f-6cdd6209f137
keywords:
- BuyNow Attribute Windows Media Player
topic_type:
- apiref
api_name:
- BuyNow
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# BuyNow Attribute

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **BuyNow** attribute is a **PARAM** value for use in commercial interactions.

## Applies To

-   [Audio Items](audio-item-attributes.md)
-   [CD Playlists](cd-playlist-attributes.md)
-   [CD Tracks](cd-track-attributes.md)
-   [DVDs](dvd-attributes.md)

## Remarks

This attribute is stored only in the library database (or cache).

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





