---
title: WM/VideoFrameRate Attribute
description: The WM/VideoFrameRate attribute is a decimal value that specifies the frame rate (in frames per second) for a video file.
ms.assetid: 6eec6e64-68b2-443c-b88a-ce87c708ab57
keywords:
- WM/VideoFrameRate Attribute Windows Media Player
topic_type:
- apiref
api_name:
- WM/VideoFrameRate
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# WM/VideoFrameRate Attribute

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **WM/VideoFrameRate** attribute is a decimal value that specifies the frame rate (in frames per second) for a video file.

## Applies To

-   [Video Items](video-item-attributes.md)

## Remarks

The Windows Media Format SDK constant for this attribute is g\_wszWMVideoFrameRate.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------|
| Version<br/> | Windows Media Player 11<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





