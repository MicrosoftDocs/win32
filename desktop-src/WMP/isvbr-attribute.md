---
title: IsVBR Attribute
description: The IsVBR attribute indicates whether the content was encoded using variable bit rate (VBR) encoding.
ms.assetid: faec0940-ef53-40a1-be54-a990884e907d
keywords:
- IsVBR Attribute Windows Media Player
topic_type:
- apiref
api_name:
- IsVBR
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IsVBR Attribute

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **IsVBR** attribute indicates whether the content was encoded using variable bit rate (VBR) encoding.

## Applies To

-   [Commonly Used Windows Media Files](commonly-used-windows-media-file-attributes.md)
-   [Video Items](video-item-attributes.md)

## Remarks

This attribute is stored only in the digital media file.

The Windows Media Format SDK constant for this attribute is g\_wszWMIsVBR.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





