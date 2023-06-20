---
title: WM/VideoHeight Attribute
description: The WM/VideoHeight attribute specifies the photo or video height in pixels.
ms.assetid: 53212678-0dcd-49d8-98fe-15a7a2cfebd4
keywords:
- WM/VideoHeight Attribute Windows Media Player
topic_type:
- apiref
api_name:
- WM/VideoHeight
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# WM/VideoHeight Attribute

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **WM/VideoHeight** attribute specifies the photo or video height in pixels.

## Applies To

-   [Photo Items](photo-item-attributes.md)
-   [Video Items](video-item-attributes.md)

## Remarks

This is read-only attribute.

The Windows Media Format SDK constant for this attribute is g\_wszWMVideoHeight.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------|
| Version<br/> | Windows Media Player 10 or later<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





