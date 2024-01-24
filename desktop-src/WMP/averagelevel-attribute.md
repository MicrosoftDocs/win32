---
title: AverageLevel Attribute
description: The AverageLevel attribute is a 16-bit amplitude value indicating the average volume level.
ms.assetid: 04ff19f1-a9a5-4e47-86a6-50c6f08b0d7d
keywords:
- AverageLevel Attribute Windows Media Player
topic_type:
- apiref
api_name:
- AverageLevel
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AverageLevel Attribute

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **AverageLevel** attribute is a 16-bit amplitude value indicating the average volume level.

## Applies To

-   [Audio Items](audio-item-attributes.md)
-   [Commonly Used Windows Media Files](commonly-used-windows-media-file-attributes.md)

## Remarks

This attribute is stored in both the library and the digital media file.

Windows Media Player sets this value in either of the following instances:

-   After it has ripped a file.
-   After it has played a file (when the Auto Volume Leveling enhancement is enabled).

The Windows Media Format SDK constant for this attribute is g\_wszAverageLevel.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





