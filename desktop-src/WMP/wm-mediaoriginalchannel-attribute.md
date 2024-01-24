---
title: WM/MediaOriginalChannel Attribute
description: The WM/MediaOriginalChannel attribute specifies the channel on which a given show was first broadcast.
ms.assetid: b183312d-bd48-46e4-832c-724c9770a9c9
keywords:
- WM/MediaOriginalChannel Attribute Windows Media Player
topic_type:
- apiref
api_name:
- WM/MediaOriginalChannel
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# WM/MediaOriginalChannel Attribute

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **WM/MediaOriginalChannel** attribute specifies the channel on which a given show was first broadcast.

## Applies To

-   [Video Items](video-item-attributes.md)

## Remarks

The Windows Media Format SDK constant for this attribute is g\_wszWMMediaOriginalChannel.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------|
| Version<br/> | Windows Media Player 10 or later<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





