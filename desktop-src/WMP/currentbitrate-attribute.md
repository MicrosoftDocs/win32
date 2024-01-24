---
title: CurrentBitrate Attribute
description: The CurrentBitrate attribute is the current bit rate of the item, in bits per second.
ms.assetid: 785b362e-ef3b-4a09-adb0-3ab6cdadb4da
keywords:
- CurrentBitrate Attribute Windows Media Player
topic_type:
- apiref
api_name:
- CurrentBitrate
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# CurrentBitrate Attribute

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **CurrentBitrate** attribute is the current bit rate of the item, in bits per second.

## Applies To

-   [Audio Items](audio-item-attributes.md)
-   [Video Items](video-item-attributes.md)

## Remarks

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

The Windows Media Format SDK constant for this attribute is g\_wszWMCurrentBitrate.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------|
| Version<br/> | Windows Media Player 9 Series only<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





