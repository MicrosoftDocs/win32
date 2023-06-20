---
title: WM/TrackNumber Attribute
description: The WM/TrackNumber attribute is the track number of the item on the album on which it was originally released.
ms.assetid: d1fc5bac-c440-470f-be5c-5aca74aee99e
keywords:
- WM/TrackNumber Attribute Windows Media Player
topic_type:
- apiref
api_name:
- WM/TrackNumber
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# WM/TrackNumber Attribute

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **WM/TrackNumber** attribute is the track number of the item on the album on which it was originally released.

## Applies To

-   [Audio Items](audio-item-attributes.md)
-   [Commonly Used Windows Media File Attributes](commonly-used-windows-media-file-attributes.md)

## Remarks

This attribute is stored in both the library and the digital media file.

Track numbers for an album start at 1.

**OriginalIndex** and **OriginalIndexLeft** are aliases for this attribute.

The Windows Media Format SDK constant for this attribute is g\_wszWMTrackNumber.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





