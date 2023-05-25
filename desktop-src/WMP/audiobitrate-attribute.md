---
title: AudioBitrate Attribute
description: The AudioBitrate attribute is the bit rate for the audio stream within a video file, in bits per second.
ms.assetid: 28272aa2-49ac-4c13-aa3e-6e733cc49514
keywords:
- AudioBitrate Attribute Windows Media Player
topic_type:
- apiref
api_name:
- AudioBitrate
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AudioBitrate Attribute

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **AudioBitrate** attribute is the bit rate for the audio stream within a video file, in bits per second.

## Applies To

-   [Video Items](video-item-attributes.md)

## Remarks

This attribute is stored in both the library and the video file.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------|
| Version<br/> | Windows Media Player 10 or later<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





